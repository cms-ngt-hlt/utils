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
    """Load a single CSV that already contains both occupancy (gpu*_usage) and
    memory (gpu*_memory) columns, named the same way the rest of the script
    expects (elapsed_seconds, gpu0_usage, gpu1_usage, ..., gpu0_memory, gpu1_memory, ...)."""
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

MEM_COLOR = "#8B0000"  # dark green  – memory (left axis)
OCC_COLOR = "#9370DB"  # dark red  – occupancy (right axis)

DEFAULT_MAX_MEM_MIB = 46068  # NVIDIA L40S

# ---------------------------------------------------------------------------
# Panel-level drawing
# ---------------------------------------------------------------------------

def _draw_panel(
    ax_mem,
    df,
    label,
    occ_filter,
    mem_filter,
    max_mem_mib,
    xlims,
    ylims,
    system_info_lines=None,
    show_cms_text=True,
):
    gpu_cols = [c for c in df.columns if re.match(occ_filter, c)]
    if not gpu_cols:
        raise ValueError(f"No column matched filter={occ_filter!r} in {list(df.columns)}")
    occ_col = gpu_cols[0]

    mem_cols = [c for c in df.columns if re.match(mem_filter, c)]
    if not mem_cols:
        raise ValueError(f"No column matched mem_filter={mem_filter!r} in {list(df.columns)}")
    mem_col = mem_cols[0]

    times = df["elapsed_seconds"].to_numpy(float)
    occup = df[occ_col].to_numpy(float)
    memory = df[mem_col].to_numpy(float)

    gpu_id = re.sub(r"_memory$", "", mem_col, flags=re.IGNORECASE).upper()

    # --- occupancy (right axis, %) -----------------------------------------
    ax_occ = ax_mem.twinx()
    rolling_window = 20
    rolling_op = [sum(occup[i:i+rolling_window])/rolling_window
                   for i in range(len(occup) - rolling_window + 1)]
    ax_occ.plot(times[rolling_window-1:rolling_window-1+len(rolling_op)], rolling_op,
                color=OCC_COLOR, linewidth=1.5, zorder=3, label="Occupancy max")

    if xlims == (0, 0):
        ax_occ.set_xlim(times.max(), times.max() + 0.2*(times.max() - times.max()))
    else:
        ax_occ.set_xlim(*xlims)

    ax_occ.set_ylabel("GPU Occupancy [%]", fontsize=12, color=OCC_COLOR)
    ax_occ.tick_params(axis="y", labelcolor=OCC_COLOR, labelsize=11)
    ax_occ.yaxis.set_major_locator(ticker.MultipleLocator(20))
    ax_occ.yaxis.grid(False)

    # --- memory (left axis, %) ------------------------------------------
    def mib_to_pct(x):
        return np.asarray(x) / max_mem_mib * 100.0

    def pct_to_mib(x):
        return np.asarray(x) / 100.0 * max_mem_mib

    ax_mem.plot(times, mib_to_pct(memory), color=MEM_COLOR, linewidth=3, zorder=3, label="Memory")
    #ax_mem.fill_between(times, 0, mib_to_pct(memory), color=MEM_COLOR, alpha=0.7, linewidth=0, zorder=2)

    mem_max_pct = mib_to_pct(memory).max()
    if xlims == (0, 0):
        ax_mem.set_xlim(times.max(), times.max() + 0.2*(times.max() - times.max()))
    else:
        ax_mem.set_xlim(*xlims)
    if ylims == (0, 0):
        ax_mem.set_ylim(0, 1.10 * mem_max_pct if mem_max_pct > 0 else 1)
    else:
        ax_mem.set_ylim(*ylims)

    # ax_occ shares the same 0-100(ish) percent range as ax_mem for visual alignment
    if ylims == (0, 0):
        ax_occ.set_ylim(0, 1.10 * mem_max_pct if mem_max_pct > 0 else 1)
    else:
        ax_occ.set_ylim(*ylims)

    ax_mem.set_xlabel("Elapsed Time [s]", fontsize=12)
    ax_mem.set_ylabel("GPU Memory [%]", fontsize=12, color=MEM_COLOR)
    ax_mem.tick_params(axis="y", labelcolor=MEM_COLOR, labelsize=11)
    ax_mem.tick_params(axis="x", labelsize=11)

    ax_mem.yaxis.grid(True, linestyle="--", alpha=1., color='#A9A9A9', zorder=0)
    ax_mem.xaxis.grid(False)
    ax_mem.set_axisbelow(True)

    # --- draw order: bring memory (ax_mem) in front of occupancy (ax_occ) ---
    # ax_occ is a twin axes created after ax_mem, so matplotlib stacks it on
    # top by default regardless of each line's own zorder. Raise ax_mem's
    # axes-level zorder above ax_occ's and make its background transparent
    # so the memory curve/fill renders in front while occupancy stays visible
    # underneath.
    ax_mem.set_zorder(ax_occ.get_zorder() + 1)
    ax_mem.patch.set_visible(False)

    if show_cms_text:
        hep.cms.label("Preliminary", ax=ax_mem, rlabel=label, fontsize=12, pad=0.5)

    # --- system-info box (top-right corner, inside axes) --------------------
    # Drawn on every panel whenever lines are provided (pass an empty list to hide it).
    if system_info_lines:
        system_info_text = "\n".join(system_info_lines)
        ax_mem.text(
            0.67, 0.95, system_info_text,
            transform=ax_mem.transAxes,
            fontsize=10,
            va="top", ha="left",
            style="italic",
            linespacing=1.4,
        )

    # --- combined legend (memory + occupancy) -------------------------------
    lines_mem, labels_mem = ax_mem.get_legend_handles_labels()
    lines_occ, labels_occ = ax_occ.get_legend_handles_labels()
    ax_mem.legend(
        lines_mem + lines_occ,
        labels_mem + labels_occ,
        loc="upper left",
        fontsize=10,
    )

    return ax_occ, gpu_id, occ_col

# ---------------------------------------------------------------------------
# Main plotting routines
# ---------------------------------------------------------------------------

def plot_memory_and_occupancy_vs_time(
    dfs,
    labels,
    occ_filter="gpu0_usage",
    mem_filter="gpu0_memory",
    max_mem_mib=DEFAULT_MAX_MEM_MIB,
    suptitle=None,
    xlims=(0.,0.),
    ylims=(0.,0.),
    outfile="memory_vs_time",
    system_info_lines=None,
):
    for df, label in zip(dfs, labels):
        fig, ax_mem = plt.subplots(figsize=(13, 6))  # Increased vertical space
        _, gpu_id, occ_id_col = _draw_panel(
            ax_mem, df, label,
            occ_filter, mem_filter, max_mem_mib,
            xlims, ylims,
            system_info_lines=system_info_lines,
        )

        if suptitle:
            fig.suptitle(suptitle, fontsize=13)

        safe_label = re.sub(r"[^\w]+", "_", label).strip("_")
        occ_id = occ_id_col.upper()
        for ext in ("png", "pdf"):
            fname = f"{outfile}_{safe_label}_{gpu_id}_mem_{occ_id}_occ.{ext}"
            plt.savefig(fname, dpi=300, bbox_inches="tight")
            print(f"Saved: {fname}")

        plt.close(fig)

def plot_memory_and_occupancy_merged(
    dfs,
    labels,
    occ_filter="gpu0_usage",
    mem_filter="gpu0_memory",
    max_mem_mib=DEFAULT_MAX_MEM_MIB,
    suptitle=None,
    outfile="memory_vs_time",
    xlims=(0., 0.),
    ylims=(0., 0.),
    system_info_lines=None,
):
    n = len(labels)
    fig, axes = plt.subplots(
        n, 1,
        figsize=(13, 5 * n + 1),
        squeeze=False,
        sharex=True,  # Share x-axis to align subplots
    )
    axes = axes[:, 0]

    for i, (df, label, ax_mem) in enumerate(zip(dfs, labels, axes)):
        _draw_panel(
            ax_mem, df, label,
            occ_filter, mem_filter, max_mem_mib,
            xlims, ylims,
            system_info_lines=system_info_lines,  # Shown on every subplot, not just the first
            show_cms_text=True,  # Show CMS label on ALL subplots
        )

        # Remove x-axis labels and ticks for all subplots except the last one
        if i < n - 1:
            ax_mem.set_xlabel("")
            ax_mem.tick_params(axis="x", labelbottom=False)

    if suptitle:
        fig.suptitle(suptitle, fontsize=13)

    # Adjust vertical spacing between subplots
    plt.subplots_adjust(hspace=0.05)  # Small gap between subplots

    for ext in ("png", "pdf"):
        fname = f"{outfile}_merged.{ext}"
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

    plot_fn = (
        plot_memory_and_occupancy_merged
        if args.merge
        else plot_memory_and_occupancy_vs_time
    )

    plot_fn(
        dfs,
        args.csv_labels,
        occ_filter=args.usage_filter,
        mem_filter=args.memory_filter,
        max_mem_mib=args.max_mem_mib,
        suptitle=args.suptitle,
        outfile=args.outfile,
        xlims=args.xlims,
        ylims=args.ylims,
        system_info_lines=args.system_info,
    )

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="CMS-style GPU memory and occupancy vs time plotter (dual y-axes)."
    )

    parser.add_argument("csv_files", nargs="+", type=Path, help="Input CSV files (1 or more), each containing both occupancy (gpu*_usage) and memory (gpu*_memory) columns.")
    parser.add_argument("--csv_labels", nargs="+", type=str, required=True, help="Legend labels, one per input CSV file (same order, same count).")
    parser.add_argument("--usage_filter", default="gpu0_usage", type=str, help="Regex to select the GPU occupancy column (e.g. gpu0_usage, gpu1_usage, ...).")
    parser.add_argument("--memory_filter", default="gpu0_memory", type=str, help="Regex to select the GPU memory column (e.g. gpu0_memory, gpu1_memory, ...).")
    parser.add_argument("--max_mem_mib", default=DEFAULT_MAX_MEM_MIB, type=float, help="Total memory (MiB) of a single GPU, used to compute the memory %% axis.")
    parser.add_argument("--suptitle", default=None, type=str, help="Overall figure title (optional).")
    parser.add_argument("--outfile", default=Path("memory_vs_time"), type=Path, help="Output base filename (without extension).")
    parser.add_argument("--threshold", default=10, type=float, help="Occupancy intervals at or under this value are excluded from the weighted average.")
    parser.add_argument("--merge", action="store_true", help="Merge all (label, dataframe) pairs as stacked subplots of a single figure instead of producing one figure per label.")

    parser.add_argument(
        '--xlims',
        type=float,
        nargs=2,
        required=False,
        default=(0., 4000.),
        help='X axis limits [xmin, xmax]. If ignored, an automatic range is employed based on the overall maximum memory value.'
    )

    parser.add_argument(
        '--ylims',
        type=float,
        nargs=2,
        required=False,
        default=(0., 120.),
        help='Y axis limits [ymin, ymax]. If ignored, an automatic range is employed based on the overall maximum memory value.'
    )

    SYSTEM_INFO_LINES = (
        r"$t\bar{t}$ + 200 PU ($\sqrt{s}$ = 14 TeV)",
        "2x AMD EPYC 9534 64-Core Processor",
        f"1 NVIDIA L40S GPU ({DEFAULT_MAX_MEM_MIB} MiB max, MPS @ 6%)",
        "16 jobs with 16 threads/streams each",
    )
    parser.add_argument(
        "--system-info",
        dest="system_info",
        nargs="*",
        type=str,
        default=SYSTEM_INFO_LINES,
        metavar="LINE",
        help="Lines of system info text to show in the top-right corner of every panel "
             "(e.g. --system-info \"line one\" \"line two\"). Pass with no arguments "
             "(--system-info) to hide the box entirely. Defaults to a preset description "
             "of the CMS GPU test system.",
    )

    args = parser.parse_args()

    if len(args.csv_files) != len(args.csv_labels):
        parser.error("Number of --csv_labels must match number of csv_files.")

    main(args)
