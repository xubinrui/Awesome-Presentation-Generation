#!/usr/bin/env python3
"""Generate the SVG diagrams in assets/ from the data tables below.

Usage: python3 scripts/make_diagrams.py

Outputs:
  assets/taxonomy.svg      input → method → output overview
  assets/paper-matrix.svg  papers placed on backbone-model × generation-method axes

Edit the PLACEMENTS table when adding papers, then re-run. Colors come from a
CVD-validated categorical palette; chip color encodes the *output type* and is
consistent across both diagrams.
"""

from pathlib import Path

# ---------------------------------------------------------------- palette ---

SURFACE = "#fcfcfb"
INK = "#0b0b0b"
INK_2 = "#52514e"
MUTED = "#898781"
HAIRLINE = "#e1e0d9"
BORDER = "#d7d6cf"

OUTPUT_COLORS = {  # validated categorical palette, fixed slot order
    "slides": "#2a78d6",
    "poster": "#1baf7a",
    "layout": "#eda100",
    "video": "#008300",
}
OUTPUT_LABELS = {
    "slides": "Slide deck",
    "poster": "Poster",
    "layout": "Layout",
    "video": "Video",
}

FONT = "system-ui, -apple-system, 'Segoe UI', sans-serif"

# ------------------------------------------------------------ matrix data ---

METHODS = [
    ("pipeline", "Staged pipeline"),
    ("agent", "Multi-agent / iterative"),
    ("code", "Code generation"),
    ("rl", "RL post-training"),
    ("diffusion", "Diffusion generation"),
]

BACKBONES = [
    ("llm", "Off-the-shelf", "text LLM"),
    ("mllm", "Multimodal", "LLM / VLM"),
    ("finetuned", "Fine-tuned /", "specialized LM"),
    ("diffmodel", "Diffusion", "model"),
]

# (short name, backbone row, method column, output type)
PLACEMENTS = [
    ("PASS", "llm", "pipeline", "slides"),
    ("Self-Verify", "llm", "pipeline", "slides"),
    ("RCPS", "llm", "agent", "slides"),
    ("ArcDeck", "llm", "agent", "slides"),
    ("PosterGen", "llm", "agent", "poster"),
    ("P2P", "llm", "agent", "poster"),
    ("DocPres", "mllm", "pipeline", "slides"),
    ("ReLayout", "mllm", "pipeline", "layout"),
    ("PPTAgent", "mllm", "agent", "slides"),
    ("DeepPresenter", "mllm", "agent", "slides"),
    ("Paper2Poster", "mllm", "agent", "poster"),
    ("Paper2Video", "mllm", "agent", "video"),
    ("PresentAgent", "mllm", "agent", "video"),
    ("PreGenie", "mllm", "code", "slides"),
    ("CreatiPoster", "mllm", "code", "poster"),
    ("EvoPresent", "mllm", "rl", "slides"),
    ("DOC2PPT", "finetuned", "pipeline", "slides"),
    ("D2S", "finetuned", "pipeline", "slides"),
    ("PosterLlama", "finetuned", "pipeline", "layout"),
    ("PosterLLaVa", "finetuned", "pipeline", "layout"),
    ("AutoPresent", "finetuned", "code", "slides"),
    ("SlideCoder", "finetuned", "code", "slides"),
    ("DeepSlides", "finetuned", "code", "slides"),
    ("AeSlides", "finetuned", "rl", "layout"),
    ("LaySPA", "finetuned", "rl", "layout"),
    ("RA-Diffusion", "diffmodel", "diffusion", "layout"),
    ("UniLayDiff", "diffmodel", "diffusion", "layout"),
    ("iPoster", "diffmodel", "diffusion", "layout"),
    ("POSTA", "diffmodel", "diffusion", "poster"),
    ("PosterOmni", "diffmodel", "diffusion", "poster"),
]

# ---------------------------------------------------------------- helpers ---


def esc(s: str) -> str:
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def text(x, y, s, size=12, fill=INK, weight="normal", anchor="start", spacing=None):
    extra = f' letter-spacing="{spacing}"' if spacing else ""
    return (
        f'<text x="{x}" y="{y}" font-family="{FONT}" font-size="{size}" '
        f'font-weight="{weight}" fill="{fill}" text-anchor="{anchor}"{extra}>{esc(s)}</text>'
    )


def chip(x, y, w, name, color):
    dot_cx, dot_cy = x + 14, y + 13
    return (
        f'<rect x="{x}" y="{y}" width="{w}" height="26" rx="6" fill="#ffffff" '
        f'stroke="{BORDER}" stroke-width="1"/>'
        f'<circle cx="{dot_cx}" cy="{dot_cy}" r="4.5" fill="{color}"/>'
        + text(x + 26, y + 17.5, name, size=12, fill=INK)
    )


def legend(x, y):
    parts = []
    for key in OUTPUT_COLORS:
        parts.append(f'<circle cx="{x + 6}" cy="{y - 4}" r="5" fill="{OUTPUT_COLORS[key]}"/>')
        label = OUTPUT_LABELS[key]
        parts.append(text(x + 17, y, label, size=12, fill=INK_2))
        x += 17 + 7.2 * len(label) + 22
    return "".join(parts)


# --------------------------------------------------------------- taxonomy ---


def build_taxonomy() -> str:
    W, H = 1240, 600
    node_w, node_h, gap = 250, 62, 28
    col_x = {"input": 70, "method": 495, "output": 920}
    top = 128
    ys = [top + i * (node_h + gap) for i in range(4)]
    cy = [y + node_h / 2 for y in ys]

    inputs = [
        ("Prompt / Topic", "a sentence or a theme"),
        ("Document / Report", "long-form source text"),
        ("Scientific Paper", "PDF with figures & structure"),
        ("Existing Deck", "+ natural-language edit requests"),
    ]
    methods = [
        ("Staged LLM pipeline", "outline → content → layout"),
        ("Multi-agent / iterative", "roles + reflection on rendered output"),
        ("Code generation", "emit python-pptx · HTML · Slidev"),
        ("Diffusion / layout model", "place and size canvas elements"),
    ]
    outputs = [
        ("Slide deck", "slides", "editable PPTX · HTML deck"),
        ("Poster", "poster", "research or artistic poster"),
        ("Layout", "layout", "positioned elements on a canvas"),
        ("Presentation video", "video", "narrated slides + synced speech"),
    ]

    # (source idx, target idx) between columns
    in_to_m = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (2, 1), (2, 0), (3, 1)]
    m_to_out = [(0, 0), (1, 0), (1, 1), (1, 3), (2, 0), (2, 1), (3, 2), (3, 1)]

    def spread(pairs, end):
        """Vertical offsets so parallel links don't overlap at a node edge."""
        idx = 0 if end == "src" else 1
        offsets = {}
        by_node = {}
        for p in pairs:
            by_node.setdefault(p[idx], []).append(p)
        for node, ps in by_node.items():
            n = len(ps)
            for i, p in enumerate(ps):
                offsets[p] = (i - (n - 1) / 2) * 12
        return offsets

    def links(pairs, x1, x2, color=None, per_pair_color=None):
        src_off = spread(pairs, "src")
        tgt_off = spread(pairs, "tgt")
        mid = (x1 + x2) / 2
        out = []
        for p in pairs:
            s, t = p
            y1, y2 = cy[s] + src_off[p], cy[t] + tgt_off[p]
            c = per_pair_color[p] if per_pair_color else color
            out.append(
                f'<path d="M {x1} {y1} C {mid} {y1}, {mid} {y2}, {x2} {y2}" '
                f'fill="none" stroke="{c}" stroke-width="2" stroke-opacity="0.5" '
                f'stroke-linecap="round"/>'
            )
        return "".join(out)

    e = []
    e.append(f'<rect width="{W}" height="{H}" rx="14" fill="{SURFACE}"/>')
    e.append(f'<rect x="0.5" y="0.5" width="{W - 1}" height="{H - 1}" rx="14" fill="none" stroke="{HAIRLINE}"/>')

    e.append(text(70, 52, "Presentation generation at a glance", size=19, weight="600"))
    e.append(text(70, 76, "what goes in, how it is generated, and what comes out", size=13, fill=INK_2))

    for label, key in [("INPUT", "input"), ("METHOD", "method"), ("OUTPUT", "output")]:
        e.append(text(col_x[key] + node_w / 2, top - 22, label, size=12, fill=MUTED,
                      weight="600", anchor="middle", spacing="2.5"))

    # links first, under nodes
    e.append(links(in_to_m, col_x["input"] + node_w, col_x["method"], color=BORDER))
    out_colors = {p: OUTPUT_COLORS[outputs[p[1]][1]] for p in m_to_out}
    e.append(links(m_to_out, col_x["method"] + node_w, col_x["output"], per_pair_color=out_colors))

    def node(x, y, title, desc, accent=None):
        parts = [
            f'<rect x="{x}" y="{y}" width="{node_w}" height="{node_h}" rx="9" '
            f'fill="#ffffff" stroke="{BORDER}" stroke-width="1"/>'
        ]
        tx = x + 18
        if accent:
            parts.append(
                f'<line x1="{x + 2}" y1="{y + 10}" x2="{x + 2}" y2="{y + node_h - 10}" '
                f'stroke="{accent}" stroke-width="4" stroke-linecap="round"/>'
            )
            tx = x + 22
        parts.append(text(tx, y + 26, title, size=14.5, weight="600"))
        parts.append(text(tx, y + 46, desc, size=12, fill=INK_2))
        return "".join(parts)

    for i, (title, desc) in enumerate(inputs):
        e.append(node(col_x["input"], ys[i], title, desc))
    for i, (title, desc) in enumerate(methods):
        e.append(node(col_x["method"], ys[i], title, desc))
    for i, (title, key, desc) in enumerate(outputs):
        e.append(node(col_x["output"], ys[i], title, desc, accent=OUTPUT_COLORS[key]))

    # RL note under the method column
    rl_y = ys[-1] + node_h + 24
    e.append(
        f'<rect x="{col_x["method"] - 10}" y="{rl_y}" width="{node_w + 20}" height="30" rx="15" '
        f'fill="none" stroke="{BORDER}" stroke-dasharray="4 4"/>'
    )
    e.append(text(col_x["method"] + node_w / 2, rl_y + 19.5,
                  "↺ RL post-training can be layered on any method",
                  size=12, fill=INK_2, anchor="middle"))

    body = "".join(e)
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" '
        f'viewBox="0 0 {W} {H}" role="img" '
        f'aria-label="Taxonomy: inputs, generation methods, and outputs">{body}</svg>\n'
    )


# ----------------------------------------------------------------- matrix ---


def build_matrix() -> str:
    W = 1240
    margin = 40
    gutter_w = 190
    header_h = 36
    chip_h, chip_gap, cell_pad = 26, 6, 12

    grid_x = margin + gutter_w
    grid_w = W - margin - grid_x
    col_w = grid_w / len(METHODS)

    cells = {}
    for name, row, col, out in PLACEMENTS:
        cells.setdefault((row, col), []).append((name, out))

    row_heights = []
    for row_key, *_ in BACKBONES:
        most = max(
            (len(cells.get((row_key, m[0]), [])) for m in METHODS),
            default=0,
        )
        row_heights.append(most * (chip_h + chip_gap) - chip_gap + 2 * cell_pad + 4)

    title_h = 96
    grid_y = title_h + header_h
    grid_h = sum(row_heights)
    H = grid_y + grid_h + 58

    e = []
    e.append(f'<rect width="{W}" height="{H}" rx="14" fill="{SURFACE}"/>')
    e.append(f'<rect x="0.5" y="0.5" width="{W - 1}" height="{H - 1}" rx="14" fill="none" stroke="{HAIRLINE}"/>')

    e.append(text(margin, 46, "Papers: backbone model × generation method", size=19, weight="600"))
    e.append(text(margin, 70, "each chip is a representative paper · chip color = output type",
                  size=13, fill=INK_2))
    e.append(legend(W - 480, 50))

    # column headers
    for j, (_, label) in enumerate(METHODS):
        cx = grid_x + j * col_w + col_w / 2
        e.append(text(cx, grid_y - 12, label, size=13, weight="600", anchor="middle"))

    # grid lines
    for j in range(len(METHODS) + 1):
        x = grid_x + j * col_w
        e.append(f'<line x1="{x}" y1="{grid_y}" x2="{x}" y2="{grid_y + grid_h}" stroke="{HAIRLINE}"/>')
    y = grid_y
    for rh in [0] + row_heights:
        y += rh
        e.append(f'<line x1="{margin}" y1="{y}" x2="{grid_x + grid_w}" y2="{y}" stroke="{HAIRLINE}"/>')
    e.append(f'<line x1="{margin}" y1="{grid_y}" x2="{grid_x + grid_w}" y2="{grid_y}" stroke="{HAIRLINE}"/>')

    # rows
    y = grid_y
    for i, (row_key, l1, l2) in enumerate(BACKBONES):
        rh = row_heights[i]
        e.append(text(margin + 8, y + rh / 2 - 4, l1, size=13, weight="600"))
        e.append(text(margin + 8, y + rh / 2 + 14, l2, size=12, fill=INK_2))
        for j, (col_key, _) in enumerate(METHODS):
            entries = cells.get((row_key, col_key), [])
            cx = grid_x + j * col_w
            if not entries:
                e.append(text(cx + col_w / 2, y + rh / 2 + 4, "—", size=13, fill=HAIRLINE,
                              anchor="middle"))
                continue
            block_h = len(entries) * (chip_h + chip_gap) - chip_gap
            cy = y + (rh - block_h) / 2
            for name, out in entries:
                e.append(chip(cx + cell_pad, cy, col_w - 2 * cell_pad, name, OUTPUT_COLORS[out]))
                cy += chip_h + chip_gap
        y += rh

    e.append(text(margin, grid_y + grid_h + 34,
                  "Representative works only — agentic systems often span several cells; "
                  "see the README tables for the full list.",
                  size=12, fill=MUTED))

    body = "".join(e)
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" '
        f'viewBox="0 0 {W} {H}" role="img" '
        f'aria-label="Matrix of papers by backbone model and generation method">{body}</svg>\n'
    )


if __name__ == "__main__":
    assets = Path(__file__).resolve().parent.parent / "assets"
    assets.mkdir(exist_ok=True)
    (assets / "taxonomy.svg").write_text(build_taxonomy(), encoding="utf-8")
    (assets / "paper-matrix.svg").write_text(build_matrix(), encoding="utf-8")
    print("wrote assets/taxonomy.svg and assets/paper-matrix.svg")
