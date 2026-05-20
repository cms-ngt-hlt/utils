#!/usr/bin/env python3
"""
Pure-math core of the two-phase HS23 farm extrapolation.

Imported by:
- farmExtrapolation_twoPhases.py — the CLI wrapper
- farmExtrapolation_tui.py       — the live Textual UI

All functions in this module are pure (no I/O, no globals beyond BASELINE).
`compute(args)` accepts an argparse-Namespace-like object (anything with the
attribute names produced by `parse_args()`).
"""

import math
from datetime import datetime
from types import SimpleNamespace

BASELINE = datetime(2025, 1, 1)


# ------------------------------------------------------------------ #
#  Helpers                                                            #
# ------------------------------------------------------------------ #

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


def optimal_split(rate_a, rate_b, budget):
    """Optimal budget split for min-of-two-linears.

    Given two per-dollar rates (a = sigma_cpu/(1-f), b = sigma_gpu/f)
    and a total budget, returns (M_a, M_b, L_balanced).
    """
    s = rate_a + rate_b
    m_a = (rate_b / s) * budget
    m_b = budget - m_a
    l_bal = (rate_a * rate_b / s) * budget
    return m_a, m_b, l_bal


# ------------------------------------------------------------------ #
#  Phase computations                                                 #
# ------------------------------------------------------------------ #

def compute_phase1(alpha, eps, f, sigma_cpu, sigma_gpu, budget):
    """Run 4: optimal CPU/GPU split and throughput."""
    if f > 0 and sigma_gpu > 0:
        a = sigma_cpu / (1 - f)
        b = sigma_gpu / f
        M_cpu, M_gpu, L_bal = optimal_split(a, b, budget)
        tp = eps * alpha * L_bal
    else:
        M_cpu = budget
        M_gpu = 0.0
        tp = eps * alpha * sigma_cpu * budget

    H_cpu = sigma_cpu * M_cpu
    H_gpu = sigma_gpu * M_gpu
    return M_cpu, M_gpu, H_cpu, H_gpu, H_cpu + H_gpu, tp


def compute_rebuy(f2, H1_total, sigma2_cpu, sigma2_gpu, eta_new):
    """External re-buy at t2 to match Run 4 total HS23 with split f2."""
    H_cpu = (1 - f2) * H1_total
    H_gpu = f2 * H1_total

    M_cpu = H_cpu / sigma2_cpu if sigma2_cpu > 0 else float("inf")
    if f2 > 0 and sigma2_gpu > 0 and eta_new > 0:
        M_gpu = H_gpu / (eta_new * sigma2_gpu)
    else:
        M_gpu = 0.0 if f2 == 0 else float("inf")

    return H_cpu, H_gpu, M_cpu, M_gpu


def compute_phase2(alpha, eps, f, sigma_cpu, sigma_gpu, eta_new,
                   H1_total, budget):
    """Run 5: optimal allocation of M2 on top of the re-buy base."""
    if f > 0 and sigma_gpu > 0:
        A = sigma_cpu / (1 - f)
        B = (eta_new * sigma_gpu) / f
        M_cpu, M_gpu, L_bal = optimal_split(A, B, budget)
        tp = eps * alpha * (L_bal + H1_total)
    else:
        M_cpu = budget
        M_gpu = 0.0
        tp = eps * alpha * ((1 - f) * H1_total + sigma_cpu * budget)

    return M_cpu, M_gpu, tp


def compute_crosschecks(alpha, eps, f, sigma_cpu, sigma_gpu, eta_new,
                        H_base_cpu, H_base_gpu, budget):
    """Wrong-model comparators: fixed split and naive HS23 sum."""
    # Fixed split
    if f > 0 and sigma_gpu > 0:
        M_cpu_fix = (1 - f) * budget
        M_gpu_fix = f * budget
        R_cpu = eps * alpha * (H_base_cpu + sigma_cpu * M_cpu_fix) / (1 - f)
        R_gpu = eps * alpha * (H_base_gpu + eta_new * sigma_gpu * M_gpu_fix) / f
        tp_fixed = min(R_cpu, R_gpu)
    else:
        tp_fixed = eps * alpha * (H_base_cpu + sigma_cpu * budget)

    # Naive HS23 sum (ignores min constraint)
    if f > 0 and sigma_gpu > 0 and sigma_cpu > 0:
        sigma_eff = 1.0 / ((1 - f) / sigma_cpu + f / sigma_gpu)
    else:
        sigma_eff = sigma_cpu
    tp_naive = eps * alpha * (H_base_cpu + H_base_gpu + sigma_eff * budget)

    return tp_fixed, tp_naive


# ------------------------------------------------------------------ #
#  Main compute orchestrator                                          #
# ------------------------------------------------------------------ #

def compute(args):
    # --- Time ---
    if args.start_date:
        Delta = years_from_baseline(args.start_date)
    elif args.delta_years is not None:
        Delta = args.delta_years
    else:
        raise SystemExit("Provide either --start-date or --delta-years.")
    N = args.years_after

    # --- Input validation ---
    for name, val in [
        ("lambda-khz", args.lambda_khz),
        ("T0", args.T0),
        ("H0", args.H0),
        ("C0", args.C0),
        ("budget1", args.budget1),
        ("budget2", args.budget2),
        ("epsilon", args.epsilon),
    ]:
        if val is None or val <= 0:
            raise SystemExit(f"--{name} must be > 0.")

    for name, val in [("f1", args.f1), ("f2", args.f2)]:
        if not 0.0 <= val <= 1.0:
            raise SystemExit(f"--{name} must be in [0, 1], got {val}.")

    f1, f2 = args.f1, args.f2
    eps = args.epsilon

    # --- GPU normalisation: resolve once, use everywhere ---
    has_gpu = (
        args.Hgpu0 is not None and args.Hgpu0 > 0
        and args.Cgpu is not None and args.Cgpu > 0
    )
    Hgpu0 = args.Hgpu0 if has_gpu else 0.0
    Cgpu = args.Cgpu if has_gpu else 1.0  # avoid division by zero in reporting

    # If no GPU, force GPU fractions to 0
    if not has_gpu:
        f1 = f2 = 0.0

    # --- Derived quantities ---
    alpha1 = args.T0 / args.H0
    alpha2 = resolve_alpha2(alpha1, args)

    growth1 = (1.0 + args.g) ** Delta
    growth2 = (1.0 + args.g) ** (Delta + N)

    sigma0_cpu = args.H0 / args.C0
    sigma1_cpu = sigma0_cpu * growth1
    sigma2_cpu = sigma0_cpu * growth2

    sigma0_gpu = Hgpu0 / Cgpu
    sigma1_gpu = sigma0_gpu * growth1
    sigma2_gpu = sigma0_gpu * growth2

    lam2 = args.lambda2_khz if args.lambda2_khz is not None else args.lambda_khz

    # --- Phase 1 (Run 4) ---
    M1_cpu, M1_gpu, H1_cpu, H1_gpu, H1_total, TP1 = compute_phase1(
        alpha1, eps, f1, sigma1_cpu, sigma1_gpu, args.budget1
    )

    # Aged Run-4 pools (reported only)
    H1_cpu_eff = (args.age_cpu_per_year ** N) * H1_cpu
    H1_gpu_eff = (args.chi_old * args.eta_old * (args.age_gpu_per_year ** N)) * H1_gpu

    # --- External re-buy ---
    H_eq_cpu, H_eq_gpu, M_eq_cpu, M_eq_gpu = compute_rebuy(
        f2, H1_total, sigma2_cpu, sigma2_gpu, args.eta_new
    )

    # --- Phase 2 (Run 5) ---
    M2_cpu, M2_gpu, TP2 = compute_phase2(
        alpha2, eps, f2, sigma2_cpu, sigma2_gpu, args.eta_new,
        H1_total, args.budget2
    )

    # --- Cross-checks ---
    TP2_fixed, TP2_naive = compute_crosschecks(
        alpha2, eps, f2, sigma2_cpu, sigma2_gpu, args.eta_new,
        H_eq_cpu, H_eq_gpu, args.budget2
    )

    # --- Speedups ---
    def speedup(lam_khz, tp):
        return max(1.0, (1000.0 * lam_khz) / tp) if tp > 0 else float("inf")

    s_req_t1 = speedup(args.lambda_khz, TP1)
    s_req_t2 = speedup(lam2, TP2)
    s_fixed = speedup(lam2, TP2_fixed)
    s_naive = speedup(lam2, TP2_naive)

    # --- Integerised counts ---
    Cref_cpu = args.Cref_cpu if (args.Cref_cpu and args.Cref_cpu > 0) else args.C0
    N1_cpu = math.floor(M1_cpu / Cref_cpu)
    N1_gpu = math.floor(M1_gpu / Cgpu) if has_gpu else 0
    N2_cpu = math.floor(M2_cpu / Cref_cpu)
    N2_gpu = math.floor(M2_gpu / Cgpu) if has_gpu else 0

    # --- Assemble result ---
    today = {
        "alpha1_events_per_HS23": alpha1,
        "required_HS23": args.lambda_khz * 1000 / alpha1,
        "CPU HS23/CHF": args.H0 / args.C0,
        "CPU CHF/HS23": args.C0 / args.H0,
    }
    if has_gpu:
        today["GPU HS23/CHF"] = Hgpu0 / Cgpu
        today["GPU CHF/HS23"] = Cgpu / Hgpu0

    return {
        "today": today,
        "phase1": {
            "alpha1_events_per_HS23": alpha1,
            "required_HS23": args.lambda_khz * 1000 / alpha1,
            "sigma1_cpu_HS23_per_$": sigma1_cpu,
            "sigma1_gpu_HS23_per_$": sigma1_gpu,
            "sigma1_cpu_$_per_HS23": 1.0 / sigma1_cpu,
            "sigma1_gpu_$_per_HS23": 1.0 / sigma1_gpu if sigma1_gpu > 0 else 0.0,
            "f1": f1,
            "M1_cpu_star": M1_cpu,
            "M1_gpu_star": M1_gpu,
            "H1_cpu_HS23": H1_cpu,
            "H1_gpu_HS23": H1_gpu,
            "H1_total_HS23": H1_total,
            "TP1_Farm_events_per_s": TP1,
            "s_req_t1": s_req_t1,
        },
        "phase2": {
            "general": {
                "alpha2_events_per_HS23": alpha2,
                "required_HS23": lam2 * 1000 / alpha2,
                "sigma2_cpu_HS23_per_$": sigma2_cpu,
                "sigma2_gpu_HS23_per_$": sigma2_gpu,
                "sigma2_cpu_$_per_HS23": 1.0 / sigma2_cpu,
                "sigma2_gpu_$_per_HS23": 1.0 / sigma2_gpu if sigma2_gpu > 0 else 0.0,
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
                "H_equiv_cpu_HS23": H_eq_cpu,
                "H_equiv_gpu_HS23": H_eq_gpu,
                "H_equiv_total_HS23": H_eq_cpu + H_eq_gpu,
                "M_equiv_total_$": M_eq_cpu + M_eq_gpu,
                "M_equiv_cpu_$": M_eq_cpu,
                "M_equiv_gpu_$": M_eq_gpu,
                "eta_new": args.eta_new,
                "note": "This capacity is INCLUDED at t2; cost is external and does not reduce M2.",
            },
            "optimal_split": {
                "M2_cpu_star_$": M2_cpu,
                "M2_gpu_star_$": M2_gpu,
            },
            "TP2_Farm_events_per_s": TP2,
            "s_req_t2": s_req_t2,
            "wrong_models": {
                "TP2_fixed_events_per_s": TP2_fixed,
                "s_fixed": s_fixed,
                "TP2_naive_events_per_s": TP2_naive,
                "s_naive": s_naive,
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


# ------------------------------------------------------------------ #
#  TUI helper: sigma trajectories over time                           #
# ------------------------------------------------------------------ #

def sigma_trajectory(args, n_points: int = 30, from_t0: bool = False):
    """Return [(t_years, sigma_cpu(t), sigma_gpu(t)), ...] sampled along the
    perf/$ growth curve.

    Two axis modes:
    - `from_t0=False` (default): x ranges over [0, N] with t=0 at t1.
    - `from_t0=True`: x ranges over [0, Δ + N] with t=0 at t0 (the T0/H0
      measurement time); t1 then sits at x = Δ and t2 at x = Δ + N.

    Uses the same exponential perf/$ growth law as `compute()`.
    """
    if args.start_date:
        Delta = years_from_baseline(args.start_date)
    elif args.delta_years is not None:
        Delta = args.delta_years
    else:
        raise SystemExit("Provide either --start-date or --delta-years.")

    N = args.years_after
    if from_t0:
        span = Delta + N
        base_exp = 0.0          # growth exponent at x = 0 (= t0)
    else:
        span = N
        base_exp = Delta        # growth exponent at x = 0 (= t1)
    if span <= 0 or n_points < 2:
        return []

    sigma0_cpu = args.H0 / args.C0
    has_gpu = (
        args.Hgpu0 is not None and args.Hgpu0 > 0
        and args.Cgpu is not None and args.Cgpu > 0
    )
    sigma0_gpu = (args.Hgpu0 / args.Cgpu) if has_gpu else 0.0

    out = []
    for i in range(n_points):
        t = span * i / (n_points - 1)
        growth = (1.0 + args.g) ** (base_exp + t)
        out.append((t, sigma0_cpu * growth, sigma0_gpu * growth))
    return out


# ------------------------------------------------------------------ #
#  Defaults / namespace builder for TUI                               #
# ------------------------------------------------------------------ #

# Default values for every CLI flag. Used by the TUI as initial state and by
# `args_namespace()` to fill in attributes the caller did not override.
ARG_DEFAULTS = {
    # required-but-no-default in CLI: pick sensible starting values
    "lambda_khz": 22.0,
    "T0": 1200.0,
    "H0": 850.0,
    "C0": 2000.0,
    "g": 0.05,
    "budget1": 5_000_000.0,
    "budget2": 3_000_000.0,
    "years_after": 3.5,
    # optional with defaults in CLI
    "Hgpu0": 4000.0,
    "Cgpu": 8000.0,
    "f1": 0.0,
    "f2": 0.0,
    "epsilon": 1.0,
    "start_date": None,
    "delta_years": 0.0,
    "lambda2_khz": None,
    "T0_phase2": None,
    "H0_phase2": None,
    "alpha2_over_alpha1": None,
    "complexity2": None,
    "age_cpu_per_year": 1.0,
    "age_gpu_per_year": 1.0,
    "chi_old": 1.0,
    "eta_old": 1.0,
    "eta_new": 1.0,
    "Cref_cpu": None,
    "json": False,
}


def args_namespace(**overrides) -> SimpleNamespace:
    """Build an argparse-Namespace-compatible object from kwargs.

    Any attribute not provided is filled from ARG_DEFAULTS. Convenient for the
    TUI which builds the namespace from its reactive dict on every recompute.
    """
    merged = dict(ARG_DEFAULTS)
    merged.update(overrides)
    return SimpleNamespace(**merged)
