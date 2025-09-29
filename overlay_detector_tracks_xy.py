#!/usr/bin/env python3
"""
overlay_detector_tracks_xy.py
-----------------------------
Overlay helical tracks in the transverse (X–Y) plane on top of a detector layout
exported from ROOT as a .C macro (via TCanvas->SaveAs(".C")).

- Parses ROOT .C to extract polylines/lines/text (very similar to the R–z script)
- Draws them with proper unit conversion to centimeters
- Simulates charged-particle helical motion in a uniform Bz field and plots XY projection
- Supports multiple pT and eta values, starting from user-chosen x0, y0, z0 (meters)
- Window controls, 10 cm tick spacing, legends, and export to PNG/PDF

Example:
    python overlay_detector_tracks_xy.py \
        --macro fullLayoutBarrelXY000.C \
        --pt 0.8 1 2 10 \
        --eta 0.6 0.8 1 1.2 1.4 1.5 2.5 3 4 \
        --x0 0.0 --y0 0.0 --z0 -0.10 \
        --R-window-cm 125 --follow-center \
        --macro-units-to-cm 0.1 \
        --pdf detector_tracks_xy.pdf \
        --png detector_tracks_xy.png --png-dpi 150
"""
import re
import argparse
from pathlib import Path
from typing import List, Optional, Tuple

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.ticker as ticker

# -----------------------------
# ROOT macro parser & renderer
# -----------------------------
def _get_color_hex(block: str):
    m = re.search(r'GetColor\("([^"]+)"\)', block)
    if m:
        return m.group(1)
    m2 = re.search(r"Set(Text|Line)Color\((\d+)\)", block)
    if m2:
        idx = int(m2.group(2))
        color_map = {
            1: "#000000",
            2: "#ff0000",
            4: "#0000ff",
            3: "#00ff00",
            6: "#ff00ff",
            5: "#00ffff",
            7: "#aaaaaa",
        }
        return color_map.get(idx, None)
    return None

def parse_root_macro(macro_path: str, units: float = 1.0, x_shift: float = 0.0, y_shift: float = 0.0):
    """
    Parse a ROOT macro (.C) produced by TCanvas->SaveAs(".C").
    Apply optional unit scaling (units [cm/macro_unit]) and XY shifts (cm).
    Return dict with keys: 'range', 'polylines', 'lines', 'texts'.
    All coordinates are converted to centimeters.
    """
    src = Path(macro_path).read_text(encoding="utf-8", errors="ignore")

    # Canvas range
    m = re.search(
        r"\bRange\(\s*([-\d\.Ee+]+)\s*,\s*([-\d\.Ee+]+)\s*,\s*([-\d\.Ee+]+)\s*,\s*([-\d\.Ee+]+)\s*\)\s*;",
        src,
    )
    if m:
        xmin, ymin, xmax, ymax = [float(g) * units for g in m.groups()]
        xmin += x_shift
        xmax += x_shift
        ymin += y_shift
        ymax += y_shift
    else:
        xmin, ymin, xmax, ymax = -150.0, -150.0, 150.0, 150.0

    # Polylines
    polylines = []
    for pm in re.finditer(
        r"pline\s*=\s*new\s+TPolyLine\((\d+),.*?\);\s*(.*?)\bDraw\(",
        src,
        flags=re.S,
    ):
        block = pm.group(2)
        color = _get_color_hex(block)
        lwm = re.search(r"SetLineWidth\((\d+)\)", block)
        lw = int(lwm.group(1)) if lwm else None
        xs, ys = [], []
        for ptm in re.finditer(
            r"SetPoint\(\s*\d+\s*,\s*([-\d\.Ee+]+)\s*,\s*([-\d\.Ee+]+)\s*\)",
            block,
        ):
            xs.append(float(ptm.group(1)) * units + x_shift)
            ys.append(float(ptm.group(2)) * units + y_shift)
        if len(xs) >= 2:
            polylines.append(dict(x=xs, y=ys, color=color, lw=lw))

    # Lines
    lines = []
    for lm in re.finditer(
        r"new\s+TLine\(\s*([-\d\.Ee+]+)\s*,\s*([-\d\.Ee+]+)\s*,\s*([-\d\.Ee+]+)\s*,\s*([-\d\.Ee+]+)\s*\)\s*;\s*(.*?)\bDraw\(",
        src,
        flags=re.S,
    ):
        x1, y1, x2, y2 = [float(v) * units for v in lm.group(1, 2, 3, 4)]
        x1 += x_shift
        x2 += x_shift
        y1 += y_shift
        y2 += y_shift
        block = lm.group(5)
        color = _get_color_hex(block)
        lwm = re.search(r"SetLineWidth\((\d+)\)", block)
        lw = int(lwm.group(1)) if lwm else None
        lines.append(dict(x1=x1, y1=y1, x2=x2, y2=y2, color=color, lw=lw))

    # TLatex
    texts = []
    for tm in re.finditer(
        r'new\s+TLatex\(\s*([-\d\.Ee+]+)\s*,\s*([-\d\.Ee+]+)\s*,\s*"([^"]*)"\s*\)\s*;\s*(.*?)\bDraw',
        src,
        flags=re.S,
    ):
        x, y, txt, block = (
            float(tm.group(1)) * units + x_shift,
            float(tm.group(2)) * units + y_shift,
            tm.group(3),
            tm.group(4),
        )
        color = _get_color_hex(block)
        sm = re.search(r"SetTextSize\(([\d\.Ee+-]+)\)", block)
        size = float(sm.group(1)) if sm else 0.02
        am = re.search(r"SetTextAlign\((\d+)\)", block)
        align = int(am.group(1)) if am else 12
        texts.append(dict(x=x, y=y, txt=txt, color=color, size=size, align=align))

    for tm in re.finditer(
        r'DrawLatex\(\s*([-\d\.Ee+]+)\s*,\s*([-\d\.Ee+]+)\s*,\s*"([^"]*)"\s*\)',
        src,
    ):
        x, y, txt = (
            float(tm.group(1)) * units + x_shift,
            float(tm.group(2)) * units + y_shift,
            tm.group(3),
        )
        texts.append(dict(x=x, y=y, txt=txt, color=None, size=0.02, align=12))

    for tm in re.finditer(
        r'new\s+TText\(\s*([-\d\.Ee+]+)\s*,\s*([-\d\.Ee+]+)\s*,\s*"([^"]*)"\s*\)\s*;\s*(.*?)\bDraw',
        src,
        flags=re.S,
    ):
        x, y, txt, block = (
            float(tm.group(1)) * units + x_shift,
            float(tm.group(2)) * units + y_shift,
            tm.group(3),
            tm.group(4),
        )
        color = _get_color_hex(block)
        sm = re.search(r"SetTextSize\(([\d\.Ee+-]+)\)", block)
        size = float(sm.group(1)) if sm else 0.02
        am = re.search(r"SetTextAlign\((\d+)\)", block)
        align = int(am.group(1)) if am else 12
        texts.append(dict(x=x, y=y, txt=txt, color=color, size=size, align=align))

    return dict(range=(xmin, ymin, xmax, ymax), polylines=polylines, lines=lines, texts=texts)

def _root_align_to_ha_va(align: int):
    H = align // 10
    V = align % 10
    ha = {1: "left", 2: "center", 3: "right"}.get(H, "left")
    va = {1: "bottom", 2: "center", 3: "top"}.get(V, "center")
    return ha, va

def draw_detector_xy(ax, macro_path: str, macro_units_to_cm: float = 1.0, x_offset_cm: float = 0.0, y_offset_cm: float = 0.0, draw_text: bool = True):
    parsed = parse_root_macro(macro_path, units=macro_units_to_cm, x_shift=x_offset_cm, y_shift=y_offset_cm)
    xmin, ymin, xmax, ymax = parsed["range"]

    for L in parsed["polylines"]:
        ax.plot(L["x"], L["y"], color=L["color"] if L["color"] else "black", linewidth=L["lw"] if L["lw"] else 1)
    for L in parsed["lines"]:
        ax.plot([L["x1"], L["x2"]], [L["y1"], L["y2"]], color=L["color"] if L["color"] else "black", linewidth=L["lw"] if L["lw"] else 1)

    if draw_text:
        for T in parsed["texts"]:
            ha, va = _root_align_to_ha_va(T["align"])
            fontsize = max(6, int(220 * T["size"]))
            kw = dict(ha=ha, va=va)
            if T["color"]:
                kw["color"] = T["color"]
            ax.text(T["x"], T["y"], T["txt"], fontsize=fontsize, **kw)

    ax.set_aspect("equal", adjustable="box")
    return xmin, ymin, xmax, ymax

# -----------------------------
# Physics: helical trajectories (XY projection)
# -----------------------------
c = 299792458.0
GeV_c_to_SI = 5.344285e-19  # 1 GeV/c in kg m/s
e_charge = 1.602176634e-19
m_mu = 1.883531627e-28
Bz = 3.8  # Tesla

def traj_XY_cm(pT_GeV: float, eta: float, q: float = -e_charge, phi0: float = 0.0, x0: float = 0.0, y0: float = 0.0, z0: float = 0.0, T_cycles: float = 2.0, npts: int = 2500) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    """
    Return x_cm(t), y_cm(t), z_cm(t) for a helix in uniform Bz, given initial state.
    Units:
        pT_GeV [GeV/c], eta [dimensionless], q [C], positions [m].
    Note: XY radius r_L = pT / (|q| B). Angular frequency omega_c = q B / (gamma m).
    """
    pT = pT_GeV * GeV_c_to_SI
    pz = pT * np.sinh(eta)
    p = pT * np.cosh(eta)
    gamma = np.sqrt(1.0 + (p / (m_mu * c)) ** 2)

    ux, uy = np.cos(phi0), np.sin(phi0)
    vx0, vy0 = (pT * ux) / (gamma * m_mu), (pT * uy) / (gamma * m_mu)
    vz0 = pz / (gamma * m_mu)

    omega_c = q * Bz / (gamma * m_mu)
    Tc = 2 * np.pi / abs(omega_c) if omega_c != 0 else np.inf

    # Time vector: cover T_cycles cyclotron periods
    if np.isfinite(Tc):
        t_end = T_cycles * Tc
    else:
        t_end = 1e-6
    t = np.linspace(0, t_end, npts)

    if omega_c != 0:
        s, ccos = np.sin(omega_c * t), np.cos(omega_c * t)
        x = x0 + (vx0 * s + vy0 * (ccos - 1.0)) / omega_c
        y = y0 + (-vx0 * (ccos - 1.0) + vy0 * s) / omega_c
    else:
        x = x0 + vx0 * t
        y = y0 + vy0 * t

    z = z0 + vz0 * t

    return 100.0 * x, 100.0 * y, 100.0 * z  # convert to cm

# -----------------------------
# Overlay function
# -----------------------------
def overlay_tracks_on_detector_xy(
    macro_path: str,
    pT_list: List[float],
    eta_list: List[float],
    q: float = -e_charge,
    phi0: float = 0.0,
    x0: float = 0.0,
    y0: float = 0.0,
    z0: float = 0.0,  # meters
    R_window_cm: float = 125.0,     # half-width of square window in X and Y
    follow_center: bool = True,     # center the window on (x0,y0) if True, else on (0,0)
    macro_units_to_cm: float = 1.0, # cm per macro unit
    x_offset_cm: float = 0.0,
    y_offset_cm: float = 0.0,
    strict_range: bool = False,     # keep macro's Range limits if True
    figsize=(11, 11),
    out_pdf: Optional[str] = None,
    out_png: Optional[str] = None,
    png_dpi: int = 300,
    draw_text: bool = True,
    show_grid: bool = True,
    T_cycles: float = 2.0,
):
    fig, ax = plt.subplots(figsize=figsize)
    xmin, ymin, xmax, ymax = draw_detector_xy(ax, macro_path, macro_units_to_cm, x_offset_cm, y_offset_cm, draw_text=draw_text)

    # Set window
    if strict_range:
        x_min, x_max = xmin, xmax
        y_min, y_max = ymin, ymax
    else:
        if follow_center:
            cx_cm, cy_cm = 100.0 * x0, 100.0 * y0
        else:
            cx_cm, cy_cm = 0.0, 0.0
        x_min, x_max = cx_cm - R_window_cm, cx_cm + R_window_cm
        y_min, y_max = cy_cm - R_window_cm, cy_cm + R_window_cm
        ax.set_xlim(x_min, x_max)
        ax.set_ylim(y_min, y_max)

    ax.set_aspect("equal", adjustable="box")

    # Tracks
    linestyles = [
        "-","--","-.",":",
        (0,(5,1,1,1)),
        (0,(3,1,1,1,1,1)),
        (0,(5,2,5,2)),
        (0,(1,1)),
        (0,(3,5,1,5)),
    ]
    colors = plt.rcParams["axes.prop_cycle"].by_key().get("color", ["C0","C1","C2","C3","C4"])

    for i_pt, pT in enumerate(pT_list):
        color = colors[i_pt % len(colors)]
        for j_eta, eta in enumerate(eta_list):
            ls = linestyles[j_eta % len(linestyles)]
            x_cm, y_cm, z_cm = traj_XY_cm(
                pT, eta, q=q, phi0=phi0, x0=x0, y0=y0, z0=z0, T_cycles=T_cycles, npts=2500
            )
            # Clip by inserting NaNs so lines break at boundaries (no chords across the window)
            outside = (x_cm < x_min) | (x_cm > x_max) | (y_cm < y_min) | (y_cm > y_max)
            x_plot = x_cm.copy(); y_plot = y_cm.copy()
            x_plot[outside] = np.nan; y_plot[outside] = np.nan
            ax.plot(x_plot, y_plot, color=color, linestyle=ls, lw=1)

    ax.set_xlabel("x [cm]")
    ax.set_ylabel("y [cm]")
    ax.set_title("Detector (from ROOT) + Muon trajectories (X–Y)")

    # 10 cm major ticks
    ax.xaxis.set_major_locator(ticker.MultipleLocator(10))
    ax.yaxis.set_major_locator(ticker.MultipleLocator(10))

    # Grid
    if show_grid:
        ax.grid(True, which="major", linewidth=0.5, alpha=0.5)

    # Legends
    pt_handles = [Line2D([0],[0], color=colors[i % len(colors)], lw=3) for i,_ in enumerate(pT_list)]
    pt_labels = [f"pT = {pT} GeV/c" for pT in pT_list]
    eta_handles = [Line2D([0],[0], color="black", linestyle=linestyles[j % len(linestyles)], lw=2) for j,_ in enumerate(eta_list)]
    eta_labels = [f"eta = {eta}" for eta in eta_list]

    leg1 = ax.legend(pt_handles, pt_labels, title="Color = pT", loc="upper center", bbox_to_anchor=(0.5, -0.12), ncol=max(1, len(pT_list)))
    leg2 = ax.legend(eta_handles, eta_labels, title="Line = eta", loc="upper center", bbox_to_anchor=(0.5, -0.24), ncol=5)
    ax.add_artist(leg1)

    plt.tight_layout()

    if out_pdf:
        with PdfPages(out_pdf) as pdf:
            pdf.savefig(fig, bbox_inches="tight")
    if out_png:
        fig.savefig(out_png, dpi=png_dpi, bbox_inches="tight")

    plt.close(fig)

# -----------------------------
# CLI
# -----------------------------
def parse_args(argv: Optional[List[str]] = None) -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Overlay XY helical tracks onto a ROOT macro of the detector.")
    p.add_argument("--macro", required=True, help="Path to ROOT .C macro (XY layout)")
    p.add_argument("--pt", nargs="+", type=float, required=True, help="List of pT values [GeV/c]")
    p.add_argument("--eta", nargs="+", type=float, required=True, help="List of eta values")
    p.add_argument("--q", type=float, default=-e_charge, help="Particle charge [C] (default: muon -e)")
    p.add_argument("--phi0", type=float, default=0.0, help="Initial azimuth in radians for transverse velocity")
    p.add_argument("--x0", type=float, default=0.0, help="Initial x [m]")
    p.add_argument("--y0", type=float, default=0.0, help="Initial y [m]")
    p.add_argument("--z0", type=float, default=0.0, help="Initial z [m]")
    p.add_argument("--R-window-cm", type=float, default=125.0, help="Half-width in cm of the square XY window")
    p.add_argument("--follow-center", action="store_true", help="Center the window on (x0,y0)")
    p.add_argument("--macro-units-to-cm", type=float, default=1.0, help="Scale: cm per macro unit (e.g., 0.1 if macro uses mm)")
    p.add_argument("--x-offset-cm", type=float, default=0.0, help="Shift macro X by this many cm")
    p.add_argument("--y-offset-cm", type=float, default=0.0, help="Shift macro Y by this many cm")
    p.add_argument("--strict-range", action="store_true", help="Use macro canvas Range instead of window params")
    p.add_argument("--figsize", nargs=2, type=float, default=[11,11], help="Figure size in inches (W H)")
    p.add_argument("--pdf", help="Output PDF path")
    p.add_argument("--png", help="Output PNG path")
    p.add_argument("--png-dpi", type=int, default=300, help="PNG DPI")
    p.add_argument("--no-text", action="store_true", help="Do not draw text from macro")
    p.add_argument("--no-grid", action="store_true", help="Do not draw major grid")
    p.add_argument("--cycles", type=float, default=2.0, help="How many cyclotron periods to draw")
    return p.parse_args(argv)

def main(argv: Optional[List[str]] = None):
    args = parse_args(argv)
    overlay_tracks_on_detector_xy(
        macro_path=args.macro,
        pT_list=args.pt,
        eta_list=args.eta,
        q=args.q,
        phi0=args.phi0,
        x0=args.x0,
        y0=args.y0,
        z0=args.z0,
        R_window_cm=args.R_window_cm,
        follow_center=args.follow_center,
        macro_units_to_cm=args.macro_units_to_cm,
        x_offset_cm=args.x_offset_cm,
        y_offset_cm=args.y_offset_cm,
        strict_range=args.strict_range,
        figsize=tuple(args.figsize),
        out_pdf=args.pdf,
        out_png=args.png,
        png_dpi=args.png_dpi,
        draw_text=not args.no_text,
        show_grid=not args.no_grid,
        T_cycles=args.cycles,
    )

if __name__ == "__main__":
    main()
