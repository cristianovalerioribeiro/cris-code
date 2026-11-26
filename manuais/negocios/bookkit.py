# -*- coding: utf-8 -*-
"""Utilitários de montagem do manual (HTML para WeasyPrint). Edição 8 final: A4 deitado, blocos de gráfico, listas em tabela, pares, rotas e trilhas."""
import html, json, os, re, math, glob

HERE = os.path.dirname(os.path.abspath(__file__))
MANIFEST = {m["id"]: m for m in json.load(open(os.path.join(HERE, "charts", "manifest.json"), encoding="utf-8"))}
TOC = []  # (id, title, level)
try:
    from routes import ROUTES
except Exception:
    ROUTES = {}

ANCHOR_LABELS = {
    "p1": "Parte I · Fundamentos", "p1-material": "Material e convenção", "p1-abertura": "Abertura e permissão", "p1-testemunho": "Testemunho",
    "p1-etica": "Ética", "encaminhar": "Quando encaminhar", "p1-higiene": "Higiene de decisão", "p1-leitura": "Leitura dos gráficos",
    "dec": "Parte II · Decisão", "dec-regras": "Regras do operador", "dec-roteiro": "Roteiro da decisão", "dec-alternativas": "Alternativas", "dec-calendario": "Calendário", "dec-trava": "O que trava",
    "neg": "Parte III · A empresa", "neg-360": "Diagnóstico 360", "neg-modelo": "Modelo de negócio", "neg-fase": "Fase do negócio", "neg-plano": "Planejamento anual",
    "soc": "Parte IV · Sociedade", "soc-roteiro": "Roteiro da sociedade", "soc-criterios": "Critérios de sociedade", "soc-ciclo": "Ciclo da sociedade",
    "prop": "Parte V · Propostas", "prop-roteiro": "Roteiro da proposta", "prop-pontos": "Pontos de atenção", "prop-trava": "Onde trava a negociação",
    "proj": "Parte VI · Projetos", "proj-roteiro": "Roteiro do projeto", "proj-premortem": "Pré-mortem", "proj-preco": "Preço e opções",
    "eq": "Parte VII · Pessoas", "eq-equipe": "Equipe como conjunto", "eq-profissional": "O que pesa no trabalho", "eq-talentos": "Talentos",
    "blo": "Parte VIII · Interferências", "blo-triagem": "Triagem da interferência",
    "esp": "Parte IX · Espaços e imóveis", "esp-ponto": "Ponto comercial", "esp-medir": "Imóvel cômodo a cômodo", "esp-planta": "Planta quadriculada", "esp-limpar": "Limpar e proteger", "esp-terreno": "Terreno", "esp-empreendimento": "Empreendimento", "esp-laudo": "Laudo complementar",
    "fin": "Parte X · Finanças", "fin-bloqueio": "Bloqueio de prosperidade", "fin-emissores": "Emissores",
    "pes": "Parte XI · A pessoa", "pes-roda": "Roda da Vida", "pes-remissao": "Quando encaminhar a pessoa",
    "reg": "Parte XII · Registro", "reg-diario": "Diário de decisões", "reg-revisao": "Revisão", "reg-fichas": "Fichas",
    "estr": "Parte XIII · Estratégia", "estr-seletor": "Seletor de ferramentas", "estr-carteira": "Carteira de projetos e tempo", "estr-swot": "SWOT", "estr-funil": "Funil de vendas", "estr-abordagem": "Abordagem e expectativas", "estr-atores": "Mapa de atores e investidores", "estr-caminhos": "Abrir caminhos: o que se faz", "estr-lider": "Roda do líder",
    "coach": "Parte XII · Coaching", "coach-rodas": "Rodas de 1 a 10", "coach-foco": "Foco e prioridade", "coach-metas": "Valores e metas", "coach-sabotadores": "Sabotadores", "coach-desbloqueio": "Protocolo de desbloqueio", "coach-casos": "Casos de coaching",
    "mapa": "Mapa do método", "glossario": "Glossário", "como-usar": "Como usar",
}
PAGE_W = 275.5  # largura útil da página A4 deitada, em mm (297 − 10 − 11,5)
SPAN0, SPAN1 = "<!--SPAN-->", "<!--/SPAN-->"

def _anchor_titles():
    t = {}
    for fn in glob.glob(os.path.join(HERE, "content_*.py")):
        if "_v" in os.path.basename(fn): continue
        src = open(fn, encoding="utf-8").read()
        for m in re.finditer(r'h[12]\(\s*f?"([^"]+)"\s*,\s*"([^"]+)"', src):
            t.setdefault(m.group(1), m.group(2))
    return t
ANCHOR_TITLES = _anchor_titles()
def _short(t, n=36):
    t = re.sub(r"^(Passo \d+[a-z]? · |Nível \d · |Apêndice [A-D] · )", "", t)
    t = re.sub(r"\s*\([^)]*\)", "", t).strip()
    return t if len(t) <= n else t[:n].rsplit(" ", 1)[0]
ID_RE = re.compile(r"^(G\d{1,3}b?|C[1-7]-(?:sinais|emocoes|corpo))$")
ROMAN = {"I": 1, "II": 2, "III": 3, "IV": 4, "V": 5, "VI": 6, "VII": 7, "VIII": 8, "IX": 9, "X": 10, "XI": 11, "XII": 12, "XIII": 13, "XIV": 14, "XV": 15, "XVI": 16}
# grupos de páginas (aba colorida na margem): partes que correm emendadas ficam no mesmo grupo
def page_group(part):
    if not part: return "g0"
    m = re.match(r"Parte ([IVX]+)", part)
    if not m: return "g5" if (part.startswith("Apêndice") or part.startswith("Termos")) else "g0"
    n = ROMAN[m.group(1)]
    return "g0" if n <= 3 else ("g4" if n <= 8 else "g5")

SHORT = {"p1": "Fundamentos para quem decide", "dec": "A decisão do dono", "neg": "A empresa como um todo", "soc": "Sócios, parceiros e investidores",
         "prop": "Propostas, contratos, clientes", "proj": "Projetos, produtos e preços", "eq": "Pessoas, equipe e liderança", "blo": "Interferências e bloqueios",
         "esp": "Espaço, ponto, terreno e empreendimento", "fin": "Finanças e prosperidade", "pes": "O empreendedor como pessoa", "reg": "Registro e calibração", "coach": "Coaching: rodas, foco, metas e desbloqueio", "estr": "Estratégia, carteira e relações-chave"}
TAB_LABEL = {"g0": "I–III", "g4": "IV–VIII", "g5": "IX–XIV"}
FALLBACK = {}
TEXTFIRST = set()  # blocos cujo texto vai antes do desenho (o desenho fica na página seguinte)
TAIL_REAL = {}  # id → cauda real na página anterior (sem descontar o título colado), para decidir o texto-antes
LABEL_FLOOR_PT = 5.0  # menor rótulo admitido ao encolher um desenho (pt)
TF_TAIL = {}  # id → mm livres depois do texto de um bloco texto-antes cujo desenho ainda saltou (escala calculada na montagem)  # id (primeiro gráfico do bloco) → mm livres na página anterior, quando o bloco saltou de página na passagem anterior

def e(s):
    return html.escape(str(s), quote=False)

def span(html_):
    """Bloco de largura total (fora das duas colunas)."""
    return SPAN0 + html_ + SPAN1

def h1(id_, title, part=None, brk=True):
    """brk=False: o capítulo segue na mesma página (sem quebra)."""
    TOC.append((id_, title, 1))
    kicker = f'<div class="kicker">{e(part)}</div>' if part else ""
    cls = "chapter " + page_group(part) + ("" if brk else " flow")
    short = SHORT.get(id_) or title.split(":")[0].strip()
    if len(short) > 44: short = short[:44].rsplit(" ", 1)[0]
    g = page_group(part)
    tab = f'<div class="tab {g}">{TAB_LABEL.get(g, "")}</div>'
    return f'<section class="{cls}" id="{id_}">{tab}{kicker}<h1 data-short="{e(short)}">{e(title)}</h1>'

def end():
    return "</section>"

def h2(id_, title, toc=True):
    if toc: TOC.append((id_, title, 2))
    return f'<h2 id="{id_}">{e(title)}</h2>'

def h3(title, id_=None):
    return f'<h3 id="{id_}">{e(title)}</h3>' if id_ else f'<h3>{e(title)}</h3>'

def p(text):
    return f'<p>{text}</p>'

def go(id_, label=None):
    label = "vá para" if label is None else label
    return f'<a class="go" href="#{id_}">{e(label)}</a>'

def goD(n, label=None):
    """Remissão a um cartão de bifurcação."""
    return f'<b>▶</b> <a class="go" href="#D{n}">{e(label or f"cartão D{n}")}</a>'

def dest(d, k=None, label=None):
    """Destino de rota: id de gráfico, 'C{k}-x' (chakra corrente) ou âncora de seção → link com página."""
    d = str(d).strip()
    if "{k}" in d:
        if k: d = d.replace("{k}", str(k))
        else:
            nome = {"sinais": "sinais", "emocoes": "emoções", "corpo": "corpo"}.get(d.split("-")[-1], d)
            return f'<a class="go" href="#ch-roteiro">{e(label or ("C·" + nome + " do chakra"))}</a>'
    if d in MANIFEST:
        return f'<a class="go" href="#fig-{d}">{e(label or d)}</a>'
    return f'<a class="go" href="#{d}">{e(label or ANCHOR_LABELS.get(d) or _short(ANCHOR_TITLES.get(d, d)))}</a>'

def _links_in(text, k=None):
    def rep(m):
        cid = m.group(0).replace("{k}", str(k)) if k else m.group(0)
        if cid in MANIFEST: return f'<a href="#fig-{cid}">{cid}</a>'
        return m.group(0)
    return re.sub(r"\bG\d{1,3}b?\b|\bC(?:\{k\}|[1-7])-(?:sinais|emocoes|corpo)\b", rep, e(text))

def steps(items, start=1):
    lis = "".join(f"<li>{it}</li>" for it in items)
    return f'<ol class="steps" start="{start}">{lis}</ol>'

def ul(items):
    return "<ul>" + "".join(f"<li>{it}</li>" for it in items) + "</ul>"

def table(headers, rows, cls=""):
    th = "".join(f"<th>{h}</th>" for h in headers)
    trs = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows)
    return f'<table class="{cls}"><thead><tr>{th}</tr></thead><tbody>{trs}</tbody></table>'

def box(kind, title, text):
    return f'<div class="box {kind}"><div class="box-title">{e(title)}</div><div>{text}</div></div>'

def pergunta(texto):
    return f'<div class="pergunta">“{e(texto)}”</div>'

def short_title(cid, n=30):
    t = re.sub(r"\s*\([^)]*\)", "", MANIFEST[cid]["title"]).strip()
    if len(t) > n: t = t[:n].rsplit(" ", 1)[0]
    return t

def _cut(label, n):
    label = str(label).strip()
    return label if len(label) <= n else label[:n].rsplit(" ", 1)[0]

def trilha(items, title="Sequência"):
    """Faixa de etapas: [(id ou âncora, rótulo curto), ...] → fichas ligadas por setas, com página."""
    chips = []
    dense = len(items) > 10
    for d, label in items:
        d = str(d)
        label = _cut(label, 20)
        if d in MANIFEST: chips.append(f'<a class="chip" href="#fig-{d}"><b>{e(d)}</b> {e(label)}</a>')
        elif "{k}" in d:
            nome = {"sinais": "sinais", "emocoes": "emoções", "corpo": "corpo"}.get(d.split("-")[-1], "")
            chips.append(f'<a class="chip" href="#ch-roteiro"><b>C·{e(nome)}</b> do chakra</a>')
        else: chips.append(f'<a class="chip" href="#{d}">{e(label)}</a>')
    return span(f'<div class="trilha">' + '<span class="arrow">›</span>'.join(chips) + '</div>')

_SVGH = {}
def _svg_height(fn):
    if fn not in _SVGH:
        src = open(os.path.join(HERE, "charts", fn), encoding="utf-8").read(400)
        mm = re.search(r'height="([\d.]+)mm"', src); _SVGH[fn] = float(mm.group(1)) if mm else 117.0
    return _SVGH[fn]

_LISTS = {}
def _list_entries(cid):
    """Lê a lista pendulável do SVG: [("H", título, cor) | ("I", texto, cor)], na ordem de leitura."""
    if cid in _LISTS: return _LISTS[cid]
    svg = open(os.path.join(HERE, "charts", MANIFEST[cid]["file"]), encoding="utf-8").read()
    out = []; color = None; pending_num = None
    for m in re.finditer(r'<rect[^>]*fill="(#[0-9a-fA-F]{6})"[^>]*/>|<text([^>]*)>([^<]*)</text>', svg):
        if m.group(1): color = m.group(1); continue
        attrs, txt = m.group(2), html.unescape(m.group(3)).strip()
        bold = 'font-weight="700"' in attrs
        if bold and txt.isdigit(): pending_num = txt; continue
        if bold: out.append(("H", txt, color)); continue
        if txt: out.append(("I", txt, color)); pending_num = None
    _LISTS[cid] = out
    return out

def _mini_svg(cid):
    """Miniatura sem texto (só setores e marcas), para cartões de bifurcação e cabeçalho das listas."""
    src = os.path.join(HERE, "charts", MANIFEST[cid]["file"]); dst_dir = os.path.join(HERE, "charts_mini"); os.makedirs(dst_dir, exist_ok=True)
    dst = os.path.join(dst_dir, MANIFEST[cid]["file"])
    if not os.path.exists(dst):
        svg = open(src, encoding="utf-8").read()
        svg = re.sub(r"<text[^>]*>[^<]*</text>", "", svg)
        open(dst, "w", encoding="utf-8").write(svg)
    return "charts_mini/" + MANIFEST[cid]["file"]

def _k_of(cid):
    m = re.match(r"^C([1-7])-", cid)
    return m.group(1) if m else None

def _head(cid, cap):
    cls = "chart-title long" if len(cap) > 40 else "chart-title"
    return f'<div class="chart-head"><span class="chart-id">{e(cid)}</span><span class="{cls}">{e(cap)}</span></div>'

def _interp_parts(cid):
    """Peças da interpretação: lado (serve, pergunta, leitura, rota, base) e linhas de resultado com destino."""
    from interp import INTERP
    it = INTERP.get(cid)
    if not it: return None
    r = ROUTES.get(cid); k = _k_of(cid)
    perg = it.get("pergunta")
    if isinstance(perg, str): perg = [perg]
    vai = list(r.get("vai") or []) if r else []
    rows = []
    norm = lambda t: re.sub(r"^[\d\s·.:\-–]+", "", str(t).strip().lower())[:14]
    prev_f = ""
    for i, (res, sg, f) in enumerate(it["res"]):
        if f.lower().startswith("idem") and prev_f:
            head = prev_f.rsplit(";", 1)[0] if prev_f.count(";") >= 1 else prev_f
            f = head + f[4:]
        prev_f = f
        extra = ""
        if vai:
            match = next((v for v in vai if norm(v[0]) == norm(res)), None)
            if match is None and len(vai) == len(it["res"]): match = vai[i]
            if match:
                d = match[1]; comp = match[2] if len(match) > 2 else ""
                toks = [t for t in re.findall(r"\w+", comp.lower()) if len(t) > 3]
                if toks and sum(t in f.lower() for t in toks) / len(toks) >= 0.6: comp = ""
                extra = ' <span class="vai">▶ ' + dest(d, k) + (" · " + _links_in(comp, k) if comp else "") + '</span>'
        rows.append((res, sg, f, f"<tr><td>{e(res)}</td><td>{e(sg)}</td><td>{e(f)}{extra}</td></tr>"))
    rota = ""
    if r:
        partes = []
        if r.get("etapa"): partes.append(f'<b>Etapa.</b> {e(r["etapa"])}')
        if r.get("vem"):
            vem = list(r["vem"]); extra = " e outros" if len(vem) > 5 else ""
            partes.append("<b>Vem de.</b> " + ", ".join(dest(v, k) for v in vem[:5]) + extra)
        if r.get("nota"): partes.append(f'<b>Atenção.</b> {e(r["nota"])}')
        rota = '<p class="rota">' + " &nbsp;·&nbsp; ".join(partes) + "</p>"
    lado = (f'<p><b>Para que serve.</b> {e(it["serve"])}</p>'
            + (('<p><b>Pergunta.</b> ' + " ".join(f"<span class=\"q\">“{e(q)}”</span>" for q in perg) + '</p>') if perg else "")
            + (f'<p><b>Como ler.</b> {e(it["leitura"])}</p>' if it.get("leitura") else "")
            + rota)
    base = ""
    inline = '<p class="res1">' + " &nbsp;·&nbsp; ".join(f"<b>{e(res)}</b>: {e(f)}" + (re.search(r'(<span class="vai">.*?</span>)', row, re.S).group(1) if 'class="vai"' in row else "") for res, sg, f, row in rows) + "</p>"
    top_text = [it["serve"], " ".join(perg or []), it.get("leitura") or "", (r.get("etapa", "") + " ".join(r.get("vem") or []) + r.get("nota", "")) if r else ""]
    return dict(it=it, rows=rows, lado=lado, base=base, top_text=top_text, inline=inline)

LEGEND_HEAD = '<table class="legend"><thead><tr><th>Resultado</th><th>O que significa</th><th>O que fazer · vá para</th></tr></thead><tbody>'

def _split_rows(P, chart_h, right_w):
    """Quantas linhas de resultado cabem ao lado do desenho (estimativa por caracteres a 7,5 pt)."""
    cpl = right_w / 1.42
    top_h = 5 + sum(math.ceil(len(t) / cpl) * 3.15 + 2.0 for t in P["top_text"] if t)
    avail = chart_h - top_h - 4
    widths = [right_w * 0.20, right_w * 0.36, right_w * 0.44]
    n = 0; acc = 0.0
    for res, sg, f, row in P["rows"]:
        extra = len(re.sub("<.*?>", "", row.split("</td><td>")[-1])) - len(f)
        lines = max(math.ceil(len(res) / (widths[0] / 1.42)), math.ceil(len(sg) / (widths[1] / 1.42)), math.ceil((len(f) + max(extra, 0)) / (widths[2] / 1.42)))
        h = lines * 3.1 + 1.8
        if acc + h <= avail + (3.0 if n == 0 else 0): acc += h; n += 1
        else: break
    total = len(P["rows"])
    if total - n <= 2: n = total            # sobra de até duas: sobe para o lado
    if n and n < total / 3 and total - n >= 6: n = 0   # menos de um terço ao lado: tudo embaixo, inteiro
    return n

_MINF = {}
def _min_font(cid):
    """Menor corpo de rótulo (mm) no SVG: rótulos radiais quando existem, senão qualquer texto."""
    if cid not in _MINF:
        svg = open(os.path.join(HERE, "charts", MANIFEST[cid]["file"]), encoding="utf-8").read()
        rot = [float(x) for x in re.findall(r'<text[^>]*font-size="([\d.]+)"[^>]*transform="rotate', svg)]
        allf = [float(x) for x in re.findall(r'font-size="([\d.]+)"', svg)]
        _MINF[cid] = min(rot) if rot else (min(allf) if allf else 3.4)
    return _MINF[cid]

TARGET_PT = 6.2
MAX_DRAW_H = 140.0  # altura máxima de um desenho na página (mm)
def need_frac(cid):
    """Fração da largura útil para o menor rótulo chegar a TARGET_PT."""
    return TARGET_PT / 2.835 / _min_font(cid) * 190.0 / PAGE_W

def _fmax_h(cid):
    return (MAX_DRAW_H - 7) / (_svg_height(MANIFEST[cid]["file"]) / 190.0) / PAGE_W

def _frac_single(cid):
    return round(min(max(0.46, min(0.60, need_frac(cid))), _fmax_h(cid), 0.60), 3)

def _est_h(html_, width_mm):
    """Altura estimada (mm) de um trecho HTML numa coluna de largura dada, a 7,5 pt."""
    if not html_: return 0.0
    cpl = max(width_mm, 20) / 1.42; h = 0.0
    for tbl in re.findall(r"<table.*?</table>", html_, re.S):
        rows = re.findall(r"<tr>(.*?)</tr>", tbl, re.S)
        ncols = max((len(re.findall(r"<t[dh][\s>]", r)) for r in rows), default=1) or 1
        for r in rows:
            cells = [re.sub("<.*?>", "", c) for c in re.findall(r"<t[dh][^>]*>(.*?)</t[dh]>", r, re.S)]
            lines = max((math.ceil(len(c) / max(cpl / ncols, 6)) for c in cells), default=1)
            h += max(lines, 1) * 3.1 + 1.8
        h += 3
    rest = re.sub(r"<table.*?</table>", "", html_, flags=re.S)
    for para in re.findall(r"<(?:p|li|h3|h2|h4|div)[^>]*>(.*?)</(?:p|li|h3|h2|h4|div)>", rest, re.S):
        t = re.sub("<.*?>", "", para).strip()
        if t: h += math.ceil(len(t) / cpl) * 3.1 + 2.0
    return h

def _rows_fit_tail(P, chart_h, right_w):
    """Quantas linhas finais da tabela cabem ao lado do desenho (sem texto acima)."""
    widths = [right_w * 0.20, right_w * 0.36, right_w * 0.44]; avail = chart_h - 10; acc = 0.0; k = 0
    for res, sg, f, row in reversed(P["rows"]):
        extra = len(re.sub("<.*?>", "", row.split("</td><td>")[-1])) - len(f)
        lines = max(math.ceil(len(res) / (widths[0] / 1.42)), math.ceil(len(sg) / (widths[1] / 1.42)), math.ceil((len(f) + max(extra, 0)) / (widths[2] / 1.42)))
        h = lines * 3.1 + 1.8
        if acc + h <= avail: acc += h; k += 1
        else: break
    return k

def chart(cid, caption=None, full=True, legend=None, beside="", frac=None):
    """Bloco de um gráfico: desenho à esquerda (largura pela necessidade de rótulo), interpretação e `beside` à direita,
    linhas de resultado ao lado quando cabem, senão em largura total abaixo."""
    m = MANIFEST[cid]; cap = caption or m["title"]; kind = m["kind"]
    if kind == "lista": return _chart_list(cid, cap, beside=beside)
    frac = frac or _frac_single(cid)
    P = _interp_parts(cid)
    sh = _svg_height(m["file"]) / 190.0
    tail = FALLBACK.get(cid)
    below = ""; textfirst = cid in TEXTFIRST
    if tail and not textfirst:
        # 1) conteúdo ao lado vai para baixo se assim o bloco cabe; 2) senão, encolher o desenho até 22 % para caber;
        # 3) senão, com cauda de 55 mm ou mais, o texto vai antes e o desenho fica na página seguinte
        if beside and tail - 8 >= PAGE_W * frac * sh + 7: below, beside = beside, ""
        else:
            if beside: below, beside = beside, ""
            f_fit = (tail - 8 - 7) / sh / PAGE_W
            if f_fit < frac and f_fit >= 0.78 * frac: frac = round(f_fit, 3)
            elif f_fit < 0.78 * frac and TAIL_REAL.get(cid, tail) >= 55: textfirst = True; TEXTFIRST.add(cid)
    img_w = PAGE_W * frac
    chart_h = img_w * sh + 7
    right_w = PAGE_W - img_w - 7
    beside_h = _est_h(beside, right_w) if beside else 0.0
    lado, body = "", below
    if P:
        top_h = _est_h(P["lado"], right_w)
        if beside and top_h + beside_h > 170: body = beside + body; beside = ""; beside_h = 0.0
        n = _split_rows(P, chart_h - beside_h, right_w)
        lado = P["lado"] + ((LEGEND_HEAD + "".join(r[3] for r in P["rows"][:n]) + "</tbody></table>") if n else "") + P["base"]
        if n < len(P["rows"]):
            body = LEGEND_HEAD.replace("<th>Resultado</th>", "<th>Resultado" + (" (cont.)" if n else "") + "</th>") + "".join(r[3] for r in P["rows"][n:]) + "</tbody></table>" + body
    elif legend:
        body = '<table class="legend"><thead><tr><th>Nº</th><th>Setor</th><th>Resultado → vá para</th></tr></thead><tbody>' + \
               "".join(f"<tr><td>{i+1}</td><td>{e(s)}</td><td>{d}</td></tr>" for i, (s, d) in enumerate(legend)) + "</tbody></table>"
    if beside: lado += f'<div class="beside">{beside}</div>'
    if textfirst and cid in TF_TAIL:
        f_fit = (TF_TAIL[cid] - 14 - 7 - 12) / sh / PAGE_W   # −12 mm: sobra para 3 linhas do bloco seguinte; sem isso o motor empurra a linha do desenho junto com ele
        f_floor = max(0.60 * frac, _w_floor(cid) / PAGE_W)   # piso: rótulo ≥ LABEL_FLOOR_PT
        if f_fit < frac and f_fit >= f_floor: frac = round(f_fit, 3); img_w = PAGE_W * frac; chart_h = img_w * sh + 7; right_w = PAGE_W - img_w - 7
    if textfirst and P:
        # encher a cauda da página anterior primeiro (cabeçalho + texto + linhas que couberem); o resto ao lado do desenho
        avail_tail = (tail or 0) - 8 - 6 - _est_h(P["lado"], PAGE_W)
        n_before = 0; acc = 0.0
        for res, sg, f, row in P["rows"]:
            lines = max(math.ceil(len(res) / (PAGE_W * 0.14 / 1.42)), math.ceil(len(sg) / (PAGE_W * 0.36 / 1.42)), math.ceil(len(f) / (PAGE_W * 0.50 / 1.42)))
            h_row = lines * 3.1 + 1.8
            if acc + h_row <= avail_tail: acc += h_row; n_before += 1
            else: break
        # tudo antes (texto e tabela inteira preenchem a cauda); o desenho abre a página seguinte com o texto da seção seguinte ao lado
        # o conteúdo "ao lado" (listas, tabelas de situação) vai para a célula do desenho quando cabe nela; senão fica antes
        beside_in = bool(beside) and _est_h(beside, right_w) <= chart_h - 6
        texto = P["lado"] + LEGEND_HEAD + "".join(r[3] for r in P["rows"]) + "</tbody></table>" + (below or "") + (f'<div class="beside">{beside}</div>' if beside and not beside_in else "")
        draw = (f'<table class="cb"><tr><td class="l" style="width:{frac*100:.1f}%"><div class="chart-head"><span class="chart-id">{e(cid)}</span><span class="chart-title">desenho · {e(cap)}</span></div>'
                f'<img src="charts/{m["file"]}" alt="{e(cap)}"/></td><td class="r">' + (f'<div class="beside tfb">{beside}</div>' if beside_in else "") + '<div class="nextrun"><!--NEXTRUN--></div></td></tr></table>')
        return span(f'<div class="chart tf" id="fig-{cid}">{_head(cid, cap)}<div class="interp">{texto}</div>{draw}</div>')
    top = (f'<table class="cb"><tr><td class="l" style="width:{frac*100:.1f}%">{_head(cid, cap)}<img src="charts/{m["file"]}" alt="{e(cap)}"/></td>'
           f'<td class="r"><div class="interp">{lado}</div></td></tr></table>')
    return span(f'<div class="chart" id="fig-{cid}">{top}' + (f'<div class="interp">{body}</div>' if body else "") + '</div>')

def _w_floor(cid):
    """Largura mínima (mm) do desenho para o menor rótulo não cair abaixo de LABEL_FLOOR_PT."""
    return LABEL_FLOOR_PT / 2.835 * 190.0 / max(_min_font(cid), 0.5)

def _label_in(label, h):
    """Rótulo do par dentro do primeiro parágrafo (mesma caixa de linha), para as colunas não o deixarem sozinho no pé."""
    if h.startswith("<p>") or h.startswith("<p "):
        i = h.find(">"); return h[:i + 1] + f'<span class="pi-id">{label}</span><br/>' + h[i + 1:]
    return f'<div class="pi-id">{label}</div>' + h

def chart_group(ids, caps=None, extra=None, widths=None, mode="side", pre=None):
    """Dois ou três gráficos na mesma linha, largura dividida pela necessidade de rótulo.
    mode="side": cada célula traz desenho + interpretação; a linha se divide entre páginas quando necessário.
    mode="stacked" (ou recuo automático): só a linha de desenhos é indivisível; interpretações em largura total abaixo."""
    caps = caps or {}; extra = extra or {}; pre = pre or {}
    ms = [MANIFEST[c] for c in ids]
    if widths is None:
        needs = [min(max(0.40, min(0.60, need_frac(c))), _fmax_h(c)) for c in ids]
        s = sum(needs); widths = [nd / s for nd in needs]
    gap = 5.0; avail = PAGE_W - gap * (len(ids) - 1)
    img_ws = [w * avail for w in widths]
    scale = 1.0; tail = FALLBACK.get(ids[0]); textfirst = ids[0] in TEXTFIRST
    if tail and not textfirst:
        row_h = max(iw * _svg_height(m["file"]) / 190.0 for iw, m in zip(img_ws, ms)) + 7
        s_fit = (tail - 8 - 7) / (row_h - 7)
        if s_fit < 1.0 and s_fit >= 0.80: scale = round(s_fit, 3)
        elif s_fit < 0.80 and TAIL_REAL.get(ids[0], tail) >= 55: textfirst = True; TEXTFIRST.add(ids[0])
        img_ws = [iw * scale for iw in img_ws]
    tw = f' style="width:{(sum(img_ws) + gap * (len(ids) - 1)) / PAGE_W * 100:.1f}%"' if scale < 1.0 else ""
    cols = []
    for c, m, iw in zip(ids, ms, img_ws):
        P = _interp_parts(c)
        if P and re.match(r"C[1-7]-(emocoes|corpo)$", c): h = P["lado"] + P["inline"]   # tabela idêntica nos sete chakras: uma linha
        else: h = (P["lado"] + P["base"] + LEGEND_HEAD + "".join(r[3] for r in P["rows"]) + "</tbody></table>") if P else ""
        cols.append(h + extra.get(c, ""))
    if textfirst:
        split_rows = False
        if ids[0] in TF_TAIL:
            hs = [iw * _svg_height(m["file"]) / 190.0 for iw, m in zip(img_ws, ms)]; row_h = max(hs) + 7
            s_ = (TF_TAIL[ids[0]] - 14 - 7 - 12) / (row_h - 7)
            s_floor = max(0.60, max(_w_floor(c) / iw for c, iw in zip(ids, img_ws)))
            if s_floor <= s_ < 1.0: img_ws = [iw * s_ for iw in img_ws]; tw = f' style="width:{(sum(img_ws) + gap * (len(ids) - 1)) / PAGE_W * 100:.1f}%"'
            elif s_ < s_floor:
                # a linha inteira não cabe nem no piso: o primeiro desenho sozinho (escalado à cauda), os outros na linha seguinte
                s0 = (TF_TAIL[ids[0]] - 14 - 7 - 12) / hs[0]
                if s0 >= max(0.60, _w_floor(ids[0]) / img_ws[0]):
                    split_rows = True; img_ws = [img_ws[0] * min(s0, 1.0)] + list(img_ws[1:])
        heads = " · ".join(ids); titles = " · ".join(_cut(caps.get(c, m["title"]), 34) for c, m in zip(ids, ms))
        texto = "".join(f'<div class="interp stk"><div class="pi-id">{e(c)} · {e(caps.get(c, m["title"]))}</div>{h}</div>' for c, m, h in zip(ids, ms, cols) if h)
        tds = ""
        for i, (c, m, iw) in enumerate(zip(ids, ms, img_ws)):
            tds += f'<td class="l" id="fig-{c}" style="width:{iw/PAGE_W*100:.1f}%"><div class="chart-head"><span class="chart-id">{e(c)}</span><span class="chart-title">desenho</span></div><img src="charts/{m["file"]}" alt=""/></td>' + ('<td class="gap"></td>' if i < len(ids) - 1 else "")
        if split_rows:   # um desenho por linha, cada um com o texto seguinte ao lado
            rows_html = ""
            for c, m, iw in zip(ids, ms, img_ws):
                rows_html += (f'<table class="cb grp"><tr><td class="l" id="fig-{c}" style="width:{iw/PAGE_W*100:.1f}%"><div class="chart-head"><span class="chart-id">{e(c)}</span><span class="chart-title">desenho</span></div><img src="charts/{m["file"]}" alt=""/></td>'
                              '<td class="gap"></td><td class="r"><div class="nextrun"><!--NEXTRUN--></div></td></tr></table>')
            return span(f'<div class="chart grp tf"><div class="chart-head"><span class="chart-id">{e(heads)}</span><span class="chart-title">{e(titles)}</span></div>{texto}{rows_html}</div>')
        if sum(img_ws) + gap * (len(ids) - 1) < 0.82 * PAGE_W:   # linha encolhida: o resto da largura recebe o texto seguinte
            tds += '<td class="gap"></td><td class="r"><div class="nextrun"><!--NEXTRUN--></div></td>'; tw = ""
        return span(f'<div class="chart grp tf"><div class="chart-head"><span class="chart-id">{e(heads)}</span><span class="chart-title">{e(titles)}</span></div>{texto}<table class="cb grp"{tw}><tr>{tds}</tr></table></div>')
    if mode == "side":
        # linha 1 (indivisível): cabeçalhos e desenhos, alinhados; abaixo, as interpretações em duas colunas equilibradas,
        # que quebram entre páginas (uma linha de tabela com as duas células não quebra no motor de PDF)
        t1 = ""
        for i, (c, m, iw) in enumerate(zip(ids, ms, img_ws)):
            t1 += f'<td class="l" id="fig-{c}" style="width:{iw/PAGE_W*100:.1f}%">{pre.get(c, "")}{_head(c, caps.get(c, m["title"]))}<img src="charts/{m["file"]}" alt=""/></td>' + ('<td class="gap"></td>' if i < len(ids) - 1 else "")
        flow = "".join(f'<div class="interp gi">{_label_in(e(c) + " · " + e(_cut(caps.get(c, m["title"]), 40)), h)}</div>' for c, m, h in zip(ids, ms, cols) if h)
        return span(f'<div class="chart grp side"><table class="cb grp"{tw}><tr>{t1}</tr></table><div class="cols grpflow">{flow}</div></div>')
    tds = ""
    for i, (c, m, iw) in enumerate(zip(ids, ms, img_ws)):
        tds += f'<td class="l" id="fig-{c}" style="width:{iw/PAGE_W*100:.1f}%">{_head(c, caps.get(c, m["title"]))}<img src="charts/{m["file"]}" alt=""/></td>' + ('<td class="gap"></td>' if i < len(ids) - 1 else "")
    stacked = "".join(f'<div class="interp stk"><div class="pi-id">{e(c)} · {e(caps.get(c, m["title"]))}</div>{h}</div>' for c, m, h in zip(ids, ms, cols) if h)
    return span(f'<div class="chart grp"><table class="cb grp"{tw}><tr>{tds}</tr></table>{stacked}</div>')

def chart_pair(a, b, cap_a=None, cap_b=None):
    caps = {}
    if cap_a: caps[a] = cap_a
    if cap_b: caps[b] = cap_b
    return chart_group([a, b], caps=caps)

def list_block(cid, cols=None, caption=None, narrow=False):
    """Lista pendulável como texto: cabeçalho, interpretação curta, itens em colunas, tabela de resultados. Sem miniatura."""
    m = MANIFEST[cid]; cap = caption or m["title"]; P = _interp_parts(cid)
    entries = _list_entries(cid); n = len(entries)
    cols = cols or (3 if n <= 27 else (4 if n <= 52 else 5))
    rows_n = math.ceil(n / cols); cells = []; num = 0
    for kind, txt, color in entries:
        if kind == "H": cells.append(f'<td class="lh" style="background:{color or "#eef2f7"}">{e(txt)}</td>')
        else:
            num += 1; cells.append(f'<td class="li" style="border-left-color:{color or "#9a9a9a"}"><span class="dot"></span><b>{num}</b> {e(txt)}</td>')
    trs = "".join("<tr>" + "".join(cells[c * rows_n + r] if c * rows_n + r < len(cells) else '<td class="li empty"></td>' for c in range(cols)) + "</tr>" for r in range(rows_n))
    items = f'<table class="lista c{cols}"><tbody>{trs}</tbody></table>'
    lado = (P["lado"] + P["base"]) if P else ""
    body = (LEGEND_HEAD + "".join(r[3] for r in P["rows"]) + "</tbody></table>") if P else ""
    if P and re.match(r"C[1-7]-sinais$", cid): body = ""; lado += '<p class="res1">O sinal mais ativo orienta o setor do G8: corpo → 3; emoção → 1; crença e atitude → 2; chips, implantes, magias e ataques → 4.</p>'
    lado_div = f'<div class="interp">{lado}</div>' if narrow else f'<div class="interp wide-lado">{lado}</div>'
    # cabeçalho + interpretação + primeiras linhas da lista num bloco indivisível (o resto da lista pode quebrar)
    k = min(1, rows_n)
    trs_head = "".join("<tr>" + "".join(cells[c * rows_n + r] if c * rows_n + r < len(cells) else '<td class="li empty"></td>' for c in range(cols)) + "</tr>" for r in range(k))
    trs_rest = "".join("<tr>" + "".join(cells[c * rows_n + r] if c * rows_n + r < len(cells) else '<td class="li empty"></td>' for c in range(cols)) + "</tr>" for r in range(k, rows_n))
    items_head = f'<table class="lista c{cols}"><tbody>{trs_head}</tbody></table>'
    items_rest = f'<table class="lista c{cols} rest"><tbody>{trs_rest}</tbody></table>' if trs_rest else ""
    return f'<div class="lb" id="fig-{cid}"><div class="keep">{_head(cid, cap)}{lado_div}{items_head}</div>{items_rest}<div class="interp">{body}</div></div>'

def _chart_list(cid, cap, beside=""):
    return span(f'<div class="chart k-lista">{list_block(cid, caption=cap)}</div>')

def list_pair(a, b, cols=2):
    """Duas listas curtas lado a lado (linha divisível entre páginas); se o bloco saltou, duas listas separadas."""
    if a in FALLBACK:
        return _chart_list(a, MANIFEST[a]["title"]) + _chart_list(b, MANIFEST[b]["title"])
    return span(f'<div class="chart grp side lp"><table class="cb grp side"><tr><td style="width:48.5%">{list_block(a, cols=cols, narrow=True)}</td><td class="gap"></td><td style="width:48.5%">{list_block(b, cols=cols, narrow=True)}</td></tr></table></div>')

def cols3(html_):
    """Trecho em três colunas, em largura total."""
    return span(f'<div class="cols three">{html_}</div>')

def img(path, caption, width="100%"):
    return f'<figure class="pic"><img src="{path}" style="width:{width}" alt="{e(caption)}"/><figcaption>{e(caption)}</figcaption></figure>'

def pagebreak():
    return '<div class="pb"></div>'

def form_table(headers, nrows, cls="form"):
    th = "".join(f"<th>{h}</th>" for h in headers)
    trs = "".join("<tr>" + "".join("<td>&nbsp;</td>" for _ in headers) + "</tr>" for _ in range(nrows))
    return f'<table class="{cls}"><thead><tr>{th}</tr></thead><tbody>{trs}</tbody></table>'

def toc_html():
    out = ['<nav class="toc" id="sumario"><h1>Sumário</h1><ul>']
    for id_, title, lvl in TOC:
        out.append(f'<li class="l{lvl}"><a href="#{id_}">{e(title)}</a></li>')
    out.append("</ul></nav>")
    return "".join(out)
