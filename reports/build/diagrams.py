"""Gera os diagramas SVG do livro em reports/assets/diagrams/."""
import math
import os

OUT = os.path.join(os.path.dirname(__file__), "..", "assets", "diagrams")
os.makedirs(OUT, exist_ok=True)

INK, ACC, GOLD, MUT, LINE = "#1d1b18", "#7a2e1d", "#a8791f", "#6b645a", "#d9d2c5"
GREEN, BLUE, PURPLE, RED = "#2f6b4a", "#2b4f7a", "#5a3b7a", "#a12a2a"
FONT = "DejaVu Sans, Liberation Sans, sans-serif"


def svg(w, h, body):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" '
            f'font-family="{FONT}">{body}</svg>')


def text(x, y, s, size=12, fill=INK, anchor="middle", weight="normal", style=""):
    return (f'<text x="{x}" y="{y}" font-size="{size}" fill="{fill}" text-anchor="{anchor}" '
            f'font-weight="{weight}" {style}>{s}</text>')


def save(name, content):
    with open(os.path.join(OUT, name), "w", encoding="utf-8") as f:
        f.write(content)


def poly(points, **kw):
    pts = " ".join(f"{x:.2f},{y:.2f}" for x, y in points)
    attrs = " ".join(f'{k.replace("_", "-")}="{v}"' for k, v in kw.items())
    return f'<polyline points="{pts}" fill="none" {attrs}/>'


# ---------------------------------------------------------------- Futhark
RUNES = [
    ("Fehu", "f", [[(3, 0), (3, 20)], [(3, 10), (9, 4)], [(3, 5), (8, 0)]]),
    ("Uruz", "u", [[(2, 20), (2, 0), (8, 6), (8, 20)]]),
    ("Thurisaz", "þ", [[(3, 0), (3, 20)], [(3, 5), (8, 10), (3, 15)]]),
    ("Ansuz", "a", [[(3, 0), (3, 20)], [(3, 0), (8, 5)], [(3, 6), (8, 11)]]),
    ("Raido", "r", [[(3, 20), (3, 0), (8, 5), (3, 10), (8, 20)]]),
    ("Kaunan", "k", [[(8, 4), (3, 10), (8, 16)]]),
    ("Gebo", "g", [[(1, 2), (9, 18)], [(9, 2), (1, 18)]]),
    ("Wunjo", "w", [[(3, 20), (3, 0), (8, 5), (3, 10)]]),
    ("Hagalaz", "h", [[(2, 0), (2, 20)], [(8, 0), (8, 20)], [(2, 7), (8, 13)]]),
    ("Naudiz", "n", [[(5, 0), (5, 20)], [(2, 7), (8, 13)]]),
    ("Isaz", "i", [[(5, 0), (5, 20)]]),
    ("Jera", "j", [[(5, 2), (1, 7), (5, 12)], [(5, 8), (9, 13), (5, 18)]]),
    ("Eihwaz", "ï", [[(5, 0), (5, 20)], [(5, 0), (8, 4)], [(5, 20), (2, 16)]]),
    ("Perth", "p", [[(3, 0), (3, 20)], [(3, 0), (6, 4), (9, 0)], [(3, 20), (6, 16), (9, 20)]]),
    ("Algiz", "z", [[(5, 0), (5, 20)], [(5, 10), (1, 2)], [(5, 10), (9, 2)]]),
    ("Sowilo", "s", [[(8, 0), (2, 7), (8, 13), (2, 20)]]),
    ("Tiwaz", "t", [[(5, 0), (5, 20)], [(1, 6), (5, 0), (9, 6)]]),
    ("Berkanan", "b", [[(3, 0), (3, 20)], [(3, 0), (8, 5), (3, 10), (8, 15), (3, 20)]]),
    ("Ehwaz", "e", [[(2, 20), (2, 0), (5, 5), (8, 0), (8, 20)]]),
    ("Mannaz", "m", [[(2, 20), (2, 0), (8, 8)], [(8, 20), (8, 0), (2, 8)]]),
    ("Laguz", "l", [[(4, 20), (4, 0), (9, 6)]]),
    ("Ingwaz", "ŋ", [[(5, 4), (9, 10), (5, 16), (1, 10), (5, 4)]]),
    ("Dagaz", "d", [[(1, 2), (1, 18), (9, 2), (9, 18), (1, 2)]]),
    ("Othala", "o", [[(1, 20), (9, 8), (5, 2), (1, 8), (9, 20)]]),
]


def rune_glyph(strokes, x, y, s=2.6, color=INK, width=3.2):
    out = ""
    for st in strokes:
        out += poly([(x + px * s, y + py * s) for px, py in st], stroke=color,
                    stroke_width=width, stroke_linecap="round", stroke_linejoin="round")
    return out


def futhark(highlight=()):
    cw, ch = 92, 112
    body = f'<rect width="{cw*8+16}" height="{ch*3+40}" fill="#fffdf9"/>'
    body += text((cw * 8 + 16) / 2, 20, "Futhark Antigo — as 24 runas (nomes reconstruídos do protogermânico)", 13, ACC, weight="bold")
    for i, (name, tr, strokes) in enumerate(RUNES):
        col, row = i % 8, i // 8
        x0, y0 = 8 + col * cw, 32 + row * ch
        hl = name in highlight
        body += (f'<rect x="{x0+3}" y="{y0+3}" width="{cw-6}" height="{ch-6}" rx="5" '
                 f'fill="{"#fbf3e2" if hl else "#ffffff"}" stroke="{GOLD if hl else LINE}" stroke-width="{1.6 if hl else 1}"/>')
        body += rune_glyph(strokes, x0 + cw / 2 - 13, y0 + 14, color=ACC if hl else INK)
        body += text(x0 + cw / 2, y0 + 84, name, 10.5, INK, weight="bold")
        body += text(x0 + cw / 2, y0 + 99, f"som: {tr}", 9, MUT)
    return svg(cw * 8 + 16, ch * 3 + 40, body)


save("futhark.svg", futhark(highlight=("Fehu", "Algiz", "Othala", "Sowilo", "Tiwaz", "Thurisaz")))


# ---------------------------------------------------------------- Estrelas
def star_points(cx, cy, r, n, step, rot=-90):
    pts = [(cx + r * math.cos(math.radians(rot + 360 * k / n)),
            cy + r * math.sin(math.radians(rot + 360 * k / n))) for k in range(n)]
    order = [(k * step) % n for k in range(n + 1)]
    return [pts[i] for i in order]


def geometria():
    W, H = 760, 300
    body = f'<rect width="{W}" height="{H}" fill="#fffdf9"/>'
    # pentagrama
    cx, cy, r = 125, 140, 95
    body += f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{LINE}" stroke-width="1.5"/>'
    body += poly(star_points(cx, cy, r, 5, 2), stroke=ACC, stroke_width=3, stroke_linejoin="round")
    body += text(cx, 262, "Pentagrama", 13, INK, weight="bold")
    body += text(cx, 280, "traço único, 5 pontas", 10, MUT)
    # hexagrama
    cx = 380
    body += f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{LINE}" stroke-width="1.5"/>'
    for rot in (-90, 90):
        pts = [(cx + r * math.cos(math.radians(rot + 120 * k)), cy + r * math.sin(math.radians(rot + 120 * k))) for k in range(4)]
        body += poly(pts, stroke=BLUE, stroke_width=3, stroke_linejoin="round")
    body += text(cx, 262, "Hexagrama", 13, INK, weight="bold")
    body += text(cx, 280, "dois triângulos entrelaçados", 10, MUT)
    # hexafólio
    cx, rr = 635, 95
    body += f'<circle cx="{cx}" cy="{cy}" r="{rr}" fill="none" stroke="{GREEN}" stroke-width="2.4"/>'
    P = [(cx + rr * math.cos(math.radians(60 * k)), cy + rr * math.sin(math.radians(60 * k))) for k in range(6)]
    for k in range(6):
        (x1, y1), (x2, y2) = P[(k - 1) % 6], P[(k + 1) % 6]
        body += f'<path d="M{x1:.2f},{y1:.2f} A{rr},{rr} 0 0 0 {x2:.2f},{y2:.2f}" fill="none" stroke="{GREEN}" stroke-width="2.4"/>'
    body += text(cx, 262, "Hexafólio", 13, INK, weight="bold")
    body += text(cx, 280, "seis pétalas traçadas a compasso", 10, MUT)
    return svg(W, H, body)


save("geometria.svg", geometria())


# ---------------------------------------------------------------- Quadrados
def grid(x0, y0, rows, cell, color, size=20):
    out = ""
    for r, row in enumerate(rows):
        for c, v in enumerate(row):
            out += (f'<rect x="{x0+c*cell}" y="{y0+r*cell}" width="{cell}" height="{cell}" fill="#fff" '
                    f'stroke="{color}" stroke-width="1.5"/>')
            out += text(x0 + c * cell + cell / 2, y0 + r * cell + cell / 2 + size * 0.36, v, size, INK, weight="bold")
    return out


def quadrados():
    W, H = 760, 330
    body = f'<rect width="{W}" height="{H}" fill="#fffdf9"/>'
    sator = ["SATOR", "AREPO", "TENET", "OPERA", "ROTAS"]
    body += grid(60, 40, sator, 48, ACC, 24)
    body += text(180, 302, "Quadrado SATOR", 13, INK, weight="bold")
    body += text(180, 320, "lê-se igual nas quatro direções", 10, MUT)
    kamea = [[4, 14, 15, 1], [9, 7, 6, 12], [5, 11, 10, 8], [16, 2, 3, 13]]
    body += grid(440, 50, kamea, 56, GOLD, 22)
    body += text(552, 302, "Quadrado mágico de Júpiter (4 × 4)", 13, INK, weight="bold")
    body += text(552, 320, "cada linha, coluna e diagonal soma 34; total 136", 10, MUT)
    return svg(W, H, body)


save("quadrados.svg", quadrados())


# ---------------------------------------------------------------- Bagua
TRI = {"Qian": (1, 1, 1), "Dui": (1, 1, 0), "Li": (1, 0, 1), "Zhen": (1, 0, 0),
       "Xun": (0, 1, 1), "Kan": (0, 1, 0), "Gen": (0, 0, 1), "Kun": (0, 0, 0)}  # linhas de baixo para cima
PT = {"Qian": "Céu", "Dui": "Lago", "Li": "Fogo", "Zhen": "Trovão", "Xun": "Vento", "Kan": "Água", "Gen": "Montanha", "Kun": "Terra"}
# posição: ângulo em graus (0 = topo = Sul, sentido horário: SO, O, NO, N, NE, L, SE)
EARLIER = ["Qian", "Xun", "Kan", "Gen", "Kun", "Zhen", "Li", "Dui"]
LATER = ["Li", "Kun", "Dui", "Qian", "Kan", "Gen", "Zhen", "Xun"]
DIRS = ["S", "SO", "O", "NO", "N", "NE", "L", "SE"]


def trigram(cx, cy, ang, lines, color):
    out = f'<g transform="translate({cx:.1f},{cy:.1f}) rotate({ang})">'
    for i, yang in enumerate(lines):  # i=0 linha de baixo = mais perto do centro
        y = 14 - i * 12
        if yang:
            out += f'<rect x="-22" y="{y-3.5}" width="44" height="7" fill="{color}"/>'
        else:
            out += f'<rect x="-22" y="{y-3.5}" width="18" height="7" fill="{color}"/><rect x="4" y="{y-3.5}" width="18" height="7" fill="{color}"/>'
    return out + "</g>"


def bagua_one(cx, cy, order, title, sub, color):
    R = 116
    out = ""
    pts = [(cx + 150 * math.cos(math.radians(-90 + 22.5 + 45 * k)), cy + 150 * math.sin(math.radians(-90 + 22.5 + 45 * k))) for k in range(9)]
    out += poly(pts, stroke=color, stroke_width=2.5)
    out += f'<circle cx="{cx}" cy="{cy}" r="40" fill="#fff" stroke="{LINE}" stroke-width="1.5"/>'
    out += text(cx, cy - 4, "centro", 10, MUT)
    out += text(cx, cy + 10, "(espelho ou", 8.5, MUT) + text(cx, cy + 21, "taiji)", 8.5, MUT)
    for k, name in enumerate(order):
        ang = 45 * k
        a = math.radians(-90 + ang)
        out += trigram(cx + R * math.cos(a), cy + R * math.sin(a), ang, TRI[name], INK)
        lx, ly = cx + 66 * math.cos(a), cy + 66 * math.sin(a)
        out += text(lx, ly + 1, name, 8.5, color, weight="bold")
        out += text(lx, ly + 11, PT[name], 7.5, MUT)
        dx, dy = cx + 168 * math.cos(a), cy + 168 * math.sin(a)
        out += text(dx, dy + 4, DIRS[k], 11, ACC, weight="bold")
    out += text(cx, cy + 205, title, 13, INK, weight="bold")
    out += text(cx, cy + 222, sub, 10, MUT)
    return out


def bagua():
    W, H = 780, 450
    body = f'<rect width="{W}" height="{H}" fill="#fffdf9"/>'
    body += bagua_one(195, 200, EARLIER, "Céu Anterior (Xiantian, atribuído a Fuxi)", "opostos frente a frente: Céu–Terra, Fogo–Água", GREEN)
    body += bagua_one(585, 200, LATER, "Céu Posterior (Houtian, atribuído ao Rei Wen)", "ciclo das estações e direções; base da bússola", BLUE)
    body += text(W / 2, 442, "Convenção chinesa: o Sul fica no alto do diagrama. A linha de baixo de cada trigrama é a mais próxima do centro.", 9.5, MUT)
    return svg(W, H, body)


save("bagua.svg", bagua())


# ---------------------------------------------------------------- Porta: três camadas
def door_frame(x, y, w, h, wall="#efe7d8"):
    out = f'<rect x="{x-70}" y="{y-50}" width="{w+140}" height="{h+50}" fill="{wall}" stroke="{LINE}"/>'
    out += f'<rect x="{x-10}" y="{y-10}" width="{w+20}" height="{h+10}" fill="#c9b79a" stroke="#8d7a5c"/>'
    out += f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="#7b5a3a" stroke="#4d3722"/>'
    out += f'<rect x="{x+12}" y="{y+14}" width="{w-24}" height="{h/2-24}" fill="none" stroke="#5f4329" stroke-width="2"/>'
    out += f'<rect x="{x+12}" y="{y+h/2+6}" width="{w-24}" height="{h/2-22}" fill="none" stroke="#5f4329" stroke-width="2"/>'
    out += f'<circle cx="{x+w-16}" cy="{y+h/2}" r="4.5" fill="{GOLD}"/>'
    out += f'<rect x="{x-70}" y="{y+h}" width="{w+140}" height="12" fill="#b9ab94" stroke="#8d7a5c"/>'
    return out


def label(x, y, w, title, lines, color):
    h = 26 + 14 * len(lines)
    out = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="5" fill="#fff" stroke="{color}" stroke-width="1.6"/>'
    out += f'<rect x="{x}" y="{y}" width="6" height="{h}" fill="{color}"/>'
    out += text(x + 14, y + 17, title, 11, color, anchor="start", weight="bold")
    for i, ln in enumerate(lines):
        out += text(x + 14, y + 33 + 14 * i, ln, 9.3, INK, anchor="start")
    return out


def tres_camadas():
    W, H = 780, 470
    dx, dy, dw, dh = 320, 90, 140, 290
    body = f'<rect width="{W}" height="{H}" fill="#fffdf9"/>'
    body += text(W / 2, 26, "A porta em três operações — proposta de síntese deste estudo", 14, ACC, weight="bold")
    body += door_frame(dx, dy, dw, dh)
    body += f'<rect x="{dx-70}" y="{dy+dh+12}" width="{dw+140}" height="36" fill="#e6dfd0" stroke="{LINE}"/>'
    body += text(dx + dw / 2, dy + dh + 35, "soleira", 10, MUT)
    # marcadores
    body += f'<rect x="{dx+10}" y="{dy-38}" width="{dw-20}" height="20" rx="3" fill="{GOLD}" opacity=".9"/>'
    body += text(dx + dw / 2, dy - 24, "verga: bênção", 9.5, "#fff", weight="bold")
    body += f'<circle cx="{dx-40}" cy="{dy+dh-28}" r="20" fill="{GREEN}" opacity=".85"/>'
    body += text(dx - 40, dy + dh - 24, "planta", 8.5, "#fff", weight="bold")
    body += f'<circle cx="{dx+dw+40}" cy="{dy+60}" r="14" fill="#34495e" opacity=".9"/>'
    body += text(dx + dw + 40, dy + 64, "olho", 8, "#fff", weight="bold")
    body += f'<rect x="{dx+dw-36}" y="{dy+dh-22}" width="26" height="18" rx="3" fill="#2a7f86" opacity=".9"/>'
    body += text(dx + dw - 23, dy + dh - 9, "sal", 8.5, "#fff", weight="bold")
    body += label(14, 80, 222, "1. REPELIR — lado de fora", [
        "Um único guardião, voltado para fora:", "planta (espada-de-são-jorge, arruda,", "guiné) ou amuleto aberto",
        "(hamsa, olho grego)."], "#34495e")
    body += label(14, 250, 222, "2. PURIFICAR — na soleira", [
        "Um gesto repetido, não um objeto:", "sal grosso renovado com regularidade,", "defumação periódica, lavar a soleira.",
        "O que não se renova vira enfeite."], "#2a7f86")
    body += label(544, 80, 222, "3. CONVIDAR — verga e interior", [
        "Uma única bênção, na tradição do", "morador: giz da Epifania na verga,", "mezuzá no umbral (casa judaica),",
        "frase própria. Figa: por dentro."], GOLD)
    body += label(544, 250, 222, "FORA DA SÍNTESE", [
        "Práticas que pedem pertença ou", "consagração: mezuzá em casa não", "judaica, ponto riscado, tronqueira,",
        "ofuda, fulu. E símbolos de ódio."], RED)
    body += text(W / 2, 452, "Síntese proposta pelo estudo a partir de padrões recorrentes; não é prescrição de nenhuma tradição nem promessa de efeito.", 9.3, MUT)
    return svg(W, H, body)


save("tres_camadas.svg", tres_camadas())


# ---------------------------------------------------------------- Mezuzá
def mezuza():
    W, H = 780, 460
    dx, dy, dw, dh = 110, 100, 150, 300
    body = f'<rect width="{W}" height="{H}" fill="#fffdf9"/>'
    body += text(W / 2, 24, "Onde vai a mezuzá — vista de quem ENTRA no cômodo", 14, ACC, weight="bold")
    body += door_frame(dx, dy, dw, dh)
    # terços
    for k in (1, 2):
        yy = dy + dh * k / 3
        body += f'<line x1="{dx-66}" y1="{yy}" x2="{dx+dw+66}" y2="{yy}" stroke="{MUT}" stroke-dasharray="5 4" stroke-width="1"/>'
    body += text(dx - 64, dy + dh / 6 + 4, "terço superior", 9, MUT, anchor="start")
    body += text(dx - 64, dy + dh / 2 + 4, "terço médio", 9, MUT, anchor="start")
    body += text(dx - 64, dy + dh * 5 / 6 + 4, "terço inferior", 9, MUT, anchor="start")
    mx, my = dx + dw + 5, dy + dh / 3 - 36
    body += f'<g><rect x="{mx-5}" y="{my}" width="10" height="38" rx="3" fill="{GOLD}" stroke="{ACC}" stroke-width="1.5"/></g>'
    body += f'<line x1="{mx+12}" y1="{my+14}" x2="{mx+70}" y2="92" stroke="{ACC}" stroke-width="1.2"/>'
    body += text(mx + 60, 70, "umbral DIREITO de quem entra,", 10.5, ACC, anchor="start", weight="bold")
    body += text(mx + 60, 85, "no início do terço superior", 10.5, ACC, anchor="start", weight="bold")
    # três costumes
    bx = 470
    body += text(bx + 140, 150, "Inclinação: a divergência medieval", 12, INK, weight="bold")
    body += text(bx + 140, 332, "Vista lateral do umbral: fora ← | → interior do cômodo", 9.3, INK)
    specs = [(0, "Vertical", "Rashi; Shulchan Aruch;", "costume sefardita"), (22, "Inclinada", "compromisso registrado", "pelo Rema; asquenazita"),
             (-90, "Horizontal", "Rabbenu Tam", "(não é costume atual)")]
    for i, (rot, t, l1, l2) in enumerate(specs):
        cx = bx + 45 + i * 96
        body += f'<rect x="{cx-38}" y="165" width="76" height="150" rx="5" fill="#fff" stroke="{LINE}"/>'
        body += f'<g transform="rotate({rot} {cx} 215)"><rect x="{cx-6}" y="188" width="12" height="54" rx="3" fill="{GOLD}" stroke="{ACC}" stroke-width="1.5"/></g>'
        body += text(cx, 270, t, 10.5, INK, weight="bold")
        body += text(cx, 285, l1, 7.6, MUT) + text(cx, 297, l2, 7.6, MUT)
    body += text(bx + 140, 348, "Na posição inclinada, o topo aponta para dentro do cômodo.", 9.3, MUT)
    body += text(W / 2, 446, "Mandamento restrito a lares judaicos; o esquema é informativo. A norma local é a do rabino de cada comunidade.", 9.3, RED)
    return svg(W, H, body)


save("mezuza.svg", mezuza())


# ---------------------------------------------------------------- Leões guardiões
def leoes():
    W, H = 780, 360
    body = f'<rect width="{W}" height="{H}" fill="#fffdf9"/>'
    body += text(W / 2, 26, "Leões guardiões chineses — vista de cima (planta)", 14, ACC, weight="bold")
    body += f'<rect x="150" y="60" width="480" height="110" fill="#efe7d8" stroke="{LINE}"/>'
    body += text(390, 105, "INTERIOR DO EDIFÍCIO", 11, MUT, weight="bold")
    body += f'<rect x="340" y="160" width="100" height="14" fill="#7b5a3a"/>'
    body += text(390, 152, "porta", 10, MUT)
    for cx, col, t1, t2, t3 in ((270, BLUE, "FÊMEA", "pata sobre o filhote", "(yin)"), (510, RED, "MACHO", "pata sobre a bola", "(yang)")):
        body += f'<circle cx="{cx}" cy="215" r="30" fill="{col}" opacity=".88"/>'
        body += text(cx, 220, t1, 10.5, "#fff", weight="bold")
        body += text(cx, 262, t2, 9.5, INK) + text(cx, 276, t3, 9.5, MUT)
    body += f'<path d="M390 330 L390 195" stroke="{INK}" stroke-width="2" marker-end="url(#a)"/>'
    body += f'<defs><marker id="a" markerWidth="10" markerHeight="10" refX="5" refY="5" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="{INK}"/></marker></defs>'
    body += text(390, 348, "observador do lado de FORA, olhando para a entrada", 10.5, INK, weight="bold")
    body += text(270, 300, "à ESQUERDA de quem olha de fora", 9.3, MUT)
    body += text(510, 300, "à DIREITA de quem olha de fora", 9.3, MUT)
    return svg(W, H, body)


save("leoes.svg", leoes())


# ---------------------------------------------------------------- 72 Nomes
def nomes72():
    W, H = 780, 300
    body = f'<rect width="{W}" height="{H}" fill="#fffdf9"/>'
    body += text(W / 2, 26, "Como se formam os 72 trigramas a partir de Êxodo 14:19–21", 14, ACC, weight="bold")
    rows = [("Versículo 19", "72 letras, lidas na ordem normal", "1ª  2ª  3ª  …  72ª", "→", GREEN),
            ("Versículo 20", "72 letras, lidas de trás para frente", "72ª  71ª  70ª  …  1ª", "←", RED),
            ("Versículo 21", "72 letras, lidas na ordem normal", "1ª  2ª  3ª  …  72ª", "→", BLUE)]
    for i, (v, d, seq, arrow, col) in enumerate(rows):
        y = 55 + i * 58
        body += f'<rect x="30" y="{y}" width="720" height="46" rx="5" fill="#fff" stroke="{col}" stroke-width="1.5"/>'
        body += f'<rect x="30" y="{y}" width="8" height="46" fill="{col}"/>'
        body += text(52, y + 20, v, 12, col, anchor="start", weight="bold")
        body += text(52, y + 36, d, 9.5, MUT, anchor="start")
        body += text(520, y + 28, seq, 12, INK, weight="bold")
        body += text(700, y + 31, arrow, 22, col, weight="bold")
    body += f'<rect x="330" y="48" width="56" height="176" rx="6" fill="none" stroke="{GOLD}" stroke-width="2.5" stroke-dasharray="6 4"/>'
    body += text(358, 246, "cada coluna = 1 nome de 3 letras", 10.5, GOLD, weight="bold")
    body += text(W / 2, 272, "Nome n = (letra n do v. 19) + (letra n contada do fim do v. 20) + (letra n do v. 21). Total: 72 nomes, 216 letras.", 10, INK)
    body += text(W / 2, 290, "O método é medieval e atestado; a tabela “um nome, uma função” é moderna.", 9.5, MUT)
    return svg(W, H, body)


save("nomes72.svg", nomes72())
print("diagramas:", sorted(os.listdir(OUT)))
