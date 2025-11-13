#!/usr/bin/env python3
#
# Usage examples:
#   python parametersFromMeasurements_cli.py \
#       --H 1679 --p-cpu-full 32.2 \
#       --num-gpus 1 --use-tp --cpu-secs 638 --gpu-secs 426 \
#       --p-cpu-elig-c 638 --p-elig 1=426 \
#       --f 0.463 --f 0.5 --f 0.8 \
#       --c-cpu 8000 --c-gpu 1423 --m2 11400000 --eta-new 1.0
#
#   python parametersFromMeasurements_cli.py --help
#
# Notes:
# - --p-elig accepts multiple entries like: --p-elig 1=426 --p-elig 2=2230 --p-elig 3=2765
# - Use --use-tp to indicate numbers are from throughput mode; omit it (or add --use-time) for timing mode.
# - If you omit costs, Phase-2 economics will be skipped.
#
from dataclasses import dataclass
from typing import Dict, List, Optional
import argparse
import numpy as np


@dataclass
class FitLine:
    intercept: float
    slope: float
    r2: float


def linear_fit_k(P_by_k: Dict[int, float]) -> FitLine:
    ks = np.array(sorted(P_by_k.keys()), dtype=float)
    Ps = np.array([P_by_k[int(k)] for k in ks], dtype=float)
    A = np.vstack([np.ones_like(ks), ks]).T
    # Least squares
    x, *_ = np.linalg.lstsq(A, Ps, rcond=None)
    a, b = x  # intercept, slope
    # R^2
    yhat = A @ x
    ss_res = np.sum((Ps - yhat) ** 2)
    ss_tot = np.sum((Ps - Ps.mean()) ** 2) if len(Ps) > 1 else 0.0
    r2 = 1.0 - ss_res / ss_tot if ss_tot > 0 else 1.0
    return FitLine(intercept=float(a), slope=float(b), r2=float(r2))


def compute_alpha(P_cpu_full: float, H: float) -> float:
    if H <= 0 or P_cpu_full <= 0:
        raise ValueError("H and P_cpu_full must be > 0")
    return P_cpu_full / H


def compute_G(p_gpu: float, P_cpu_elig_c: float) -> float:
    if P_cpu_elig_c <= 0:
        raise ValueError("P_cpu_elig_c must be > 0")
    return p_gpu / P_cpu_elig_c


def hs23_per_gpu(p_gpu: float, alpha: float) -> float:
    if alpha <= 0:
        raise ValueError("alpha must be > 0")
    return p_gpu / alpha


def amdahl_speedup(f: float, G_eff: float, k: int) -> float:
    return 1.0 / ((1.0 - f) + (f / (G_eff * max(k, 1))))


def phase2_sigma_eff(
    f: float, sigma_cpu: float, sigma_gpu: float, eta_new: float = 1.0
) -> float:
    # Harmonic mean blend of per-$ capacities
    return 1.0 / ((1.0 - f) / sigma_cpu + f / (eta_new * sigma_gpu))


def summarize_results(
    H: float,
    P_cpu_full: float,
    Speedup_gpu: Dict[str, float],
    P_cpu_elig_c: float,
    P_elig_by_k: Dict[int, float],
    f_scenarios: List[float],
    C_cpu: Optional[float] = None,
    C_gpu: Optional[float] = None,
    M2: Optional[float] = None,
    eta_new: float = 1.0,
):
    print("=== Inputs ===")
    print(f"H (CPU HS23 from IT):              {H:.4f}")
    print(f"P_cpu_full (CPU-only full pipe):   {P_cpu_full:.4f} ev/s")
    print(f"P_cpu_elig_c (CPU-eligible):       {P_cpu_elig_c:.4f} ev/s")

    for k in sorted(P_elig_by_k.keys()):
        print(f"P_elig({k}) (eligible-only with {k} GPUs): {P_elig_by_k[k]:.4f} ev/s")

    alpha = compute_alpha(P_cpu_full, H)

    if len(P_elig_by_k.keys()) == 1:
        k1 = next(iter(P_elig_by_k))
        p_gpu = P_elig_by_k[k1]
        fit = None
    else:
        fit = linear_fit_k(P_elig_by_k)
        # The per-GPU eligible throughput at k=1 predicted by the fit:
        p_gpu = fit.slope * 1 + fit.intercept

    G = compute_G(p_gpu, P_cpu_elig_c)
    S = 1
    if Speedup_gpu["useTP"]:
        print(Speedup_gpu)
        S = p_gpu / Speedup_gpu["CPU"]
    else:
        S = Speedup_gpu["CPU"] / p_gpu
    k = Speedup_gpu["numGPUs"]
    fraction = k * G * (1 - 1 / S) / (k * G - 1)
    H_gpu0 = G * H

    print("\n=== Derived ===")
    print(f"alpha (events per HS23):           {alpha:.6f}")
    if fit is None:
        print(f"Eligible-only: {p_gpu:.3f} ev/s with 1 GPU (no fit available)")
    else:
        print(
            f"Eligible-only fit: P(k) = a + b k, a={fit.intercept:.3f}, b={fit.slope:.3f}, R^2={fit.r2:.4f}"
        )
    print(f"p_gpu (per-GPU eligible throughput): {p_gpu:.3f} ev/s")
    print(f"G (eligible speedup vs CPU):         {G:.3f} x")
    print(f"S (speedup of full code):            {S:.3f} x with {k} GPUs")
    print(f"f (fraction of full code ported):    {100 * fraction:.1f}%")
    print(f"H_gpu0 (HS23 per GPU):               {H_gpu0:.6f} HS23/GPU")

    # Optional per-$ and Phase-2
    if C_cpu is not None and C_gpu is not None:
        sigma_cpu = H / C_cpu
        sigma_gpu = H_gpu0 / C_gpu
        print(f"\nsigma_cpu (HS23 per $ CPU):        {sigma_cpu:.8f}")
        print(f"sigma_gpu (HS23 per $ per-GPU):    {sigma_gpu:.8f}")
        if M2 is not None:
            for f in f_scenarios:
                sig_eff = phase2_sigma_eff(f, sigma_cpu, sigma_gpu, eta_new=eta_new)
                H_gain = sig_eff * M2
                print(
                    f"Phase-2: f={f:.3f} → sigma_eff={sig_eff:.8f}, HS23 gain from M2={H_gain:.3f}"
                )

    # Predict box-level speedups for k=1..4 under each f using G_eff=G
    print("\n=== Predicted box-level speedup S_k for k=1..4 (fixed CPU budget) ===")
    for f in f_scenarios:
        S_list = [amdahl_speedup(f, G, k) for k in [1, 2, 3, 4]]
        print(
            f"f={f:.3f}: S1={S_list[0]:.3f}, S2={S_list[1]:.3f}, S3={S_list[2]:.3f}, S4={S_list[3]:.3f}"
        )
        P_pred = [P_cpu_full * s for s in S_list]
        print(f"        P(k) ev/s: {', '.join(f'{p:.1f}' for p in P_pred)}")


def _parse_p_elig(values: List[str]) -> Dict[int, float]:
    out: Dict[int, float] = {}
    for item in values:
        if "=" in item:
            k_str, v_str = item.split("=", 1)
        elif ":" in item:
            k_str, v_str = item.split(":", 1)
        else:
            raise argparse.ArgumentTypeError(
                "--p-elig entry '{item}' must be like k=val or k:val"
            )
        try:
            k = int(k_str.strip())
            v = float(v_str.strip())
        except ValueError:
            raise argparse.ArgumentTypeError(
                "--p-elig entry '{item}' has invalid number formats"
            )
        if k < 1:
            raise argparse.ArgumentTypeError("--p-elig k must be >= 1")
        out[k] = v
    return out


def build_arg_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        description="Extrapolate GPU/CPU farm metrics from measured data (CLI version).",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    # TDR defaults carried over from the original script
    TDR_defaults = {
        "H": 1679.0,
        "P_cpu_full": 32.2,
        "num_gpus": 1,
        "use_tp": True,
        "cpu_secs": 638.0,
        "gpu_secs": 426.0,
        "P_cpu_elig_c": 638.0,
        "P_elig_by_k": {1: 426.0},
        "f_scenarios": [],
        "C_cpu": None,
        "C_gpu": None,
        "M2": None,
        "eta_new": 1.0,
    }

    p.add_argument(
        "--H", type=float, default=TDR_defaults["H"], help="IT HS23 for CPU (H)"
    )
    p.add_argument(
        "--p-cpu-full",
        type=float,
        default=TDR_defaults["P_cpu_full"],
        help="CPU-only full pipeline throughput (events/s) with GPUs off",
    )
    p.add_argument(
        "--num-gpus",
        type=int,
        default=TDR_defaults["num_gpus"],
        help="Number of GPUs used in the measured speedup",
    )
    g_mode = p.add_mutually_exclusive_group()
    g_mode.add_argument(
        "--use-tp",
        dest="use_tp",
        action="store_true",
        help="Indicates numbers are from throughput mode",
    )
    g_mode.add_argument(
        "--use-time",
        dest="use_tp",
        action="store_false",
        help="Indicates numbers are from timing mode",
    )
    p.set_defaults(use_tp=TDR_defaults["use_tp"])
    #    p.add_argument(
    #        "--cpu-secs",
    #        type=float,
    #        default=TDR_defaults["cpu_secs"],
    #        help="CPU time/throughput value used for the speedup ratio (units depend on mode)",
    #    )
    #    p.add_argument(
    #        "--gpu-secs",
    #        type=float,
    #        default=TDR_defaults["gpu_secs"],
    #        help="GPU time/throughput value used for the speedup ratio (units depend on mode)",
    #    )
    p.add_argument(
        "--p-cpu-elig-c",
        type=float,
        default=TDR_defaults["P_cpu_elig_c"],
        help="Eligible-only CPU baseline throughput at the slice that feeds one GPU (events/s)",
    )
    p.add_argument(
        "--p-elig",
        action="append",
        default=None,
        metavar="k=val",
        help="Eligible-only throughput (events/s) with k GPUs; repeatable: --p-elig 1=426 --p-elig 2=2230 ...",
    )
    p.add_argument(
        "--f",
        dest="f_scenarios",
        action="append",
        type=float,
        default=None,
        help="Scenario f value(s) to forecast; repeat for multiple",
    )
    p.add_argument(
        "--c-cpu",
        type=float,
        default=TDR_defaults["C_cpu"],
        help="Cost attributed to CPU complex (optional)",
    )
    p.add_argument(
        "--c-gpu",
        type=float,
        default=TDR_defaults["C_gpu"],
        help="Cost per GPU (optional)",
    )
    p.add_argument(
        "--m2", type=float, default=TDR_defaults["M2"], help="Phase-2 budget (optional)"
    )
    p.add_argument(
        "--eta-new",
        type=float,
        default=TDR_defaults["eta_new"],
        help="GPU perf factor at Phase-2 (if newer GPU model)",
    )
    return p


def main(argv=None):
    parser = build_arg_parser()
    args = parser.parse_args(argv)

    # Convert p-elig entries
    if args.p_elig is None:
        P_elig_by_k = {1: 426.0}  # TDR default
    else:
        P_elig_by_k = _parse_p_elig(args.p_elig)

    # Convert f scenarios
    if args.f_scenarios is None:
        f_scenarios: List[float] = []
    else:
        f_scenarios = args.f_scenarios

    Speedup_gpu = {
        "numGPUs": int(args.num_gpus),
        "useTP": bool(args.use_tp),
        "CPU": float(args.p_cpu_elig_c),
    }

    summarize_results(
        H=float(args.H),
        P_cpu_full=float(args.p_cpu_full),
        Speedup_gpu=Speedup_gpu,
        P_cpu_elig_c=float(args.p_cpu_elig_c),
        P_elig_by_k=P_elig_by_k,
        f_scenarios=f_scenarios,
        C_cpu=args.c_cpu,
        C_gpu=args.c_gpu,
        M2=args.m2,
        eta_new=float(args.eta_new),
    )


if __name__ == "__main__":
    main()
