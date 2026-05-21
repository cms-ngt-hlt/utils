#!/usr/bin/env python3
"""Live TUI for the two-phase farm extrapolation projection.

Edit any input parameter on the left; the projection re-runs after each
change and the result panels update live.

Setup
-----
    python3 -m venv .venv
    .venv/bin/pip install textual textual-plotext cairosvg
    .venv/bin/python farmExtrapolation_tui.py [--lambda-khz X --T0 Y ...]

(`cairosvg` is only needed for PNG screenshot export via Ctrl+I.)

All flags accepted by `farmExtrapolation_twoPhases.py` are accepted here and
pre-fill the inputs at launch. Missing flags fall back to baked-in defaults.

Keys
----
    Tab / Shift+Tab    move focus between inputs
    Up / Down          step a focused input by its configured ±step
    ‹ / ›  glyphs      same, by mouse
    Ctrl+R  (or r)     reset all inputs to defaults
    Ctrl+S  (or s)     write farm_extrapolation_<ts>.json to cwd
    Ctrl+L  (or l)     load parameters from a saved JSON
    Ctrl+I  (or i)     save the current view as a high-res PNG screenshot
    Ctrl+Q  (or q)     quit

Pass --load PATH at launch to start with a saved snapshot pre-loaded.
"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime
from typing import Any

from textual import events
from textual.app import App, ComposeResult
from textual.binding import Binding
from textual.containers import Center, Horizontal, Vertical, VerticalScroll
from textual.reactive import reactive
from textual.screen import ModalScreen
from textual.widgets import (
    Button,
    Collapsible,
    DataTable,
    Footer,
    Header,
    Input,
    Label,
    RadioButton,
    RadioSet,
    Static,
)
from textual_plotext import PlotextPlot
from rich.text import Text

from farm_extrapolation_lib import (
    ARG_DEFAULTS,
    args_namespace,
    compute,
    sigma_trajectory,
)


# Shared CPU/GPU palette, used by both the Rich-markup widgets (hex form) and
# the plotext line plot (RGB form, since plotext renders to the terminal's
# true-color channel rather than going through Rich). matplotlib tab10
# blue/orange — distinctive without looking neon on a dark terminal.
CPU_COLOR_HEX = "#1f77b4"
GPU_COLOR_HEX = "#ff7f0e"
CPU_COLOR_RGB = (31, 119, 180)
GPU_COLOR_RGB = (255, 127, 14)


# Per-parameter ± step sizes for the buttons and Up/Down keys.
PARAM_STEPS: dict[str, float] = {
    "lambda_khz": 1.0,
    "lambda2_khz": 1.0,
    "T0": 50.0,
    "H0": 50.0,
    "C0": 50.0,
    "Hgpu0": 50.0,
    "Cgpu": 50.0,
    "g": 0.01,
    "epsilon": 0.05,
    "budget1": 100_000.0,
    "budget2": 100_000.0,
    "f1": 0.05,
    "f2": 0.05,
    "years_after": 0.5,
    "delta_years": 0.5,
    "alpha2_over_alpha1": 0.1,
    "complexity2": 0.1,
    "T0_phase2": 50.0,
    "H0_phase2": 50.0,
    "eta_new": 0.05,
    "eta_old": 0.05,
    "chi_old": 0.05,
    "age_cpu_per_year": 0.05,
    "age_gpu_per_year": 0.05,
}

# Inputs grouped by collapsible section; each entry is (key, display_label).
SECTIONS: list[tuple[str, list[tuple[str, str]]]] = [
    # Run 4 and Run 5 sit next to each other, sharing the same parameter order
    # (λ, T0, H0, [C], M, f) so the eye can scan them as parallel columns.
    ("Run 4", [
        ("lambda_khz", "λ (kHz)"),
        ("T0", "T0 (ev/s)"),
        ("H0", "H0 (HS23)"),
        ("C0", "C0 ($)"),
        ("budget1", "M1 ($)"),
        ("f1", "f1"),
    ]),
    ("Run 5", [
        ("lambda2_khz", "λ2 (kHz)"),
        ("T0_phase2", "T0-phase2 ev/s"),
        ("H0_phase2", "H0-phase2 HS23"),
        # (no separate C @ t2 input — Run 5 reuses C0 from Run 4)
        ("budget2", "M2 ($)"),
        ("f2", "f2"),
    ]),
    ("GPU baseline", [
        ("Hgpu0", "Hgpu0"),
        ("Cgpu", "Cgpu ($)"),
    ]),
    ("Growth & timing", [
        ("g", "g (frac/yr)"),
        ("epsilon", "ε"),
        ("delta_years", "Δ years"),
        ("years_after", "yrs t1->t2"),
    ]),
    ("Aging (advanced)", [
        ("eta_new", "η_new"),
        ("eta_old", "η_old"),
        ("chi_old", "χ_old"),
        ("age_cpu_per_year", "CPU age/yr"),
        ("age_gpu_per_year", "GPU age/yr"),
    ]),
]

# Inputs constrained to the [0, 1] interval.
UNIT_INTERVAL_PARAMS = {"f1", "f2", "epsilon"}

# Inputs that may legitimately be blank (compute() treats them as "use default").
NULLABLE_PARAMS = {
    "lambda2_khz",
    "alpha2_over_alpha1", "complexity2",
    "T0_phase2", "H0_phase2",
}


# Per-parameter help text shown in the bottom panel when the input or its ±
# buttons gain focus. Two lines: title + body.
PARAM_HELP: dict[str, tuple[str, str]] = {
    "lambda_khz": (
        "λ — Run-4 input rate (kHz)",
        "The L1A rate the HLT farm must keep up with at phase 1. "
        "Speedup-needed and gauges compare farm throughput against this rate.",
    ),
    "T0": (
        "T0 — CPU reference throughput (events/s)",
        "Measured per-node CPU throughput on the reference node at t1. "
        "Combined with H0 to derive α₁ = T0/H0 (events per HS23).",
    ),
    "H0": (
        "H0 — CPU HS23 score at t1",
        "HEPScore23 of the reference CPU node at t1. Used in α₁ and σ_cpu.",
    ),
    "C0": (
        "C0 — CPU unit cost ($)",
        "Price of one reference CPU node at t1. Together with H0 it sets the "
        "baseline σ_cpu = H0/C0 (HS23 per $).",
    ),
    "Hgpu0": (
        "Hgpu0 — GPU HS23-equivalent per GPU at baseline",
        "How much HS23-equivalent compute one GPU provides at t1. "
        "Set to 0 (or leave blank) to model a CPU-only farm.",
    ),
    "Cgpu": (
        "Cgpu — GPU unit cost ($)",
        "Price of one GPU at t1. With Hgpu0 it sets σ_gpu = Hgpu0/Cgpu.",
    ),
    "f1": (
        "f1 — GPUable fraction at phase 1 (0..1)",
        "Fraction of HLT work that can run on GPU at t1. The model splits "
        "M1 between CPU and GPU to balance the two bottlenecks (min-of-two).",
    ),
    "budget1": (
        "M1 — Run-4 budget ($)",
        "Total dollars available for phase-1 hardware. Allocated optimally "
        "between CPU and GPU given f1, σ_cpu, σ_gpu.",
    ),
    "g": (
        "g — Annual perf/$ improvement (fraction)",
        "Yearly growth rate of HS23/$ for new hardware (e.g. 0.05 = +5%/yr). "
        "Drives σ_cpu(t) and σ_gpu(t) shown in the curve plot.",
    ),
    "epsilon": (
        "ε — Global efficiency in (0, 1]",
        "Multiplicative utilization factor on farm throughput. 1.0 means the "
        "farm runs at theoretical peak; lower values discount it.",
    ),
    "delta_years": (
        "Δ years — gap from the T0/H0 measurement to phase 1",
        "Years elapsed between when T0 and H0 were measured and the phase-1 "
        "evaluation point. σ grows by (1+g)^Δ from those measured values "
        "to reach σ@t1. Set to 0 if t1 coincides with the measurement.",
    ),
    "years_after": (
        "Years t1→t2 — gap between phase 1 and phase 2",
        "Phase 2 (Run 5) is evaluated this many years after phase 1. "
        "Hardware perf/$ grows over this span, aging factors are applied.",
    ),
    "budget2": (
        "M2 — Run-5 budget ($)",
        "Dollars available for phase-2 hardware on top of the (external) "
        "Run-4-equivalent re-buy. Allocated optimally per f2.",
    ),
    "f2": (
        "f2 — GPUable fraction at phase 2 (0..1)",
        "Fraction of HLT work that can run on GPU at t2 — typically higher "
        "than f1 as more code is ported.",
    ),
    "lambda2_khz": (
        "λ2 — Run-5 input rate (kHz)",
        "Trigger rate at phase 2. Leave blank to reuse λ (Run-4 rate).",
    ),
    "T0_phase2": (
        "T0-phase2 (CLI: --T0-phase2) — CPU reference throughput at t2 (events/s)",
        "Measured per-node CPU throughput at phase 2. Paired with H0-phase2 "
        "to set α₂ = T0-phase2 / H0-phase2. Must be set together; if both "
        "are filled they override the α₂ mode radio.",
    ),
    "H0_phase2": (
        "H0-phase2 (CLI: --H0-phase2) — CPU HS23 at t2",
        "HEPScore23 of the reference node at phase 2. Provide together with "
        "T0-phase2; either both or neither.",
    ),
    "alpha2_over_alpha1": (
        "α₂/α₁ — phase-2 vs phase-1 alpha ratio",
        "Active when the α₂ mode is 'ratio'. α₂ = α₁ × this. <1 means "
        "phase-2 work is more expensive per event; >1 means cheaper.",
    ),
    "complexity2": (
        "complexity₂ — phase-2 complexity multiplier",
        "Active when the α₂ mode is 'complexity factor'. α₂ = α₁ / this. "
        "complexity₂ > 1 means phase-2 events take more HS23 each.",
    ),
    "eta_new": (
        "η_new — phase-2 new-GPU performance factor",
        "Multiplicative correction on phase-2 GPU throughput vs. the "
        "extrapolated baseline. Use 1.0 for no correction.",
    ),
    "eta_old": (
        "η_old — aged Run-4 GPU efficiency factor (reported only)",
        "How much Run-4 GPUs still contribute at t2. Currently informational "
        "only — Run-4 hardware is IGNORED in the phase-2 optimization.",
    ),
    "chi_old": (
        "χ_old — aged Run-4 utilization factor (reported only)",
        "Multiplicative throughput penalty on aged Run-4 GPUs. "
        "Informational only at the moment.",
    ),
    "age_cpu_per_year": (
        "CPU age/year — per-year CPU performance decay (reported only)",
        "Multiplicative yearly factor on aged CPU HS23 (e.g. 0.95 = -5%/yr). "
        "Reported in the aging section, not used in the t2 optimization.",
    ),
    "age_gpu_per_year": (
        "GPU age/year — per-year GPU performance decay (reported only)",
        "Multiplicative yearly factor on aged GPU HS23. Informational.",
    ),
}

DEFAULT_HELP = (
    "Help",
    "Focus any input (Tab/Shift-Tab) to see what it controls. "
    "Press ± or Up/Down to step its value. Ctrl-Q quits, Ctrl-R resets.\n"
    "Tab into the Phase tables (top right) and ↑/↓ through the rows for "
    "explanations of each derived quantity.",
)


# Help text for the derived rows in the Phase 1, Phase 2, and Cross-check
# tables. Keys must match the first-column label exactly. The event handler
# looks these up by (table_id, row_label) when a row gets highlighted.
DERIVED_HELP_PHASE1: dict[str, tuple[str, str]] = {
    "alpha": (
        "α₁ — events per HS23 at phase 1",
        "α₁ = T0 / H0. How many events of HLT work fit in one HS23 unit "
        "of CPU compute. Combined with σ and ε to get throughput.",
    ),
    "σ_cpu @t0 (HS23/$)": (
        "σ_cpu @t0 — CPU HS23 per dollar at the time T0/H0 were measured",
        "Raw H0 / C0, at the instant of the baseline measurement. "
        "Annual perf/$ growth (g) is then applied over Δ years to reach σ@t1.",
    ),
    "σ_gpu @t0 (HS23/$)": (
        "σ_gpu @t0 — GPU HS23-equivalent per dollar at the GPU measurement time",
        "Hgpu0 / Cgpu at the instant Hgpu0 and Cgpu were measured. "
        "Zero when no GPU baseline is configured.",
    ),
    "growth @t1 (×)": (
        "growth @t1 — perf/$ multiplier from baseline to t1",
        "(1 + g) ** Δ, where Δ = 'Δ years' input. "
        "Multiplies σ@t0 to obtain σ@t1.",
    ),
    "σ_cpu @t1 (HS23/$)": (
        "σ_cpu @t1 — CPU HS23 per dollar at phase 1",
        "σ_cpu @t0 × growth @t1. Used in the optimal CPU/GPU budget split "
        "for Run 4.",
    ),
    "σ_gpu @t1 (HS23/$)": (
        "σ_gpu @t1 — GPU HS23-equivalent per dollar at phase 1",
        "σ_gpu @t0 × growth @t1.",
    ),
    "M_cpu": (
        "M_cpu — optimal CPU spend in M1 ($)",
        "Allocated optimally from the Run-4 budget M1 to balance the CPU "
        "and GPU streams (min-of-two-linears) when f1 > 0. When f1 = 0, "
        "all of M1 goes to CPU.",
    ),
    "M_gpu": (
        "M_gpu — optimal GPU spend in M1 ($)",
        "Remainder of M1 after M_cpu is allocated. Zero when f1 = 0 or "
        "no GPU baseline is configured.",
    ),
    "H_total (HS23)": (
        "H_total — total HS23 capacity bought with M1",
        "H_cpu + H_gpu = σ_cpu @t1 × M_cpu + σ_gpu @t1 × M_gpu. "
        "The aggregate HS23 compute of the Run-4 farm.",
    ),
    "throughput @t1": (
        "throughput @t1 — farm event rate at phase 1 (events/s)",
        "ε × α₁ × (balanced rate). Compare to λ = Run-4 input rate; "
        "if TP < λ the farm is undersized.",
    ),
    "N_cpu": (
        "N_cpu — integer CPU node count (phase 1)",
        "floor(M_cpu / Cref_cpu), where Cref_cpu defaults to C0. "
        "How many real machines you can buy.",
    ),
    "N_gpu": (
        "N_gpu — integer GPU count (phase 1)",
        "floor(M_gpu / Cgpu). Zero when no GPU baseline is configured.",
    ),
    "speedup needed @t1": (
        "speedup needed @t1 — gap between λ and TP at phase 1",
        "max(1, 1000·λ / TP). How many times faster per-event "
        "processing must become to meet λ. 1.00 means TP already meets λ.",
    ),
}

DERIVED_HELP_PHASE2: dict[str, tuple[str, str]] = {
    "alpha": (
        "α₂ — events per HS23 at phase 2",
        "Determined by the α₂ mode: same as α₁, α₁ × ratio, α₁ / complexity, "
        "or T0-phase2 / H0-phase2 when both are set (last takes priority).",
    ),
    "σ_cpu @t0 (HS23/$)": (
        "σ_cpu @t0 — CPU HS23 per dollar at the baseline measurement",
        "Same value as in the Phase 1 panel — H0 / C0 at the instant T0 and "
        "H0 were measured. Multiplied by growth @t2 to reach σ_cpu @t2.",
    ),
    "σ_gpu @t0 (HS23/$)": (
        "σ_gpu @t0 — GPU HS23-equivalent per dollar at the baseline",
        "Same value as in the Phase 1 panel — Hgpu0 / Cgpu at the GPU "
        "measurement instant. Multiplied by growth @t2 to reach σ_gpu @t2.",
    ),
    "growth @t2 (×)": (
        "growth @t2 — perf/$ multiplier from baseline to t2",
        "(1 + g) ** (Δ + N), where N = 'yrs t1->t2'. Multiplies σ@t0 to "
        "obtain σ@t2.",
    ),
    "σ_cpu @t2 (HS23/$)": (
        "σ_cpu @t2 — CPU HS23 per dollar at phase 2",
        "σ_cpu @t0 × growth @t2.",
    ),
    "σ_gpu @t2 (HS23/$)": (
        "σ_gpu @t2 — GPU HS23-equivalent per dollar at phase 2",
        "σ_gpu @t0 × growth @t2.",
    ),
    "M_cpu": (
        "M_cpu — optimal CPU spend from M2 ($)",
        "Optimal CPU portion of the Run-5 budget M2, on top of the external "
        "Run-4-equivalent re-buy. Does NOT include the re-buy cost (M_rebuy).",
    ),
    "M_gpu": (
        "M_gpu — optimal GPU spend from M2 ($)",
        "Remainder of M2 allocated to GPUs at phase 2.",
    ),
    "M_rebuy (extra)": (
        "M_rebuy — external Run-4-equivalent re-buy at t2 ($)",
        "Cost to externally re-acquire a Run-4-sized HS23 farm at t2 prices "
        "with split f2. Reported separately — NOT subtracted from M2.",
    ),
    "H_total (HS23)": (
        "H_total — total HS23 capacity at phase 2",
        "H1_total (re-bought Run-4-equivalent) + new HS23 bought with M2 "
        "(σ_cpu @t2 × M_cpu + η_new × σ_gpu @t2 × M_gpu). Comparable with "
        "the Phase 1 H_total row.",
    ),
    "throughput @t2": (
        "throughput @t2 — farm event rate at phase 2 (events/s)",
        "ε × α₂ × (balanced new throughput + H1_total). Compare to λ2.",
    ),
    "N_cpu": (
        "N_cpu — integer CPU node count (phase 2)",
        "floor(M_cpu / Cref_cpu). Phase-2-only count, excluding "
        "the re-buy nodes.",
    ),
    "N_gpu": (
        "N_gpu — integer GPU count (phase 2)",
        "floor(M_gpu / Cgpu). Phase-2-only count.",
    ),
    "speedup needed @t2": (
        "speedup needed @t2 — gap between λ2 and TP at phase 2",
        "max(1, 1000·λ2 / TP2). 1.00 means TP2 already meets λ2.",
    ),
}

DERIVED_HELP_CROSSCHECK: dict[str, tuple[str, str]] = {
    "optimal (this model)": (
        "optimal — speedup with the correct (min-of-two-linears) split",
        "TP obtained by allocating M2 between CPU and GPU so that the two "
        "per-dollar rates balance. The right answer.",
    ),
    "fixed split (wrong)": (
        "fixed split — speedup with a naive (1−f, f) budget split",
        "Budget split is forced to (1−f) for CPU and f for GPU, ignoring "
        "that the slower stream is the bottleneck. Lower TP than optimal.",
    ),
    "naive HS23 sum (wrong)": (
        "naive HS23 sum — speedup ignoring the min constraint",
        "Treats CPU and GPU HS23 as additive. Overestimates TP because "
        "the actual farm rate is bounded by the slower of the two streams.",
    ),
}

DERIVED_HELP_BY_TABLE: dict[str, dict[str, tuple[str, str]]] = {
    "phase1-table": DERIVED_HELP_PHASE1,
    "phase2-table": DERIVED_HELP_PHASE2,
    "crosscheck-table": DERIVED_HELP_CROSSCHECK,
}


# --------------------------------------------------------------------- #
#  Formatting helpers                                                   #
# --------------------------------------------------------------------- #

def fmt_money(x: float) -> str:
    if x is None:
        return "—"
    ax = abs(x)
    if ax >= 1e9:
        return f"${x/1e9:.2f}B"
    if ax >= 1e6:
        return f"${x/1e6:.2f}M"
    if ax >= 1e3:
        return f"${x/1e3:.1f}k"
    return f"${x:.0f}"


def fmt_rate(x: float) -> str:
    if x is None:
        return "—"
    if x >= 1e6:
        return f"{x/1e6:.2f} Mev/s"
    if x >= 1e3:
        return f"{x/1e3:.2f} kev/s"
    return f"{x:.1f} ev/s"


def fmt_value(x: Any) -> str:
    """Render a parameter value into the Input field."""
    if x is None:
        return ""
    if isinstance(x, float):
        return f"{x:g}"
    return str(x)


def fmt_speedup(factor: float) -> Text:
    """Bold, color-coded speedup factor for the 'speedup needed' row.

    Green at ×1.00 (farm meets λ), graded through yellow to deep red at ≥×3.
    """
    f = max(1.0, float(factor))
    if f >= 3.0:
        r, g, b = 180, 0, 0
    else:
        # Interpolate green → yellow → red on the [1, 3] range.
        t = (f - 1.0) / 2.0  # 0..1
        if t <= 0.5:
            tt = t * 2.0  # 0..1: green -> yellow
            r = int(200 * tt)
            g = 180
            b = 0
        else:
            tt = (t - 0.5) * 2.0  # 0..1: yellow -> red
            r = 200
            g = int(180 * (1.0 - tt))
            b = 0
    return Text(f"×{factor:.2f}", style=f"bold rgb({r},{g},{b})")


# --------------------------------------------------------------------- #
#  Custom widgets                                                       #
# --------------------------------------------------------------------- #

class ParamInput(Input):
    """Input that maps Up/Down arrows to ±step."""

    BINDINGS = [
        Binding("up", "param_step(1)", show=False),
        Binding("down", "param_step(-1)", show=False),
    ]

    def __init__(self, *args: Any, param_key: str = "", **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self._param_key = param_key

    def action_param_step(self, sign: int) -> None:
        app = self.app
        if hasattr(app, "step_param"):
            app.step_param(self._param_key, sign)


class _PathDialog(ModalScreen[str | None]):
    """Shared modal asking the user for a file path. Dismisses with the
    entered path on confirm, or None on cancel. Subclasses just supply the
    title, hint, confirm-button label, and placeholder."""

    BINDINGS = [
        Binding("escape", "cancel", "Cancel", show=False),
    ]

    DEFAULT_CSS = """
    _PathDialog {
        align: center middle;
    }
    _PathDialog > Vertical {
        background: $surface;
        border: round $accent;
        padding: 1 2;
        width: 70;
        height: auto;
    }
    _PathDialog Input {
        margin: 1 0;
    }
    _PathDialog Horizontal {
        height: 3;
        align-horizontal: right;
    }
    _PathDialog Button {
        margin-left: 1;
    }
    """

    title_text = "File path"
    hint_text = ""
    confirm_label = "OK"
    placeholder_text = ""

    def __init__(self, initial_path: str = "") -> None:
        super().__init__()
        self._initial_path = initial_path

    def compose(self) -> ComposeResult:
        with Vertical():
            yield Label(f"[bold]{self.title_text}[/bold]")
            if self.hint_text:
                yield Label(self.hint_text, classes="hint")
            yield Input(
                value=self._initial_path,
                placeholder=self.placeholder_text,
                id="path-input",
            )
            with Horizontal():
                yield Button("Cancel", id="path-cancel")
                yield Button(self.confirm_label, id="path-confirm",
                             variant="primary")

    def on_mount(self) -> None:
        inp = self.query_one("#path-input", Input)
        inp.focus()
        # Move cursor to end so Enter accepts the suggestion as-is, but the
        # user can also backspace/edit it.
        inp.cursor_position = len(inp.value)

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "path-confirm":
            self.dismiss(self.query_one("#path-input", Input).value)
        else:
            self.dismiss(None)

    def on_input_submitted(self, event: Input.Submitted) -> None:
        self.dismiss(event.value)

    def action_cancel(self) -> None:
        self.dismiss(None)


class LoadDialog(_PathDialog):
    title_text = "Load parameters from JSON"
    hint_text = "Enter the path to a snapshot saved with Ctrl+S."
    confirm_label = "Load"
    placeholder_text = "/path/to/farm_extrapolation_*.json"


class SaveDialog(_PathDialog):
    title_text = "Save parameters as JSON"
    hint_text = "Press Enter to use the suggested filename, or edit it first."
    confirm_label = "Save"
    placeholder_text = "farm_extrapolation_*.json"


class ScreenshotDialog(_PathDialog):
    title_text = "Save current view as image"
    hint_text = (
        "Defaults to a high-res PNG. End the filename with .svg to keep "
        "the raw vector format instead."
    )
    confirm_label = "Save"
    placeholder_text = "farm_extrapolation_*.png"


def load_payload_from_json(path: str) -> tuple[dict[str, Any], str]:
    """Read a JSON saved by `action_save` (or compatible) and return
    (params_dict, alpha2_mode). Raises ValueError with a friendly message
    if the file is missing or malformed."""
    import os
    path = os.path.expanduser(path)
    try:
        with open(path) as fh:
            raw = json.load(fh)
    except FileNotFoundError:
        raise ValueError(f"file not found: {path}")
    except json.JSONDecodeError as e:
        raise ValueError(f"not valid JSON: {e}")
    if not isinstance(raw, dict):
        raise ValueError("top-level JSON must be an object")
    params_in = raw.get("params") or {}
    if not isinstance(params_in, dict):
        raise ValueError("'params' must be an object")
    # Only keep keys we recognise; coerce numeric values.
    params: dict[str, Any] = {}
    for k, v in params_in.items():
        if k not in ARG_DEFAULTS:
            continue
        if v is None:
            params[k] = None
        else:
            try:
                params[k] = float(v)
            except (TypeError, ValueError):
                # leave as-is (e.g. start_date string); compute() will validate
                params[k] = v
    mode = raw.get("alpha2_mode", "same")
    if mode not in ("same", "ratio", "complexity"):
        mode = "same"
    return params, mode


class StepButton(Static, can_focus=False):
    """A flat single-character clickable chevron. Used in place of Button so
    we get strict 1-cell rendering (Textual's Button widget injects padding
    and a min-width that silently clip the row)."""

    def __init__(self, content: str, *, param_key: str, sign: int, **kwargs: Any) -> None:
        super().__init__(content, **kwargs)
        self._param_key = param_key
        self._sign = sign

    def on_click(self) -> None:
        app = self.app
        if hasattr(app, "step_param"):
            app.step_param(self._param_key, self._sign)


# --------------------------------------------------------------------- #
#  The App                                                              #
# --------------------------------------------------------------------- #

class FarmTUI(App):
    """Live interactive view of the two-phase farm projection."""

    CSS = """
    Screen {
        layout: horizontal;
    }
    #inputs-column {
        width: 42;
        border: solid $primary;
        padding: 0 1;
    }
    #results-column {
        width: 1fr;
        padding: 0 1;
    }
    /* Row widths are fully fixed so columns line up across all sections.
       Unicode glyphs (λ, ε) make 1fr rendering shift slightly per row;
       fixed widths sidestep that. Total: 14 + 1 + 18 + 1 = 34, leaves
       cushion inside the 42-wide inputs column. */
    .param-row {
        height: 1;
        width: 34;
        margin: 0;
        padding: 0;
    }
    .param-row Label {
        width: 14;
        min-width: 14;
        max-width: 14;
        content-align: left middle;
        padding: 0;
        margin: 0;
    }
    /* Flat single-cell chevron (a Static, not a Button — Button's default CSS
       silently overrides ours and clips the right chevron). */
    .step-btn {
        min-width: 1;
        width: 1;
        max-width: 1;
        height: 1;
        margin: 0;
        padding: 0;
        color: $text-muted;
    }
    .step-btn:hover {
        color: $accent;
        text-style: bold;
    }
    /* Borderless fixed-width input. Fixed width keeps the right chevron at
       the same column on every row. */
    .param-row ParamInput {
        width: 18;
        min-width: 18;
        max-width: 18;
        height: 1;
        border: none;
        padding: 0 1;
        margin: 0;
        background: $surface;
    }
    .param-row ParamInput:focus {
        background: $boost;
        color: $accent;
    }
    .param-row ParamInput.-invalid {
        background: $error 20%;
    }
    .panel {
        border: solid $accent;
        padding: 0 1;
        margin: 0 0 1 0;
        height: auto;
    }
    .phase-tables {
        height: auto;
    }
    .phase-tables DataTable {
        width: 1fr;
        height: auto;
    }
    #sigma-plot {
        height: 15;
    }
    #error-line {
        color: $error;
        height: 1;
        padding: 0 1;
        background: $surface;
    }
    RadioSet {
        height: auto;
    }
    Collapsible {
        margin: 0;
        padding: 0;
    }
    """

    # Ctrl-combos work even when an Input has focus (where plain letters would
    # be consumed as text). Plain 'q'/'r'/'s'/'l'/'i' also work outside inputs.
    BINDINGS = [
        Binding("ctrl+q,q", "quit", "Quit"),
        Binding("ctrl+r,r", "reset", "Reset"),
        Binding("ctrl+s,s", "save", "Save JSON"),
        Binding("ctrl+l,l", "load", "Load JSON"),
        Binding("ctrl+i,i", "save_image", "Save PNG"),
    ]

    def __init__(self, initial: dict[str, Any]) -> None:
        super().__init__()
        self.title = "NGT Farm Extrapolation"
        self.params: dict[str, Any] = dict(initial)
        self.alpha2_mode: str = self._infer_alpha2_mode(initial)
        self.result: dict | None = None
        self.last_error: str = ""
        # Suppress recompute storms while we programmatically set inputs.
        self._suspend_recompute = False

    @staticmethod
    def _infer_alpha2_mode(initial: dict[str, Any]) -> str:
        if initial.get("alpha2_over_alpha1") is not None:
            return "ratio"
        if initial.get("complexity2") is not None:
            return "complexity"
        return "same"

    # ------- layout ------- #

    def compose(self) -> ComposeResult:
        yield Header()
        with Horizontal():
            with VerticalScroll(id="inputs-column"):
                for section_title, items in SECTIONS:
                    with Collapsible(title=section_title, collapsed=False):
                        for key, label in items:
                            yield self._make_param_row(key, label)
                with Collapsible(title="α₂ mode", collapsed=False):
                    yield RadioSet(
                        RadioButton(
                            "same as α₁",
                            value=(self.alpha2_mode == "same"),
                            id="alpha-same",
                        ),
                        RadioButton(
                            "α₂/α₁ ratio",
                            value=(self.alpha2_mode == "ratio"),
                            id="alpha-ratio",
                        ),
                        RadioButton(
                            "complexity factor",
                            value=(self.alpha2_mode == "complexity"),
                            id="alpha-cplx",
                        ),
                        id="alpha-mode-set",
                    )
                    yield self._make_param_row("alpha2_over_alpha1", "α₂/α₁")
                    yield self._make_param_row("complexity2", "complexity")
            with VerticalScroll(id="results-column"):
                with Horizontal(classes="panel phase-tables"):
                    yield DataTable(id="phase1-table")
                    yield DataTable(id="phase2-table")
                yield Static("", id="budget-bars", classes="panel")
                yield Static("", id="throughput-gauges", classes="panel")
                yield PlotextPlot(id="sigma-plot", classes="panel")
                yield DataTable(id="crosscheck-table", classes="panel")
                yield Static("", id="help-panel", classes="panel")
                yield Static("", id="error-line")
        yield Footer()

    def _make_param_row(self, key: str, label: str) -> Horizontal:
        # Pre-pad to 14 cells. Belt-and-suspenders alongside the CSS width
        # constraint — Textual's default Label CSS sometimes shrink-fits.
        padded = label.ljust(14)[:14]
        return Horizontal(
            Label(padded),
            StepButton("‹", id=f"dec-{key}", classes="step-btn",
                       param_key=key, sign=-1),
            ParamInput(
                value=fmt_value(self.params.get(key)),
                id=f"in-{key}",
                param_key=key,
            ),
            StepButton("›", id=f"inc-{key}", classes="step-btn",
                       param_key=key, sign=+1),
            classes="param-row",
        )

    # ------- lifecycle ------- #

    def on_mount(self) -> None:
        t1 = self.query_one("#phase1-table", DataTable)
        t1.add_columns("Phase 1", "value")
        t1.cursor_type = "row"
        t1.zebra_stripes = True

        t2 = self.query_one("#phase2-table", DataTable)
        t2.add_columns("Phase 2", "value")
        t2.cursor_type = "row"
        t2.zebra_stripes = True

        cc = self.query_one("#crosscheck-table", DataTable)
        cc.add_columns("Cross-check", "TP", "speedup")
        cc.cursor_type = "row"
        cc.zebra_stripes = True

        for sel, title in [
            ("#budget-bars", "Budget split (M_cpu / M_gpu)"),
            ("#throughput-gauges", "Throughput vs required λ"),
            ("#sigma-plot", "Sigma curves: HS23 per $ vs years"),
            ("#crosscheck-table", "Cross-check speedups (this vs wrong models)"),
            ("#help-panel", "Help"),
        ]:
            self.query_one(sel).border_title = title

        self._show_help_for(None)  # default text
        self._sync_alpha2_inputs()
        self._recompute()

    # ------- input events ------- #
    # (StepButton chevrons handle their own clicks via on_click.)

    def on_input_changed(self, event: Input.Changed) -> None:
        if self._suspend_recompute:
            return
        inp_id = event.input.id or ""
        if not inp_id.startswith("in-"):
            return
        key = inp_id[len("in-"):]
        text = event.value.strip()
        if text == "":
            if key in NULLABLE_PARAMS:
                self.params[key] = None
            else:
                self._show_error(f"{key} cannot be empty")
                return
        else:
            try:
                val = float(text)
            except ValueError:
                self._show_error(f"invalid number for {key}: {text!r}")
                return
            if key in UNIT_INTERVAL_PARAMS and not (0.0 <= val <= 1.0):
                self._show_error(f"{key} must be in [0, 1] (got {val})")
                return
            self.params[key] = val
        self._recompute()

    def on_radio_set_changed(self, event: RadioSet.Changed) -> None:
        rid = event.pressed.id or ""
        if rid == "alpha-same":
            self.alpha2_mode = "same"
        elif rid == "alpha-ratio":
            self.alpha2_mode = "ratio"
        elif rid == "alpha-cplx":
            self.alpha2_mode = "complexity"
        self._sync_alpha2_inputs()
        self._recompute()

    # ------- step helper ------- #

    def step_param(self, key: str, sign: int) -> None:
        if key not in PARAM_STEPS:
            return
        cur = self.params.get(key)
        if cur is None:
            cur = ARG_DEFAULTS.get(key)
            if cur is None:
                cur = 0.0
        step = PARAM_STEPS[key]
        new_val = float(cur) + sign * step
        if key in UNIT_INTERVAL_PARAMS:
            new_val = max(0.0, min(1.0, new_val))
        self.params[key] = new_val
        # Update the Input widget; this will fire on_input_changed which
        # will re-validate and call _recompute().
        inp = self.query_one(f"#in-{key}", ParamInput)
        inp.value = fmt_value(new_val)

    # ------- alpha2 mode ------- #

    def _sync_alpha2_inputs(self) -> None:
        ratio_in = self.query_one("#in-alpha2_over_alpha1", ParamInput)
        cplx_in = self.query_one("#in-complexity2", ParamInput)
        ratio_in.disabled = self.alpha2_mode != "ratio"
        cplx_in.disabled = self.alpha2_mode != "complexity"

    def _build_namespace(self):
        kwargs = dict(self.params)
        # T0 @t2 / H0 @t2 take priority over the radio modes when BOTH are
        # filled — this mirrors `resolve_alpha2()` in farm_extrapolation_lib.
        # That way users can directly override α₂ from the Run 5 section
        # without having to touch the α₂ mode radio.
        has_t0h0_phase2 = (
            kwargs.get("T0_phase2") is not None
            and kwargs.get("H0_phase2") is not None
        )
        if has_t0h0_phase2:
            kwargs["alpha2_over_alpha1"] = None
            kwargs["complexity2"] = None
        else:
            if self.alpha2_mode == "same":
                kwargs["alpha2_over_alpha1"] = None
                kwargs["complexity2"] = None
            elif self.alpha2_mode == "ratio":
                kwargs["complexity2"] = None
            elif self.alpha2_mode == "complexity":
                kwargs["alpha2_over_alpha1"] = None
        # Don't pass start_date through (we always use delta_years from the TUI)
        kwargs["start_date"] = None
        return args_namespace(**kwargs)

    # ------- recompute & refresh ------- #

    def _recompute(self) -> None:
        try:
            ns = self._build_namespace()
            self.result = compute(ns)
        except SystemExit as e:
            self._show_error(str(e))
            return
        except Exception as e:
            self._show_error(f"{type(e).__name__}: {e}")
            return
        self._show_error("")
        self._refresh_panels(ns)

    def _show_error(self, msg: str) -> None:
        self.last_error = msg
        self.query_one("#error-line", Static).update(msg)

    # ------- contextual help (driven by focus changes) ------- #

    def on_descendant_focus(self, event: events.DescendantFocus) -> None:
        """React to focus changes — update the help panel for the focused input
        (or its ± button, or the highlighted row of a focused DataTable).
        `App.focused` is a property, not a reactive, so we hook the
        DescendantFocus event instead."""
        widget = event.widget
        if isinstance(widget, DataTable):
            self._show_derived_help_for_table(widget)
            return
        key = self._focused_param_key(widget)
        self._show_help_for(key)

    def on_data_table_row_highlighted(self,
                                      event: DataTable.RowHighlighted) -> None:
        """When the row cursor moves within a focused result table, update
        the help panel to describe the newly-highlighted derived quantity."""
        self._show_derived_help_for_table(event.data_table)

    def _show_derived_help_for_table(self, table: DataTable) -> None:
        helpdict = DERIVED_HELP_BY_TABLE.get(table.id or "")
        if helpdict is None:
            self._show_help_for(None)
            return
        try:
            row = table.get_row_at(table.cursor_row)
            label = str(row[0]).strip()
        except Exception:
            self._show_help_for(None)
            return
        if not label:
            self._show_help_for(None)
            return
        title, body = helpdict.get(
            label,
            (label, "(no help text registered for this row)"),
        )
        self._render_help_panel(title, body)

    @staticmethod
    def _focused_param_key(widget) -> str | None:
        if isinstance(widget, ParamInput):
            return widget._param_key or None
        wid = getattr(widget, "id", None) or ""
        if wid.startswith("dec-"):
            return wid[len("dec-"):]
        if wid.startswith("inc-"):
            return wid[len("inc-"):]
        if wid == "alpha-same":
            return "_alpha_mode_same"
        if wid == "alpha-ratio":
            return "alpha2_over_alpha1"
        if wid == "alpha-cplx":
            return "complexity2"
        return None

    def _show_help_for(self, key: str | None) -> None:
        if key is None:
            title, body = DEFAULT_HELP
        elif key == "_alpha_mode_same":
            title = "α₂ mode — same as α₁"
            body = (
                "Use α₂ = α₁: phase-2 events cost the same in HS23 as phase 1. "
                "Switch to ratio or complexity to model harsher reconstruction."
            )
        else:
            title, body = PARAM_HELP.get(
                key, (key, "(no help text registered for this control)")
            )
        self._render_help_panel(title, body)

    def _render_help_panel(self, title: str, body: str) -> None:
        try:
            panel = self.query_one("#help-panel", Static)
        except Exception:
            return
        panel.update(f"[bold]{title}[/bold]\n{body}")

    def _refresh_panels(self, ns) -> None:
        if not self.result:
            return
        r = self.result
        p1 = r["phase1"]
        p2 = r["phase2"]
        ints = r["integers"]

        # Growth multipliers applied to baseline H0/C0 to reach σ at t1/t2.
        # Surfacing them — together with σ@t0 — makes the projection chain
        # obvious: σ@t1 = σ@t0 × growth1, σ@t2 = σ@t0 × growth2.
        growth1 = (1.0 + ns.g) ** ns.delta_years
        growth2 = (1.0 + ns.g) ** (ns.delta_years + ns.years_after)
        sigma0_cpu = (ns.H0 / ns.C0) if (ns.H0 and ns.C0) else 0.0
        sigma0_gpu = (
            (ns.Hgpu0 / ns.Cgpu) if (ns.Hgpu0 and ns.Cgpu) else 0.0
        )

        # --- Phase 1 table --- #
        t1 = self.query_one("#phase1-table", DataTable)
        t1.clear()
        for k, v in [
            ("alpha", f"{p1['alpha1_events_per_HS23']:.3g}"),
            ("σ_cpu @t0 (HS23/$)", f"{sigma0_cpu:.3g}"),
            ("σ_gpu @t0 (HS23/$)", f"{sigma0_gpu:.3g}"),
            ("growth @t1 (×)", f"×{growth1:.3f}"),
            ("σ_cpu @t1 (HS23/$)", f"{p1['sigma1_cpu_HS23_per_$']:.3g}"),
            ("σ_gpu @t1 (HS23/$)", f"{p1['sigma1_gpu_HS23_per_$']:.3g}"),
            ("M_cpu", fmt_money(p1["M1_cpu_star"])),
            ("M_gpu", fmt_money(p1["M1_gpu_star"])),
            # Blank spacer to align the rows below with Phase 2's M_rebuy row.
            ("", ""),
            ("H_total (HS23)", f"{p1['H1_total_HS23']:.3g}"),
            ("throughput @t1", fmt_rate(p1["TP1_Farm_events_per_s"])),
            ("N_cpu", f"{ints['N1_cpu']:,}"),
            ("N_gpu", f"{ints['N1_gpu']:,}"),
            ("speedup needed @t1", fmt_speedup(p1["s_req_t1"])),
        ]:
            t1.add_row(k, v)

        # --- Phase 2 table --- #
        # Row order mirrors the Phase 1 table so the two panels read as
        # parallel columns: alpha → σ@t0 → growth → σ@phase → money
        # (with the P2-only M_rebuy slotted right after the M_cpu/M_gpu pair)
        # → H_total → throughput → counts → speedup.
        sigma2_cpu_v = p2["general"]["sigma2_cpu_HS23_per_$"]
        sigma2_gpu_v = p2["general"]["sigma2_gpu_HS23_per_$"]
        M2_cpu_v = p2["optimal_split"]["M2_cpu_star_$"]
        M2_gpu_v = p2["optimal_split"]["M2_gpu_star_$"]
        # Total HS23 at t2 = re-bought Run-4-equivalent (= H1_total) + new
        # capacity bought with M2 (CPU spend at σ_cpu, GPU spend discounted by
        # eta_new). Mirrors how Phase 1 reports H_total = H_cpu + H_gpu.
        H2_new = sigma2_cpu_v * M2_cpu_v + ns.eta_new * sigma2_gpu_v * M2_gpu_v
        H2_total = p1["H1_total_HS23"] + H2_new

        t2 = self.query_one("#phase2-table", DataTable)
        t2.clear()
        for k, v in [
            ("alpha", f"{p2['general']['alpha2_events_per_HS23']:.3g}"),
            ("σ_cpu @t0 (HS23/$)", f"{sigma0_cpu:.3g}"),
            ("σ_gpu @t0 (HS23/$)", f"{sigma0_gpu:.3g}"),
            ("growth @t2 (×)", f"×{growth2:.3f}"),
            ("σ_cpu @t2 (HS23/$)", f"{sigma2_cpu_v:.3g}"),
            ("σ_gpu @t2 (HS23/$)", f"{sigma2_gpu_v:.3g}"),
            ("M_cpu", fmt_money(M2_cpu_v)),
            ("M_gpu", fmt_money(M2_gpu_v)),
            ("M_rebuy (extra)", fmt_money(p2["external_rebuy_base"]["M_equiv_total_$"])),
            ("H_total (HS23)", f"{H2_total:.3g}"),
            ("throughput @t2", fmt_rate(p2["TP2_Farm_events_per_s"])),
            ("N_cpu", f"{ints['N2_cpu']:,}"),
            ("N_gpu", f"{ints['N2_gpu']:,}"),
            ("speedup needed @t2", fmt_speedup(p2["s_req_t2"])),
        ]:
            t2.add_row(k, v)

        # --- Budget bars --- #
        self.query_one("#budget-bars", Static).update(
            self._render_budget_bars(p1, p2)
        )

        # --- Throughput gauges --- #
        self.query_one("#throughput-gauges", Static).update(
            self._render_throughput_gauges(ns, p1, p2)
        )

        # --- Sigma plot --- #
        plot = self.query_one("#sigma-plot", PlotextPlot)
        traj = sigma_trajectory(ns, n_points=40, from_t0=True)
        plot.plt.clear_figure()
        plot.plt.theme("pro")
        if traj:
            ts = [t for (t, _, _) in traj]
            ss_cpu = [c for (_, c, _) in traj]
            ss_gpu = [g for (_, _, g) in traj]
            plot.plt.plot(ts, ss_cpu, label="σ_cpu", color=CPU_COLOR_RGB)
            if any(v > 0 for v in ss_gpu):
                plot.plt.plot(ts, ss_gpu, label="σ_gpu", color=GPU_COLOR_RGB)
            # Reference markers for the two evaluation points.
            try:
                plot.plt.vline(ns.delta_years, color="white")
                plot.plt.vline(ns.delta_years + ns.years_after, color="white")
            except Exception:
                # Older plotext without vline — skip the markers silently.
                pass
            plot.plt.xlabel("years from t0 (T0/H0 measurement) — "
                            "vertical lines mark t1 and t2")
            plot.plt.ylabel("HS23/$")
        plot.refresh()

        # --- Cross-check table --- #
        cc = self.query_one("#crosscheck-table", DataTable)
        cc.clear()
        cc.add_row(
            "optimal (this model)",
            fmt_rate(p2["TP2_Farm_events_per_s"]),
            f"×{p2['s_req_t2']:.2f}",
        )
        cc.add_row(
            "fixed split (wrong)",
            fmt_rate(p2["wrong_models"]["TP2_fixed_events_per_s"]),
            f"×{p2['wrong_models']['s_fixed']:.2f}",
        )
        cc.add_row(
            "naive HS23 sum (wrong)",
            fmt_rate(p2["wrong_models"]["TP2_naive_events_per_s"]),
            f"×{p2['wrong_models']['s_naive']:.2f}",
        )

    # ------- bar / gauge rendering ------- #

    @staticmethod
    def _stacked_bar(cpu: float, gpu: float, width: int = 28) -> str:
        total = cpu + gpu
        if total <= 0:
            return "[dim]" + "·" * width + "[/dim]"
        n_cpu = round(width * cpu / total)
        n_gpu = width - n_cpu
        return (
            f"[{CPU_COLOR_HEX}]{'█' * n_cpu}[/{CPU_COLOR_HEX}]"
            f"[{GPU_COLOR_HEX}]{'█' * n_gpu}[/{GPU_COLOR_HEX}]"
        )

    def _render_budget_bars(self, p1: dict, p2: dict) -> str:
        p1c = p1["M1_cpu_star"]
        p1g = p1["M1_gpu_star"]
        p2c = p2["optimal_split"]["M2_cpu_star_$"]
        p2g = p2["optimal_split"]["M2_gpu_star_$"]
        lines = [
            f"[bold]P1[/bold]  {self._stacked_bar(p1c, p1g)}  "
            f"[{CPU_COLOR_HEX}]CPU {fmt_money(p1c)}[/{CPU_COLOR_HEX}]  "
            f"[{GPU_COLOR_HEX}]GPU {fmt_money(p1g)}[/{GPU_COLOR_HEX}]",
            f"[bold]P2[/bold]  {self._stacked_bar(p2c, p2g)}  "
            f"[{CPU_COLOR_HEX}]CPU {fmt_money(p2c)}[/{CPU_COLOR_HEX}]  "
            f"[{GPU_COLOR_HEX}]GPU {fmt_money(p2g)}[/{GPU_COLOR_HEX}]",
            "",
            "[dim]Phase-2 bar shows the optimal split of M2 only — the external "
            "re-buy is reported as M_rebuy in the table.[/dim]",
        ]
        return "\n".join(lines)

    @staticmethod
    def _gauge_bar(ratio: float, width: int = 24) -> str:
        """Render a 0..1+ ratio as a filled bar, color-coded by headroom."""
        capped = max(0.0, min(1.0, ratio))
        n_fill = round(width * capped)
        n_empty = width - n_fill
        if ratio >= 1.0:
            color = "green"
        elif ratio >= 0.9:
            color = "yellow"
        else:
            color = "red"
        return (
            f"[{color}]{'█' * n_fill}[/{color}]"
            f"[dim]{'░' * n_empty}[/dim]"
        )

    def _render_throughput_gauges(self, ns, p1: dict, p2: dict) -> str:
        lam1 = ns.lambda_khz * 1000.0
        lam2 = (ns.lambda2_khz if ns.lambda2_khz is not None else ns.lambda_khz) * 1000.0
        tp1 = p1["TP1_Farm_events_per_s"]
        tp2 = p2["TP2_Farm_events_per_s"]
        r1 = (tp1 / lam1) if lam1 > 0 else 0.0
        r2 = (tp2 / lam2) if lam2 > 0 else 0.0
        return "\n".join([
            f"[bold]P1[/bold]  λ={lam1/1000:.1f}k  TP={tp1/1000:.2f}k  "
            f"{self._gauge_bar(r1)}  [bold]{r1*100:5.1f}%[/bold]",
            f"[bold]P2[/bold]  λ={lam2/1000:.1f}k  TP={tp2/1000:.2f}k  "
            f"{self._gauge_bar(r2)}  [bold]{r2*100:5.1f}%[/bold]",
            "",
            "[dim]≥100% green: TP meets λ.  90–100% yellow.  <90% red.[/dim]",
        ])

    # ------- key actions ------- #

    def action_reset(self) -> None:
        """Reset every input to ARG_DEFAULTS."""
        self._suspend_recompute = True
        try:
            for key, default in ARG_DEFAULTS.items():
                if key == "json":
                    continue
                self.params[key] = default
                try:
                    inp = self.query_one(f"#in-{key}", ParamInput)
                except Exception:
                    continue
                inp.value = fmt_value(default)
            self.alpha2_mode = "same"
            self.query_one("#alpha-same", RadioButton).value = True
            self._sync_alpha2_inputs()
        finally:
            self._suspend_recompute = False
        self._recompute()

    def action_save(self) -> None:
        """Open the save-as modal pre-filled with a timestamped suggestion."""
        ts = datetime.now().strftime("%Y%m%d_%H%M%S")
        suggested = f"farm_extrapolation_{ts}.json"
        self.push_screen(SaveDialog(initial_path=suggested),
                         callback=self._on_save_path)

    def _on_save_path(self, path: str | None) -> None:
        if not path:
            return
        path = path.strip()
        if not path:
            self._show_error("save cancelled: empty filename")
            return
        # Expand ~ for the user's convenience.
        import os
        target = os.path.expanduser(path)
        payload = {
            "params": {k: v for k, v in self.params.items() if k != "json"},
            "alpha2_mode": self.alpha2_mode,
            "result": self.result,
        }
        try:
            with open(target, "w") as fh:
                json.dump(payload, fh, indent=2, default=str)
            self._show_error(f"saved → {target}")
        except Exception as e:
            self._show_error(f"save failed: {e}")

    def action_save_image(self) -> None:
        """Open the screenshot dialog, pre-filled with a PNG suggestion."""
        ts = datetime.now().strftime("%Y%m%d_%H%M%S")
        suggested = f"farm_extrapolation_{ts}.png"
        self.push_screen(ScreenshotDialog(initial_path=suggested),
                         callback=self._on_save_image_path)

    def _on_save_image_path(self, path: str | None) -> None:
        if not path:
            return
        path = path.strip()
        if not path:
            return
        import os
        import tempfile
        from pathlib import Path

        target = os.path.expanduser(path)
        wants_svg = target.lower().endswith(".svg")
        if not wants_svg and not target.lower().endswith(".png"):
            target = target + ".png"

        target_path = Path(target).resolve()
        target_dir = str(target_path.parent)
        target_name = target_path.name

        # Textual writes SVG only. For SVG output, drop straight to the
        # target. For PNG, write SVG to a temp file then convert via cairosvg.
        if wants_svg:
            try:
                written = self.save_screenshot(filename=target_name,
                                               path=target_dir)
                self._show_error(f"saved → {written}")
            except Exception as e:
                self._show_error(f"image save failed: {e}")
            return

        try:
            import cairosvg
        except ImportError:
            self._show_error(
                "PNG export needs cairosvg — `pip install cairosvg` "
                "or save with a .svg extension instead."
            )
            return

        with tempfile.NamedTemporaryFile(
            mode="w", suffix=".svg", delete=False
        ) as tmp:
            tmp_svg = tmp.name
        try:
            tmp_path = Path(tmp_svg)
            written_svg = self.save_screenshot(
                filename=tmp_path.name, path=str(tmp_path.parent)
            )
            # High-res: 3600 px wide → roughly 4x what a default 900-px
            # terminal screenshot would render at.
            cairosvg.svg2png(
                url=written_svg, write_to=str(target_path),
                output_width=3600,
            )
            self._show_error(f"saved → {target_path}")
        except Exception as e:
            self._show_error(f"image save failed: {e}")
        finally:
            try:
                os.unlink(tmp_svg)
            except OSError:
                pass

    def action_load(self) -> None:
        """Open the load-from-JSON modal. On confirm, apply the snapshot."""
        self.push_screen(LoadDialog(), callback=self._on_load_path)

    def _on_load_path(self, path: str | None) -> None:
        if not path:
            return
        try:
            params, mode = load_payload_from_json(path)
        except ValueError as e:
            self._show_error(f"load failed: {e}")
            return
        self.apply_payload(params, mode)
        self._show_error(f"loaded ← {path}")

    def apply_payload(self, params: dict[str, Any], alpha2_mode: str) -> None:
        """Merge a loaded snapshot into the current state and refresh widgets.

        Keys present in `params` override current values; keys absent are
        left as-is. `alpha2_mode` updates the radio selection.
        """
        self._suspend_recompute = True
        try:
            for key, value in params.items():
                if key not in ARG_DEFAULTS:
                    continue
                self.params[key] = value
                try:
                    inp = self.query_one(f"#in-{key}", ParamInput)
                except Exception:
                    continue
                inp.value = fmt_value(value)
            # Drive the α₂ radio
            if alpha2_mode not in ("same", "ratio", "complexity"):
                alpha2_mode = "same"
            self.alpha2_mode = alpha2_mode
            rb_id = {"same": "alpha-same", "ratio": "alpha-ratio",
                     "complexity": "alpha-cplx"}[alpha2_mode]
            try:
                self.query_one(f"#{rb_id}", RadioButton).value = True
            except Exception:
                pass
            self._sync_alpha2_inputs()
        finally:
            self._suspend_recompute = False
        self._recompute()


# --------------------------------------------------------------------- #
#  Entry point                                                          #
# --------------------------------------------------------------------- #

def _build_parser() -> argparse.ArgumentParser:
    """Same flags as farmExtrapolation_twoPhases.py but none are required —
    missing ones fall back to ARG_DEFAULTS."""
    p = argparse.ArgumentParser(
        description="Live TUI for the two-phase farm extrapolation."
    )
    p.add_argument("--lambda-khz", type=float)
    p.add_argument("--T0", type=float)
    p.add_argument("--H0", type=float)
    p.add_argument("--C0", type=float)
    p.add_argument("--Hgpu0", type=float)
    p.add_argument("--Cgpu", type=float)
    p.add_argument("--f1", type=float)
    p.add_argument("--budget1", type=float)
    p.add_argument("--g", type=float)
    p.add_argument("--start-date", type=str)
    p.add_argument("--delta-years", type=float)
    p.add_argument("--epsilon", type=float)
    p.add_argument("--years-after", type=float)
    p.add_argument("--budget2", type=float)
    p.add_argument("--f2", type=float)
    p.add_argument("--lambda2-khz", type=float)
    p.add_argument("--T0-phase2", type=float)
    p.add_argument("--H0-phase2", type=float)
    p.add_argument("--alpha2-over-alpha1", type=float)
    p.add_argument("--complexity2", type=float)
    p.add_argument("--age-cpu-per-year", type=float)
    p.add_argument("--age-gpu-per-year", type=float)
    p.add_argument("--chi-old", type=float)
    p.add_argument("--eta-old", type=float)
    p.add_argument("--eta-new", type=float)
    p.add_argument("--Cref-cpu", type=float)
    p.add_argument(
        "--load",
        type=str,
        metavar="PATH",
        help="Pre-load a saved snapshot JSON before showing the TUI. "
             "Explicit --flag overrides still take precedence.",
    )
    return p


def _build_initial(cli_args: argparse.Namespace) -> tuple[dict[str, Any], str]:
    """Layered initial state: defaults → loaded JSON → explicit CLI flags.

    Returns (initial_params_dict, alpha2_mode).
    """
    initial = dict(ARG_DEFAULTS)
    alpha2_mode = "same"

    # Layer 1: --load JSON (if provided)
    load_path = getattr(cli_args, "load", None)
    if load_path:
        try:
            loaded, loaded_mode = load_payload_from_json(load_path)
        except ValueError as e:
            raise SystemExit(f"--load: {e}")
        for k, v in loaded.items():
            initial[k] = v
        alpha2_mode = loaded_mode

    # Layer 2: --start-date convenience → delta_years
    if getattr(cli_args, "start_date", None):
        from farm_extrapolation_lib import years_from_baseline
        initial["delta_years"] = years_from_baseline(cli_args.start_date)

    # Layer 3: explicit CLI overrides win
    for key in ARG_DEFAULTS:
        if key in ("json", "start_date"):
            continue
        cli_val = getattr(cli_args, key, None)
        if cli_val is not None:
            initial[key] = cli_val

    # If CLI flags also pin a specific α₂ mode, honour that over the loaded one.
    if getattr(cli_args, "alpha2_over_alpha1", None) is not None:
        alpha2_mode = "ratio"
    elif getattr(cli_args, "complexity2", None) is not None:
        alpha2_mode = "complexity"

    return initial, alpha2_mode


def main() -> None:
    args = _build_parser().parse_args()
    initial, alpha2_mode = _build_initial(args)
    # Seed the α₂ inputs so `_infer_alpha2_mode` picks them up.
    if alpha2_mode == "ratio" and initial.get("alpha2_over_alpha1") is None:
        initial["alpha2_over_alpha1"] = 1.0
    if alpha2_mode == "complexity" and initial.get("complexity2") is None:
        initial["complexity2"] = 1.0
    app = FarmTUI(initial=initial)
    app.run()


if __name__ == "__main__":
    main()
