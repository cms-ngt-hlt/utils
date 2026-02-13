#!/usr/bin/env python3

# usage:
# python3 /data/evernazz/NanoAOD/2026_01_12/NGT_Timing/Plot_GPU_Profile.py \
#  --file1 gpu_memory_NGTScouting_16j_16t_16s.csv \
#  --file2 gpu_memory_NGTScoutingNewBaseline_16j_16t_16s.csv \
#  --file3 gpu_memory_NGTScoutingCAExt_16j_16t_16s.csv \
#  --label1 "Patatrack" \
#  --label2 "Ext. Patatrack + LST + MkFit" \
#  --label3 "Ext. Patatrack" \
#  --type memory_mib \
#  --output memory_profile_gpu.png

import argparse
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import mplhep as hep

def read_file(path):
    return pd.read_csv(path)

def main(args):
    # CMS style
    plt.style.use(hep.style.CMS)

    dfs = [
        read_file(args.file1),
        read_file(args.file2),
        read_file(args.file3),
    ]
    if args.file4:
        dfs.append(read_file(args.file4))

    labels = [
        args.label1,
        args.label2,
        args.label3,
    ]
    if args.label4:
        labels.append(args.label4)

    if len(dfs) == 4:
        colors = [ "#3f8fda", "#ffa90e", "#832db6", "#bd1f01"]
        markers = [ "o", "s", "d", "D"]
    else:
        colors = [ "#ffa90e", "#832db6", "#bd1f01"]
        markers = [ "s", "d", "D"]

    fig, ax = plt.subplots(figsize=(10, 10))

    ymax = 0.0
    for i, (df, label) in enumerate(zip(dfs, labels)):
        ax.plot(
            df["elapsed_seconds"],
            df[args.type] / 1024.0,
            label=label,
            linewidth=2,
            color=colors[i],
            marker=markers[i],
            markersize=4,
        )
        ymax = max(ymax, df[args.type].max() / 1024.0)
        print(df[args.type].max() / 1024.0)

    ax.set_xlabel("Elapsed time [s]")
    device = 'GPU' if args.type == "memory_mib" else 'CPU'
    ax.set_ylabel(f"{device} Memory usage [GiB]")
    if len(dfs) == 3:
        ax.set_ylim(top=1.25 * ymax)
    else:
        ax.set_ylim(top=1.35 * ymax)

    ax.legend(
        loc="upper left",
        # bbox_to_anchor=(1.01, 1.0),
        # frameon=False,
        fontsize=20,
    )

    ax.grid(True, alpha=0.75, linestyle="dashdot", linewidth=0.75)

    hep.cms.label(
        "Internal",
        data=False,
        com=14,
        ax=ax,
    )

    plt.tight_layout()
    print(f"Saved plots to: {args.output}")
    plt.savefig(f"{args.output}", dpi=150, bbox_inches="tight")
    plt.savefig(f"{args.output.replace('.png', '.pdf')}", dpi=150, bbox_inches="tight")
    plt.show()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Plot memory usage vs time in CMS style"
    )

    parser.add_argument("--file1", help="First input CSV file")
    parser.add_argument("--file2", help="Second input CSV file")
    parser.add_argument("--file3", help="Third input CSV file")
    parser.add_argument("--file4", help="Fourth input CSV file")

    parser.add_argument("--label1", default="Sample 1")
    parser.add_argument("--label2", default="Sample 2")
    parser.add_argument("--label3", default="Sample 3")
    parser.add_argument("--label4", default="Sample 4")

    parser.add_argument("--output", default="memory_comparison_gpu.png")
    parser.add_argument("--type", default="rss_mib")

    args = parser.parse_args()
    main(args)