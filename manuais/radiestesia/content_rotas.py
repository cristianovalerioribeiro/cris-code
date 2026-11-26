# -*- coding: utf-8 -*-
"""Edição 8 final: fluxo mestre deitado em largura total, bifurcações em cartões com miniatura, caminhos completos, fichas de teorias.
Dados: routes.py (ROUTES, CAMINHOS, DECISOES) e teorias.py (TEORIAS, GLOSSARIO)."""
import os, re
from bookkit import *
from bookkit import _links_in, _mini_svg, ANCHOR_LABELS
try:
    from routes import CAMINHOS, DECISOES
except Exception:
    CAMINHOS, DECISOES = [], []
try:
    from teorias import TEORIAS, GLOSSARIO
except Exception:
    TEORIAS, GLOSSARIO = [], []

HERE = os.path.dirname(os.path.abspath(__file__))
ACC = "#1f4e8c"; AMBER = "#b58900"

def fluxo_svg():
    """Fluxo mestre em duas faixas: largura de cada caixa calculada pelo conteúdo; decisões em losango com as saídas
    rotuladas sobre as linhas; retornos tracejados em faixas próprias (sem cruzar caixas)."""
    W = 275.0; GAP = 3.0; DW = 30.0; FS = 2.35; CH = 4.1; TF = 2.9
    def chip_w(t): return FS * 0.56 * len(t) + 3.4
    def pack(cs, wbox):
        x = 0.0; rows = 1
        for c in cs:
            w = chip_w(c)
            if x > 0 and x + w > wbox - 4.4: rows += 1; x = 0.0
            x += w + 1.4
        return rows
    def need_w(title, cs, target):
        lo = max(max(chip_w(c) for c in cs), TF * 0.56 * len(title)) + 4.4
        w = lo
        while pack(cs, w) > target and w < 160: w += 0.5
        return w
    R1 = [("box", "Abertura", ["G1 convenção", "trio de permissão", "pergunta escrita", "testemunho"], 2, "#eef2f8"),
          ("box", "Nível 1 · Triagem", ["G3 vitalidade", "G2 + G5 campos", "G6 aura", "G4 polaridade", "G24 áreas"], 3, "#eef2f8"),
          ("dec", "Limpar|antes?", None, None, None),
          ("box", "Pré-ciclo (se a triagem pedir)", ["G15 interferência", "G28 origem", "G16 ambiente", "G25 posição", "G22 técnica", "G23 tempo"], 3, "#f3f9f3"),
          ("box", "Nível 2 · Sete chakras", ["G5 qual chakra", "G2 % de cada um", "G7 forma", "G6 silhueta", "G29 secundários"], 3, "#eef2f8"),
          ("dec", "Algum chakra|abaixo de 70?", None, None, None)]
    R2 = [("box", "Nível 3 · Capítulo do chakra (G8)", ["C·sinais do chakra", "G8 biômetro de causas", "1 Emocional → C·emoções, G9", "2 Mental → G10, G55", "3 Física → C·corpo, G12", "4 Energética → G15, G60", "5 Ambiental → G16, G82", "6 Linhagem → G17, G36", "7 Espiritual → G18, G34", "8 Outro → nomear"], 5, "#eef2f8"),
          ("box", "Nível 4 · Decodificação", ["G19 origem", "G35 época", "G21 contexto", "G36 pessoa", "G61 evento", "G62 ganho", "G58 sustenta", "G60 corpo sutil"], 4, "#eef2f8"),
          ("box", "Nível 5 · Harmonização", ["G22 técnica", "G41 a G47", "G23 tempo e dose", "afirmação até 80"], 4, "#eef2f8"),
          ("box", "Reavaliação", ["G2 remedir o chakra", "G7 forma de novo"], 2, "#eef2f8"),
          ("dec", "Chakra em|70 ou mais?", None, None, None),
          ("box", "Fechamento", ["seis passos", "devolutiva", "remedida 7 dias", "retorno 21 a 30 dias", "caderno"], 5, "#f3f9f3")]
    WB = W - 4.0  # faixa da direita reservada ao caminho "não → Fechamento"
    def widths(row):
        ws = [DW if k == "dec" else need_w(t, cs, tg) for k, t, cs, tg, _ in row]
        total = sum(ws) + GAP * (len(row) - 1)
        extra = WB - total
        nb = sum(1 for k, *_ in row if k == "box")
        if extra > 0: ws = [w + (extra / nb if k == "box" else 0) for w, (k, *_) in zip(ws, row)]
        else:
            # estourou: encolhe só as caixas na proporção; os chips reorganizam-se em mais linhas
            box_sum = sum(w for w, (k, *_) in zip(ws, row) if k == "box")
            avail = WB - GAP * (len(row) - 1) - DW * (len(row) - nb)
            ws = [w * avail / box_sum if k == "box" else w for w, (k, *_) in zip(ws, row)]
        return ws, extra
    w1, e1 = widths(R1); w2, e2 = widths(R2)
    if min(e1, e2) < 0: FS -= 0.1; CH = 4.0; w1, e1 = widths(R1); w2, e2 = widths(R2)
    def row_h(row, ws):
        h = 0
        for (k, t, cs, tg, _), w in zip(row, ws):
            if k == "box": h = max(h, 6.0 + pack(cs, w) * (CH + 1.1) + 1.6)
        return h
    out = []
    def chips(cs, x0, y0, wbox):
        x, y = x0 + 2.2, y0
        for c in cs:
            w = chip_w(c)
            if x > x0 + 2.2 and x + w > x0 + wbox - 2.2: x = x0 + 2.2; y += CH + 1.1
            out.append(f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{CH}" rx="2.1" fill="white" stroke="{ACC}" stroke-width="0.25"/>'
                       f'<text x="{x + w/2:.1f}" y="{y + CH*0.71:.1f}" font-size="{FS}" text-anchor="middle" fill="#111">{e(c)}</text>')
            x += w + 1.4
    def box(x, y, w, h, title, cs, fill):
        out.append(f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" rx="2" fill="{fill}" stroke="{ACC}" stroke-width="0.35"/>'
                   f'<text x="{x + 2.2:.1f}" y="{y + 4.0:.1f}" font-size="{TF}" font-weight="700" fill="{ACC}">{e(title)}</text>')
        chips(cs, x, y + 6.0, w)
    def diamond(x, y, w, h, q):
        cx, cy = x + w / 2, y + h / 2; hh = min(h, 30) / 2
        out.append(f'<path d="M{cx:.1f} {cy - hh:.1f} L{x + w:.1f} {cy:.1f} L{cx:.1f} {cy + hh:.1f} L{x:.1f} {cy:.1f} Z" fill="#fff6d9" stroke="{AMBER}" stroke-width="0.4"/>')
        lines = q.split("|")
        for i, ln in enumerate(lines):
            out.append(f'<text x="{cx:.1f}" y="{cy + 1.0 + (i - (len(lines) - 1) / 2) * 3.4:.1f}" font-size="2.7" font-weight="700" text-anchor="middle" fill="#111">{e(ln)}</text>')
        return cx, cy, hh
    def arrow_h(x0, x1, y, color=ACC, dash=""):
        d = -1 if x1 < x0 else 1
        out.append(f'<line x1="{x0:.1f}" y1="{y:.1f}" x2="{x1 - 1.6*d:.1f}" y2="{y:.1f}" stroke="{color}" stroke-width="0.4" {dash}/>'
                   f'<path d="M{x1 - 1.9*d:.1f} {y - 1.3:.1f} L{x1:.1f} {y:.1f} L{x1 - 1.9*d:.1f} {y + 1.3:.1f} Z" fill="{color}"/>')
    def head_v(x, y, color, up=False):
        s = -1 if up else 1
        out.append(f'<path d="M{x - 1.3:.1f} {y - 1.9*s:.1f} L{x:.1f} {y:.1f} L{x + 1.3:.1f} {y - 1.9*s:.1f} Z" fill="{color}"/>')
    def path(pts, color, dash=False, hop_at=None):
        d = f"M{pts[0][0]:.1f} {pts[0][1]:.1f}"
        for (x, y) in pts[1:]:
            d += f" L{x:.1f} {y:.1f}"
        out.append(f'<path d="{d}" fill="none" stroke="{color}" stroke-width="0.4"' + (' stroke-dasharray="1.5 1.0"' if dash else "") + '/>')
    def label(x, y, t, color, anchor="middle"):
        out.append(f'<text x="{x:.1f}" y="{y:.1f}" font-size="2.3" text-anchor="{anchor}" fill="{color}">{e(t)}</text>')
    GREEN, RED = "#2e7d32", "#c62828"
    y_lane0 = 4.0; y1 = 8.0
    H1 = row_h(R1, w1); row1_bottom = y1 + H1
    laneB = row1_bottom + 4.5; laneA = row1_bottom + 9.0; y2 = row1_bottom + 13.5
    H2 = row_h(R2, w2); row2_bottom = y2 + H2; laneC = row2_bottom + 4.5
    # posições
    def place(row, ws, y, H):
        xs = []; x = 0.0
        for (k, t, cs, tg, fill), w in zip(row, ws):
            xs.append((x, w)); x += w + GAP
        return xs
    X1 = place(R1, w1, y1, H1); X2 = place(R2, w2, y2, H2)
    C = {}
    for (k, t, cs, tg, fill), (x, w) in zip(R1, X1):
        if k == "box": box(x, y1, w, H1, t, cs, fill); C[t] = (x, w, y1, H1)
        else: C[t] = diamond(x, y1, w, H1, t) + (x, w)
    for (k, t, cs, tg, fill), (x, w) in zip(R2, X2):
        if k == "box": box(x, y2, w, H2, t, cs, fill); C[t] = (x, w, y2, H2)
        else: C[t] = diamond(x, y2, w, H2, t) + (x, w)
    # setas da linha 1 e 2
    m1 = y1 + H1 / 2; m2 = y2 + H2 / 2
    for (xa, wa), (xb, wb) in zip(X1, X1[1:]): arrow_h(xa + wa, xb, m1)
    for (xa, wa), (xb, wb) in zip(X2, X2[1:]): arrow_h(xa + wa, xb, m2)
    # rótulos "sim" nas setas de linha que saem dos losangos
    d1 = C["Limpar|antes?"]; d2 = C["Algum chakra|abaixo de 70?"]; d3 = C["Chakra em|70 ou mais?"]
    label(d1[3] + d1[4] + 0.3, m1 - 2.4, "sim", GREEN, anchor="start"); label(d3[3] + d3[4] + 0.3, m2 - 2.4, "sim", GREEN, anchor="start")
    # D1 não → Nível 2 (faixa de cima)
    n2 = C["Nível 2 · Sete chakras"]; n2cx = n2[0] + n2[1] / 2
    path([(d1[0], d1[1] - d1[2]), (d1[0], y_lane0), (n2cx, y_lane0), (n2cx, y1 - 0.2)], RED); head_v(n2cx, y1, RED)
    label((d1[0] + n2cx) / 2, y_lane0 - 0.9, "não: vai direto ao Nível 2", RED)
    # D2 sim → Nível 3 (faixa A)
    n3 = C["Nível 3 · Capítulo do chakra (G8)"]; n3cx = n3[0] + n3[1] / 2
    path([(d2[0], d2[1] + d2[2]), (d2[0], laneA), (n3cx, laneA), (n3cx, y2 - 0.2)], GREEN); head_v(n3cx, y2, GREEN)
    label((d2[0] + n3cx) / 2, laneA + 3.0, "sim: abre o capítulo do chakra prioritário (Nível 3)", GREEN)
    # D2 não → Fechamento (faixa da direita)
    fe = C["Fechamento"]; xr = W - 1.2
    path([(d2[3] + d2[4], d2[1]), (xr, d2[1]), (xr, m2), (fe[0] + fe[1] + 0.2, m2)], RED); 
    out.append(f'<path d="M{fe[0] + fe[1] + 1.9:.1f} {m2 - 1.3:.1f} L{fe[0] + fe[1]:.1f} {m2:.1f} L{fe[0] + fe[1] + 1.9:.1f} {m2 + 1.3:.1f} Z" fill="{RED}"/>')
    label(xr - 1.2, laneA + 0.8, "não: Fechamento", RED, anchor="end")
    # D3 sim e há tempo → Nível 2 (faixa B, tracejada), com salto onde cruza a faixa A
    xv = d3[0]; xin = n2cx + 10
    out.append(f'<path d="M{xv:.1f} {d3[1] - d3[2]:.1f} V{laneA + 1.6:.1f} A1.6 1.6 0 0 1 {xv:.1f} {laneA - 1.6:.1f} V{laneB:.1f} H{xin:.1f} V{row1_bottom + 0.2:.1f}" fill="none" stroke="{AMBER}" stroke-width="0.4" stroke-dasharray="1.5 1.0"/>')
    head_v(xin, row1_bottom, AMBER, up=True)
    label((xv + xin) / 2, laneB - 0.9, "sim, e há tempo: próximo chakra fora da faixa (volta ao Nível 2)", "#7a5c00")
    # D3 não → G8 (faixa C, tracejada)
    xg = n3cx + 12
    out.append(f'<path d="M{xv:.1f} {d3[1] + d3[2]:.1f} V{laneC:.1f} H{xg:.1f} V{row2_bottom + 0.2:.1f}" fill="none" stroke="{AMBER}" stroke-width="0.4" stroke-dasharray="1.5 1.0"/>')
    head_v(xg, row2_bottom, AMBER, up=True)
    label((xv + xg) / 2, laneC + 3.0, "não: outra causa no mesmo chakra (volta ao G8)", "#7a5c00")
    # legenda
    yl = laneC + 7.5
    out.append(f'<line x1="0" y1="{yl:.1f}" x2="8" y2="{yl:.1f}" stroke="{ACC}" stroke-width="0.4"/><text x="10" y="{yl + 0.9:.1f}" font-size="2.3" fill="#333">segue</text>'
               f'<line x1="24" y1="{yl:.1f}" x2="32" y2="{yl:.1f}" stroke="{AMBER}" stroke-width="0.4" stroke-dasharray="1.5 1.0"/><text x="34" y="{yl + 0.9:.1f}" font-size="2.3" fill="#333">retorno</text>'
               f'<text x="52" y="{yl + 0.9:.1f}" font-size="2.3" fill="{GREEN}">verde: sim</text><text x="70" y="{yl + 0.9:.1f}" font-size="2.3" fill="{RED}">vermelho: não</text>'
               f'<text x="96" y="{yl + 0.9:.1f}" font-size="2.3" fill="#333">cada ficha é um gráfico; a interpretação e a rota estão no bloco do gráfico</text>')
    Htot = yl + 4
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W + 2}mm" height="{Htot:.1f}mm" viewBox="-1 0 {W + 2} {Htot:.1f}" font-family="Inter, DejaVu Sans, sans-serif">'
           + "".join(out) + "</svg>")
    path_ = os.path.join(HERE, "figs", "fluxo_mestre.svg")
    open(path_, "w", encoding="utf-8").write(svg)
    return path_

def mapa_topo(rows):
    """Fluxo em largura total; abaixo, em duas colunas, a tabela de etapas, as quatro decisões e como ler."""
    fluxo_svg()
    fig = span('<figure class="pic flow"><img src="figs/fluxo_mestre.svg" alt="Fluxo mestre"/><figcaption>Fluxo mestre: nove etapas, três decisões (losangos) e dois retornos. As demais ramificações estão nos cartões de bifurcação e dentro de cada gráfico.</figcaption></figure>')
    t = table(["Etapa", "Capítulo", "Gráficos"], rows, cls="small")
    return fig

def _thumb(onde):
    m = re.search(r"G\d{1,3}b?|C[1-7]-(?:sinais|emocoes|corpo)", onde)
    if m and m.group(0) in MANIFEST and MANIFEST[m.group(0)]["kind"] not in ("lista", "barômetro"):
        cid = m.group(0); return f'<a href="#fig-{cid}"><img class="thumb" src="{_mini_svg(cid)}" alt="{cid}"/></a>'
    return ""

def mapa_rotas():
    H = []
    if DECISOES:
        H.append(h2("rotas-decisoes", "As bifurcações: se der isto, vá para"))
        H.append(p("Cada cartão é um ponto em que o resultado muda o caminho. A miniatura mostra o gráfico (só setores e números; os nomes estão no gráfico impresso e no bloco do gráfico). A coluna da direita diz o gráfico ou a parte a abrir, com a página."))
        for nd, (onde, perg, res) in enumerate(DECISOES, 1):
            th = _thumb(onde)
            rows = ""
            for r in res:
                r_res, r_dest, r_obs = (list(r) + ["", ""])[:3]
                rows += f"<tr><td>{e(r_res)}</td><td>{dest(r_dest)}" + ((" · " + _links_in(r_obs)) if r_obs else "") + "</td></tr>"
            head = f'<div class="dhead">{th}<div class="dtxt"><div class="did">D{nd} · {e(onde)}</div><div class="q">{e(perg)}</div></div></div>'
            H.append(f'<div class="dcard" id="D{nd}">{head}<table class="small"><thead><tr><th>Se der</th><th>Vá para</th></tr></thead><tbody>{rows}</tbody></table></div>')
    return "".join(H)

def _hum(t):
    """Troca ids genéricos de chakra por texto legível nas fichas e no glossário."""
    return re.sub(r"C\{k\}-(sinais|emocoes|corpo)", lambda m: "C·" + {"sinais": "sinais", "emocoes": "emoções", "corpo": "corpo"}[m.group(1)] + " do chakra", str(t))

def teorias_cap():
    """Edição 10: dos apêndices fica só o glossário, emendado ao fim da última Parte."""
    if not GLOSSARIO: return ""
    H = [h1("glossario", "Glossário", "Termos usados no manual", brk=False)]
    H.append(cols3('<div class="gloss">' + "".join(f"<p><b>{e(a)}</b> — {e(_hum(b))}</p>" for a, b in GLOSSARIO) + "</div>"))
    H.append(end())
    return "".join(H)
