#!/usr/bin/env python3
"""Relatorio enxuto das 30 construtoras com contatos mais consistentes.
Entradas: dados/v3/selecao30.json (07_consistencia.py) e dados/v3/pesquisa/*.json.
Saidas: fichas_v3/index.html (+ artifact_index.html), Construtoras_30_contatos.pdf/.xlsx."""
import json, re
from datetime import date
from html import escape
from pathlib import Path

R = Path(__file__).resolve().parent.parent
OUT = R / "fichas_v3"
SEL = json.load(open(R / "dados/v3/selecao30.json"))
HOJE = date.today().strftime("%d/%m/%Y")
RUIM = re.compile(r"contab|contador|fiscal|jurid|advog|escritorio|\bdp\b|pessoal|cobranca|tributa|legaliza")

def e(x): return escape(str(x)) if x not in (None, "", [], {}) else ""
def dig(t): return re.sub(r"\D", "", str(t or ""))
def fonte(u): return f' <a class="src" href="{e(u)}">↗</a>' if isinstance(u, str) and u.startswith("http") else ""
def site_link(u):
    if not u: return ""
    h = u if u.startswith("http") else "https://" + u
    t = re.sub(r"^https?://(www\.)?", "", u).rstrip("/")
    return f'<a href="{e(h)}">{e(t)}</a>'

def juntar(x):
    p = {}
    f = R / "dados/v3/pesquisa" / f"{x['dominio']}.json"
    if f.exists():
        try: p = json.load(open(f))
        except json.JSONDecodeError: p = {}
    em = {}
    for y in p.get("emails") or []:
        k = str(y.get("email", "")).lower().strip()
        if "@" in k and not RUIM.search(k):
            em[k] = dict(email=k, area=y.get("area") or "", conf=bool(y.get("confirmado")), fonte=y.get("fonte"))
    for k in x["emails_bons"]:
        em.setdefault(k, dict(email=k, area="Receita", conf=False, fonte=""))
    fo = {}
    for y in p.get("telefones") or []:
        d = dig(y.get("numero"))[-8:]
        if len(d) == 8:
            fo[d] = dict(numero=y.get("numero"), tipo=y.get("tipo") or "", conf=bool(y.get("confirmado")), fonte=y.get("fonte"))
    for n in x["fixos"]:
        fo.setdefault(dig(n)[-8:], dict(numero=n, tipo="fixo", conf=False, fonte=""))
    raizes = {re.sub(r"^https?://(www\.)?", "", u or "").split("/")[0].split(".")[0] for u in ((p.get("site") or {}).get("url"), x["dominio"])} - {""}
    em = {k: y for k, y in em.items() if y["conf"] or k.split("@")[-1].split(".")[0] in raizes}   # outro dominio so se publicado
    em = sorted(em.values(), key=lambda y: (not y["conf"], y["area"] in ("financeiro", "outro", "Receita")))
    fo = sorted(fo.values(), key=lambda y: (not y["conf"], y["tipo"] != "fixo"))
    obras = [o for o in (p.get("empreendimentos_ativos") or []) if o.get("nome")]
    site = p.get("site") or {}
    pts = 2 * bool(site.get("confirmado")) + 2 * any(y["conf"] for y in em) + 2 * any(y["conf"] and y["tipo"] in ("fixo", "0800") for y in fo) \
          + bool(obras) + bool((p.get("decisor") or {}).get("nome"))
    if any(re.search(r"contador|reclame aqui[^;]*nota [0-4][,.]", str(a), re.I) for a in p.get("alertas") or []):
        pts -= 2                                                        # contato de contador ou reputacao ruim
    nivel = "Alta" if pts >= 7 else "Média" if pts >= 4 else "Baixa"
    return dict(x=x, p=p, em=em, fo=fo, obras=obras, site=site.get("url") or x["dominio"], site_ok=site.get("confirmado"),
                pts=pts, nivel=nivel, marca=p.get("marca") or x["nome"].title())

AJ = json.load(open(R / "dados/v3/ajustes.json")) if (R / "dados/v3/ajustes.json").exists() else {}

def img(dom):
    """Print da home (fichas_v3/img/<dominio>.jpg), gerado por 09_capturar_sites.py."""
    import base64
    f = OUT / "img" / f"{dom}.jpg"
    if f.exists():
        return f'<img class="thumb" alt="Página inicial de {e(dom)}" src="data:image/jpeg;base64,{base64.b64encode(f.read_bytes()).decode()}">'
    return f'<div class="thumb vazio"><span>imagem do site<br>pendente</span></div>'

def pessoas(i):
    x, p = i["x"], i["p"]
    lst = list((AJ.get(x["dominio"]) or {}).get("pessoas") or [])
    dec = p.get("decisor") or {}
    if dec.get("nome") and not any(dec["nome"].split()[0].lower() == y["nome"].split()[0].lower() for y in lst):
        lst.append(dict(nome=dec["nome"], cargo=dec.get("cargo"), linkedin=dec.get("linkedin"), email="", email_status="", fonte=dec.get("fonte")))
    out = []
    for y in lst[:2]:
        partes = [f'<b>{e(y["nome"])}</b>', e(y.get("cargo"))]
        if y.get("email"): partes.append(f'<span class="mono">{e(y["email"])}</span> <span class="tag">{e(y.get("email_status"))}</span>')
        elif y.get("email_status"): partes.append(f'<span class="tag">{e(y["email_status"])}</span>')
        if str(y.get("linkedin", "")).startswith("http"): partes.append(f'<a href="{e(y["linkedin"])}">LinkedIn</a>')
        out.append("<li>" + " · ".join(z for z in partes if z) + fonte(y.get("fonte")) + "</li>")
    if not out:
        out.append(f'<li class="mut">Sem decisor público; sócios na Receita: {e(", ".join(x["socios_pf"][:3]).title())}</li>')
    return "".join(out)

def cartao(i, n):
    x, p = i["x"], i["p"]
    chip = lambda y: '<span class="ok">✔</span>' if y["conf"] else '<span class="rf" title="só no cadastro da Receita">R</span>'
    em = "".join(f'<li>{chip(y)} <span class="mono">{e(y["email"])}</span>{fonte(y["fonte"])}</li>' for y in i["em"][:3])
    fo = "".join(f'<li>{chip(y)} <span class="mono">{e(y["numero"])}</span> <span class="tag">{e(y["tipo"])}</span></li>' for y in i["fo"][:3])
    ob = " · ".join(f'<b>{e(o.get("nome"))}</b> <span class="mut">({e(o.get("bairro") or o.get("cidade") or "local n/d")}{", " + e(o.get("unidades")) + " un." if o.get("unidades") else ""})</span>{fonte(o.get("fonte"))}'
                    for o in i["obras"][:4])
    if not ob:
        ob = '<span class="mut">sem obra ativa confirmada; SPEs recentes: ' + e(", ".join(f'{s["bairro"]} {s["ano"]}' for s in x["spes_recentes"][:3])) + "</span>"
    nota = (AJ.get(x["dominio"]) or {}).get("nota") or p.get("resumo") or ""
    al = (p.get("alertas") or [""])[0]
    return f"""<article class="card" id="{e(x['dominio'])}">
 <div class="topo">{img(x['dominio'])}
  <div class="id"><div class="l1"><span class="n">{n:02d}</span><h2>{e(i['marca'])}</h2><span class="nv {i['nivel'].lower()}">{i['nivel']}</span></div>
   <p class="sub">{site_link(i['site'])} · {e(p.get('segmento') or x['segmento'])} · {x['spe_desde_2023']} SPEs desde 2023</p>
   {f'<p class="res">{e(nota)}</p>' if nota else ''}</div></div>
 <h3>Contato direto</h3><ul class="pes">{pessoas(i)}</ul>
 <div class="cols"><div><h3>E-mails</h3><ul>{em or '<li class="mut">—</li>'}</ul></div>
  <div><h3>Telefones</h3><ul>{fo or '<li class="mut">—</li>'}</ul></div></div>
 <h3>Obras ativas</h3><p class="obras">{ob}</p>
 {f'<p class="al">⚠ {e(al)}</p>' if al else ''}
</article>"""

CSS = """
/* Layout: tabela-resumo no topo; cartoes compactos em duas colunas (tela e impressao) */
:root{--bg:#fafaf8;--fg:#1b2127;--mut:#5d6873;--bd:#dce0e3;--soft:#eff1f0;--ac:#1d6a58;--ok:#1a7a43;--pa:#9d5d00;--fa:#b3261e;
--display:"Archivo",Arial,sans-serif;--body:"Source Sans 3",-apple-system,Segoe UI,Roboto,sans-serif;--mono:"JetBrains Mono",ui-monospace,Menlo,monospace}
@media (prefers-color-scheme: dark){:root:not([data-theme="light"]){--bg:#111514;--fg:#e3e8e6;--mut:#98a4a0;--bd:#2a3230;--soft:#191f1d;--ac:#62c3a6;--ok:#58c98a;--pa:#e8b15b;--fa:#ff8a80;color-scheme:dark}}
:root[data-theme="dark"]{--bg:#111514;--fg:#e3e8e6;--mut:#98a4a0;--bd:#2a3230;--soft:#191f1d;--ac:#62c3a6;--ok:#58c98a;--pa:#e8b15b;--fa:#ff8a80;color-scheme:dark}
@media print{:root,:root:not([data-theme="light"]){--bg:#fff;--fg:#1b2127;--mut:#5d6873;--bd:#dce0e3;--soft:#eff1f0;--ac:#1d6a58;--ok:#1a7a43;--pa:#9d5d00;--fa:#b3261e;color-scheme:light}}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--fg);font:13.5px/1.4 var(--body)}
main{max-width:1100px;margin:0 auto;padding-block:24px;padding-inline:16px}
a{color:var(--ac);text-decoration:none;overflow-wrap:anywhere}a:hover,a:focus-visible{text-decoration:underline}a.src{color:var(--mut);font-size:11px}
h1{font:700 26px var(--display);margin:0 0 4px;text-wrap:balance}h2{font:700 15.5px var(--display);margin:0;flex:1;min-width:0}
h3{font-size:10.5px;text-transform:uppercase;letter-spacing:.06em;color:var(--mut);margin:8px 0 2px}
.sub,.mut{color:var(--mut)}.mono{font-family:var(--mono);font-size:11.5px}
table{width:100%;border-collapse:collapse;font-size:12px;font-variant-numeric:tabular-nums}th,td{text-align:left;padding:4px 6px;border-bottom:1px solid var(--bd);vertical-align:top}
th{background:var(--soft);font-weight:600;white-space:nowrap}.wrap{overflow-x:auto;margin:10px 0 18px}
.grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:12px}
.card{border:1px solid var(--bd);border-radius:8px;padding:10px 12px;break-inside:avoid;min-width:0}
.topo{display:flex;gap:10px;align-items:flex-start}.id{min-width:0;flex:1}
.thumb{width:132px;aspect-ratio:16/10;max-width:100%;object-fit:cover;object-position:top;border:1px solid var(--bd);border-radius:5px;flex:none}
.thumb.vazio{display:flex;align-items:center;justify-content:center;background:var(--soft);font-size:10.5px;color:var(--mut);text-align:center}
.l1{display:flex;gap:8px;align-items:baseline}.n{font:600 12px var(--mono);color:var(--mut)}
.nv{font-size:10.5px;padding:0 7px;border-radius:10px;border:1px solid var(--bd);white-space:nowrap}.nv.alta{color:var(--ok)}.nv.média{color:var(--pa)}.nv.baixa{color:var(--fa)}
.card .sub{margin:1px 0 2px;font-size:12px}.res{margin:2px 0;font-size:12.5px}
.cols{display:grid;grid-template-columns:minmax(0,1.3fr) minmax(0,1fr);gap:10px}
ul{margin:0;padding-left:0;list-style:none}li{margin:1px 0}.pes li{font-size:12.5px}
.tag{font-size:10.5px;color:var(--mut)}.ok{color:var(--ok);font-weight:700}.rf{font:600 10px var(--mono);color:var(--mut);border:1px solid var(--bd);border-radius:3px;padding:0 3px}
.obras{margin:0;font-size:12.5px}.al{color:var(--pa);font-size:11.5px;margin:6px 0 0}.intro p{margin:4px 0;max-width:80ch}
@media (max-width:760px){.grid,.cols{grid-template-columns:1fr}table{display:block;overflow-x:auto}.thumb{width:104px}}
@page{size:A4;margin:9mm}@media print{a.src{display:none}main{padding:0}body{font-size:12px}.grid{gap:8px}}
"""
FONTES = ('<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wght@700'
          '&family=JetBrains+Mono:wght@400;600&family=Source+Sans+3:wght@400;600;700&display=swap">')

def main():
    itens = [juntar(x) for x in SEL if not (AJ.get(x["dominio"]) or {}).get("remover")]
    itens.sort(key=lambda i: (-i["pts"], -i["x"]["score"]))
    linhas = []
    for n, i in enumerate(itens, 1):
        em = next((y["email"] for y in i["em"] if y["conf"]), i["em"][0]["email"] if i["em"] else "")
        fo = next((y["numero"] for y in i["fo"] if y["conf"] and y["tipo"] in ("fixo", "0800")),
                  next((y["numero"] for y in i["fo"] if y["tipo"] == "fixo"), i["fo"][0]["numero"] if i["fo"] else ""))
        linhas.append(f'<tr><td>{n}</td><td><a href="#{e(i["x"]["dominio"])}"><b>{e(i["marca"])}</b></a></td><td>{site_link(i["site"])}</td>'
                      f'<td class="mono">{e(em)}</td><td class="mono">{e(fo)}</td><td>{len(i["obras"])}</td><td>{e(i["nivel"])}</td></tr>')
    alta = sum(i["nivel"] == "Alta" for i in itens); em_c = sum(any(y["conf"] for y in i["em"]) for i in itens)
    fo_c = sum(any(y["conf"] for y in i["fo"]) for i in itens); ob_c = sum(bool(i["obras"]) for i in itens)
    corpo = f"""<div class="intro"><h1>{len(itens)} construtoras para prospectar</h1>
<p class="sub">BH e região metropolitana · {HOJE} · porte médio e pequeno, escolhidas pela consistência dos contatos</p>
<p>Todas têm site próprio, e-mail no domínio da empresa (sem contabilidade, jurídico ou fiscal), telefone fixo que não se repete em
outras empresas e SPE aberta desde 2023. Grandes incorporadoras ficaram de fora. ✔ = o contato aparece no site ou em outra publicação da empresa; R = só no cadastro do CNPJ na Receita. <b>Consistência</b>: Alta, Média ou Baixa, conforme site, e-mail e fixo confirmados,
obra ativa e decisor identificado.</p>
<p><b>{alta}</b> com consistência alta · <b>{em_c}</b> com e-mail publicado · <b>{fo_c}</b> com telefone publicado · <b>{ob_c}</b> com obra ativa localizada.</p></div>
<div class="wrap"><table><thead><tr><th>#</th><th>Construtora</th><th>Site</th><th>E-mail principal</th><th>Telefone</th><th>Obras ativas</th><th>Consistência</th></tr></thead>
<tbody>{''.join(linhas)}</tbody></table></div>
<div class="grid">{''.join(cartao(i, n) for n, i in enumerate(itens, 1))}</div>"""
    OUT.mkdir(exist_ok=True)
    miolo = f"<title>30 construtoras para prospectar</title>{FONTES}<style>{CSS}</style><main>{corpo}</main>"
    (OUT / "artifact_index.html").write_text(miolo, encoding="utf-8")
    (OUT / "index.html").write_text('<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">'
                                    + miolo.replace("<main>", "</head><body><main>", 1) + "</body></html>", encoding="utf-8")
    planilha(itens)
    print(f"{len(itens)} cartões · alta {alta} · e-mail publicado {em_c} · fone publicado {fo_c} · obras {ob_c}")

def planilha(itens):
    from openpyxl import Workbook
    from openpyxl.styles import Font, PatternFill, Alignment
    wb = Workbook(); ws = wb.active; ws.title = "30 construtoras"
    cab = ["#", "Construtora", "Site", "Consistência", "Segmento", "E-mails publicados", "E-mails (Receita)", "Telefones publicados",
           "Telefones (Receita)", "Quem procurar", "Cargo", "LinkedIn", "Endereço", "Obras ativas", "Resumo", "Alertas"]
    ws.append(cab)
    for n, i in enumerate(itens, 1):
        p = i["p"]; dec = p.get("decisor") or {}
        ws.append([n, i["marca"], i["site"], i["nivel"], p.get("segmento") or i["x"]["segmento"],
                   "\n".join(y["email"] for y in i["em"] if y["conf"]), "\n".join(y["email"] for y in i["em"] if not y["conf"]),
                   "\n".join(f'{y["numero"]} ({y["tipo"]})' for y in i["fo"] if y["conf"]), "\n".join(y["numero"] for y in i["fo"] if not y["conf"]),
                   dec.get("nome", ""), dec.get("cargo", ""), dec.get("linkedin", ""), (p.get("endereco") or {}).get("texto", ""),
                   "\n".join(f'{o.get("nome")} – {", ".join(z for z in (o.get("bairro"), o.get("cidade")) if z)} – {o.get("status", "")}' for o in i["obras"]),
                   p.get("resumo", ""), "; ".join(p.get("alertas") or [])])
    for c in ws[1]: c.font = Font(bold=True, color="FFFFFF"); c.fill = PatternFill("solid", fgColor="1D6A58")
    larg = [4, 28, 30, 12, 12, 34, 34, 24, 18, 26, 22, 30, 36, 50, 50, 40]
    for k, w in enumerate(larg): ws.column_dimensions[ws.cell(1, k + 1).column_letter].width = w
    for row in ws.iter_rows(min_row=2):
        for c in row: c.alignment = Alignment(wrap_text=True, vertical="top")
    ws.freeze_panes = "C2"; ws.auto_filter.ref = ws.dimensions
    wb.save(R / "Construtoras_30_contatos.xlsx")

if __name__ == "__main__":
    main()
