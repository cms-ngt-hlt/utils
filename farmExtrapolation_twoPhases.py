#!/usr/bin/env python3
"""
Two-phase HS23 model (NGT_Task311) — Run 5 ignores aged Run 4 hardware.
We *only* consider, at t2, the replacement of a Run 4-sized HS23 farm using
the f2 CPU/GPU split (external re-buy). That capacity is included; its cost is
reported but does not reduce M2. Then we allocate M2 optimally to extend t2.

What this script does
---------------------
1) Run 4 (t1): optimize split and report TP1 and HS23 pools.
2) Compute external re-buy at t2 to match Run 4 total HS23 with split f2.
3) Run 5 (t2): ignore aged Run 4; start from external re-buy only;
   allocate M2 optimally to meet harsher conditions.
4) Wrong-model cross-checks (fixed split, naive HS23 sum).
5) Integerized node counts.

"""

import argparse
import json
import math
from datetime import datetime

BASELINE = datetime(2025, 1, 1)


def years_from_baseline(start_date_str):
    t1 = datetime.strptime(start_date_str, "%Y-%m-%d")
    return (t1 - BASELINE).days / 365.25


def resolve_alpha2(alpha1, args):
    if args.T0_phase2 is not None or args.H0_phase2 is not None:
        if args.T0_phase2 is None or args.H0_phase2 is None:
            raise SystemExit("Provide both --T0-phase2 and --H0-phase2, or neither.")
        if args.T0_phase2 <= 0 or args.H0_phase2 <= 0:
            raise SystemExit("--T0-phase2 and --H0-phase2 must be positive.")
        return args.T0_phase2 / args.H0_phase2
    if args.alpha2_over_alpha1 is not None:
        if args.alpha2_over_alpha1 <= 0:
            raise SystemExit("--alpha2-over-alpha1 must be > 0.")
        return alpha1 * args.alpha2_over_alpha1
    if args.complexity2 is not None:
        if args.complexity2 <= 0:
            raise SystemExit("--complexity2 must be > 0.")
        return alpha1 / args.complexity2
    return alpha1


def clamp01(x):
    return max(0.0, min(1.0, x))


def parse_args():
    p = argparse.ArgumentParser(
        description="Two-phase HS23 model with external Run 5re-buy; no aged carryover at t2."
    )
    # Common /Run 4
    p.add_argument(
        "--lambda-khz", type=float, required=True, help="Run-4 input rate in kHz."
    )
    p.add_argument(
        "--T0",
        type=float,
        required=True,
        help="CPU reference throughput at t1 (events/s).",
    )
    p.add_argument("--H0", type=float, required=True, help="CPU HS23 at t1 baseline.")
    p.add_argument("--C0", type=float, required=True, help="CPU unit cost [$].")

    p.add_argument(
        "--Hgpu0", type=float, help="GPU HS23-equivalent at baseline (per GPU)."
    )
    p.add_argument("--Cgpu", type=float, help="GPU unit cost [$].")

    p.add_argument(
        "--f1", type=float, default=0.0, help="GPUable fraction at phase 1 (0..1)."
    )
    p.add_argument("--budget1", type=float, required=True, help="Run-4 budget M1 [$].")

    p.add_argument(
        "--g", type=float, required=True, help="Annual perf/$ improvement (fraction)."
    )

    # Timing
    p.add_argument("--start-date", type=str, help="YYYY-MM-DD")
    p.add_argument("--delta-years", type=float, help="Years from 2025-01-01 to start.")
    p.add_argument(
        "--epsilon", type=float, default=1.0, help="Global efficiency in (0,1]."
    )

    # Run-5
    p.add_argument(
        "--years-after",
        type=float,
        required=True,
        help="Years after start for Run-5.",
    )
    p.add_argument("--budget2", type=float, required=True, help="Run-5 budget M2 [$].")
    p.add_argument(
        "--f2", type=float, default=0.0, help="GPUable fraction at phase 2 (0..1)."
    )
    p.add_argument(
        "--lambda2-khz",
        type=float,
        help="Run-5 input rate in kHz (defaults to lambda-khz).",
    )

    # alpha2 resolution
    p.add_argument(
        "--T0-phase2", type=float, help="CPU reference throughput at t2 (events/s)."
    )
    p.add_argument("--H0-phase2", type=float, help="CPU HS23 at t2 baseline.")
    p.add_argument("--alpha2-over-alpha1", type=float, help="alpha2 = alpha1 * X.")
    p.add_argument("--complexity2", type=float, help="alpha2 = alpha1 / complexity2.")

    # Aging / compatibility (still reported; not used in t2 optimization)
    p.add_argument("--age-cpu-per-year", type=float, default=1.0)
    p.add_argument("--age-gpu-per-year", type=float, default=1.0)
    p.add_argument("--chi-old", type=float, default=1.0)
    p.add_argument("--eta-old", type=float, default=1.0)
    p.add_argument("--eta-new", type=float, default=1.0)

    # Integerization helper
    p.add_argument(
        "--Cref-cpu",
        type=float,
        help="Per-CPU-node spend for integer counts (defaults to C0).",
    )

    # Output
    p.add_argument("--json", action="store_true")
    return p.parse_args()


def compute(args):
    # Times
    if args.start_date:
        Delta = years_from_baseline(args.start_date)
    elif args.delta_years is not None:
        Delta = args.delta_years
    else:
        raise SystemExit("Provide either --start-date or --delta-years.")
    N = args.years_after

    # Sanity
    req_positive = [
        ("lambda-khz", args.lambda_khz),
        ("T0", args.T0),
        ("H0", args.H0),
        ("C0", args.C0),
        ("budget1", args.budget1),
        #        ("g", args.g),
        #        ("years-after", args.years_after),
        ("budget2", args.budget2),
        ("epsilon", args.epsilon),
    ]
    for name, val in req_positive:
        if val is None or val <= 0:
            raise SystemExit(f"--{name} must be > 0.")

    f1 = clamp01(args.f1)
    f2 = clamp01(args.f2)
    eps = args.epsilon

    # alpha
    alpha1 = args.T0 / args.H0
    alpha2 = resolve_alpha2(alpha1, args)

    # Growth
    growth1 = (1.0 + args.g) ** Delta
    growth2 = (1.0 + args.g) ** (Delta + N)

    # Per-dollar capacities
    sigma0_cpu = args.H0 / args.C0
    sigma1_cpu = sigma0_cpu * growth1
    sigma2_cpu = sigma0_cpu * growth2

    use_gpu = (
        args.Hgpu0 is not None
        and args.Hgpu0 > 0
        and args.Cgpu is not None
        and args.Cgpu > 0
    )
    if use_gpu:
        sigma0_gpu = args.Hgpu0 / args.Cgpu
        sigma1_gpu = sigma0_gpu * growth1
        sigma2_gpu = sigma0_gpu * growth2
    else:
        sigma1_gpu = sigma2_gpu = 0.0

    # ---------------- Run-4 (optimal split) ----------------
    if use_gpu and f1 > 0:
        a1 = sigma1_cpu / (1.0 - f1)
        b1 = sigma1_gpu / f1
        M1_cpu_star = (b1 / (a1 + b1)) * args.budget1 if (a1 + b1) > 0 else 0.0
        M1_cpu_star = max(0.0, min(args.budget1, M1_cpu_star))
        M1_gpu_star = args.budget1 - M1_cpu_star
        TP1_opt = (
            eps * alpha1 * (a1 * b1 / (a1 + b1)) * args.budget1
            if (a1 + b1) > 0
            else 0.0
        )
    else:
        rho1 = (args.T0 / args.C0) * growth1
        M1_cpu_star = args.budget1
        M1_gpu_star = 0.0
        TP1_opt = eps * rho1 * args.budget1

    H1_cpu = sigma1_cpu * M1_cpu_star
    H1_gpu = sigma1_gpu * M1_gpu_star if use_gpu else 0.0
    H1_total = H1_cpu + H1_gpu

    # Aged Run-4 pools (reported but not used at t2)
    H1_cpu_eff = (args.age_cpu_per_year**N) * H1_cpu
    H1_gpu_eff = (args.chi_old * args.eta_old * (args.age_gpu_per_year**N)) * H1_gpu

    # ---------------- Run-5: external re-buy only (base) ----------------
    H_equiv_cpu_target = (1.0 - f2) * H1_total
    H_equiv_gpu_target = f2 * H1_total

    M_equiv_cpu = (H_equiv_cpu_target / sigma2_cpu) if sigma2_cpu > 0 else float("inf")
    if use_gpu and sigma2_gpu > 0 and args.eta_new > 0 and f2 > 0:
        M_equiv_gpu = H_equiv_gpu_target / (args.eta_new * sigma2_gpu)
    else:
        M_equiv_gpu = 0.0 if f2 == 0.0 else float("inf")
    M_equiv_total = M_equiv_cpu + M_equiv_gpu

    # Base at t2 ignores aged Run-4; only re-buy counts
    Hbase_cpu_t2 = H_equiv_cpu_target
    Hbase_gpu_t2 = H_equiv_gpu_target

    # ---------------- Run-5 (optimal split of our M2) ----------------
    if use_gpu and f2 > 0:
        A = sigma2_cpu / (1.0 - f2)
        B = (args.eta_new * sigma2_gpu) / f2
        C_cpu = Hbase_cpu_t2 / (1.0 - f2)

        M2_cpu_star = ((B * args.budget2) / (A + B)) if (A + B) > 0 else 0.0
        M2_cpu_star = max(0.0, min(args.budget2, M2_cpu_star))
        M2_gpu_star = args.budget2 - M2_cpu_star

        L_bal = ((A * B * args.budget2) / (A + B)) if (A + B) > 0 else 0.0
        TP2_opt = eps * alpha2 * (L_bal + H1_total)
    else:
        A = sigma2_cpu
        C_cpu = Hbase_cpu_t2
        M2_cpu_star = args.budget2
        M2_gpu_star = 0.0
        L_bal = C_cpu + A * M2_cpu_star
        TP2_opt = eps * alpha2 * L_bal

    # ---------------- Comparators ----------------
    if use_gpu and f2 > 0:
        M2_cpu_fixed = (1.0 - f2) * args.budget2
        M2_gpu_fixed = f2 * args.budget2
        Rcpu2_fixed = (
            eps * alpha2 * ((Hbase_cpu_t2 + sigma2_cpu * M2_cpu_fixed) / (1.0 - f2))
        )
        Rgpu2_fixed = (
            eps
            * alpha2
            * ((Hbase_gpu_t2 + args.eta_new * sigma2_gpu * M2_gpu_fixed) / f2)
        )
        TP2_fixed = min(Rcpu2_fixed, Rgpu2_fixed)
    else:
        TP2_fixed = eps * alpha2 * (Hbase_cpu_t2 + sigma2_cpu * args.budget2)

    if use_gpu and f2 > 0 and sigma2_cpu > 0 and sigma2_gpu > 0:
        denom = (1.0 - f2) / sigma2_cpu + f2 / sigma2_gpu
        sigma_eff2 = 1.0 / denom if denom > 0 else 0.0
    else:
        sigma_eff2 = sigma2_cpu
    TP2_naive = eps * alpha2 * (Hbase_cpu_t2 + Hbase_gpu_t2 + sigma_eff2 * args.budget2)

    # ---------------- Speed-ups vs load ----------------
    lam2 = args.lambda2_khz if args.lambda2_khz is not None else args.lambda_khz
    s_req_t1 = (1000.0 * args.lambda_khz) / TP1_opt if TP1_opt > 0 else float("inf")
    s_req_t2 = (1000.0 * lam2) / TP2_opt if TP2_opt > 0 else float("inf")
    s_fixed = (1000.0 * lam2) / TP2_fixed if TP2_fixed > 0 else float("inf")
    s_naive = (1000.0 * lam2) / TP2_naive if TP2_naive > 0 else float("inf")

    # ---------------- Integerized counts ----------------
    Cref_cpu = args.Cref_cpu if (args.Cref_cpu and args.Cref_cpu > 0) else args.C0
    N1_cpu = math.floor(M1_cpu_star / Cref_cpu) if Cref_cpu > 0 else 0
    N1_gpu = (
        math.floor(M1_gpu_star / args.Cgpu)
        if (use_gpu and args.Cgpu and args.Cgpu > 0)
        else 0
    )
    N2_cpu = math.floor(M2_cpu_star / Cref_cpu) if Cref_cpu > 0 else 0
    N2_gpu = (
        math.floor(M2_gpu_star / args.Cgpu)
        if (use_gpu and args.Cgpu and args.Cgpu > 0)
        else 0
    )

    res = {
        "phase1": {
            "alpha1_events_per_HS23": alpha1,
            "required_HS23": args.lambda_khz * 1000 / alpha1,
            "sigma1_cpu_HS23_per_$": sigma1_cpu,
            "sigma1_gpu_HS23_per_$": sigma1_gpu if use_gpu else 0.0,
            "f1": f1,
            "M1_cpu_star": M1_cpu_star,
            "M1_gpu_star": M1_gpu_star,
            "H1_cpu_HS23": H1_cpu,
            "H1_gpu_HS23": H1_gpu,
            "H1_total_HS23": H1_total,
            "TP1_Farm_events_per_s": TP1_opt,
            "s_req_t1": max(1.0, s_req_t1),
        },
        "phase2": {
            "general": {
                "alpha2_events_per_HS23": alpha2,
                "required_HS23": args.lambda2_khz * 1000 / alpha2,
                "sigma2_cpu_HS23_per_$": sigma2_cpu,
                "sigma2_gpu_HS23_per_$": sigma2_gpu if use_gpu else 0.0,
                "f2": f2,
            },
            "aging_phase1_report_only": {
                "H1_cpu_eff_HS23": H1_cpu_eff,
                "H1_gpu_eff_HS23": H1_gpu_eff,
                "chi_old": args.chi_old,
                "eta_old": args.eta_old,
                "age_gpu_per_year": args.age_gpu_per_year,
                "age_cpu_per_year": args.age_cpu_per_year,
                "note": "Aged Run-4 is IGNORED in t2 optimization per latest hypothesis.",
            },
            "external_rebuy_base": {
                "H_equiv_cpu_HS23": H_equiv_cpu_target,
                "H_equiv_gpu_HS23": H_equiv_gpu_target,
                "H_equiv_total_HS23": H_equiv_gpu_target + H_equiv_cpu_target,
                "M_equiv_total_$": M_equiv_total,
                "M_equiv_cpu_$": M_equiv_cpu,
                "M_equiv_gpu_$": M_equiv_gpu,
                "eta_new": args.eta_new,
                "note": "This capacity is INCLUDED at t2; cost is external and does not reduce M2.",
            },
            "optimal_split": {
                "M2_cpu_star_$": M2_cpu_star,
                "M2_gpu_star_$": M2_gpu_star,
            },
            "TP2_Farm_events_per_s": TP2_opt,
            "s_req_t2": max(1.0, s_req_t2),
            "wrong_models": {
                "TP2_fixed_events_per_s": TP2_fixed,
                "s_fixed": max(1.0, s_fixed),
                "TP2_naive_events_per_s": TP2_naive,
                "s_naive": max(1.0, s_naive),
            },
        },
        "integers": {
            "Cref_cpu_$": Cref_cpu,
            "N1_cpu": N1_cpu,
            "N1_gpu": N1_gpu,
            "N2_cpu": N2_cpu,
            "N2_gpu": N2_gpu,
        },
    }
    return res


def main():
    args = parse_args()
    res = compute(args)
    if args.json:
        print(json.dumps(res, indent=2))
        return

    print("\n=== Run 4 (t1) ===")
    for k, v in res["phase1"].items():
        print(f"{k:32s}: {v}")

    print("\n=== Run 5 (t2) ===")
    for k, v in res["phase2"]["general"].items():
        print(f"{k:32s}: {v}")

    print("\n=== Run 5 (t2) External Re-buy Base ONLY ===")
    for k, v in res["phase2"]["external_rebuy_base"].items():
        print(f"{k:32s}: {v}")

    print("\n=== Run 5 (t2) Results (Aged Run-4 Ignored) ===")
    print(f"{'TP2_Farm_events_per_s':32s}: {res['phase2']['TP2_Farm_events_per_s']}")
    print(f"{'s_req_t2':32s}: {res['phase2']['s_req_t2']}")

    print("\n   Wrong-model cross-checks:")
    for k, v in res["phase2"]["wrong_models"].items():
        print(f"   {k:30s}: {v}")

    print("\n=== Integerized counts (rounded) ===")
    for k, v in res["integers"].items():
        print(f"{k:32s}: {v}")


if __name__ == "__main__":
    main()
