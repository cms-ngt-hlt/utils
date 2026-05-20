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

The pure-math core lives in `farm_extrapolation_lib`; this script is just the
CLI wrapper around it. For a live, interactive interface use
`farmExtrapolation_tui.py`.
"""

import argparse
import json

from farm_extrapolation_lib import compute


# ------------------------------------------------------------------ #
#  Argument parsing                                                   #
# ------------------------------------------------------------------ #

def parse_args():
    p = argparse.ArgumentParser(
        description="Two-phase HS23 model with external Run 5 re-buy; no aged carryover at t2."
    )
    # Common / Run 4
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
    p.add_argument(
        "--start-date",
        type=str,
        help="Phase-1 evaluation date (YYYY-MM-DD). Convenience converter — "
             "internally subtracts the 2025-01-01 default reference. Prefer "
             "--delta-years for direct control.",
    )
    p.add_argument(
        "--delta-years",
        type=float,
        help="Years between the T0/H0 measurement and phase 1. σ grows by "
             "(1+g)^Δ from the measured σ@t0 over this interval.",
    )
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


# ------------------------------------------------------------------ #
#  Output                                                             #
# ------------------------------------------------------------------ #

def pprint_result(d, indent=0):
    """Recursively print a nested result dict."""
    prefix = "  " * indent
    for k, v in d.items():
        if isinstance(v, dict):
            print(f"{prefix}=== {k} ===")
            pprint_result(v, indent + 1)
        else:
            print(f"{prefix}{k:32s}: {v}")


def main():
    args = parse_args()
    res = compute(args)
    if args.json:
        print(json.dumps(res, indent=2))
        return

    print("\n=== Inputs ===")
    for k, v in vars(args).items():
        print(f"{k:32s}: {v}")
    print()

    pprint_result(res)


if __name__ == "__main__":
    main()
