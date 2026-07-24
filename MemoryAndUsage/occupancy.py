import sys
import math
import argparse
import re
from pathlib import Path

import numpy as np
import pandas as pd
import mplhep as hep
hep.style.use("CMS")

import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# ---------------------------------------------------------------------------
# Loaders
# ---------------------------------------------------------------------------

def load_gpu_csv(csv_path):
    """Load a single CSV containing occupancy (gpu*_usage) columns, named the
    way the rest of the script expects (elapsed_seconds, gpu0_usage, gpu1_usage, ...)."""
    df = pd.read_csv(csv_path)
    return df.sort_values("elapsed_seconds").reset_index(drop=True)

# ---------------------------------------------------------------------------
# Statistics helpers
# ---------------------------------------------------------------------------

def compute_weighted_average(df, threshold=1.0, filter=None):
    gpu_cols = [c for c in df.columns if c.startswith("gpu")]
    if filter:
        gpu_cols = [c for c in df.columns if re.match(filter, c)]

    times = df["elapsed_seconds"].to_numpy(float)
    if len(times) < 2:
        print("Not enough samples to compute time-weighted averages.")
        return

    diffs = np.diff(times)
    total_time = diffs.sum()

    print(f"\n--- Time-Weighted GPU Averages (filtered at {threshold:.2f}%) ---")
    print(f"Activity threshold: {threshold}% (intervals at/under this are ignored)\n")

    for col in gpu_cols:
        occup = df[col].to_numpy(float)
        interval_occupancies = occup[:-1]
        interval_widths = diffs

        mask = interval_occupancies > threshold
        if not mask.any():
            print(f"{col.upper():<6}: No intervals above {threshold}% threshold")
            continue

        kept_occupancies = interval_occupancies[mask]
        kept_widths = interval_widths[mask]

        active_time = kept_widths.sum()
        weighted_avg = np.average(kept_occupancies, weights=kept_widths)
        print(
            f"{col.upper():<6}: {weighted_avg:6.2f} "
            f"(active time {active_time:.1f}s / total {total_time:.1f}s)"
        )
    print("------------------------------------------------------------\n")

def print_average_occupancy(df, filter=None):
    gpu_cols = [c for c in df.columns if c.startswith("gpu")]
    if filter:
        gpu_cols = [c for c in df.columns if re.match(filter, c)]

    print("\n---------------- FLAT GPU Occupancy Averages ----------------")
    for col in gpu_cols:
        mean_val = df[col].mean()
        max_val = df[col].max()
        min_val = df[col].min()
        print(f"{col.upper():<6}: Mean: {mean_val:6.2f}, Min: {min_val:6.2f}, Max: {max_val:6.2f}")
    print("---------------------------------------------------\n")

# ---------------------------------------------------------------------------
# Colours
# ---------------------------------------------------------------------------

# A qualitative palette; cycles if there are more curves than colors.
DEFAULT_PALETTE = [
    "#9370DB",  # purple
    "#8B0000",  # dark red
    "#1B7837",  # dark green
    "#2166AC",  # blue
    "#E08214",  # orange
    "#666666",  # grey
    "#C51B7D",  # magenta
    "#54278F",  # violet
]

def _rolling_max(values, window):
    """Rolling-max smoothing."""
    if window <= 1 or len(values) <= window + 1:
        return values, np.arange(len(values))
    smoothed = [max(values[i:i + window]) for i in range(len(values) - window - 1)]
    idx = np.arange(window - 1, window - 1 + len(smoothed))
    return np.array(smoothed), idx

def _rolling_mean(values, window):
    """Rolling-max smoothing."""
    if window <= 1 or len(values) <= window + 1:
        return values, np.arange(len(values))
    smoothed = [np.mean(values[i:i + window]) for i in range(len(values) - window + 1)]
    idx = np.arange(window - 1, window - 1 + len(smoothed))
    return np.array(smoothed), idx

def _rolling_std(values, window):
    """Compute rolling standard deviation with a given window."""
    if window <= 1 or len(values) < window:
        return np.zeros_like(values), np.arange(len(values))
    smoothed = [np.std(values[i:i + window]) for i in range(len(values) - window + 1)]
    idx = np.arange(window - 1, len(values))
    return np.array(smoothed), idx
# ---------------------------------------------------------------------------
# Main plotting routines
# ---------------------------------------------------------------------------

def plot_occupancy_overlay(
    dfs,
    labels,
    occ_filter="gpu0_usage",
    rolling_window=50,
    suptitle=None,
    xlims=(0., 0.),
    ylims=(0., 0.),
    outfile="occupancy_comparison",
    system_info_lines=None,
    colors=None,
):
    """Overlay every (df, label) occupancy trace on a single shared axis so
    they can be compared directly."""
    colors = colors or DEFAULT_PALETTE

    fig, ax = plt.subplots(figsize=(13, 6))

    max_time = 0.0
    for i, (df, label) in enumerate(zip(dfs, labels)):
        gpu_cols = [c for c in df.columns if re.match(occ_filter, c)]
        if not gpu_cols:
            raise ValueError(f"No column matched filter={occ_filter!r} in {list(df.columns)}")
        occ_col = gpu_cols[0]

        times = df["elapsed_seconds"].to_numpy(float)
        occup = df[occ_col].to_numpy(float)
        max_time = max(max_time, times.max() if len(times) else 0.0)

        smoothed, idx = _rolling_mean(occup, rolling_window)
        std_dev, _ = _rolling_std(occup, rolling_window)  # Assuming you have a function for rolling std
        color = colors[i % len(colors)]
        
        # Plot the smoothed line
        ax.plot(times[idx], smoothed, color=color, linewidth=1.8, zorder=3, label=label)
        
        # Clip the values to a maximum of 100
        lower_bound = np.clip(smoothed - std_dev, a_min=None, a_max=100)
        upper_bound = np.clip(smoothed + std_dev, a_min=None, a_max=100)
        
        ax.fill_between(
            times[idx],
            lower_bound,
            upper_bound,
            color=color,
            alpha=0.2,  # Transparency
            zorder=2
        )
        
    if xlims == (0, 0):
        ax.set_xlim(0, max_time)
    else:
        ax.set_xlim(*xlims)

    if ylims == (0, 0):
        ax.set_ylim(0, 105)
    else:
        ax.set_ylim(*ylims)

    ax.set_xlabel("Elapsed Time [s]", fontsize=12)
    ax.set_ylabel("GPU Occupancy [%]", fontsize=12)
    ax.yaxis.set_major_locator(ticker.MultipleLocator(20))
    ax.tick_params(axis="both", labelsize=11)

    ax.yaxis.grid(True, linestyle="--", alpha=1.0, color="#A9A9A9", zorder=0)
    ax.xaxis.grid(False)
    ax.set_axisbelow(True)

    hep.cms.label("Preliminary", ax=ax, rlabel='', fontsize=12, pad=0.5)

    if system_info_lines:
        system_info_text = "\n".join(system_info_lines)
        ax.text(
            0.73, 0.95, system_info_text,
            transform=ax.transAxes,
            fontsize=10,
            va="top", ha="left",
            style="italic",
            linespacing=1.4,
        )

    ax.legend(loc="upper left", fontsize=10)

    if suptitle:
        fig.suptitle(suptitle, fontsize=13)

    for ext in ("png", "pdf"):
        fname = f"{outfile}_overlay.{ext}"
        plt.savefig(fname, dpi=300, bbox_inches="tight")
        print(f"Saved: {fname}")

    plt.close(fig)

def plot_occupancy_stacked(
    dfs,
    labels,
    occ_filter="gpu0_usage",
    rolling_window=50,
    suptitle=None,
    xlims=(0., 0.),
    ylims=(0., 0.),
    outfile="occupancy_comparison",
    system_info_lines=None,
    colors=None,
):
    """One occupancy curve per subplot, stacked vertically, sharing the x-axis
    — useful when overlaying all curves in one axis gets too busy."""
    colors = colors or DEFAULT_PALETTE

    n = len(labels)
    fig, axes = plt.subplots(
        n, 1,
        figsize=(13, 4 * n + 1),
        squeeze=False,
        sharex=True,
    )
    axes = axes[:, 0]

    max_time = 0.0
    for df in dfs:
        t = df["elapsed_seconds"].to_numpy(float)
        if len(t):
            max_time = max(max_time, t.max())

    for i, (df, label, ax) in enumerate(zip(dfs, labels, axes)):
        gpu_cols = [c for c in df.columns if re.match(occ_filter, c)]
        if not gpu_cols:
            raise ValueError(f"No column matched filter={occ_filter!r} in {list(df.columns)}")
        occ_col = gpu_cols[0]

        times = df["elapsed_seconds"].to_numpy(float)
        occup = df[occ_col].to_numpy(float)

        smoothed, idx = _rolling_max(occup, rolling_window)
        color = colors[i % len(colors)]
        ax.plot(times[idx], smoothed, color=color, linewidth=1.8, zorder=3, label=label)

        ax.set_xlim(*xlims) if xlims != (0, 0) else ax.set_xlim(0, max_time)
        ax.set_ylim(*ylims) if ylims != (0, 0) else ax.set_ylim(0, 105)

        ax.set_ylabel("GPU Occupancy [%]", fontsize=12)
        ax.yaxis.set_major_locator(ticker.MultipleLocator(20))
        ax.tick_params(axis="both", labelsize=11)
        ax.yaxis.grid(True, linestyle="--", alpha=1.0, color="#A9A9A9", zorder=0)
        ax.xaxis.grid(False)
        ax.set_axisbelow(True)

        hep.cms.label("Preliminary", ax=ax, rlabel='', fontsize=12, pad=0.5)

        if system_info_lines:
            system_info_text = "\n".join(system_info_lines)
            ax.text(
                0.67, 0.95, system_info_text,
                transform=ax.transAxes,
                fontsize=10,
                va="top", ha="left",
                style="italic",
                linespacing=1.4,
            )

        ax.legend(loc="upper left", fontsize=10)

        if i < n - 1:
            ax.set_xlabel("")
            ax.tick_params(axis="x", labelbottom=False)
        else:
            ax.set_xlabel("Elapsed Time [s]", fontsize=12)

    if suptitle:
        fig.suptitle(suptitle, fontsize=13)

    plt.subplots_adjust(hspace=0.05)

    for ext in ("png", "pdf"):
        fname = f"{outfile}_stacked.{ext}"
        plt.savefig(fname, dpi=300, bbox_inches="tight")
        print(f"Saved: {fname}")

    plt.close(fig)

# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main(args):
    dfs = []

    for csv_file, lab in zip(args.csv_files, args.csv_labels):
        df = load_gpu_csv(csv_file)

        print(f"\n=== {lab} ({csv_file}) ===")
        print_average_occupancy(df, filter=args.usage_filter)
        compute_weighted_average(df, threshold=args.threshold, filter=args.usage_filter)

        dfs.append(df)

    plot_fn = plot_occupancy_stacked if args.stacked else plot_occupancy_overlay

    plot_fn(
        dfs,
        args.csv_labels,
        occ_filter=args.usage_filter,
        rolling_window=args.rolling_window,
        suptitle=args.suptitle,
        outfile=args.outfile,
        xlims=args.xlims,
        ylims=args.ylims,
        system_info_lines=args.system_info,
    )

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="CMS-style GPU occupancy comparison plotter (overlays or stacks multiple runs on a shared axis)."
    )

    parser.add_argument("csv_files", nargs="+", type=Path, help="Input CSV files (1 or more), each containing an occupancy (gpu*_usage) column.")
    parser.add_argument("--csv_labels", nargs="+", type=str, required=True, help="Legend labels, one per input CSV file (same order, same count).")
    parser.add_argument("--usage_filter", default="gpu0_usage", type=str, help="Regex to select the GPU occupancy column (e.g. gpu0_usage, gpu1_usage, ...).")
    parser.add_argument("--rolling_window", default=5, type=int, help="Window size for the rolling-max smoothing applied to each occupancy curve.")
    parser.add_argument("--suptitle", default=None, type=str, help="Overall figure title (optional).")
    parser.add_argument("--outfile", default=Path("occupancy_comparison"), type=Path, help="Output base filename (without extension).")
    parser.add_argument("--threshold", default=10, type=float, help="Occupancy intervals at or under this value are excluded from the weighted average.")
    parser.add_argument("--stacked", action="store_true", help="Draw one subplot per run, stacked vertically, instead of overlaying all curves on a single shared axis.")

    parser.add_argument(
        '--xlims',
        type=float,
        nargs=2,
        required=False,
        default=(0., 4000.),
        help='X axis limits [xmin, xmax]. If ignored, an automatic range is used based on the overall maximum elapsed time.'
    )

    parser.add_argument(
        '--ylims',
        type=float,
        nargs=2,
        required=False,
        default=(0., 105.),
        help='Y axis limits [ymin, ymax]. If ignored, defaults to 0-105%%.'
    )

    SYSTEM_INFO_LINES = (
        r"$t\bar{t}$ + 200 PU ($\sqrt{s}$ = 14 TeV)",
        "2x AMD EPYC 9534 64-Core Processor",
        "1 NVIDIA L40S GPU",
        "16 jobs with 16 threads/streams each",
    )
    parser.add_argument(
        "--system-info",
        dest="system_info",
        nargs="*",
        type=str,
        default=SYSTEM_INFO_LINES,
        metavar="LINE",
        help="Lines of system info text to show in the top-right corner of the plot(s) "
             "(e.g. --system-info \"line one\" \"line two\"). Pass with no arguments "
             "(--system-info) to hide the box entirely. Defaults to a preset description "
             "of the CMS GPU test system.",
    )

    args = parser.parse_args()

    if len(args.csv_files) != len(args.csv_labels):
        parser.error("Number of --csv_labels must match number of csv_files.")

    main(args)
