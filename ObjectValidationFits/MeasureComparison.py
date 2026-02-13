import numpy as np
import matplotlib.pyplot as plt
import mplhep as hep
import argparse

def plot_intervals_many(values, sigmas, title="Compatibility", names=None, output="compatibility.png"):
    values = np.asarray(values, dtype=float)
    sigmas = np.asarray(sigmas, dtype=float)
    n = len(values)

    if len(sigmas) != n:
        raise ValueError("values and sigmas must have the same length")

    if names is None:
        names = [f"m{i}" for i in range(n)]

    plt.style.use(hep.style.CMS)

    fig, ax = plt.subplots(figsize=(10, n * 1.5))

    y = np.arange(n)[::-1]

    color_cycle = plt.rcParams["axes.prop_cycle"].by_key().get("color", ["C0"])

    # vertical offset for text
    text_offset = 0.18

    for i, (mu, s, yi) in enumerate(zip(values, sigmas, y)):
        c = color_cycle[i % len(color_cycle)]

        # ±2σ
        ax.hlines(yi, mu - 2*s, mu + 2*s, linewidth=3, alpha=0.35, color=c)

        # ±1σ
        ax.hlines(yi, mu - s, mu + s, linewidth=6, color=c)

        # central marker
        ax.plot(mu, yi, "o", color=c, markersize=5)

        # ---- TEXT LABEL ----
        label = rf"${mu:.3g} \pm {s:.2g}$"
        ax.text(
            mu, yi + text_offset,
            label,
            ha="center",
            va="bottom",
            fontsize=15,
            color=c
        )

    ax.set_yticks(y)
    ax.set_yticklabels(names, fontsize=15)
    ax.set_xlabel("value")
    ax.set_title(title)

    xmin = np.min(values - 2*sigmas)
    xmax = np.max(values + 2*sigmas)
    pad = 0.05 * (xmax - xmin) if xmax > xmin else 1.0
    ax.set_xlim(xmin - pad, xmax + pad)

    ax.set_ylim(-1, n)
    plt.tight_layout()

    if output:
        if not output.lower().endswith((".png", ".pdf", ".svg")):
            output += ".png"
        plt.savefig(output, dpi=300)

    plt.show()

'''
python3 /data/evernazz/NanoAOD/2026_01_12/utils/ObjectValidationFits/MeasureComparison.py \
    --values 4.38 4.30 \
    --sigmas 0.06 0.06 \
    --names "ResX Legacy" "ResY Legacy" \
    --output "comparison_Legacy_ResX_vs_ResY.png"

python3 /data/evernazz/NanoAOD/2026_01_12/utils/ObjectValidationFits/MeasureComparison.py \
    --values 4.34 4.24 \
    --sigmas 0.06 0.05 \
    --names "ResX Patatrack" "ResY Patatrack" \
    --output "comparison_Patatrack_ResX_vs_ResY.png"

python3 /data/evernazz/NanoAOD/2026_01_12/utils/ObjectValidationFits/MeasureComparison.py \
    --values 6.12 5.81 \
    --sigmas 0.09 0.08 \
    --names "ResX Ext Patatrack" "ResY Ext Patatrack" \
    --output "comparison_Ext_Patatrack_ResX_vs_ResY.png"

python3 /data/evernazz/NanoAOD/2026_01_12/utils/ObjectValidationFits/MeasureComparison.py \
    --values 4.38 4.30 4.34 4.24 6.12 5.81 \
    --sigmas 0.06 0.06 0.06 0.05 0.09 0.08 \
    --names "ResX Legacy" "ResY Legacy" "ResX Patatrack" "ResY Patatrack" "ResX Ext Patatrack" "ResY Ext Patatrack" \
    --output "comparison_All_ResX_vs_ResY.png"
'''

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--values", type=float, nargs="+", required=True)
    parser.add_argument("--sigmas", type=float, nargs="+", required=True)
    parser.add_argument("--names", type=str, nargs="*", default=None)
    parser.add_argument("--title", type=str, default="")
    parser.add_argument("--output", type=str, default="compatibility.png")

    args = parser.parse_args()

    plot_intervals_many(
        values=args.values,
        sigmas=args.sigmas,
        title=args.title,
        names=args.names,
        output=args.output
    )
