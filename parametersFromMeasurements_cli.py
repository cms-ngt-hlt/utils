#!/usr/bin/env python3
#
# CLI tool to extrapolate GPU/CPU farm metrics from measured data,
# and to reason about Amdahl fractions and ported-code fraction.
#
# Example:
#   python parametersFromMeasurements_cli.py \
#       --H 1679 --p-cpu-full 32.2 \
#       --num-gpus 1 --use-tp --cpu-meas 638 --gpu-meas 426 \
#       --p-cpu-elig-c 638 --p-elig 1=426 \
#       --u 0.55 \
#       --f 0.463 --f 0.5 --f 0.8
#
#   python parametersFromMeasurements_cli.py --help
#
# Notes:
# - --p-elig accepts multiple entries like: --p-elig 1=426 --p-elig 2=2230 --p-elig 3=2765
# - Use --use-tp when the CPU/GPU measurement values (--cpu-meas/--gpu-meas) are throughputs
#   in events per second (ev/s). Use --use-time when they are time-per-event measurements
#   in milliseconds per event (ms/v).
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


def amdahl_speedup(f: float, G: float, k: int) -> float:
    """
    Amdahl speedup with GPU speedup G on fraction f of the runtime,
    using k GPUs (assuming ideal scaling in the eligible part).

    S = 1 / ((1 - f) + f / (G * k))
    """
    return 1.0 / ((1.0 - f) + (f / (G * max(k, 1))))


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
    u: float = 1.0,
):
    """
    u is the measured average per-GPU utilization on the full workflow (0 < u <= 1).

    This function:
      1. Computes G (eligible-only speedup) from eligible-only measurements.
      2. Computes S_full from CPU/GPU full-workflow measurements.
      3. Computes:
         - f_inf = 1 - 1 / S_full  (ideal G->infinity estimate of ported fraction)
         - f_amdahl = G*k*(1 - 1/S_full)/(G*k - 1)
                     = (1 - 1/S_full)/(1 - 1/(G*k))
           (finite-G Amdahl effective fraction with k GPUs)
      4. Uses u ONLY as a diagnostic:
         - f_port_from_u = u * G * k / S_full  (from u = f_port * S_full / (G*k))
         - u_max         = S_full / (G * k)
         - u_implied_from_finf = f_inf * S_full / (G * k)
         and prints warnings if the triple (S_full, G, k, u) is inconsistent
         with the simple Amdahl model where GPUs only work on the ported part.
    """

    if u <= 0.0:
        raise ValueError("u must be > 0")

    print("=== Inputs ===")
    print(f"H (CPU HS23 from IT):              {H:.4f}")
    print(f"P_cpu_full (CPU-only full pipe):   {P_cpu_full:.4f} ev/s")
    print(f"P_cpu_elig_c (CPU-eligible):       {P_cpu_elig_c:.4f} ev/s")
    print(f"u (per-GPU utilization, full wf):  {u:.3f}")

    for kk in sorted(P_elig_by_k.keys()):
        print(
            f"P_elig({kk}) (eligible-only with {kk} GPUs): {P_elig_by_k[kk]:.4f} ev/s"
        )

    # Raw measurements used for the speedup ratio
    unit_label = "ev/s" if Speedup_gpu["useTP"] else "ms/v"
    print("\n=== Raw speedup inputs ===")
    print(f"CPU measurement for speedup:       {Speedup_gpu['CPU']:.4f} {unit_label}")
    print(f"GPU measurement for speedup:       {Speedup_gpu['GPU']:.4f} {unit_label}")

    alpha = compute_alpha(P_cpu_full, H)

    # Derive per-GPU eligible throughput p_gpu from eligible-only measurements.
    # Here the GPU is assumed to be at ~100% utilization for the eligible kernels.
    k_single: Optional[int] = None
    if len(P_elig_by_k.keys()) == 1:
        # Only one measurement available: assume a line passing through
        # (k=0, P_cpu_elig_c) and (k=k1, P_elig(k1)), and use that to infer
        # the total eligible-only throughput at k=1.
        k1 = next(iter(P_elig_by_k))
        k_single = k1
        P_total_k1 = P_elig_by_k[k1]
        # P(k) = P_cpu_elig_c + ((P_total_k1 - P_cpu_elig_c) / k1) * k
        # so P(1) = P_cpu_elig_c + (P_total_k1 - P_cpu_elig_c) / k1
        p_gpu = P_cpu_elig_c + (P_total_k1 - P_cpu_elig_c) / k1
        fit = None
    else:
        fit = linear_fit_k(P_elig_by_k)
        # The per-GPU eligible throughput at k=1 predicted by the fit:
        p_gpu = fit.slope * 1 + fit.intercept

    # Ideal (eligible-only) speedup for the GPU-eligible slice (per GPU)
    G = compute_G(p_gpu, P_cpu_elig_c)

    # Measured full-pipeline speedup S_full (no manipulation by u).
    if Speedup_gpu["useTP"]:
        S_full = Speedup_gpu["GPU"] / Speedup_gpu["CPU"]
    else:
        S_full = Speedup_gpu["CPU"] / Speedup_gpu["GPU"]
    k = Speedup_gpu["numGPUs"]

    # --- Amdahl and ported-fraction diagnostics ---

    # Ideal infinite-G estimate of ported fraction (independent of k):
    f_inf = 1.0 - 1.0 / S_full

    # Finite-G Amdahl effective fraction with k GPUs:
    # S_full = 1 / ((1 - f) + f/(G*k)) => f = G*k*(1 - 1/S_full)/(G*k - 1)
    denom = G * k - 1.0
    if abs(denom) < 1e-12:
        f_amdahl = float("nan")
    else:
        f_amdahl = (G * k * (1.0 - 1.0 / S_full)) / denom

    # Clamp for interpretability
    if not np.isnan(f_inf):
        f_inf = max(0.0, min(1.0, f_inf))
    if not np.isnan(f_amdahl):
        f_amdahl = max(0.0, min(1.0, f_amdahl))

    # From per-GPU utilization equation in the simple model:
    #   u = f_port * S_full / (G*k)  =>  f_port = u * G * k / S_full
    f_port_from_u = u * G * k / S_full
    # Upper bound on utilization if f_port <= 1:
    u_max = S_full / (G * k)

    # u implied if f_port ≈ f_inf:
    u_implied_from_finf = f_inf * S_full / (G * k)

    H_gpu0 = G * H  # Ideal per-GPU HS23 (from eligible-only measurement)

    print("\n=== Derived (Amdahl / ported-fraction view) ===")
    print(f"alpha (events per HS23):           {alpha:.6f}")
    if fit is None:
        if k_single is None:
            print(f"Eligible-only: {p_gpu:.3f} ev/s per GPU (no fit available)")
        else:
            total = P_elig_by_k[k_single]
            print(
                f"Eligible-only: {total:.3f} ev/s total with {k_single} GPU(s) "
                f"(anchored on CPU baseline {P_cpu_elig_c:.3f} ev/s) "
                f"→ inferred P_elig(1) = {p_gpu:.3f} ev/s"
            )
    else:
        print(
            f"Eligible-only fit: P(k) = a + b k, a={fit.intercept:.3f}, "
            f"b={fit.slope:.3f}, R^2={fit.r2:.4f}"
        )
    print(f"p_gpu (eligible-only at 1 GPU):     {p_gpu:.3f} ev/s")
    print(f"G (eligible speedup vs CPU, ideal): {G:.3f} x")
    print(f"S_full (full pipeline speedup):     {S_full:.3f} x with {k} GPUs")

    print(f"f_inf (G→∞ ported fraction est):    {100.0 * f_inf:.1f}%")
    if np.isnan(f_amdahl):
        print("f_amdahl (finite-G Amdahl fraction):  n/a (G*k very close to 1)")
    else:
        print(
            f"f_amdahl (finite-G Amdahl fraction): {100.0 * f_amdahl:.1f}% "
            "(effective accelerated time share with finite G and k)"
        )

    print(
        f"f_port_from_u (from u = f_port*S/(G*k)): {100.0 * f_port_from_u:.1f}% "
        "(>100% means the simple no-overlap model is violated)"
    )
    print(f"u_max (max per-GPU u if f_port<=1):      {100.0 * u_max:.1f}%")
    print(
        f"u_implied_from_finf (if f_port≈f_inf):   {100.0 * u_implied_from_finf:.1f}%"
    )

    # Warnings about contradictions in the simple model
    eps = 1e-3
    if f_port_from_u > 1.0 + eps:
        print(
            "\n[Warning] f_port_from_u > 1. This means the triple "
            f"(S_full={S_full:.3f}, G={G:.3f}, k={k}, u={u:.3f}) cannot be "
            "explained by the simple model where GPUs only work on the ported "
            "fraction with speedup G and no overlap."
        )
    if u > u_max + eps:
        print(
            "[Warning] u > u_max. Under the simple Amdahl+no-overlap model, "
            "this per-GPU utilization is impossible. This indicates additional "
            "GPU activity, overlapping stages, or mismatched baselines."
        )

    print(f"\nH_gpu0 (HS23 per GPU, ideal eligible-only): {H_gpu0:.6f} HS23/GPU")

    # Idealized perfect-GPU comparison using f_inf as the ported fraction
    if 0.0 <= f_inf < 1.0:
        S_perfect = 1.0 / (1.0 - f_inf)
        P_full_perfect = P_cpu_full * S_perfect
        print(
            f"\n=== Idealized comparison (perfect GPUs, f_port ≈ f_inf={f_inf:.3f}) ==="
        )
        print(f"Ideal speedup S_perfect (G→∞):      {S_perfect:.3f} x")
        print(f"Ideal full-pipe throughput:         {P_full_perfect:.3f} ev/s")
    else:
        print("\n=== Idealized comparison ===")
        print("f_inf not in [0,1], cannot form a clean perfect-G comparison.")

    # Optional per-$ and Phase-2
    if C_cpu is not None and C_gpu is not None:
        sigma_cpu = H / C_cpu
        sigma_gpu = H_gpu0 / C_gpu
        print(f"\n=== Economics ===")
        print(f"sigma_cpu (HS23 per $ CPU):        {sigma_cpu:.8f}")
        print(f"sigma_gpu (HS23 per $ per-GPU):    {sigma_gpu:.8f}")
        if M2 is not None:
            for f in f_scenarios:
                # Here, f in scenarios is interpreted as an Amdahl effective fraction
                sig_eff = phase2_sigma_eff(f, sigma_cpu, sigma_gpu, eta_new=eta_new)
                H_gain = sig_eff * M2
                print(
                    f"Phase-2: f_eff={f:.3f} → sigma_eff={sig_eff:.8f}, "
                    f"HS23 gain from M2={H_gain:.3f}"
                )

    # Predict box-level speedups for k=1..4 under each f scenario
    # (interpreting f_scenarios as Amdahl effective fractions)
    print("\n=== Predicted box-level speedup S_k for k=1..4 (fixed CPU budget) ===")
    for f in f_scenarios:
        S_list = [amdahl_speedup(f, G, k_val) for k_val in [1, 2, 3, 4]]
        print(
            f"f_eff={f:.3f}: "
            f"S1={S_list[0]:.3f}, "
            f"S2={S_list[1]:.3f}, "
            f"S3={S_list[2]:.3f}, "
            f"S4={S_list[3]:.3f}"
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
                f"--p-elig entry '{item}' must be like k=val or k:val"
            )
        try:
            k = int(k_str.strip())
            v = float(v_str.strip())
        except ValueError:
            raise argparse.ArgumentTypeError(
                f"--p-elig entry '{item}' has invalid number formats"
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

    # Example defaults
    TDR_defaults = {
        "H": 1679.0,
        "P_cpu_full": 32.2,
        "num_gpus": 1,
        "use_tp": True,
        "cpu_meas": 638.0,
        "gpu_meas": 426.0,
        "P_cpu_elig_c": 638.0,
        "P_elig_by_k": {1: 426.0},
        "f_scenarios": [],
        "C_cpu": None,
        "C_gpu": None,
        "M2": None,
        "eta_new": 1.0,
        "u": 1.0,
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
        help=(
            "Indicates CPU/GPU measurement values (--cpu-meas/--gpu-meas) are "
            "throughputs in events per second (ev/s)"
        ),
    )
    g_mode.add_argument(
        "--use-time",
        dest="use_tp",
        action="store_false",
        help=(
            "Indicates CPU/GPU measurement values (--cpu-meas/--gpu-meas) are "
            "time per event in milliseconds per event (ms/v)"
        ),
    )
    p.set_defaults(use_tp=TDR_defaults["use_tp"])

    p.add_argument(
        "--cpu-meas",
        dest="cpu_meas",
        type=float,
        default=TDR_defaults["cpu_meas"],
        help=(
            "CPU value used for the speedup ratio. "
            "If --use-tp: throughput in events/s (ev/s). "
            "If --use-time: time per event in ms/v."
        ),
    )
    p.add_argument(
        "--gpu-meas",
        dest="gpu_meas",
        type=float,
        default=TDR_defaults["gpu_meas"],
        help=(
            "GPU value used for the speedup ratio. "
            "If --use-tp: throughput in events/s (ev/s). "
            "If --use-time: time per event in ms/v."
        ),
    )
    p.add_argument(
        "--p-cpu-elig-c",
        type=float,
        default=TDR_defaults["P_cpu_elig_c"],
        help=(
            "Eligible-only CPU baseline throughput at the slice that feeds one GPU "
            "(events/s)"
        ),
    )
    p.add_argument(
        "--p-elig",
        action="append",
        default=None,
        metavar="k=val",
        help=(
            "Eligible-only throughput (events/s) with k GPUs; repeatable: "
            "--p-elig 1=426 --p-elig 2=2230 ..."
        ),
    )
    p.add_argument(
        "--f",
        dest="f_scenarios",
        action="append",
        type=float,
        default=None,
        help=(
            "Scenario f_eff value(s) (Amdahl effective fractions) to forecast; "
            "repeat for multiple"
        ),
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
    p.add_argument(
        "--u",
        type=float,
        default=TDR_defaults["u"],
        help=(
            "Average per-GPU utilization on the full workflow (0 < u <= 1). "
            "Used only for consistency checks and for computing "
            "f_port_from_u = u * G * k / S_full."
        ),
    )

    return p


def main(argv=None):
    parser = build_arg_parser()
    args = parser.parse_args(argv)

    # Convert p-elig entries
    if args.p_elig is None:
        P_elig_by_k = {1: 426.0}  # example default
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
        "CPU": float(args.cpu_meas),
        "GPU": float(args.gpu_meas),
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
        u=float(args.u),
    )


if __name__ == "__main__":
    main()
