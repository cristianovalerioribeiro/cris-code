# -*- coding: utf-8 -*-
"""Gera os biômetros (gráficos radiestésicos) do manual em SVG (unidades em mm). Versão 2: cores, ícones, listas penduláveis."""
import math, os, json, html

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "charts")
os.makedirs(OUT, exist_ok=True)
FONT = "Inter, 'DejaVu Sans', Arial, sans-serif"
INK = "#111"; QUIET = "#555"; LINE = "#2b2b2b"; GRID = "#9a9a9a"; ACCENT = "#1f4e8c"
FILL_A = "#ffffff"; FILL_B = "#f1f1f1"
PASTEL = ["#fde2e2", "#fdebd3", "#fff6cc", "#e3f4e1", "#dcecfb", "#e6e0f5", "#f3e1ef", "#e0f2f1", "#f0efe6", "#e8f1dc", "#fbe8e0", "#e3e9f6"]
CAT_COLORS = {"emocional": "#fbe3e3", "mental": "#e6e0f5", "fisica": "#e3f4e1", "energetica": "#fff3cc", "ambiental": "#e0f2f1", "transgeracional": "#fdebd3", "espiritual": "#dcecfb", "outro": "#f1f1f1"}
CAUSA_COLORS = [CAT_COLORS[k] for k in ("emocional", "mental", "fisica", "energetica", "ambiental", "transgeracional", "espiritual", "outro")]
CHAKRA_COLORS = {1: "#c62828", 2: "#ef6c00", 3: "#f9a825", 4: "#2e7d32", 5: "#1976d2", 6: "#283593", 7: "#6a1b9a"}
CHAKRA_TINT = {1: "#fbe0e0", 2: "#fde8d5", 3: "#fff6c8", 4: "#dff1e2", 5: "#d9e9fa", 6: "#dfe2f4", 7: "#ece0f5"}
CHAKRA_TINT2 = {1: "#fdf0f0", 2: "#fef4ea", 3: "#fffbe6", 4: "#eff8f0", 5: "#ecf4fc", 6: "#eff0f9", 7: "#f5effa"}
CHAKRA_NAMES = {1: "Básico", 2: "Sacral", 3: "Plexo solar", 4: "Cardíaco", 5: "Laríngeo", 6: "Frontal", 7: "Coronário"}
SANS = {1: "Muladhara", 2: "Svadhisthana", 3: "Manipura", 4: "Anahata", 5: "Vishuddha", 6: "Ajna", 7: "Sahasrara"}
CH = CHAKRA_NAMES

def esc(s): return html.escape(str(s), quote=True)
def polar(cx, cy, r, deg):
    a = math.radians(deg); return cx + r * math.cos(a), cy - r * math.sin(a)
def _arc_segments(cx, cy, r, a0, a1):
    """Arco de a0 a a1 em comandos A de no máximo 90°, para que todos os renderizadores desenhem o mesmo círculo."""
    sweep = 1 if a0 > a1 else 0
    n = max(1, int(math.ceil(abs(a0 - a1) / 90.0 - 1e-9)))
    out = []; a = a0
    for i in range(n):
        b = a0 + (a1 - a0) * (i + 1) / n
        x, y = polar(cx, cy, r, b)
        out.append(f"A{r:.2f} {r:.2f} 0 0 {sweep} {x:.2f} {y:.2f}")
        a = b
    return " ".join(out)
def arc_path(cx, cy, r, a0, a1):
    x0, y0 = polar(cx, cy, r, a0)
    return f"M{x0:.2f} {y0:.2f} " + _arc_segments(cx, cy, r, a0, a1)
def wedge(cx, cy, r0, r1, a0, a1):
    x0, y0 = polar(cx, cy, r1, a0); x2, y2 = polar(cx, cy, r0, a1)
    return (f"M{x0:.2f} {y0:.2f} " + _arc_segments(cx, cy, r1, a0, a1) + f" L{x2:.2f} {y2:.2f} " + _arc_segments(cx, cy, r0, a1, a0) + " Z")

def radial_text(cx, cy, r_in, r_out, deg, text, size=3.4, color=INK, weight="500"):
    """Rótulo centrado na faixa entre r_in e r_out, lido de dentro para fora (direita) ou de fora para dentro (esquerda)."""
    lines = text.split("\n")
    r_mid = (r_in + r_out) / 2
    x, y = polar(cx, cy, r_mid, deg)
    rot = -deg if deg <= 90 else 180 - deg
    n = len(lines)
    out = [f'<text font-size="{size}" fill="{color}" font-weight="{weight}" text-anchor="middle" transform="translate({x:.2f} {y:.2f}) rotate({rot:.2f})">']
    for i, ln in enumerate(lines):
        dy = (i - (n - 1) / 2) * (size * 1.15) + size * 0.35
        out.append(f'<tspan x="0" y="{dy:.2f}">{esc(ln)}</tspan>')
    out.append('</text>'); return "".join(out)

def pendulo_icon(cx, cy):
    return (f'<circle cx="{cx}" cy="{cy}" r="2.4" fill="white" stroke="{ACCENT}" stroke-width="0.7"/>'
            f'<circle cx="{cx}" cy="{cy}" r="0.9" fill="{ACCENT}"/>')

def testemunho(cx, cy, w=40, h=16, label=None):
    return f'<rect x="{cx-w/2:.2f}" y="{cy:.2f}" width="{w}" height="{h}" rx="1.2" fill="none" stroke="{GRID}" stroke-width="0.45" stroke-dasharray="1.4 1"/>'

def svg_wrap(body, w, h):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}mm" height="{h}mm" viewBox="0 0 {w} {h}" font-family="{FONT}">'
            f'<rect x="0" y="0" width="{w}" height="{h}" fill="white"/>{body}</svg>')


def _fit_radial(labels, r_in, r_out, n, lo=2.6, hi=5.2, margin_w=3.0):
    """Maior fonte (mm) tal que cada rótulo radial caiba no comprimento r_out-r_in e na largura angular do setor."""
    import math as _m
    best = lo
    s = hi
    while s >= lo:
        ok = True
        for lab in labels:
            lines = str(lab).split("\n"); maxlen = max(len(l) for l in lines)
            w = maxlen * 0.52 * s; h = len(lines) * 1.15 * s
            r_mid = (r_in + r_out) / 2; r_inner = r_mid - w / 2
            if w > (r_out - r_in) - margin_w or r_inner < r_in or h > 0.86 * r_inner * _m.pi / n:
                ok = False; break
        if ok: best = s; break
        s = round(s - 0.1, 2)
    return best

# ---------- Leque ----------
def fan(sectors, title_center=None, R=86, r0=22, label_size=None, groups=None, w=190, h=None, numbers=True, colors=None, icons=None, tint=None):
    cy = 96 + (9 if groups else 0); cx = w / 2
    h = h or cy + 21
    n = len(sectors)
    if n > 15: r0 = max(r0, 36)
    elif n > 12: r0 = max(r0, 30)
    elif n > 9: r0 = max(r0, 26)
    _cap = label_size or 5.2
    label_size = min(_cap, _fit_radial(sectors, r0 + 3.5, (R - 3) if not icons else (R - 14.5), n))
    step = 180.0 / n
    out = []
    for i, s in enumerate(sectors):
        a0 = 180 - i * step; a1 = 180 - (i + 1) * step
        if colors: fill = colors[i % len(colors)]
        elif tint: fill = tint[0] if i % 2 == 0 else tint[1]
        else: fill = FILL_A if i % 2 == 0 else FILL_B
        out.append(f'<path d="{wedge(cx, cy, r0, R, a0, a1)}" fill="{fill}" stroke="{LINE}" stroke-width="0.35"/>')
        mid = (a0 + a1) / 2
        r_label_out = R - 3 if not icons else R - 14.5
        tcol = INK
        if colors:
            hx = fill.lstrip('#'); rr, gg, bb = int(hx[0:2], 16), int(hx[2:4], 16), int(hx[4:6], 16)
            if 0.299 * rr + 0.587 * gg + 0.114 * bb < 140: tcol = '#ffffff'
        out.append(radial_text(cx, cy, r0 + 3.5, r_label_out, mid, s, size=label_size, color=tcol))
        if icons and icons[i]:
            ix, iy = polar(cx, cy, R - 6, mid)
            out.append(icons[i](ix, iy))
        if numbers:
            nx, ny = polar(cx, cy, R + 4.8, mid)
            out.append(f'<circle cx="{nx:.2f}" cy="{ny:.2f}" r="3.0" fill="white" stroke="{LINE}" stroke-width="0.35"/>')
            out.append(f'<text x="{nx:.2f}" y="{ny+1.2:.2f}" font-size="3.4" fill="{INK}" text-anchor="middle" font-weight="600">{i+1}</text>')
    out.append(f'<path d="{arc_path(cx, cy, R, 180, 0)}" fill="none" stroke="{LINE}" stroke-width="0.7"/>')
    out.append(f'<path d="{arc_path(cx, cy, r0, 180, 0)}" fill="none" stroke="{LINE}" stroke-width="0.7"/>')
    out.append(f'<line x1="{cx-R:.2f}" y1="{cy}" x2="{cx-r0:.2f}" y2="{cy}" stroke="{LINE}" stroke-width="0.7"/>')
    out.append(f'<line x1="{cx+r0:.2f}" y1="{cy}" x2="{cx+R:.2f}" y2="{cy}" stroke="{LINE}" stroke-width="0.7"/>')
    if groups:
        acc = 0
        for gi, (gname, count, gcolor) in enumerate(groups):
            a0 = 180 - acc * step; a1 = 180 - (acc + count) * step; acc += count
            out.append(f'<path d="{wedge(cx, cy, R + 9, R + 14.5, a0, a1)}" fill="{gcolor}" stroke="{LINE}" stroke-width="0.3"/>')
            mid = (a0 + a1) / 2; gx, gy = polar(cx, cy, R + 11.75, mid)
            out.append(f'<text x="0" y="0" font-size="3.1" fill="{INK}" font-weight="700" text-anchor="middle" transform="translate({gx:.2f} {gy:.2f}) rotate({90 - mid:.2f})"><tspan x="0" y="1.1">{esc(gname)}</tspan></text>')
    if title_center:
        out.append(f'<text x="{cx}" y="{cy-9}" font-size="3.8" fill="{ACCENT}" text-anchor="middle" font-weight="700">{esc(title_center)}</text>')
    out.append(pendulo_icon(cx, cy))
    out.append(testemunho(cx, cy + 5, w=40, h=14))
    return svg_wrap("".join(out), w, h)

# ---------- Escala semicircular ----------
def dial(vmin, vmax, major, minor, micro=None, marks=None, fmt=None, R=86, w=190, h=117, blind=False, title_center=None, zones=None, zone_labels=None):
    cx, cy = w / 2, 96
    out = []; span = vmax - vmin
    ang = lambda v: 180 - 180 * (v - vmin) / span
    fmt = fmt or (lambda v: f"{int(v)}" if float(v).is_integer() else f"{v}")
    if zones:
        for z0, z1, color in zones:
            out.append(f'<path d="{wedge(cx, cy, R - 11, R, ang(z0), ang(z1))}" fill="{color}" stroke="none"/>')
            out.append(f'<path d="{wedge(cx, cy, 8, R - 11, ang(z0), ang(z1))}" fill="{color}" fill-opacity="0.35" stroke="none"/>')
    else:
        out.append(f'<path d="{wedge(cx, cy, R - 11, R, 180, 0)}" fill="{FILL_B}" stroke="none"/>')
    def tick(v, length, width, color=LINE):
        a = ang(v); x0, y0 = polar(cx, cy, R, a); x1, y1 = polar(cx, cy, R - length, a)
        return f'<line x1="{x0:.2f}" y1="{y0:.2f}" x2="{x1:.2f}" y2="{y1:.2f}" stroke="{color}" stroke-width="{width}"/>'
    if micro:
        v = vmin
        while v <= vmax + 1e-9: out.append(tick(v, 2.5, 0.2, "#777")); v += micro
    v = vmin
    while v <= vmax + 1e-9: out.append(tick(v, 5.5, 0.4)); v += minor
    v = vmin
    while v <= vmax + 1e-9:
        out.append(tick(v, 10, 0.7))
        if not blind:
            if abs(v - vmin) < 1e-9:
                out.append(f'<text x="{cx - R + 1:.2f}" y="{cy + 5.5:.2f}" font-size="4.2" fill="{INK}" font-weight="700" text-anchor="start">{esc(fmt(v))}</text>')
            elif abs(v - vmax) < 1e-9:
                out.append(f'<text x="{cx + R - 1:.2f}" y="{cy + 5.5:.2f}" font-size="4.2" fill="{INK}" font-weight="700" text-anchor="end">{esc(fmt(v))}</text>')
            else:
                x, y = polar(cx, cy, R + 5.5, ang(v))
                out.append(f'<text x="{x:.2f}" y="{y+1.5:.2f}" font-size="4.2" fill="{INK}" font-weight="700" text-anchor="middle">{esc(fmt(v))}</text>')
        v += major
    out.append(f'<path d="{arc_path(cx, cy, R, 180, 0)}" fill="none" stroke="{LINE}" stroke-width="0.8"/>')
    out.append(f'<path d="{arc_path(cx, cy, R - 11, 180, 0)}" fill="none" stroke="{LINE}" stroke-width="0.45"/>')
    for v in [vmin + span * f for f in (0, 0.25, 0.5, 0.75, 1)]:
        a = ang(v); x0, y0 = polar(cx, cy, 8, a); x1, y1 = polar(cx, cy, R - 11, a)
        out.append(f'<line x1="{x0:.2f}" y1="{y0:.2f}" x2="{x1:.2f}" y2="{y1:.2f}" stroke="{GRID}" stroke-width="0.25" stroke-dasharray="1 1.5"/>')
    for m in (marks or []):
        v, label, color = m; a = ang(v)
        x0, y0 = polar(cx, cy, R + 1, a); x1, y1 = polar(cx, cy, R - 17, a)
        out.append(f'<line x1="{x0:.2f}" y1="{y0:.2f}" x2="{x1:.2f}" y2="{y1:.2f}" stroke="{color}" stroke-width="1"/>')
        out.append(radial_text(cx, cy, R - 42, R - 20, a, label, size=3.2, color=color, weight="700"))
    for v, txt in (zone_labels or []):
        a = ang(v); x, y = polar(cx, cy, R - 52, a)
        out.append(f'<text x="{x:.2f}" y="{y:.2f}" font-size="4.0" fill="{INK}" font-weight="600" text-anchor="middle">{esc(txt)}</text>')
    if title_center:
        out.append(f'<text x="{cx}" y="{cy-10}" font-size="3.8" fill="{ACCENT}" text-anchor="middle" font-weight="700">{esc(title_center)}</text>')
    out.append(pendulo_icon(cx, cy)); out.append(testemunho(cx, cy + 5, w=40, h=14))
    return svg_wrap("".join(out), w, h)

# ---------- Régua linear ----------
def ruler(vmin, vmax, major, minor, blind=False, marks=None, w=190, h=42, fmt=None, label=None, zones=None):
    x0, x1, y = 12, w - 12, 20
    fmt = fmt or (lambda v: f"{int(v)}"); span = vmax - vmin
    X = lambda v: x0 + (x1 - x0) * (v - vmin) / span
    out = []
    if zones:
        for z0, z1, color in zones:
            out.append(f'<rect x="{X(z0):.2f}" y="{y-8}" width="{X(z1)-X(z0):.2f}" height="8" fill="{color}"/>')
    else:
        out.append(f'<rect x="{x0}" y="{y-8}" width="{x1-x0}" height="8" fill="{FILL_B}"/>')
    out.append(f'<line x1="{x0}" y1="{y}" x2="{x1}" y2="{y}" stroke="{LINE}" stroke-width="0.8"/>')
    v = vmin
    while v <= vmax + 1e-9:
        out.append(f'<line x1="{X(v):.2f}" y1="{y}" x2="{X(v):.2f}" y2="{y-4}" stroke="{LINE}" stroke-width="0.3"/>'); v += minor
    v = vmin
    while v <= vmax + 1e-9:
        out.append(f'<line x1="{X(v):.2f}" y1="{y}" x2="{X(v):.2f}" y2="{y-8}" stroke="{LINE}" stroke-width="0.7"/>')
        if not blind: out.append(f'<text x="{X(v):.2f}" y="{y+6}" font-size="4.0" fill="{INK}" font-weight="700" text-anchor="middle">{esc(fmt(v))}</text>')
        v += major
    for m in (marks or []):
        v, lab, color = m
        out.append(f'<line x1="{X(v):.2f}" y1="{y-11}" x2="{X(v):.2f}" y2="{y+1}" stroke="{color}" stroke-width="1"/>')
        out.append(f'<text x="{X(v):.2f}" y="{y-12.5}" font-size="3.2" fill="{color}" font-weight="700" text-anchor="middle">{esc(lab)}</text>')
    if label: out.append(f'<text x="{x0}" y="{y+13}" font-size="3" fill="{QUIET}">{esc(label)}</text>')
    return svg_wrap("".join(out), w, h)

# ---------- Anéis ----------
def rings(ring_specs, R=92, w=190, h=128, thick=None, fonts=None, sector_colors=None):
    cx, cy = w / 2, 100
    out = []; nr = len(ring_specs)
    thick = thick or [(R - 14) / nr] * nr
    r_top = R
    for ri, (rname, sectors, color) in enumerate(ring_specs):
        r1 = r_top; r0 = r1 - thick[ri]; r_top = r0; n = len(sectors); step = 180.0 / n
        for i, s in enumerate(sectors):
            a0 = 180 - i * step; a1 = 180 - (i + 1) * step
            fill = sector_colors[ri][i % len(sector_colors[ri])] if sector_colors and sector_colors[ri] else color
            op = 1 if sector_colors and sector_colors[ri] else (0.9 if i % 2 == 0 else 0.45)
            out.append(f'<path d="{wedge(cx, cy, r0, r1, a0, a1)}" fill="{fill}" fill-opacity="{op}" stroke="{LINE}" stroke-width="0.3"/>')
            fs = _fit_radial(sectors, r0 + 2, r1 - 1.5, n, lo=2.4, hi=4.4, margin_w=1.5)
            out.append(radial_text(cx, cy, r0 + 2, r1 - 1.5, (a0 + a1) / 2, s, size=fs))
    out.append(f'<path d="{arc_path(cx, cy, R, 180, 0)}" fill="none" stroke="{LINE}" stroke-width="0.7"/>')
    lx = cx - R
    for i, (rn, _, color) in enumerate(ring_specs):
        x = lx + i * 46
        out.append(f'<rect x="{x}" y="{cy+8}" width="4" height="4" fill="{color}" stroke="{LINE}" stroke-width="0.3"/>')
        out.append(f'<text x="{x+5.5}" y="{cy+11.6}" font-size="3.1" fill="{INK}" font-weight="600">{i+1}º {esc(rn)}</text>')
    out.append(pendulo_icon(cx, cy)); out.append(testemunho(cx, cy + 14, w=40, h=13))
    return svg_wrap("".join(out), w, h)

# ---------- Relógio ----------
def clock(ring_values, R=92, w=190, h=134):
    cx, cy = w / 2, 100
    out = []; nr = len(ring_values); thickness = (R - 16) / nr
    for ri, (rname, values, color) in enumerate(ring_values):
        r1 = R - ri * thickness; r0 = r1 - thickness
        out.append(f'<path d="{wedge(cx, cy, r0, r1, 180, 0)}" fill="{color}" stroke="{LINE}" stroke-width="0.35"/>')
        n = len(values)
        for i, v in enumerate(values):
            a = 180 - 180 * i / (n - 1)
            x0, y0 = polar(cx, cy, r1, a); x1, y1 = polar(cx, cy, r1 - 2.5, a)
            out.append(f'<line x1="{x0:.2f}" y1="{y0:.2f}" x2="{x1:.2f}" y2="{y1:.2f}" stroke="{LINE}" stroke-width="0.4"/>')
            tx, ty = polar(cx, cy, (r0 + r1) / 2 + 0.5, a)
            out.append(f'<text x="{tx:.2f}" y="{ty+1.2:.2f}" font-size="{min(3.8, thickness * 0.27):.2f}" fill="{INK}" font-weight="700" text-anchor="middle">{esc(v)}</text>')
    lx = cx - R
    for i, (rn, _, color) in enumerate(ring_values):
        col = i % 3; row = i // 3
        x = lx + col * 62; y = cy + 8 + row * 5.5
        out.append(f'<rect x="{x}" y="{y}" width="4" height="4" fill="{color}" stroke="{LINE}" stroke-width="0.3"/>')
        out.append(f'<text x="{x+5.5}" y="{y+3.4}" font-size="3.0" fill="{INK}" font-weight="600">{i+1}º {esc(rn)}</text>')
    out.append(pendulo_icon(cx, cy)); out.append(testemunho(cx, cy + 20, w=40, h=13))
    return svg_wrap("".join(out), w, h)

# ---------- Lista pendulável ----------
def list_chart(items, groups=None, cols=2, w=190, row_h=7.2, font=3.3, header_colors=None, max_h=226, max_row=9.2, max_font=4.4):
    """items: lista de str; groups: lista de (nome, count, cor) na ordem dos itens. Cada linha tem um alvo para o pêndulo."""
    entries = []
    if groups:
        acc = 0
        for gname, count, color in groups:
            entries.append(("H", gname, color))
            for it in items[acc:acc + count]:
                entries.append(("I", it, color))
            acc += count
    else:
        entries = [("I", it, None) for it in items]
    per_col = math.ceil(len(entries) / cols)
    col_w = (w - 10) / cols
    chunks = []; rest = list(entries)
    for ci in range(cols):
        take = per_col if ci < cols - 1 else len(rest)
        chunk = rest[:take]
        if ci < cols - 1 and len(chunk) > 3:
            for back in (1, 2, 3):
                if chunk[-back][0] == "H":
                    chunk = chunk[:-back]; break
        chunks.append(chunk); rest = rest[len(chunk):]
    if rest: chunks[-1].extend(rest)
    rows = max(len(c) for c in chunks)
    row_h = min(max_row, (max_h - 10) / rows)
    maxlen = max(len(t) for _, t, _ in entries)
    font = min(max_font, row_h * 0.5, (col_w - 19) / (maxlen * 0.52))
    h = rows * row_h + 10
    out = []
    num = 0
    for ci in range(cols):
        chunk = chunks[ci]
        x = 5 + ci * col_w
        for ri, (kind, text, color) in enumerate(chunk):
            y = 5 + ri * row_h
            if kind == "H":
                out.append(f'<rect x="{x}" y="{y}" width="{col_w-3}" height="{row_h-0.8}" rx="1" fill="{color}" stroke="none"/>')
                out.append(f'<text x="{x+3}" y="{y+row_h*0.68}" font-size="{font}" fill="{INK}" font-weight="700">{esc(text)}</text>')
            else:
                num += 1
                fill = color if color else "#f6f6f6"
                out.append(f'<rect x="{x}" y="{y}" width="{col_w-3}" height="{row_h-0.8}" rx="1" fill="{fill}" fill-opacity="{0.35 if color else 1}" stroke="{GRID}" stroke-width="0.25"/>')
                out.append(f'<circle cx="{x+5}" cy="{y+row_h/2-0.4}" r="2.1" fill="white" stroke="{ACCENT}" stroke-width="0.5"/>')
                out.append(f'<circle cx="{x+5}" cy="{y+row_h/2-0.4}" r="0.6" fill="{ACCENT}"/>')
                out.append(f'<text x="{x+9.5}" y="{y+row_h*0.66}" font-size="{font}" fill="{INK}" font-weight="700">{num}</text>')
                out.append(f'<text x="{x+16}" y="{y+row_h*0.66}" font-size="{font}" fill="{INK}">{esc(text)}</text>')
    return svg_wrap("".join(out), w, h)

# ---------- Ícones de movimento (G7) ----------
def ic_circle(x, y):
    return f'<circle cx="{x}" cy="{y}" r="3.4" fill="none" stroke="{ACCENT}" stroke-width="0.7"/><path d="M{x+4} {y-0.8} l-1.5 -1.6 l-0.8 2.2 z" fill="{ACCENT}"/>'
def ic_ellipse(angle):
    return lambda x, y: f'<ellipse cx="{x}" cy="{y}" rx="4.2" ry="2" fill="none" stroke="{ACCENT}" stroke-width="0.7" transform="rotate({angle} {x} {y})"/>'
def ic_line(angle):
    return lambda x, y: f'<line x1="{x-4.2}" y1="{y}" x2="{x+4.2}" y2="{y}" stroke="{ACCENT}" stroke-width="0.9" transform="rotate({angle} {x} {y})"/>'
def ic_erratic(x, y):
    return f'<path d="M{x-4.5} {y+2} l1.8 -4 l1.8 5 l1.8 -6 l1.8 4 l1.8 -3" fill="none" stroke="{ACCENT}" stroke-width="0.7"/>'
def ic_dot(x, y):
    return f'<circle cx="{x}" cy="{y}" r="1.3" fill="{ACCENT}"/>'
def ic_ccw(x, y):
    return f'<circle cx="{x}" cy="{y}" r="3.4" fill="none" stroke="#c62828" stroke-width="0.7"/><path d="M{x-3.4} {y-0.8} l1.5 -1.6 l0.8 2.2 z" fill="#c62828"/>'
def ic_cw(x, y):
    return f'<circle cx="{x}" cy="{y}" r="3.4" fill="none" stroke="#2e7d32" stroke-width="0.7"/><path d="M{x+3.4} {y-0.8} l-1.5 -1.6 l-0.8 2.2 z" fill="#2e7d32"/>'

# ---------- Silhueta (figura de 300 unidades de altura; escala em mm por unidade) ----------
_LEFT = [(-7, 41), (-8, 50), (-14, 54), (-26, 58), (-36, 66), (-42, 80), (-46, 110), (-47, 135), (-44, 152), (-38, 156), (-33, 150), (-31, 135), (-30, 110), (-29, 86), (-27, 76), (-26, 95), (-24, 118), (-27, 140), (-30, 160), (-29, 185), (-27, 215), (-25, 245), (-24, 275), (-25, 292), (-27, 300), (-8, 300), (-7, 285), (-5, 255), (-4, 225), (-3, 195), (-1, 175), (0, 168)]

def figure(cx, top, k=0.75, fill="#f4f4f4"):
    """Desenha a figura humana (frente ou costas, mesma forma). Retorna (svg, função de conversão (ux, uy) -> (x, y))."""
    def P(ux, uy): return cx + ux * k, top + uy * k
    pts = _LEFT + [(-x, y) for x, y in reversed(_LEFT[:-1])]
    d = "M" + " L".join(f"{P(x, y)[0]:.2f} {P(x, y)[1]:.2f}" for x, y in pts) + " Z"
    hx, hy = P(0, 22)
    svg = (f'<circle cx="{hx:.2f}" cy="{hy:.2f}" r="{19*k:.2f}" fill="{fill}" stroke="{LINE}" stroke-width="0.55"/>'
           f'<path d="{d}" fill="{fill}" stroke="{LINE}" stroke-width="0.55" stroke-linejoin="round"/>')
    return svg, P

CHAKRA_U = {7: 2, 6: 18, 5: 46, 4: 90, 3: 120, 2: 145, 1: 168}

def mini_ruler(x, y, width=40, tint="#eee"):
    out = [f'<rect x="{x}" y="{y-2.6:.2f}" width="{width}" height="2.6" fill="{tint}"/>',
           f'<line x1="{x}" y1="{y:.2f}" x2="{x+width}" y2="{y:.2f}" stroke="{LINE}" stroke-width="0.45"/>']
    for t in range(0, 11):
        xx = x + width * t / 10; ln = 2.6 if t % 5 == 0 else 1.4
        out.append(f'<line x1="{xx:.2f}" y1="{y-ln:.2f}" x2="{xx:.2f}" y2="{y:.2f}" stroke="{LINE}" stroke-width="0.35"/>')
    for t, lab in ((0, "0"), (5, "50"), (10, "100")):
        out.append(f'<text x="{x + width*t/10:.2f}" y="{y+4:.2f}" font-size="2.9" fill="{QUIET}" text-anchor="middle">{lab}</text>')
    return "".join(out)

def silhouette_chakras(w=190, h=240, back=False):
    out = []; k = 0.74; top = 8
    cx = 66
    body, P = figure(cx, top, k); out.append(body)
    ks = range(2, 7) if back else range(1, 8)
    for kk in ks:
        x, y = P(0, CHAKRA_U[kk])
        dash = ' stroke-dasharray="1.6 1.1"' if back else ""
        out.append(f'<circle cx="{x:.2f}" cy="{y:.2f}" r="4.2" fill="{CHAKRA_TINT[kk]}" stroke="{CHAKRA_COLORS[kk]}" stroke-width="1.1"{dash}/>')
        out.append(f'<text x="{x:.2f}" y="{y+1.4:.2f}" font-size="3.8" fill="{INK}" text-anchor="middle" font-weight="700">{kk}{"B" if back else ""}</text>')
        name = CHAKRA_NAMES[kk] + (" B" if back else "")
        out.append(f'<text x="{cx-42:.2f}" y="{y+1.4:.2f}" font-size="4.4" fill="{CHAKRA_COLORS[kk]}" font-weight="700" text-anchor="end">{esc(name)}</text>')
        out.append(f'<line x1="{cx-40:.2f}" y1="{y:.2f}" x2="{x-5:.2f}" y2="{y:.2f}" stroke="{GRID}" stroke-width="0.3"/>')
        out.append(f'<line x1="{x+5:.2f}" y1="{y:.2f}" x2="{cx+58:.2f}" y2="{y:.2f}" stroke="{GRID}" stroke-width="0.3"/>')
        out.append(mini_ruler(cx + 60, y, 44, CHAKRA_TINT[kk]))
        out.append(f'<text x="{cx+106:.2f}" y="{y+1.2:.2f}" font-size="2.8" fill="{QUIET}">%</text>')
    return svg_wrap("".join(out), w, h - 6)

def silhouette_points(points, w=190, h=240, title=None, font=4.3, k=0.74):
    """points: (nome, ux, uy, lado) em unidades da figura."""
    out = []; top = 10; cx = 95
    body, P = figure(cx, top, k); out.append(body)
    slots = {"R": 10, "L": 10}
    for name, ux, uy, side in sorted(points, key=lambda p: (p[3], p[2])):
        px, py = P(ux, uy)
        out.append(f'<circle cx="{px:.2f}" cy="{py:.2f}" r="2.4" fill="{ACCENT}" stroke="white" stroke-width="0.5"/>')
        ly = max(slots[side], py - 2); slots[side] = ly + 8.5
        lx = cx + 48 if side == "R" else cx - 48
        anchor = "start" if side == "R" else "end"
        tx = lx + 7 if side == "R" else lx - 7
        out.append(f'<line x1="{px:.2f}" y1="{py:.2f}" x2="{lx + (-2 if side=="R" else 2):.2f}" y2="{ly-1.2:.2f}" stroke="{GRID}" stroke-width="0.35"/>')
        out.append(f'<circle cx="{lx:.2f}" cy="{ly-1.2:.2f}" r="2.3" fill="white" stroke="{ACCENT}" stroke-width="0.55"/>')
        out.append(f'<text x="{tx:.2f}" y="{ly:.2f}" font-size="{font}" fill="{INK}" text-anchor="{anchor}">{esc(name)}</text>')
    return svg_wrap("".join(out), w, h - 6)

# ================= LISTAS =================
CAUSAS = ["Emocional", "Mental e\npsicológica", "Física e\nde saúde", "Energética\n(interferência)", "Ambiental", "Transgeracional\ne ancestral", "Espiritual e\nexistencial", "Outro"]
FAMILIAS = ["Não sou bom o\nbastante, não mereço", "Não estou seguro,\no mundo é perigoso", "Não tenho controle,\nsou impotente", "Não posso confiar", "Não pertenço,\nestou só", "Não posso me\nexpressar", "Preciso ser perfeito\nou agradar", "É minha culpa,\ndevo pagar", "Outra"]
FERIDAS = ["Rejeição\n(fugitivo)", "Abandono\n(dependente)", "Humilhação\n(masoquista)", "Traição\n(controlador)", "Injustiça\n(rígido)"]
SISTEMAS = ["Auditivo", "Cardíaco", "Circulatório", "Digestivo", "Endócrino", "Esquelético", "Imunológico", "Linfático", "Muscular", "Nervoso\ncentral", "Nervoso\nperiférico", "Psicológico", "Reprodutor\nfeminino", "Reprodutor\nmasculino", "Respiratório", "Urinário", "Visual", "Outro"]
TIPOS = ["Patógeno", "Toxina", "Nutrição e\nhábitos", "Estrutura", "Circuito", "Outro"]
INTERF = ["Miasma", "Egrégora\nnegativa", "Larva astral", "Forma-\npensamento", "Cordão ou\nvínculo", "Implante", "Programa\n(medo, controle)", "Portal aberto", "Entidade ou\nobsessor", "Energia densa\nde lugar/objeto", "Inveja,\n\"olho gordo\"", "Magia ou\ntrabalho", "Outro"]
FONTES_AMB = ["Linha Hartmann", "Cruzamento\nHartmann", "Linha Curry", "Cruzamento\nCurry", "Zona Benker", "Veio d'água", "Falha\n(seca, úmida)", "Rede elétrica", "Wi-Fi e\nroteador", "Celular", "Torre ou\ntransformador", "Histórico\ndo imóvel", "Vizinhança", "Objeto\nherdado", "Presente", "Objeto antigo", "Planta ou\nanimal", "Outro"]
FONTES_GRUPOS = [("GEOPATIA", 7, "#e0f2f1"), ("ELETROMAGNÉTICA", 4, "#fff3cc"), ("LUGAR", 2, "#dcecfb"), ("OBJETO", 4, "#fdebd3"), ("", 1, "#f1f1f1")]
TEMAS_ESP = ["Propósito", "Fé e confiança\nna vida", "Conexão", "Perdão", "Sentido", "Pertencimento", "Entrega", "Outro"]
ORIGENS = ["Própria", "Absorvida", "Compartilhada", "Herdada", "Pré-natal", "Pré-concepção", "Coletiva"]
EPOCAS = ["Pré-\nconcepção", "Gestação", "Nascimento", "0 a 7", "7 a 14", "14 a 21", "21 a 30", "30 a 40", "40 a 50", "50 a 60", "60 a 70", "70 a 80", "80 a 90"]
CONTEXTOS = ["Família", "Parceiro", "Trabalho", "Saúde", "Morte", "Dinheiro", "Lugar", "Corpo", "Outro"]
TECNICAS = ["Comando de\nneutralização", "Liberação pelo\nVaso Governador", "Pêndulo\nHebraico", "Gráfico\nradiônico", "Cromoterapia", "Cristal", "Floral", "Afirmação", "Som e\nfrequência", "Aromaterapia", "Reiki ou\nimposição", "Prática\ncorporal", "Outra"]
COMODOS = ["Quarto:\ncabeceira", "Quarto:\npés da cama", "Quarto:\nlado da cama", "Posto de\ntrabalho", "Sala", "Cozinha", "Entrada", "Outro"]
REMED = ["Mudar de lugar", "Neutralizar\n(comando, gráfico)", "Dispositivo\n(placa, pirâmide)", "Medir radônio\ne campos", "Outro"]
CONFLITO = ["\"Bocado\"\n(endoderma)", "Ataque ou ninho\n(mesoderma antigo)", "Desvalorização\n(mesoderma novo)", "Separação, território,\nidentidade (ectoderma)"]
ORIG_INTERF = ["Própria", "Externa:\npessoa", "Externa:\nlugar", "Externa:\nobjeto", "Herdada"]
FORMAS = ["Círculo\nhorário", "Círculo\nanti-horário", "Elipse\nà direita", "Elipse\nà esquerda", "Vertical", "Horizontal", "Errático", "Parado"]
RESPOSTAS = ["Não posso ou\nnão devo responder", "Não", "Neutro, nenhuma\ndas anteriores", "Sim", "Pronto para\na pergunta"]
CHAKRAS7 = [f"{k} {CH[k]}\n({SANS[k]})" for k in range(1, 8)]
ESTADO = ["Saúde normal", "Enfermo", "Muito enfermo", "Grave", "Agonizante", "Crítico", "Estado terminal", "Processo de\nmorte"]
AGENTES = ["Agentes\nbiológicos", "Agentes\nquímicos", "Alimentação", "Energia de forma:\nobjetos", "Energia de forma:\nparanormalidade", "Formas-\npensamento", "Fator genético", "Geopatogenia", "Local de dormir", "Higienização", "Magia negra", "Miasmas", "Obsessores", "Ondas eletro-\nmagnéticas", "Psiquismo", "Rede elétrica", "Toxemia", "Vida sexual"]
CAUSAS_FIS = ["Alimentação\ndeficiente", "Alimentação\nabusiva", "Cansaço físico", "Doenças\nhereditárias", "Doenças\ngenéticas", "Distúrbios\nhormonais", "Sedentarismo", "Excesso de\nexercício", "Sono de má\nqualidade", "Sobrecarga de\nestudos", "Sobrecarga de\ntrabalho", "Sobrecarga de\nvida social", "TPM", "Envelhecimento", "Outra"]
CAUSAS_ESP = ["Obsessão\nespiritual", "Missão\nespiritual", "Vampirismo de\nencarnado", "Vampirismo de\ndesencarnado", "Autoobsessão", "Desequilíbrio\nespiritual", "Falta de fé,\ndesconexão", "Falta de\nproteção", "Atividades\ndurante o sono", "Automagia", "Ataque\nespiritual", "Mau olhado", "Miasmas,\nlarvas astrais", "Negativismo", "Resgate de\nvidas passadas", "Rombo na aura", "Mediunidade\ncontida", "Mediunidade\nnegada", "Outra"]
FASES = ["Gestação", "Parto", "0 a 7", "7 a 14", "14 a 21", "21 a 28", "28 a 35", "35 a 42", "42 a 49", "49 a 56", "56 a 63", "63 a 70", "70 a 77", "77 a 84", "Acima de 84", "Outras\nencarnações"]
PESSOAS = ["Pai", "Mãe", "Irmão, irmã", "Avô, avó", "Tio, tia", "Primo, prima", "Vizinho,\nvizinha", "Amigo", "Amiga", "Namorado,\nnamorada", "Noivo, noiva", "Marido,\nesposa", "Ex-parceiro", "Filho, filha", "Neto, neta", "Patrão,\npatroa", "Colega de\ntrabalho", "Pessoa\ndesconhecida"]
GLANDULAS = ["Suprarrenais", "Hipófise", "Pineal", "Hipotálamo", "Tireoide", "Paratireoide", "Pâncreas", "Timo", "Ovários", "Testículos", "Próstata", "Outra"]
CORES = [("Vermelho", "#e53935"), ("Laranja", "#fb8c00"), ("Amarelo", "#fdd835"), ("Verde", "#43a047"), ("Azul", "#1e88e5"), ("Índigo", "#3949ab"), ("Violeta", "#8e24aa"), ("Branco", "#ffffff"), ("Rosa", "#f48fb1"), ("Magenta", "#d81b60"), ("Turquesa", "#26a69a"), ("Dourado", "#d4a017")]
SOLFEGGIO = ["174 Hz\nalívio da dor", "285 Hz\nregeneração", "396 Hz\nbásico, medo", "417 Hz\nsacral, mudança", "528 Hz\nplexo, transformação", "639 Hz\ncardíaco, relações", "741 Hz\nlaríngeo, expressão", "852 Hz\nfrontal, intuição", "963 Hz\ncoronário, conexão"]
ETIQUETAS = ["Limpeza\n(limpiar impurezas)", "Proteção", "Mem Hei Shin\n(cura)", "Refuah\n(cura)", "Shalom\n(paz)", "Ahava\n(amor)", "Chaim\n(vida)", "Emet\n(verdade)", "Parnassah\n(abundância)", "Tlishut\n(desapego)", "Lajatz\n(estresse)", "Tav\n(selamento)", "Keter, Luz, Amor\n(fechamento)", "Outra"]
GRAF_CATS = ["Saúde", "Materialização", "Proteção", "Conexão divina", "Relacionamento", "Potencialização", "Limpeza", "Outro"]
GRAF_LISTA = [("SAÚDE", ["Triturador", "Diafragma horário", "Antidepressão", "Relax do sono", "Triturador com Turbilhão", "Programador celular", "Antidor", "Diafragma anti-horário", "Escudo protetor", "Estrela de 5 pontas", "Alta Vitalidade", "Magnetismo Vital e Curativo"], "#e3f4e1"),
              ("MATERIALIZAÇÃO", ["Turbilhão", "Turbilhão com Júpiter", "Prosperador", "Turbilhão com Prosperador", "Quadrata", "Saúde financeira", "Cruz Atlante", "Trígono protetor"], "#fff6cc"),
              ("PROTEÇÃO", ["Nove Círculos", "Luxor", "Cruz Cósmica", "Yoshua", "SCAP", "Antimagia", "Labirinto d'Amiens", "YHWH 3 círculos", "YHWH 7 círculos", "Escudo mágico", "Psicoprotetor", "Tetragrammaton"], "#dcecfb"),
              ("CONEXÃO DIVINA", ["Triângulo", "Estrela de 6 pontas", "Vesica Piscis", "Chama Trina", "Antahkarana", "Cubo de Metatron"], "#e6e0f5"),
              ("RELACIONAMENTO", ["Desembaraçador de relacionamento afetivo", "Turbilhão com Vênus", "Harmonia", "Harmonia familiar", "Turbilhão com Mercúrio", "Autoestima", "Amor Universal"], "#fbe3e3"),
              ("POTENCIALIZAÇÃO", ["Magnetron", "Baguá", "Espiral", "Shin", "Decágono duplo", "Captador de energia solar", "Pirâmide de Quéops"], "#fdebd3"),
              ("LIMPEZA", ["Código 21", "Desimpregnador", "Flor da Vida", "Desembaraçador material", "Tri-círculo", "Corte energético", "Limpeza e Recarga", "Espiral anti-horária"], "#e0f2f1")]
FLORAIS = [("MEDO", ["Rock Rose (pânico, terror)", "Mimulus (medos conhecidos)", "Cherry Plum (medo de perder o controle)", "Aspen (medos vagos)", "Red Chestnut (medo pelos outros)"], "#fbe3e3"),
           ("INCERTEZA", ["Cerato (dúvida de si)", "Scleranthus (indecisão)", "Gentian (desânimo após revés)", "Gorse (desesperança)", "Hornbeam (cansaço de começar)", "Wild Oat (rumo da vida)"], "#fff6cc"),
           ("DESINTERESSE PELO PRESENTE", ["Clematis (sonhador)", "Honeysuckle (vive no passado)", "Wild Rose (apatia)", "Olive (exaustão)", "White Chestnut (pensamentos repetitivos)", "Mustard (tristeza sem causa)", "Chestnut Bud (não aprende com erros)"], "#e3f4e1"),
           ("SOLIDÃO", ["Water Violet (reserva, orgulho)", "Impatiens (impaciência)", "Heather (egocentrismo)"], "#dcecfb"),
           ("HIPERSENSIBILIDADE", ["Agrimony (máscara de alegria)", "Centaury (não diz não)", "Walnut (proteção em mudanças)", "Holly (ódio, ciúme, inveja)"], "#e6e0f5"),
           ("DESÂNIMO E DESESPERO", ["Larch (falta de confiança)", "Pine (culpa)", "Elm (sobrecarga)", "Sweet Chestnut (angústia extrema)", "Star of Bethlehem (choque, trauma)", "Willow (ressentimento)", "Oak (luta além do limite)", "Crab Apple (autoaversão, limpeza)"], "#fdebd3"),
           ("PREOCUPAÇÃO COM OS OUTROS", ["Chicory (amor possessivo)", "Vervain (entusiasmo excessivo)", "Vine (dominação)", "Beech (intolerância)", "Rock Water (rigidez consigo)"], "#e0f2f1"),
           ("EMERGÊNCIA", ["Rescue (5 florais de emergência)"], "#f1f1f1")]
CRISTAIS = [(f"{k} {CH[k].upper()}", lst, CHAKRA_TINT[k]) for k, lst in {
    1: ["Jaspe vermelho", "Hematita", "Turmalina negra", "Ônix", "Granada", "Quartzo fumê", "Obsidiana", "Rubi"],
    2: ["Cornalina", "Calcita laranja", "Pedra do sol", "Jaspe", "Ágata de fogo", "Coral", "Pedra da lua"],
    3: ["Citrino", "Olho de tigre", "Pirita", "Âmbar", "Topázio imperial", "Calcita amarela"],
    4: ["Quartzo rosa", "Quartzo verde", "Aventurina", "Esmeralda", "Kunzita", "Rodonite", "Jade"],
    5: ["Turquesa", "Água-marinha", "Sodalita", "Celestita", "Larimar", "Quartzo azul", "Calcedônia azul"],
    6: ["Ametista", "Lápis-lazúli", "Fluorita", "Azurita", "Cianita", "Sodalita"],
    7: ["Quartzo transparente", "Selenita", "Pedra da lua", "Ametista", "Diamante", "Fluorita"]}.items()]
OLEOS = [(f"{k} {CH[k].upper()}", lst, CHAKRA_TINT[k]) for k, lst in {
    1: ["Patchouli", "Vetiver", "Cedro", "Mirra"], 2: ["Ylang-ylang", "Laranja doce", "Jasmim", "Sândalo"], 3: ["Limão", "Gengibre", "Alecrim", "Capim-limão"],
    4: ["Rosa", "Gerânio", "Bergamota", "Lavanda"], 5: ["Camomila azul", "Eucalipto", "Hortelã", "Tea tree"], 6: ["Lavanda", "Olíbano", "Sálvia esclareia", "Manjericão"], 7: ["Olíbano", "Mirra", "Lótus", "Sândalo"]}.items()]
EMO60 = [("1 CORAÇÃO OU INTESTINO DELGADO", ["Abandono", "Traição", "Desamparo", "Perda", "Amor não recebido", "Esforço não reconhecido", "Desgosto", "Insegurança", "Alegria excessiva", "Vulnerabilidade"], "#fbe3e3"),
         ("2 BAÇO OU ESTÔMAGO", ["Ansiedade", "Desespero", "Repulsa", "Nervosismo", "Preocupação", "Fracasso", "Impotência", "Desesperança", "Falta de controle", "Baixa autoestima"], "#fff6cc"),
         ("3 PULMÃO OU CÓLON", ["Choro", "Desânimo", "Rejeição", "Tristeza", "Pesar", "Confusão", "Atitude defensiva", "Luto", "Autoagressão", "Teimosia"], "#f0efe6"),
         ("4 FÍGADO OU VESÍCULA", ["Raiva", "Amargura", "Culpa", "Ódio", "Ressentimento", "Depressão", "Frustração", "Indecisão", "Pânico", "Sentir-se usado"], "#e3f4e1"),
         ("5 RINS OU BEXIGA", ["Culpar", "Pavor", "Medo", "Horror", "Irritação", "Conflito", "Insegurança criativa", "Terror", "Falta de apoio", "Vacilação"], "#dcecfb"),
         ("6 GLÂNDULAS E ÓRGÃOS SEXUAIS", ["Humilhação", "Ciúme", "Anseio", "Luxúria", "Sobrecarga", "Orgulho", "Vergonha", "Choque", "Indignidade", "Sentir-se sem valor"], "#fdebd3")]
PSICO = ["Agressividade", "Angústia", "Apatia", "Ansiedade", "Baixa autoestima", "Autoobsessão", "Autopiedade", "Cansaço mental", "Ceticismo", "Ciúmes", "Criticismo", "Culpas", "Decepções", "Depressão", "Desapontamento", "Descrença", "Dominação", "Egoísmo", "Extroversão", "Fixação", "Frustração", "Histeria", "Hostilidades", "Infelicidade", "Insegurança", "Intolerância", "Introversão", "Inveja", "Irritabilidade, mau humor", "Medos", "Melancolia, nostalgia", "Ódio", "Orgulho, preconceitos", "Passividade", "Preguiça física", "Preguiça mental", "Preocupação", "Presunção", "Rancor", "Solidão", "Tendência a suicídio", "Traição", "Timidez", "Tristeza", "Traumas", "TDAH", "TOC", "Burnout", "Síndrome do pânico", "Vítima de abuso ou assédio sexual", "Vítima de violência doméstica ou urbana", "Conflito de gênero ou sexualidade", "Conflito com família ou filhos", "Conflito de relacionamento", "Maternidade ou paternidade", "Mudança de cidade", "Mudança de emprego", "Desemprego", "Dívidas elevadas", "Doença terminal na família", "Luto"]
ORGAOS = ["Baço", "Bexiga", "Cérebro", "Cólon", "Coração", "Costelas", "Dentes", "Duodeno", "Coluna vertebral", "Esôfago", "Faringe", "Fígado", "Glândulas mamárias", "Glândulas salivares", "Intestino delgado", "Intestino grosso", "Laringe", "Língua", "Meninges", "Nariz", "Olhos", "Ouvidos", "Ovários", "Pâncreas", "Paratireoide", "Pele", "Trompas", "Útero", "Vértebras", "Vesícula biliar", "Próstata", "Testículos", "Pulmões", "Rins", "Tireoide", "Memória"]

EMO_CHAKRA = {
    1: ["Medo", "Pavor", "Terror", "Horror", "Culpar", "Irritação", "Conflito", "Insegurança\ncriativa", "Falta de apoio", "Vacilação", "Rejeição", "Tristeza", "Desânimo", "Choro", "Pesar", "Outra (G9)"],
    2: ["Vergonha", "Humilhação", "Culpa", "Ciúme", "Anseio", "Luxúria", "Sobrecarga", "Orgulho", "Choque", "Indignidade", "Sentir-se\nsem valor", "Outra (G9)"],
    3: ["Ansiedade", "Nervosismo", "Preocupação", "Desespero", "Repulsa", "Fracasso", "Impotência", "Desesperança", "Falta de\ncontrole", "Baixa\nautoestima", "Raiva", "Amargura", "Ódio", "Ressentimento", "Frustração", "Indecisão", "Outra (G9)"],
    4: ["Abandono", "Traição", "Desamparo", "Perda", "Amor não\nrecebido", "Esforço não\nreconhecido", "Desgosto", "Insegurança", "Alegria\nexcessiva", "Vulnerabilidade", "Luto", "Tristeza", "Pesar", "Outra (G9)"],
    5: ["Confusão", "Atitude\ndefensiva", "Teimosia", "Raiva\nengolida", "Amargura", "Ressentimento", "Frustração", "Indecisão", "Humilhação", "Vergonha", "Outra (G9)"],
    6: ["Desespero", "Preocupação", "Nervosismo", "Confusão", "Pavor", "Horror", "Terror", "Indecisão", "Ilusão\n(autoengano)", "Outra (G9)"],
    7: ["Luto", "Desânimo", "Tristeza", "Pesar", "Indignidade", "Sentir-se\nsem valor", "Orgulho", "Abandono", "Perda", "Apego", "Outra (G9)"],
}
CORPO_CHAKRA = {
    1: ["Ossos", "Pernas e pés", "Base da coluna,\nciático", "Reto", "Cólon", "Sangue", "Imunidade", "Suprarrenais", "Outro (G12)"],
    2: ["Órgãos sexuais", "Útero ou\npróstata", "Bexiga", "Rins", "Intestino\ngrosso", "Lombar", "Pelve e\nquadris", "Apêndice", "Outro (G12)"],
    3: ["Estômago", "Fígado", "Vesícula", "Pâncreas", "Intestino\ndelgado", "Adrenais", "Baço", "Coluna média,\ndiafragma", "Outro (G12)"],
    4: ["Coração", "Circulação", "Pulmões", "Timo", "Mamas", "Braços e\nmãos", "Ombros e\nescápulas", "Costelas", "Outro (G12)"],
    5: ["Garganta", "Tireoide e\nparatireoides", "Boca, dentes\ne gengivas", "Pescoço e\ncervical", "Ouvidos", "Esôfago e\ntraqueia", "Mandíbula", "Outro (G12)"],
    6: ["Olhos", "Cérebro", "Sistema\nnervoso", "Hipófise", "Pineal", "Nariz e seios\nda face", "Ouvidos", "Outro (G12)"],
    7: ["Pele", "Músculos", "Esqueleto", "Córtex\ncerebral", "Sistema nervoso\ncentral", "Sono e\nvigília", "Outro (G12)"],
}


# ---- Listas de referência: CHAKRA.pdf (desequilíbrios por chakra), roda SOLAR, Mesa Mannah ----
SINAIS_CHAKRA = {
    7: ["Desconexão espiritual", "Sensação de confinamento", "Apego excessivo à matéria", "Preocupação intensa", "Mediunidade descontrolada", "Busca incessante de gurus", "Falta de fé", "Dores de cabeça ou enxaqueca", "Confusão mental", "Desordens do sono", "Problemas nervosos", "Psicoses", "Transtorno bipolar", "Depressão profunda", "Neuroses", "Dificuldade de memorização e foco"],
    6: ["Medo", "Pânico", "Bloqueio", "Traumas", "Carências", "Rejeição", "Confusão mental", "Falta de criatividade", "Falta de clareza", "Falta de discernimento", "Esquecimento", "Perda da razão", "Autocrítica", "Culpa", "Falta de merecimento", "Mentiras", "Falta de concentração", "Doenças físicas", "Doenças mentais", "Ataques espirituais", "Chips", "Implantes", "Artefatos de magia", "Falta de disciplina", "Problemas de caráter", "Irresponsabilidade", "Julgamento"],
    5: ["Gula", "Inapetência", "Traumas", "Medos", "Doenças", "Falta de expressão", "Mentiras", "Mudez", "Solilóquios", "Alcoolismo", "Drogadição", "Tabagismo", "Bloqueios", "Timidez", "Orgulho", "Irritação", "Soberba", "Agressividade", "Reatividade", "Gagueira", "Retardo na fala", "Palavrões", "Xingamentos", "Desequilíbrios", "Infantilidade vocal", "Frustração", "Mau uso da palavra", "Magias", "Maldições", "Pragas", "Chips", "Implantes"],
    4: ["Depressão ou angústia", "Esgotamento", "Crises de choro", "Crise de identidade", "Peito apertado", "Melancolia", "Incapacidade de amar", "Insônia", "Problemas pulmonares", "Não aceitar ajuda", "Dificuldade de chorar", "Desprezo", "Raiva", "Medo de se relacionar", "Dificuldade de respirar"],
    3: ["Necessidade de controle", "Dificuldade de confiar", "Irritação e autoritarismo", "Ansiedade e egoísmo", "Preconceito e intransigência", "Timidez", "Abuso de poder", "Arrogância", "Baixa autoestima", "Desconfiança", "Dificuldade em dizer não", "Impaciência", "Tirania e agressividade", "Perfeccionismo", "Dependência e vulnerabilidade", "Sensibilidade extrema"],
    2: ["Medo", "Distração", "Tristeza", "Apego", "Dependência emocional", "Vícios e autodestruição", "Alergias alimentares", "Problemas nos rins ou fígado", "Dores lombares e cóccix", "Problemas na bexiga ou vesícula", "Inveja", "Falta de paixão", "Confusão", "Ciúmes", "Problemas sexuais"],
    1: ["Conflitos internos", "Avareza", "Impulsividade", "Ódio ou raiva", "Medo", "Dificuldade financeira", "Insegurança", "Ineficiência", "Falta de libido", "Coluna ou quadril", "Pensamentos acelerados", "Dívidas financeiras", "Falta de vitalidade", "Ansiedade excessiva", "Excesso de energia", "Sono difícil", "Disfunção erétil", "Violência e agressividade", "Falta de objetividade", "Depressão", "Fadiga", "Outros"],
}
SOLAR_PSICO = ["Choque,\nnotícia ruim", "Preocupações", "Stress", "Negativismo", "Insegurança", "Timidez", "Ansiedade", "Depressão", "Angústia", "Pânico", "Burnout", "Anorexia\nou bulimia", "TDAH", "TOC", "Pensamentos\nsuicidas", "Traumas de\ninfância", "Traumas\nvida adulta", "Luto", "Doença\nterminal", "Desespero", "Solidão", "Dívidas", "Desemprego", "Aposentadoria", "Mudança de\nemprego", "Mudança\nde cidade", "Divórcio", "Casamento", "Vítima de\nassédio sexual", "Vítima de\nabuso sexual", "Vítima de viol.\ndoméstica", "Vítima de viol.\nurbana", "Vítima de\nassédio moral", "Vítima de\npreconceito", "Conflito de\nsexualidade", "Conflito\ncom filhos", "Conflitos\nfamiliares", "Conflitos de\nrelacionamento", "Fim de\nrelacionamento", "Novo\nrelacionamento", "Maternidade ou\npaternidade", "Síndrome do\nninho vazio"]
SOLAR_ESP = ["Desconexão com\no Eu superior", "Falta de\noração", "Conduta\nerrada", "Mau uso\nda palavra", "Pessoa\ninfluenciável", "Autoobsessão", "Obsessão", "Inveja", "Mau olhado", "Encantamento", "\"Trabalho\"", "Vampirismo de\nencarnado", "Vampirismo de\ndesencarnado", "Ataque\nespiritual", "Missão\nespiritual", "Prova\nespiritual", "Resgate de\nvidas passadas", "Miasmas", "Rombo\nna aura", "Mediunidade\nforçada", "Mediunidade\ncontida", "Atividade durante\ndesdobramento", "Negativismo", "Ateísmo", "Materialismo", "Promiscuidade"]
SOLAR_FIS = ["Deficiências\nalimentação", "Abusos\nalimentação", "Falta de\nexercício", "Excesso de\nexercício", "Falta de\ndescanso", "Sono de má\nqualidade", "Pouco sono", "Sono\nexcessivo", "TPM", "Distúrbios\nhormonais", "Adoecimento", "Envelhecimento", "Pouco lazer", "Sobrecarga\ntrabalho", "Sobrecarga\nestudos", "Sobrecarga\nvida social"]
MANNAH_ORIGEM = ["Espiritual", "Seres\nnegativos", "Autoobsessão", "Psico-\nemocional", "Ambiente", "Magia,\narquepadia", "Outras vidas", "Aprisionamento", "Criança\ninterior", "Sistêmico", "Confusão\nmental", "Realidades\nparalelas", "Outro"]
MANNAH_INFLU = ["Cordões,\nganchos", "Capacetes,\nsondas", "Chips,\nimplantes", "Portal negativo,\nfenda", "Artefatos\numbralinos", "Artefatos\nextraterrestres", "Iniciações\nnegativas", "Simbiose", "Conexões\nnegativas", "Emaranhamento", "Maldição", "Inveja,\nolho gordo", "Amarração", "Fragmento de\nalma, clone", "Outra"]
MANNAH_SERES = ["Miasmas,\nlarvas astrais", "Ovoides,\nparasitas", "Obsessores", "Seres\namorfos", "Magos negros,\ncasulos", "Draconianos,\nreptilianos", "Hologramas", "Arcontes", "Insetoides", "Demônios", "Dementadores", "Succubus,\nincubus", "Elementais\nnegativos", "Vampiros\nenergéticos", "Outro"]
MANNAH_SIST = ["Exclusão", "Dívida,\nfalência", "Lealdade", "Assassinato", "Aborto", "Abuso", "Pertencimento", "Traição", "Segredo", "Humilhação", "Injustiça", "Escravidão", "Ancestralidade\nmasculina", "Ancestralidade\nfeminina", "Outra"]
MANNAH_TRAT = ["Gráficos\nradiônicos", "Mesa holográfica\nde autocura", "Mesa holográfica\nde prosperidade", "Terapia multid.\narcturiana", "Energização\nda alma", "Registros\nakáshicos", "Apometria", "Reiki", "Florais\netéricos", "Criança\ninterior", "EFT", "Ho'oponopono", "Proteção\nespiritual", "Códigos de\nGrabovoi", "Outro"]
HAWKINS = ["Vergonha\n20", "Culpa\n30", "Apatia\n50", "Tristeza\n75", "Medo\n100", "Apego\n125", "Raiva\n150", "Orgulho\n175", "Coragem\n200", "Neutralidade\n250", "Disposição\n310", "Aceitação\n350", "Razão\n400", "Amor\n500", "Alegria\n540", "Paz\n600", "Iluminação\n700"]

def chakra_state_wheel(w=190, h=134):
    """Roda de chakras com estado: anel externo 7 chakras, anel interno 4 estados por chakra (nulo, hipo, normal, hiper)."""
    estados = ["nulo", "hipo", "normal", "hiper"]
    outer = [f"{k} {CH[k]}" for k in range(1, 8)]
    inner = [e for _ in range(7) for e in estados]
    sc_outer = [CHAKRA_TINT[k] for k in range(1, 8)]
    sc_inner = [c for k in range(1, 8) for c in (CHAKRA_TINT[k], CHAKRA_TINT2[k], CHAKRA_TINT[k], CHAKRA_TINT2[k])]
    svg = rings([("CHAKRA (anel externo)", outer, "#e6e6e6"), ("ESTADO (anel interno)", inner, "#f6f6f6")], R=86, thick=[22, 42], fonts=[3.2, 2.4], sector_colors=[sc_outer, sc_inner], h=h)
    return svg


# ---------- Desdobramentos de causas (edição 3) ----------
CRENCAS_FRASES = [
    ("NÃO SOU BOM O BASTANTE, NÃO MEREÇO", ["Não mereço ser feliz", "Não sou digno de amor", "Nunca faço o suficiente", "Os outros são melhores que eu", "Não mereço prosperar", "Sou um fracasso"], "#fde2e2"),
    ("NÃO ESTOU SEGURO, O MUNDO É PERIGOSO", ["Não é seguro ser eu mesmo", "Algo ruim vai acontecer", "Não posso relaxar", "Se eu me expuser, me machucam", "Não tenho onde me apoiar", "Preciso estar sempre alerta"], "#fdebd3"),
    ("NÃO TENHO CONTROLE, SOU IMPOTENTE", ["Nada do que faço muda as coisas", "Sou vítima das circunstâncias", "Não consigo", "Dependo dos outros para tudo", "Meu corpo me trai", "Desisto antes de tentar"], "#fff6cc"),
    ("NÃO POSSO CONFIAR", ["As pessoas sempre me decepcionam", "Não confio em mim", "A vida não me sustenta", "Quem ama, trai", "Só posso contar comigo", "Deus me abandonou"], "#e3f4e1"),
    ("NÃO PERTENÇO, ESTOU SÓ", ["Ninguém me entende", "Sou diferente, não me encaixo", "Estou sozinho no mundo", "Não faço parte da minha família", "Serei rejeitado", "Não tenho lugar"], "#dcecfb"),
    ("NÃO POSSO ME EXPRESSAR", ["Minha opinião não importa", "Se eu falar, perco o amor", "É perigoso dizer não", "Devo ficar quieto", "Não sei o que sinto", "Minhas necessidades não contam"], "#e6e0f5"),
    ("PRECISO SER PERFEITO OU AGRADAR", ["Só sou amado se agradar", "Errar é inaceitável", "Preciso cuidar de todos", "Não posso descansar", "Tenho que ser forte sempre", "Devo ser o que esperam de mim"], "#f3e1ef"),
    ("É MINHA CULPA, DEVO PAGAR", ["A culpa é minha", "Mereço sofrer", "Não mereço perdão", "Preciso me punir", "Sou responsável pela dor dos outros", "Estou aqui para pagar"], "#e0f2f1"),
]
BAROMETRO = [
    ("CONSCIENTE (presente)", [("Aceitação", "acolhido, aberto, receptivo", "Antagonismo", "atacado, na defensiva, contrariado"), ("Disposição", "pronto, motivado, cooperativo", "Raiva", "furioso, irritado, frustrado"), ("Interesse", "curioso, atento, envolvido", "Ressentimento", "magoado, amargo, injustiçado")]),
    ("SUBCONSCIENTE (passado)", [("Entusiasmo", "animado, inspirado, vivo", "Hostilidade", "agressivo, vingativo, cruel"), ("Segurança", "confiante, firme, protegido", "Medo de perder", "inseguro, ansioso, ciumento"), ("Igualdade", "justo, respeitado, par", "Culpa, luto", "envergonhado, arrependido, enlutado")]),
    ("CORPO (memória celular)", [("Sintonia", "em paz, em harmonia, presente", "Indiferença", "apático, frio, desligado"), ("Unidade", "pertencente, inteiro, unido", "Separação", "abandonado, rejeitado, só"), ("Escolha", "livre, no comando, responsável", "Sem escolha", "preso, sem saída, resignado")]),
]
FISICA_DESD = [
    ("PATÓGENO", ["Fungo ou mofo", "Bactéria", "Vírus", "Parasita", "Príon", "Patógeno energético (“carona”)"], "#fde2e2"),
    ("TOXINA", ["Metal pesado", "Químico (agrotóxico, limpeza, cosmético)", "Alimentar (aditivo, glúten, lactose)", "Medicamento", "Radiação eletromagnética", "Veneno biológico (picada, mofo)", "Dentária (amálgama, canal)", "Álcool, tabaco, drogas"], "#fdebd3"),
    ("NUTRIÇÃO E HÁBITOS", ["Desidratação", "Carência de nutriente", "Carência de proteína", "pH ácido", "Eletrólitos", "Sono insuficiente ou ruim", "Falta de exercício", "Excesso de exercício", "Alimentação abusiva", "Falta de luz solar", "Carência de uma cor", "Respiração curta"], "#fff6cc"),
    ("ESTRUTURA", ["Coluna (vértebra)", "Crânio e mandíbula (ATM)", "Pelve e quadril", "Articulação", "Músculo e fáscia", "Nervo comprimido", "Órgão deslocado", "Cicatriz interferente"], "#e3f4e1"),
    ("CIRCUITO", ["Chakra", "Meridiano", "Órgão", "Glândula", "Sistema", "Desconexão corpo e espírito", "Desconexão dos hemisférios", "Desconexão cérebro e órgão", "Campo magnético"], "#dcecfb"),
]
SUSTENTA = ["Emoção presa", "Crença", "Hábito ou\nvício", "Vínculo com\npessoa", "Lugar", "Objeto", "Voto, pacto\nou contrato", "Trauma não\nintegrado", "Karma, outra\nvida", "Nada: pode\nsair agora"]
VOTOS = [
    ("VOTOS (feitos por mim, nesta ou em outra vida)", ["Voto de pobreza", "Voto de castidade ou celibato", "Voto de silêncio", "Voto de obediência", "Voto de sofrimento ou sacrifício", "Voto de solidão", "Voto de invisibilidade", "Voto de lealdade a um morto", "Voto de vingança", "Voto de não ter sucesso", "Voto de não sentir"], "#e6e0f5"),
    ("PROMESSAS E JURAMENTOS", ["Promessa a pai ou mãe", "Promessa a um moribundo", "Juramento religioso", "Juramento de grupo ou ordem", "Promessa não cumprida"], "#dcecfb"),
    ("PACTOS E CONTRATOS", ["Pacto com entidade", "Contrato de alma vencido", "Acordo de linhagem (lealdade)", "Contrato de sofrimento (“vou pagar”)", "Acordo com pessoa viva (dependência)", "Amarração", "Maldição recebida", "Maldição lançada", "Autossabotagem assumida"], "#fde2e2"),
    ("AÇÃO SOBRE O ITEM (lista CQM)", ["Transmutar", "Diluir", "Assumir", "Pacificar", "Perdoar", "Aceitar", "Destruir", "Apagar", "Reconciliar", "Rescindir, cancelar"], "#e3f4e1"),
]
CORPOS = ["Físico", "Etérico", "Astral\n(emocional)", "Mental\ninferior", "Mental superior\n(causal)", "Búdico", "Átmico", "Borda da aura\n(rombo)", "Um chakra"]
EVENTOS = ["Perda ou\nmorte", "Separação ou\nabandono", "Violência\nou abuso", "Acidente ou\ncirurgia", "Doença (própria\nou de alguém)", "Mudança (casa,\ncidade, país)", "Humilhação\npública", "Susto ou\nchoque", "Traição", "Fracasso ou\ndemissão", "Nascimento\n(próprio, de filho)", "Segredo\ndescoberto", "Decisão\nforçada", "Conflito\nprolongado", "Guerra, catástrofe,\npandemia", "Nenhum: lento\ne cumulativo"]
GANHO = ["Atenção e\ncuidado", "Evitar\nresponsabilidade", "Evitar\nconflito", "Identidade (quem\nsou sem isso)", "Lealdade\nà família", "Punição\n(culpa)", "Medo de\nmudar", "Hábito e\nrotina", "Ambiente que\nmantém", "Nenhum\nganho"]

def barometro(w=190):
    out = []; y = 6
    for lvl, rows in BAROMETRO:
        out.append(f'<rect x="5" y="{y}" width="{w-10}" height="6.5" rx="1" fill="#eceff4"/>')
        out.append(f'<text x="8" y="{y+4.6}" font-size="3.4" fill="{INK}" font-weight="700">{esc(lvl)}</text>')
        out.append(f'<text x="{w/2 - 8}" y="{y+4.6}" font-size="3" fill="#2e7d32" font-weight="700" text-anchor="end">lado positivo</text>')
        out.append(f'<text x="{w - 8}" y="{y+4.6}" font-size="3" fill="#b71c1c" font-weight="700" text-anchor="end">lado negativo</text>')
        y += 8
        for pos, pos_w, neg, neg_w in rows:
            for side, (name, words, color, x0) in enumerate([(pos, pos_w, "#e3f4e1", 5), (neg, neg_w, "#fde2e2", w/2 + 1)]):
                bw = w/2 - 6
                out.append(f'<rect x="{x0}" y="{y}" width="{bw}" height="13" rx="1.2" fill="{color}" stroke="{GRID}" stroke-width="0.3"/>')
                out.append(f'<circle cx="{x0+6}" cy="{y+6.5}" r="2.3" fill="white" stroke="{ACCENT}" stroke-width="0.55"/><circle cx="{x0+6}" cy="{y+6.5}" r="0.7" fill="{ACCENT}"/>')
                out.append(f'<text x="{x0+11}" y="{y+5.6}" font-size="4.0" fill="{INK}" font-weight="700">{esc(name)}</text>')
                out.append(f'<text x="{x0+11}" y="{y+10.6}" font-size="3.0" fill="{QUIET}">{esc(words)}</text>')
            y += 15
        y += 4
    return svg_wrap("".join(out), w, y + 2)


# ---------- Limpeza de pessoas e de espaços (edição 3) ----------
AURA_ESTADO = [("Tamanho", ["Encolhida", "Média", "Expandida"], "#e6e0f5"),
               ("Proteção", ["Desprotegida\n(aberta)", "Parcial", "Protegida\n(fechada)"], "#dcecfb"),
               ("Integridade", ["Íntegra", "Com fugas", "Com furos", "Fissurada", "Rompida"], "#fff6cc"),
               ("Conteúdo", ["Limpa", "Impregnada", "Com intrusos"], "#fde2e2")]
REMOVER = [
    ("SERES E PRESENÇAS", ["Encosto, obsessor", "Mago negro, feiticeiro", "Consciência não atual", "Clone, holografia", "Elemental perturbado", "Espírito de morte", "Vampirismo (encarnado)"], "#fde2e2"),
    ("IMPLANTES E DISPOSITIVOS", ["Chip, antena, implante energético", "Implante metálico", "Implante astral", "Implante orgânico", "Sonda, capacete", "Holograma, programa inserido"], "#fdebd3"),
    ("RESÍDUOS E IMPREGNAÇÕES", ["Miasma", "Larva astral, magnética", "Forma-pensamento própria", "Forma-pensamento alheia", "Egrégora negativa", "Energia absorvida de pessoa", "Energia absorvida de lugar", "Energia de objeto", "Impregnação de cirurgia, anestesia", "Resíduo de droga, medicamento", "Fuga ou furo na aura"], "#fff6cc"),
    ("VÍNCULOS E PROGRAMAS", ["Cordão energético", "Amarração", "Voto, pacto, contrato", "Maldição (materna, familiar)", "Mal de olho, inveja", "Magia, ritual, “trabalho”", "Programa de medo ou controle", "Semente de energia invasora", "Peso kármico assumido"], "#e3f4e1"),
    ("CONTEÚDO PRÓPRIO", ["Emoção presa", "Crença limitante", "Trauma não integrado", "Memória celular", "Criança interior negligenciada", "Nada a remover: só energizar"], "#dcecfb"),
]
TEC_PESSOA = ["Giro anti-horário\nsobre o chakra", "Comando de\nneutralização", "Comando\n“em Luz”", "Pêndulo Hebraico\n(etiqueta)", "Gráfico\nDesimpregnador", "Gráfico SCAP", "Gráfico\nTriturador", "Gráfico Luxor", "Corte de\ncordão", "Encaminhamento\n(seres)", "Apometria,\ncasa espírita", "Defumação,\nbanho de ervas", "Cristal,\nselenita", "Outra"]
SELO = ["Giro horário\ncom luz", "Etiqueta de selo\n(Keter, Arcanjo)", "Escudo Protetor\n(gráfico)", "Antimagia", "Nove Círculos", "SCAP com\ncristal", "Comando de\nproteção", "Cristal\npessoal", "Banho de\nervas", "Oração,\nmantra"]
VERBOS = ["Embaralhar\n(scramble)", "Neutralizar", "Transformar", "Transmutar", "Encaminhar\n(à luz)", "Dissolver", "Preencher", "Selar"]
FONTES_DESD = [
    ("GEOPATIA", ["Linha Hartmann", "Nó (cruzamento) Hartmann", "Linha Curry", "Nó Curry", "Sobreposição Hartmann e Curry", "Zona Benker", "Veio d’água", "Falha seca", "Falha úmida", "Chaminé cosmotelúrica, vórtice", "Radônio (medir)"], "#e0f2f1"),
    ("ELETROMAGNÉTICA", ["Quadro ou rede elétrica", "Fiação na parede da cabeceira", "Wi-Fi, roteador", "Celular na cabeceira", "Micro-ondas, eletrodomésticos", "Torre, antena", "Transformador, alta tensão", "Cama com molas ou metal"], "#fff3cc"),
    ("MEMÓRIA E HISTÓRICO", ["Memória de parede", "Antigos moradores", "Morte no imóvel", "Doença longa", "Brigas, violência", "Ritual, “trabalho” no terreno", "Terreno carregado (cemitério, pântano)", "Terreno com histórico (hospital, delegacia, funerária, incêndio)", "Obra ou reforma recente"], "#dcecfb"),
    ("SERES E FORMAS", ["Entidade, “hóspede”", "Forma-pensamento acumulada", "Egrégora da casa ou do bairro", "Elemental perturbado", "Portal ou espelho aberto", "Energia de vizinho", "Consciência coletiva, massa"], "#e6e0f5"),
    ("OBJETOS", ["Objeto herdado", "Presente recebido", "Antiguidade, objeto de leilão", "Espelho", "Quadro, imagem, estátua", "Arma", "Couro, osso, plumas, flores secas", "Bonecos, pelúcia, travesseiros antigos", "Amuletos, “santinhos”, objetos de ritual", "Joias e roupas antigas", "Planta doente", "Objeto de ex-morador", "Desordem, lixo acumulado"], "#fdebd3"),
]
COMODOS_LISTA = ["Casa inteira", "Entrada, porta principal", "Sala de estar", "Sala de jantar", "Cozinha", "Área de serviço", "Banheiro 1", "Banheiro 2", "Quarto principal", "Quarto 2", "Quarto 3", "Escritório, posto de trabalho", "Corredor, escada", "Varanda", "Garagem", "Quintal, terreno", "Porão, sótão, depósito", "Outro cômodo 1", "Outro cômodo 2"]
BAGUA = ["Prosperidade", "Sucesso,\nreputação", "Relacionamentos", "Família", "Saúde\n(centro)", "Criatividade,\nfilhos", "Espiritualidade,\nsabedoria", "Trabalho,\ncarreira", "Amigos,\nviagens"]
TEC_AMBIENTE = [
    ("GRÁFICOS", ["Desimpregnador (72 setas)", "Diafragma I (+ quartzo rosa)", "Antimagia", "SCAP (energizar depois)", "Luxor", "Nove Círculos", "Vórtice, Turbilhão", "Decágono com endereço", "Mapeador eletromagnético", "Protetor psíquico"], "#e6e0f5"),
    ("COMANDOS", ["Neutralizar, embaralhar (anti-horário)", "Elevar, preencher (horário)", "“Limpeza de Ambiente em Luz”", "Apometria de ambiente (21 a 33 dias)", "Fechar portais e espelhos", "Fechar escudos da casa"], "#dcecfb"),
    ("FÍSICOS", ["Copo de água com sal, 24 h, no centro", "Sal grosso nos cantos, trocar em 7 dias", "Defumação: cantos e atrás das portas", "Vela branca consagrada", "Som alto 3 min por cômodo", "Pano com sal ou anil, do fundo para a porta", "Janelas abertas, sol", "Limpeza física, descarte", "Caiação (memória de parede)", "Plantas, cristais nos cantos", "Mudar móveis, cores, iluminação", "Música, textos sagrados, imagens protetoras"], "#e3f4e1"),
    ("GEOPATIA", ["Mover a cama 30 a 70 cm", "Mover a mesa de trabalho", "Casal: os dois lados em célula neutra", "Cortiça, lã ou sisal sob a cama", "Geopuntura: cobre em 2 pontos", "Pirâmide sobre o nó", "Cacto Cereus peruvianus", "Placa, orgonite"], "#e0f2f1"),
    ("ELETROMAGNÉTICO", ["Wi-Fi desligado à noite", "Celular fora do quarto", "Cabeceira longe do quadro e da fiação", "Medir radônio e campos"], "#fff3cc"),
]
DISTANCIAS = ["1 m", "2 m", "5 m", "10 m", "20 m", "50 m", "100 m", "200 m", "500 m", "1 km", "2 km", "5 km", "10 km", "20 km", "50 km", "100 km", "mais de\n100 km"]
RUMOS = ["N", "NNE", "NE", "ENE", "E", "ESE", "SE", "SSE", "S", "SSO", "SO", "OSO", "O", "ONO", "NO", "NNO"]
OBJ_SIT = ["Dentro de casa", "No carro", "No trabalho", "Com alguém", "Na rua,\nperdido", "Descartado,\nno lixo", "Roubado", "Em outra\ncasa", "Não existe\nmais"]
OBJ_ONDE = ["À vista", "Dentro de\nalgo", "Embaixo de\nalgo", "Atrás de\nalgo", "Escondido"]
OBJ_ALT = ["No chão", "Abaixo da\ncintura", "Altura dos\nolhos", "Acima da\ncabeça"]

def rose(labels, R=78, r0=26, w=190, h=190):
    cx, cy = w / 2, 90
    out = []; n = len(labels); step = 360.0 / n
    for i, lab in enumerate(labels):
        a0 = 90 - i * step + step / 2; a1 = a0 - step
        fill = PASTEL[i % len(PASTEL)] if i % 4 else "#e8edf5"
        out.append(f'<path d="{wedge(cx, cy, r0, R, a0, a1)}" fill="{fill}" stroke="{LINE}" stroke-width="0.35"/>')
        tx, ty = polar(cx, cy, (R + r0) / 2, (a0 + a1) / 2)
        big = i % 4 == 0
        out.append(f'<text x="{tx:.2f}" y="{ty+1.3:.2f}" font-size="{4.8 if big else 3.5}" fill="{INK}" font-weight="{700 if big else 500}" text-anchor="middle">{esc(lab)}</text>')
        ox, oy = polar(cx, cy, R + 5, (a0 + a1) / 2)
        out.append(f'<text x="{ox:.2f}" y="{oy+1:.2f}" font-size="2.6" fill="{QUIET}" text-anchor="middle">{int(round((i*step)%360))}°</text>')
    out.append(f'<circle cx="{cx}" cy="{cy}" r="{R}" fill="none" stroke="{LINE}" stroke-width="0.7"/>')
    out.append(f'<circle cx="{cx}" cy="{cy}" r="{r0}" fill="white" stroke="{LINE}" stroke-width="0.5"/>')
    out.append(pendulo_icon(cx, cy))
    out.append(testemunho(cx, cy + 6, w=28, h=11))
    return svg_wrap("".join(out), w, h - 10)

def grid_chart(cols=10, rows=8, w=190, h=175):
    cell = 15.5; x0 = 16; y0 = 12
    out = []
    letters = "ABCDEFGHIJ"
    for c in range(cols):
        x = x0 + c * cell
        out.append(f'<text x="{x+cell/2:.2f}" y="{y0-5.2:.2f}" font-size="3.6" fill="{ACCENT}" font-weight="700" text-anchor="middle">{c+1}</text>')
        out.append(f'<circle cx="{x+cell/2:.2f}" cy="{y0-1.8:.2f}" r="1.3" fill="white" stroke="{ACCENT}" stroke-width="0.4"/>')
    for r in range(rows):
        y = y0 + r * cell
        out.append(f'<text x="{x0-7.5:.2f}" y="{y+cell/2+1.3:.2f}" font-size="3.6" fill="{ACCENT}" font-weight="700" text-anchor="middle">{letters[r]}</text>')
        out.append(f'<circle cx="{x0-3:.2f}" cy="{y+cell/2:.2f}" r="1.3" fill="white" stroke="{ACCENT}" stroke-width="0.4"/>')
        for c in range(cols):
            x = x0 + c * cell
            out.append(f'<rect x="{x:.2f}" y="{y:.2f}" width="{cell}" height="{cell}" fill="{"#f7f9fc" if (r+c)%2 else "white"}" stroke="{GRID}" stroke-width="0.3"/>')
            out.append(f'<text x="{x+1.2:.2f}" y="{y+3.2:.2f}" font-size="2.2" fill="{QUIET}">{letters[r]}{c+1}</text>')
    gy = y0 + rows * cell
    out.append(f'<rect x="{x0}" y="{y0}" width="{cols*cell}" height="{rows*cell}" fill="none" stroke="{LINE}" stroke-width="0.7"/>')
    return svg_wrap("".join(out), w, gy + 6)

def ruler_list(items, w=190, row_h=9.2, font=3.7):
    out = []; y = 6
    for i, it in enumerate(items):
        out.append(f'<rect x="5" y="{y}" width="{w-10}" height="{row_h-1}" rx="1" fill="{PASTEL[i % len(PASTEL)]}" fill-opacity="0.35" stroke="{GRID}" stroke-width="0.25"/>')
        out.append(f'<circle cx="10" cy="{y+row_h/2-0.5:.2f}" r="2.1" fill="white" stroke="{ACCENT}" stroke-width="0.5"/><circle cx="10" cy="{y+row_h/2-0.5:.2f}" r="0.6" fill="{ACCENT}"/>')
        out.append(f'<text x="15" y="{y+row_h*0.62:.2f}" font-size="{font}" fill="{INK}" font-weight="700">{i+1}</text>')
        out.append(f'<text x="21" y="{y+row_h*0.62:.2f}" font-size="{font}" fill="{INK}">{esc(it)}</text>')
        out.append(mini_ruler(w - 64, y + row_h - 3.2, 54, "#ffffff"))
        y += row_h
    return svg_wrap("".join(out), w, y + 4)


CEAP_CAUSAS = [
    ("CAUSAS DE ENERGIAS NOCIVAS (curso CEAP)", ["Correntes de água subterrânea", "Esgotos, matéria em decomposição", "Condutos de água contaminada", "Fendas e aterros geológicos", "Cavernas e estratificações", "Jazidas de minerais nocivos", "Casa “morbosa” (muros impregnados)", "Objetos “preparados” em rituais", "Ossadas, túmulos sob a casa", "Redes Hartmann e Curry", "Televisores, micro-ondas, aparelhos"], "#e0f2f1"),
    ("OBJETOS A VERIFICAR (CEAP)", ["Quadros, imagens, estatuetas", "Plumas e flores secas", "Móveis antigos, leilão", "Objetos de arte e decoração", "Bonecas, bichos de pelúcia", "Travesseiros, almofadas", "Santinhos, patuás, pedras “da sorte”", "Formas assimétricas, pontiagudas"], "#fdebd3"),
    ("TERRENOS COM MEMÓRIA (Formação Holística)", ["Imóvel incendiado (com vítimas)", "Antiga delegacia", "Antiga funerária", "Antigo hospital", "Antigo cemitério", "Antigo templo", "Antigo lixão", "Antigo matadouro"], "#e6e0f5"),
]
INFL_EXT = ["Energia\ntelúrica", "Algum lugar\n(visitado, trabalho)", "Energia de\nforma", "Desequilíbrio\nde íons (clima)", "Energia\nprovocada", "Ambiente\nfamiliar", "Ambiente\nprofissional", "Seres fora\ndo físico", "Relaciona-\nmentos", "Energia de\npessoas"]

MEDEIROS = [
    ("CAUSAS DAS ENERGIAS NOCIVAS (Medeiros)", ["Falha telúrica", "Rochas ou materiais radioativos", "Ondas nocivas (de forma)", "Águas subterrâneas", "Correntes elétricas de alta tensão", "Fossa, esgoto", "Materiais nocivos", "Organização incorreta dos espaços", "Desarmonia cromática", "Cruzamento de linhas Hartmann"], "#e0f2f1"),
    ("ENERGIAS NOCIVAS PARANORMAIS (Medeiros)", ["Entidades desencarnadas", "Memórias cristalizadas no espaço", "Vestes ou tecidos antigos", "Móveis antigos", "Espelhos antigos", "Joias antigas", "Objetos rituais utilizados", "Imagens religiosas antigas", "Objetos consagrados", "Cerimônias de invocação", "Rituais mágicos negativos", "Feitiçaria exterior", "Egrégoras negativas", "Uso incorreto de velas", "Músicas de campo negativo"], "#e6e0f5"),
    ("PURIFICADORES (Medeiros)", ["Sal marinho", "Incensos", "Óleos essenciais", "Velas", "Mandalas", "Pentagrama", "Heptagrama", "Cristal de quartzo", "Cristal de ametista", "Bola de cristal", "Runas", "Textos sagrados", "Imagens protetoras", "Músicas", "Plantas verdes"], "#e3f4e1"),
    ("NEUTRALIZAÇÃO (Medeiros)", ["Mudar a localização dos móveis", "Mudar a decoração", "Ventilação", "Mudar as cores", "Introduzir uma cor", "Purificação", "Exorcismo do lugar", "Ritual de limpeza", "Harmonização energética", "Mudar a iluminação"], "#fff6cc"),
]
AMB_SUBTIL = ["Magia", "Atividade\nhumana", "Ondas de\nforma", "Memória dos\nmóveis", "Poluição\nelétrica", "Presença de\nentidades", "Memória das\nparedes", "Veios\nd’água", "Falha\ngeobiológica", "Ondas\ntelúricas", "Local\nnormal"]

QUEM_IMPRIME = ["A própria\npessoa", "Parceiro,\nparceira", "Filho, filha", "Pai", "Mãe", "Irmão, irmã", "Outro\nmorador", "Visita\nfrequente", "Ex-morador", "Vizinho", "O lugar em si\n(telúrico, histórico)", "Ninguém:\nneutro"]
ONDE_PESSOA = ["Quarto\npróprio", "Quarto\ndo casal", "Quarto dos\nfilhos", "Quarto dos pais\n(casa dos pais)", "Sala", "Escritório, posto\nde trabalho", "Casa de\noutra pessoa", "Trabalho\nfora", "Em trânsito,\nviagem", "Outro"]

# ---------- Aplicações da vida prática (edição 5) ----------
AREAS_VIDA = ["Saúde e\ncorpo", "Emocional", "Relações\nafetivas", "Família", "Trabalho e\nvocação", "Dinheiro", "Casa e\nambiente", "Espiritualidade\ne missão"]
DECISAO = ["Sim", "Não", "Ainda não\n(espere)", "Refazer a\npergunta", "Não me cabe\nresponder"]
MOMENTO = ["Agora", "Em dias", "Em semanas", "Em meses", "Depois de resolver\noutra coisa", "Não é o\nmomento"]
ALTERNATIVAS = ["Opção A", "Opção B", "Opção C", "Opção D", "Nenhuma\ndelas", "Outra, ainda\nnão vista"]
ERROS = [
    ("CAUSAS DE ERRO NA LEITURA (Medeiros)", ["Causa desconhecida", "Alteração das energias por doença", "Fadiga", "Postura incorreta", "Falta de concentração", "Questão mal formulada", "Momento desfavorável", "Influência de terceiros", "Influência de campos vibratórios", "Influência mental nas respostas", "Condicionamento da resposta", "Interpretação errada"], "#fde2e2"),
    ("OBSTÁCULOS DA PESSOA (Medeiros)", ["Agressividade", "Alterações de saúde", "Atitudes rígidas", "Comportamentos retrógrados", "Falta de autoestima", "Falta de espiritualidade", "Falta de iniciativa", "Falta de vontade", "Ideias preconcebidas", "Ignorância", "Instabilidade", "Outra"], "#fff6cc"),
]
RELACAO = ["Sintonia\ngeral", "Físico,\natração", "Emocional", "Mental,\ncomunicação", "Energético,\ndisposição", "Espiritual,\nvalores", "Confiança", "Apoio,\namizade", "Padrão\nrepetido", "Cordão\ndesequilibrado", "Área que pede\natenção", "Gráfico\nemissor"]
RELACAO_PEDE = ["Comunicação", "Tempo\njuntos", "Limites", "Intimidade", "Dinheiro", "Família de\norigem", "Projeto\ncomum", "Cuidado\npróprio"]
TENSAO = ["Comunicação", "Hierarquia", "Ciúme,\ncompetição", "Dinheiro", "Valores", "Sobrecarga", "Falta de\ncompanheirismo", "Desorganização", "Doença", "Apego", "Pessoa\ntóxica", "Falta de\nconfiança", "Medo da\nrejeição", "Propósitos\ndiferentes"]
EMPRESA = ["Energia geral\ndo negócio", "Ponto, espaço\nfísico", "Clima da\nequipe", "Liderança", "Produto ou\nserviço", "Nome e\nidentidade", "Clientes: fluxo\ne afinidade", "Finanças: entrada,\nsaída, bloqueio", "Sintonia entre\nsócios", "Comunicação\nexterna", "Área que pede\natenção primeiro"]
OBJETO_EMP = ["A empresa\ncomo um todo", "As pessoas\n(com consentimento)", "O produto\nou serviço", "A identidade\n(nome, marca)", "O espaço\n(loja, escritório)"]
PROSP = [
    ("BLOQUEIOS DA PROSPERIDADE (22)", ["Padrões mentais", "Padrões comportamentais", "Dispositivo implantado", "Desequilíbrio físico", "Consumismo", "Acumulação", "Apego ao passado", "Medo do futuro", "Magia trevosa", "Insegurança, dependência", "Consumismo, conforto", "Aversão ao dinheiro", "Falta de objetivo", "Crenças limitantes", "Autossabotagem", "Padrões ancestrais", "Dívidas kármicas", "Ambientes tóxicos", "Pessoas tóxicas", "Obsessores", "Vitimismo", "Outros"], "#fff6cc"),
    ("O QUE AFETA A PROSPERIDADE (MAP, 15)", ["Não merecimento", "Autossabotagem", "Baixa autoestima", "Absorve conselhos invejosos", "Vício emocional", "Falta de intuição", "Egocentrismo", "Falta de generosidade", "Crenças limitantes", "Raiva por algo ou alguém", "Fora da missão de vida", "Absorve as energias das pessoas", "Não soltar", "Falta de autoconhecimento", "Procrastinação"], "#e3f4e1"),
]
TRABALHO = ["Stress", "Falta de\npropósito", "Insatisfação", "Falta de\nfeedback", "Desequilíbrio\nvida e trabalho", "Relação com\na chefia", "Relação com\ncolegas", "Remuneração", "Insegurança,\nmedo de perder", "Mudança\ndesejada"]
DOSE = [("Forma", ["Gotas", "Goles", "Comprimidos", "Colheres", "Gramas", "Mililitros"], "#dcecfb"),
        ("Vezes por dia", ["1", "2", "3", "4", "6", "Uma vez\nsó"], "#e3f4e1"),
        ("Horário", ["Ao acordar", "Manhã", "Tarde", "Noite", "Ao deitar", "Com as\nrefeições"], "#fff6cc"),
        ("Duração", ["3 dias", "7 dias", "14 dias", "21 dias", "1 mês", "Contínuo"], "#fde2e2")]
ALIMENTOS = [
    ("GRUPOS (Medeiros)", ["Carnes vermelhas", "Carnes brancas", "Peixes", "Frutos do mar", "Laticínios", "Ovos", "Cereais", "Vegetais", "Fungos", "Frutos"], "#e3f4e1"),
    ("PLANTAS: TONIFICAÇÃO (Medeiros)", ["Alho", "Cravo", "Gengibre", "Ginseng", "Nogueira"], "#fde2e2"),
    ("PLANTAS: ELIMINAÇÃO (Medeiros)", ["Cúrcuma", "Fumária", "Funcho", "Parietária", "Salsa"], "#dcecfb"),
    ("PLANTAS: MANUTENÇÃO (Medeiros)", ["Canela", "Cedro", "Hipericão", "Malva", "Melissa"], "#e6e0f5"),
    ("ALIMENTOS POR COR (cromoterapia)", ["Vermelha: beterraba, tomate, morango, uva", "Laranja: casca alaranjada", "Amarela: cenoura, abóbora, milho, manga", "Verde: hortaliças e frutas verdes", "Azul e índigo: ameixa, amora, aspargo", "Violeta: berinjela, brócolis roxo, uva roxa"], "#f3e1ef"),
]
VITAMINAS = ["A: abacate, abóbora, brócolis, cenoura, espinafre, manga, melão, pêssego", "B1: amêndoa, arroz integral, levedura de cerveja, aveia, amendoim", "B2: abacate, amendoim, castanha, espinafre, feijão-branco, brócolis", "B5: amendoim, levedura de cerveja, pimentão, trigo integral", "B6: farelo e gérmen de trigo, leite, levedura de cerveja, melado", "B12: amêndoa, cereais integrais, leite, batata, gérmen de trigo", "C: abacaxi, mamão, alface, caju, espinafre, limão, alho, cebola, laranja", "D: gema de ovo, leite e derivados", "E: abacate, óleos vegetais, gérmen de trigo", "K: hortaliças verdes, couve, brócolis", "P (flavonoides): frutas cítricas, uva", "H (biotina): gema de ovo, levedura, nozes"]
MAGER = [("Branco\nmedicinal", "#ffffff"), ("Violeta\nmuito pura", "#e6e0f5"), ("Azul\npotável", "#dcecfb"), ("Verde\nrica em sais", "#e3f4e1"), ("Amarelo\nsaturada", "#fff6cc"), ("Vermelho\nférrea", "#fde2e2"), ("Cinza\npoluída", "#e0e0e0"), ("Preto\nestagnada", "#c8c8c8")]
ROUPAS = [("Branco\npaz, calma", "#ffffff"), ("Vermelho\ncoragem", "#fde2e2"), ("Amarelo\nintuição, dinheiro", "#fff6cc"), ("Laranja\nsucesso", "#fdebd3"), ("Verde\nganho, calma", "#e3f4e1"), ("Azul\nharmonia", "#dcecfb"), ("Violeta\ninspiração", "#e6e0f5"), ("Rosa\nsimpatia", "#f3e1ef"), ("Preto\nafasta inveja", "#e0e0e0"), ("Marrom\nevitar", "#f0efe6")]
TALENTOS = ["Criar", "Cuidar", "Organizar", "Ensinar", "Comunicar", "Construir", "Analisar"]
DESENVOLVER = ["Desenvolvimento\nintelectual", "Saúde e\ndisposição", "Equilíbrio\nemocional", "Recursos\nfinanceiros", "Contribuição\nsocial", "Realização e\npropósito", "Criatividade,\nhobbies, diversão", "Plenitude e\nfelicidade", "Espiritualidade"]
ATIVIDADES = ["Agricultura", "Arte", "Biologia", "Comércio", "Diplomacia", "Direito", "Economia, finanças", "Engenharia", "Ensino", "Filosofia", "Física, química", "Gestão", "História", "Informática", "Jornalismo", "Medicina", "Política", "Psicologia", "Religião", "Veterinária", "Outra"]

ERVAS_CHAKRA = [
    ("1 BÁSICO · raiz de dente-de-leão", ["Cenoura", "Batata", "Nabo", "Rabanete", "Cebola", "Alho"], CHAKRA_TINT[1]),
    ("2 SACRAL · gardênia", ["Calêndula", "Sândalo (óleo)", "Coentro", "Erva-doce", "Alcaçuz", "Canela", "Baunilha", "Gergelim", "Cominho"], CHAKRA_TINT[2]),
    ("3 PLEXO SOLAR · alecrim", ["Lavanda (óleo)", "Bergamota", "Anis", "Aipo", "Hortelã", "Gengibre", "Melissa", "Açafrão", "Erva-doce"], CHAKRA_TINT[3]),
    ("4 CARDÍACO · espinheiro-branco", ["Pimenta caiena", "Jasmim", "Lavanda", "Manjericão", "Sálvia", "Tomilho", "Coentro", "Salsa"], CHAKRA_TINT[4]),
    ("5 LARÍNGEO · trevo vermelho", ["Erva-cidreira", "Eucalipto (óleo)", "Tussilagem", "Hortelã-pimenta", "Sálvia", "Capim-limão"], CHAKRA_TINT[5]),
    ("6 FRONTAL · eufrásia", ["Menta", "Jasmim", "Zimbro", "Artemísia", "Papoula", "Alecrim", "Lavanda"], CHAKRA_TINT[6]),
    ("7 CORONÁRIO · lavanda", ["Lótus", "Lavanda (todos os chakras)"], CHAKRA_TINT[7]),
]

SOCIO = ["Valores\ne ética", "Visão do\nnegócio", "Complemen-\ntaridade", "Confiança", "Comunicação", "Comprometi-\nmento e tempo", "Capacidade\nfinanceira", "Apetite\na risco", "Rede de\ncontatos", "Regras de saída\ne conflito", "Sintonia geral\nda sociedade", "Outro\ncritério"]
PROJETO = ["Viabilidade", "Momento", "Retorno\nfinanceiro", "Risco", "Alinhamento\ncom o propósito", "Demanda dos\nclientes", "Capacidade\nda equipe", "Recursos\ne prazo", "Impacto na\nvida pessoal", "Aprendizado", "Favorabilidade\ngeral", "Outro\ncritério"]
SITUACAO = ["Sócio ou\nparceiro", "Projetos ou\nprodutos", "Contratar, promover\nou desligar", "Expandir, filial,\nmudar de ponto", "Investir, empréstimo,\npreço", "Fechar, vender,\nencerrar", "Cliente ou\nfornecedor", "Conflito\ninterno", "Outra"]
# ---------- Manual de Radiestesia para Negócios: gráficos próprios (G111 em diante) ----------
# Os gráficos G1 a G110 reaproveitados vêm do Manual de Radiestesia Terapêutica (../radiestesia/charts) sem alteração.
REUSE = ["G1","G2","G3","G4","G9","G10","G24","G28","G59","G62","G66","G67","G69","G70","G71","G82","G83","G84","G85","G86","G87","G88",
         "G89","G90","G91","G92","G94","G95","G101","G103","G106","G107","G108","G109","G110"]
TRAVA = ["Falta de\ninformação", "Medo de\nerrar", "Medo de perder\no que tem", "Medo do\njulgamento", "Conflito de\nvalores", "Pressão de\nterceiro",
         "Lealdade a\nalguém", "Apego ao\nmodelo antigo", "Cansaço e\nsobrecarga", "Dinheiro", "Não é\na hora", "Outra"]
PROPOSTA = ["Preço e\npagamento", "Prazo", "Escopo e\nentregas", "Garantias e\npenalidades", "Saída e\nrescisão", "Exclusividade e\ndependência",
            "Responsabilidades\ne riscos", "Reputação e\nhistórico", "Alinhamento\nde valores", "Informação\nque falta", "Momento", "Outro"]
NEGOCIACAO = ["Fator nosso:\npreço, prazo, dúvida", "Fator da\noutra parte", "Contexto e\nmercado", "Terceiro\nenvolvido", "Ambiente ou\nmemória do local",
              "Pessoa que\ndrena", "Ganho em\nnão fechar", "Falta\ninformação"]
MODELO = ["Segmentos\nde clientes", "Proposta\nde valor", "Canais", "Relacionamento\ncom clientes", "Receitas", "Recursos-\nchave", "Atividades-\nchave", "Parcerias", "Custos"]
FASE = ["Ideia", "Validação", "Lançamento", "Crescimento", "Platô", "Reinvenção", "Sucessão", "Encerramento"]
TERRENO = ["Energia geral\n(Bovis)", "Água\nsubterrânea", "Falhas e\nredes", "Histórico e\nmemória", "Vizinhança\ne entorno", "Acesso e\nfluxo",
           "Afinidade com\no público", "Afinidade com\no empreendedor", "Momento", "Risco", "Impacto na\nvida do dono", "Outro"]
EMPREEND = ["Terreno", "Projeto", "Aprovações", "Financiamento\ne caixa", "Obra e\nfornecedores", "Equipe", "Vendas e\ncomercialização",
            "Clientes e\npós-venda", "Parceiros\ne sócios", "Jurídico e\ncontratos", "Comunicação", "Outro"]
INTERF_NEG = ["Em mim\n(quem decide)", "Numa\nrelação", "Na equipe", "No espaço", "Memória do local\nou do negócio", "Contrato\nenergético",
              "Coletivo:\ninveja, olhares", "Não é energético:\nvoltar aos números"]
PONTO = ["Energia do\nimóvel (Bovis)", "Fluxo de\npessoas", "Visibilidade", "Acesso e\nestacionamento", "Vizinhança e\nconcorrência", "Memória\ndo ponto",
         "Afinidade com\no público", "Afinidade com\no dono", "Custo e\ncontrato", "Momento", "Risco", "Outro"]

def compat_chart(w=190, h=96):
    """Compatibilidade para um objetivo: dois testemunhos, o objetivo escrito e a régua de 0 a 100 com as faixas do manual."""
    out = []
    for x, lab in ((34, "T1 · quem pede"), (156, "T2 · o outro, o projeto ou o lugar")):
        out.append(f'<rect x="{x-24}" y="10" width="48" height="22" rx="2" fill="{FILL_B}" stroke="{LINE}" stroke-width="0.4" stroke-dasharray="1.6 1.1"/>')
        out.append(f'<text x="{x}" y="36.5" font-size="3.0" fill="{QUIET}" text-anchor="middle" font-weight="600">{esc(lab)}</text>')
    out.append(f'<rect x="66" y="12" width="58" height="18" rx="2" fill="white" stroke="{ACCENT}" stroke-width="0.5"/>')
    out.append(f'<text x="95" y="19" font-size="3.4" fill="{ACCENT}" text-anchor="middle" font-weight="700">OBJETIVO</text>')
    out.append(f'<text x="95" y="24.5" font-size="2.6" fill="{QUIET}" text-anchor="middle">sociedade · parceria · projeto · lugar · contrato</text>')
    out.append(f'<line x1="58" y1="21" x2="66" y2="21" stroke="{LINE}" stroke-width="0.4"/><line x1="124" y1="21" x2="132" y2="21" stroke="{LINE}" stroke-width="0.4"/>')
    x0, x1, y = 16, w - 16, 66
    X = lambda v: x0 + (x1 - x0) * v / 100
    for z0, z1, c in ((0, 40, "#fbe3e3"), (40, 70, "#fff6cc"), (70, 100, "#e3f4e1")):
        out.append(f'<rect x="{X(z0):.1f}" y="{y-9}" width="{X(z1)-X(z0):.1f}" height="9" fill="{c}"/>')
    out.append(f'<line x1="{x0}" y1="{y}" x2="{x1}" y2="{y}" stroke="{LINE}" stroke-width="0.8"/>')
    for v in range(0, 101, 2):
        hgt = 9 if v % 10 == 0 else (5 if v % 10 == 5 else 2.5)
        out.append(f'<line x1="{X(v):.1f}" y1="{y}" x2="{X(v):.1f}" y2="{y-hgt}" stroke="{LINE}" stroke-width="{0.7 if v % 10 == 0 else 0.3}"/>')
        if v % 10 == 0: out.append(f'<text x="{X(v):.1f}" y="{y+6}" font-size="4.0" fill="{INK}" font-weight="700" text-anchor="middle">{v}</text>')
    for v, lab, c in ((40, "abaixo de 40: não seguir", "#c62828"), (70, "70 ou mais: seguir", "#2e7d32")):
        out.append(f'<line x1="{X(v):.1f}" y1="{y-13}" x2="{X(v):.1f}" y2="{y+1}" stroke="{c}" stroke-width="1"/>')
        out.append(f'<text x="{X(v):.1f}" y="{y-14.5}" font-size="3.0" fill="{c}" font-weight="700" text-anchor="middle">{esc(lab)}</text>')
    out.append(f'<text x="{(X(40)+X(70))/2:.1f}" y="{y-14.5}" font-size="3.0" fill="#8a6d00" font-weight="700" text-anchor="middle">40 a 69: por projeto, com prazo</text>')
    out.append(f'<text x="{x0}" y="{y+13}" font-size="3" fill="{QUIET}">Percentual de compatibilidade entre T1 e T2 para o objetivo escrito, hoje. Pergunta uma vez; registra; compara entre sessões.</text>')
    out.append(f'<text x="{x0}" y="{y+18}" font-size="3" fill="{QUIET}">Pêndulo no ponto azul e deslizando pela régua; parada no valor. Convenção deste manual, a partir do gráfico de pesquisa de compatibilidade de referência.</text>')
    out.append(pendulo_icon(w / 2, y + 26))
    return svg_wrap("".join(out), w, h)

def build():
    import json, shutil
    R = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "radiestesia", "charts")
    rman = {m["id"]: m for m in json.load(open(os.path.join(R, "manifest.json"), encoding="utf-8"))}
    manifest = []
    for cid in REUSE:
        m = rman[cid]; shutil.copy(os.path.join(R, m["file"]), os.path.join(OUT, m["file"])); manifest.append(m)
    def save(cid, title, svg, kind, items=None, note=""):
        fn = f"{cid}.svg"
        with open(os.path.join(OUT, fn), "w", encoding="utf-8") as f: f.write(svg)
        manifest.append({"id": cid, "title": title, "file": fn, "kind": kind, "items": [i.replace("\n", " ") for i in (items or [])], "note": note})
    save("G111", "Trava da decisão", fan(TRAVA, colors=PASTEL[:12]), "leque", TRAVA)
    save("G112", "Proposta ou contrato: pontos de atenção", fan(PROPOSTA, colors=PASTEL[:12]), "leque", PROPOSTA)
    save("G113", "Onde trava a negociação", fan(NEGOCIACAO, colors=PASTEL[:8]), "leque", NEGOCIACAO)
    save("G114", "Modelo de negócio: bloco frágil", fan(MODELO, colors=PASTEL[:9]), "leque", MODELO)
    save("G115", "Fase do negócio", fan(FASE, colors=PASTEL[:8]), "leque", FASE)
    save("G116", "Terreno para empreender: critérios", fan(TERRENO, colors=PASTEL[:12]), "leque", TERRENO)
    save("G117", "Empreendimento: onde está o peso", fan(EMPREEND, colors=PASTEL[:12]), "leque", EMPREEND)
    save("G118", "Compatibilidade para um objetivo (0 a 100)", compat_chart(), "escala")
    save("G119", "Interferência no negócio: onde está", fan(INTERF_NEG, colors=PASTEL[:8]), "leque", INTERF_NEG)
    save("G120", "Ponto comercial: critérios", fan(PONTO, colors=PASTEL[:12]), "leque", PONTO)
    with open(os.path.join(OUT, "manifest.json"), "w", encoding="utf-8") as f:
        json.dump(manifest, f, ensure_ascii=False, indent=1)
    print(f"{len(manifest)} gráficos em {OUT} ({len(REUSE)} reaproveitados, {len(manifest)-len(REUSE)} novos)")

if __name__ == "__main__":
    build()
