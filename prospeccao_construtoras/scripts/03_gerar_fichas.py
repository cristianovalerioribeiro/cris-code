#!/usr/bin/env python3
"""Gera as fichas: fichas/index.html (ranking), fichas/<dominio>.html (uma por
construtora) e fichas/relatorio.html (tudo junto, pronto para virar PDF).
Entradas: dados/selecao30.json (base Receita), dados/pesquisa/*.json (pesquisa
web), dados/top100.json (mapeamento amplo) e, se existirem, fichas/img/*.jpg e
dados/sites_status.json (captura dos sites)."""
import base64, json, re
from datetime import date
from html import escape
from pathlib import Path

R = Path(__file__).resolve().parent.parent
SEL = json.load(open(R / "dados/selecao30.json"))
TOP = json.load(open(R / "dados/top100.json"))
STATUS = json.load(open(R / "dados/sites_status.json")) if (R / "dados/sites_status.json").exists() else {}
HOJE = date.today().strftime("%d/%m/%Y")

def e(x):
    return escape(str(x)) if x not in (None, "") else ""

def g(d, *ks, default=""):
    for k in ks:
        if not isinstance(d, dict):
            return default
        d = d.get(k)
    return default if d in (None, "", [], {}) else d

def link(url, txt=None):
    if not url:
        return ""
    u = url if url.startswith("http") else "https://" + url
    txt = txt or re.sub(r"^https?://(www\.)?", "", url).rstrip("/")
    return f'<a href="{e(u)}">{e(txt)}</a>'

def fonte(url):
    return f' <a class="src" href="{e(url)}">[fonte]</a>' if url and str(url).startswith("http") else ""

def fmt_fone(n):
    d = re.sub(r"\D", "", str(n))
    if d.startswith("55") and len(d) > 11:
        d = d[2:]
    if len(d) == 10:
        return f"({d[:2]}) {d[2:6]}-{d[6:]}"
    if len(d) == 11:
        return f"({d[:2]}) {d[2:7]}-{d[7:]}"
    return str(n)

def fmt_cnpj(c):
    c = re.sub(r"\D", "", str(c))
    return f"{c[:2]}.{c[2:5]}.{c[5:8]}/{c[8:12]}-{c[12:]}" if len(c) == 14 else c

def brl(v):
    try:
        return "R$ " + f"{float(v):,.0f}".replace(",", ".")
    except (TypeError, ValueError):
        return ""

def num(x, default=0.0):
    m = re.search(r"\d+(?:[.,]\d+)?", str(x if x is not None else ""))
    return float(m.group().replace(",", ".")) if m else default

def pesquisa(dom):
    p = R / "dados/pesquisa" / f"{dom}.json"
    if not p.exists():
        return {}
    try:
        return json.load(open(p))
    except json.JSONDecodeError:
        return {}

# ---------------------------------------------------------------- validadores
def validadores(b, p):
    """Lista de (nome, estado, detalhe). estado: ok | falha | parcial | nd."""
    v = []
    site = g(p, "site") or {}
    st = STATUS.get(b["dominio"], {})
    conf = site.get("confirmado_da_empresa")
    v.append(("Site oficial confirmado", "ok" if conf is True else ("falha" if conf is False else "nd"),
              link(site.get("url") or b["dominio"])))
    no_ar = "ok" if st.get("no_ar") else ("falha" if st else
            {"sim": "ok", "nao": "falha"}.get(site.get("no_ar"), "nd"))
    v.append(("Site no ar", no_ar, "captura automática" if st else "segundo a busca" if no_ar != "nd" else "não verificado"))
    ig = g(p, "instagram") or {}
    v.append(("Instagram da empresa", "ok" if ig.get("url") and ig.get("ativo_2026") == "sim"
              else "parcial" if ig.get("url") else "falha",
              (link(ig.get("url")) + (f" · {e(ig.get('seguidores'))} seguidores" if ig.get("seguidores") else ""))))
    li = g(p, "linkedin_empresa") or {}
    v.append(("LinkedIn da empresa", "ok" if li.get("url") else "falha", link(li.get("url"))))
    fones = g(p, "telefones", default=[])
    fixo = [t for t in fones if t.get("tipo") == "fixo" and t.get("validado") == "confirmado"]
    conf_any = [t for t in fones if t.get("validado") == "confirmado"]
    v.append(("Telefone fixo próprio (não é do contador)", "ok" if fixo else "parcial" if conf_any else "falha",
              fmt_fone(fixo[0]["numero"]) if fixo else (fmt_fone(conf_any[0]["numero"]) + " (não fixo)" if conf_any else "")))
    emails = g(p, "emails", default=[])
    em = [x for x in emails if x.get("validado") == "confirmado"]
    v.append(("E-mail comercial confirmado", "ok" if em else "falha", e(em[0]["email"]) if em else ""))
    socios = g(p, "socios_receita", default=[]) or [{"nome": s} for s in b["socios_top"].split(" | ") if s]
    v.append(("Sócios identificados (Receita)", "ok" if socios else "falha", f"{len(socios)} sócio(s)"))
    cf = g(p, "controladores_finais", default=[])
    v.append(("Controlador final (pessoa física)", "ok" if cf else "parcial" if socios else "falha",
              ", ".join(e(c.get("nome")) for c in cf[:3])))
    dec = [d for d in g(p, "diretores_e_decisores", default=[]) if d.get("linkedin")]
    v.append(("Decisor com LinkedIn", "ok" if dec else "falha",
              ", ".join(e(d.get("nome")) for d in dec[:2])))
    sa = g(p, "saude") or {}
    rj = sa.get("recuperacao_judicial_ou_falencia")
    v.append(("Sem recuperação judicial/falência", "falha" if rj == "sim" else "ok" if rj else "nd", ""))
    ra = sa.get("reclame_aqui") or {}
    nota = num(ra.get("nota"), None) if ra.get("nota") else None
    v.append(("Reclame Aqui", "nd" if nota is None and not ra.get("reputacao") else
              "ok" if (nota or 0) >= 7 else "parcial" if (nota or 0) >= 5 else "falha",
              " ".join(x for x in (f"nota {ra.get('nota')}" if ra.get("nota") else "", e(ra.get("reputacao"))) if x)
              or "sem página"))
    neg = sa.get("noticias_negativas") or []
    proc = sa.get("processos_relevantes") or []
    v.append(("Sem notícia/processo negativo relevante", "ok" if not neg and not proc else "parcial",
              f"{len(neg)} notícia(s), {len(proc)} processo(s)" if neg or proc else ""))
    rp = g(p, "resumo_portfolio") or {}
    lanc = num(rp.get("qtd_lancamentos_2024_2026"), 0)
    v.append(("Lançando em 2024–2026", "ok" if lanc > 0 or b["spe_desde_2023"] > 0 else "falha",
              f"{int(lanc)} lançamento(s) na web · {b['spe_desde_2023']} SPE(s) abertas desde 2023"))
    ad = g(p, "aderencia_hadron") or {}
    enc = ad.get("encaixe")
    v.append(("Encaixe no perfil Hadron (médio R$10–14 mil/m² ou MCMV)",
              "ok" if enc in ("mcmv", "medio", "misto") else "falha" if enc in ("alto", "fora") else "nd",
              e(enc)))
    return v

def pct(v):
    pts = {"ok": 1, "parcial": 0.5, "falha": 0, "nd": 0}
    return round(100 * sum(pts[s] for _, s, _ in v) / len(v))

ICONE = {"ok": "✔", "parcial": "◐", "falha": "✘", "nd": "?"}

# ---------------------------------------------------------------- blocos
def tabela(cab, linhas, cls=""):
    if not linhas:
        return '<p class="vazio">Nada encontrado.</p>'
    h = "".join(f"<th>{c}</th>" for c in cab)
    b = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in l) + "</tr>" for l in linhas)
    return f'<table class="{cls}"><thead><tr>{h}</tr></thead><tbody>{b}</tbody></table>'

def selo(estado, txt):
    return f'<span class="selo {estado}">{ICONE[estado]} {txt}</span>'

def img_site(dom):
    p = R / "fichas/img" / f"{dom}.jpg"
    if p.exists():
        return f'<img class="print" alt="Página inicial de {e(dom)}" src="data:image/jpeg;base64,{base64.b64encode(p.read_bytes()).decode()}">'
    return ('<div class="semprint">Captura da página inicial pendente: o ambiente desta análise não tinha acesso '
            'direto aos sites. Rode <code>scripts/04_capturar_sites.js</code> com a rede liberada e gere de novo.</div>')

def ficha(b, p, pos):
    v = validadores(b, p)
    nome = g(p, "nome_comercial") or b["nome"]
    ad = g(p, "aderencia_hadron") or {}
    cr = g(p, "contato_recomendado") or {}
    sa = g(p, "saude") or {}
    rp = g(p, "resumo_portfolio") or {}
    eixo = "MCMV / econômico" if b["eixo"] == "mcmv" else "Médio (R$ 10–14 mil/m²)"
    site = g(p, "site", "url") or b["dominio"]

    fones = [[f'<b>{e(fmt_fone(t.get("numero")))}</b>', e(t.get("tipo")), e(t.get("origem")),
              selo({"confirmado": "ok", "contador_provavel": "falha"}.get(t.get("validado"), "nd"),
                   {"confirmado": "confirmado", "contador_provavel": "contador provável"}.get(t.get("validado"), "não confirmado")),
              fonte(t.get("fonte"))] for t in g(p, "telefones", default=[])]
    for f in b["fones_contador"].split(";"):
        if f and not any(re.sub(r"\D", "", str(t.get("numero"))).endswith(f[-8:]) for t in g(p, "telefones", default=[])):
            fones.append([e(fmt_fone(f)), "—", "receita", selo("falha", "repetido em ≥5 grupos da base"), ""])
    emails = [[f'<b>{e(x.get("email"))}</b>', e(x.get("origem")),
               selo({"confirmado": "ok", "contador_provavel": "falha"}.get(x.get("validado"), "nd"),
                    e(x.get("validado") or "não confirmado")), fonte(x.get("fonte"))] for x in g(p, "emails", default=[])]
    canais = [[e(c.get("tipo")), link(c.get("url"))] for c in g(p, "outros_canais", default=[]) if c.get("url")]
    socios = [[e(s.get("nome")), e(s.get("tipo")), e(s.get("qualificacao")), fonte(s.get("fonte"))]
              for s in g(p, "socios_receita", default=[])] or \
             [[e(s), "", "base Receita jul/2026", ""] for s in b["socios_top"].split(" | ") if s]
    ctrl = [[e(c.get("nome")), e(c.get("via")), fonte(c.get("fonte"))] for c in g(p, "controladores_finais", default=[])]
    dec = [[f'<b>{e(d.get("nome"))}</b>', e(d.get("cargo")), link(d.get("linkedin"), "LinkedIn") if d.get("linkedin") else "",
            e(d.get("outras_referencias")), fonte(d.get("fonte"))] for d in g(p, "diretores_e_decisores", default=[])]
    emps = [[e(x.get("nome")), e(", ".join(y for y in (x.get("bairro"), x.get("cidade")) if y)), e(x.get("status")),
             e(x.get("unidades")), e(x.get("area_m2")), e(x.get("preco_m2")), e(x.get("mcmv")), fonte(x.get("fonte"))]
            for x in g(p, "empreendimentos", default=[])]
    spes = [[fmt_cnpj(c["cnpj"]), e(c["razao_social"]), e(c["inicio_atividade"][:4]), e(c["bairro"])]
            for c in b["cnpjs"][:12]]
    neg = "".join(f'<li>{e(n.get("data"))} {e(n.get("resumo"))}{fonte(n.get("fonte"))}</li>'
                  for n in (sa.get("noticias_negativas") or []) + (sa.get("processos_relevantes") or []))
    pos_ = "".join(f'<li>{e(n.get("data"))} {e(n.get("resumo"))}{fonte(n.get("fonte"))}</li>'
                   for n in sa.get("noticias_positivas") or [])
    alertas = "".join(f"<li>{e(a)}</li>" for a in g(p, "alertas", default=[]))
    ra = sa.get("reclame_aqui") or {}
    end = g(p, "endereco_comercial") or {}
    sem_pesquisa = '<p class="alerta">Pesquisa web ainda não disponível para esta construtora; a ficha mostra só a base da Receita.</p>' if not p else ""

    return f"""
<section class="ficha" id="{e(b['dominio'])}">
 <header class="topo">
  <div><span class="pos">#{pos}</span> <span class="eixo {b['eixo']}">{eixo}</span></div>
  <h2>{e(nome)}</h2>
  <p class="sub">{link(site)} · CNPJ matriz {fmt_cnpj(g(p, 'cnpj_matriz') or b['cnpj_matriz'])} · {e(b['razao_matriz'])}</p>
  <div class="kpis">
   <div><b>{e(ad.get('nota_0a10', '–'))}</b><span>aderência Hadron (0–10)</span></div>
   <div><b>{e(g(p, 'confianca_geral_0a10', default='–'))}</b><span>confiança dos dados (0–10)</span></div>
   <div><b>{pct(v)}%</b><span>validadores atendidos</span></div>
   <div><b>{b['n_spe']}</b><span>SPEs/CNPJs do grupo na base</span></div>
   <div><b>{e(rp.get('qtd_lancamentos_2024_2026') or '–')}</b><span>lançamentos 2024–26</span></div>
  </div>
 </header>
 {sem_pesquisa}
 <div class="contato">
  <h3>Contato recomendado</h3>
  <p><b>{e(cr.get('nome') or '—')}</b> {('· ' + e(cr.get('cargo'))) if cr.get('cargo') else ''}<br>
  Canal: {e(cr.get('canal') or '—')}<br><span class="muted">{e(cr.get('por_que'))}</span></p>
 </div>
 <p class="just"><b>Por que está na lista:</b> {e(ad.get('justificativa') or '—')}</p>
 {f'<ul class="alertas">{alertas}</ul>' if alertas else ''}

 <h3>Parâmetros de validação</h3>
 {tabela(['', 'Validador', 'Detalhe'], [[f'<span class="ic {s}">{ICONE[s]}</span>', n, d] for n, s, d in v], 'val')}

 <h3>Como falar com a empresa</h3>
 <h4>Telefones</h4>{tabela(['Número', 'Tipo', 'Origem', 'Validação', ''], fones)}
 <h4>E-mails</h4>{tabela(['E-mail', 'Origem', 'Validação', ''], emails)}
 <p><b>Endereço comercial:</b> {e(end.get('texto') or '—')}{fonte(end.get('fonte'))}</p>
 {('<h4>Outros canais</h4>' + tabela(['Canal', 'Endereço'], canais)) if canais else ''}

 <h3>Quem manda</h3>
 <h4>Sócios na Receita (matriz)</h4>{tabela(['Nome', 'Tipo', 'Qualificação', ''], socios)}
 <h4>Controladores finais (subindo a cadeia de sócios PJ)</h4>{tabela(['Nome', 'Via', ''], ctrl)}
 <h4>Diretores e decisores</h4>{tabela(['Nome', 'Cargo', 'LinkedIn', 'Referências', ''], dec)}

 <h3>Portfólio e mercado</h3>
 <p><b>Total de projetos:</b> {e(rp.get('qtd_total_projetos') or '—')} ·
    <b>Faixa de preço:</b> {e(rp.get('faixa_preco_m2') or '—')} ·
    <b>Tipologia:</b> {e(rp.get('tipologia_principal') or b['tipologias'] or '—')}<br>
    <b>Onde atua:</b> {e(', '.join(rp.get('bairros_cidades') or []) or b['regioes'] or '—')}</p>
 {tabela(['Empreendimento', 'Local', 'Status', 'Unid.', 'Área m²', 'Preço/m²', 'MCMV', ''], emps, 'emp')}
 <h4>Página inicial do site</h4>{img_site(b['dominio'])}

 <h3>Saúde da empresa</h3>
 <p><b>Situação cadastral:</b> {e(sa.get('situacao_cadastral') or '—')} ·
    <b>Idade:</b> {e(sa.get('idade_empresa_anos') or '—')} anos ·
    <b>Reclame Aqui:</b> {e(' '.join(x for x in (str(ra.get('nota') or ''), ra.get('reputacao') or '') if x) or 'sem página')}{fonte(ra.get('fonte'))} ·
    <b>Recuperação judicial/falência:</b> {e(sa.get('recuperacao_judicial_ou_falencia') or '—')}</p>
 {f'<h4>Pontos de atenção</h4><ul>{neg}</ul>' if neg else ''}
 {f'<h4>Sinais positivos</h4><ul>{pos_}</ul>' if pos_ else ''}

 <h3>Base da Receita (jul/2026)</h3>
 <p>{b['n_cnpj']} CNPJs no grupo · {b['n_spe']} SPEs/incorporação · {b['spe_desde_2023']} abertas desde 2023 ·
    capital somado {brl(b['capital_total'])} · coesão de sócios {int(b['coesao_socios'] * 100)}%<br>
    <span class="muted">Contatos da Receita repetidos em 5 ou mais grupos sem relação (contador provável):
    {e(b['fones_contador'] or 'nenhum')} {e(b['emails_contador'])}</span></p>
 <h4>CNPJs mais recentes do grupo</h4>{tabela(['CNPJ', 'Razão social', 'Início', 'Bairro'], spes, 'spe')}
 <p class="rodape">Pesquisa em {e(g(p, 'data_pesquisa') or HOJE)}. Só contatos profissionais publicados pela empresa,
 por órgão oficial ou pela pessoa como representante da empresa.</p>
</section>"""

# ---------------------------------------------------------------- montagem
CSS = """
/* Layout: ficha de uma coluna, leitura de cima para baixo; tabelas rolam dentro do proprio bloco */
:root{--bg:#fbfbf9;--fg:#1c2228;--mut:#5f6b76;--bd:#dde1e4;--soft:#f0f2f1;--ac:#1f6f5c;--ok:#1a7a43;--pa:#a36100;--fa:#b3261e;
--warn-bg:#fdf1dc;--warn-fg:#6e4400;--display:"Archivo",Arial,sans-serif;--body:"Source Sans 3",-apple-system,Segoe UI,Roboto,sans-serif;--mono:"JetBrains Mono",ui-monospace,monospace}
@media (prefers-color-scheme: dark){:root:not([data-theme="light"]){--bg:#121615;--fg:#e4e8e6;--mut:#9aa6a1;--bd:#2b3331;--soft:#1a201e;--ac:#5fc0a3;--ok:#58c98a;--pa:#e9b25c;--fa:#ff8a80;--warn-bg:#35280f;--warn-fg:#f3d6a2;color-scheme:dark}}
:root[data-theme="dark"]{--bg:#121615;--fg:#e4e8e6;--mut:#9aa6a1;--bd:#2b3331;--soft:#1a201e;--ac:#5fc0a3;--ok:#58c98a;--pa:#e9b25c;--fa:#ff8a80;--warn-bg:#35280f;--warn-fg:#f3d6a2;color-scheme:dark}
@media print{:root,:root:not([data-theme="light"]){--bg:#fff;--fg:#1c2228;--mut:#5f6b76;--bd:#dde1e4;--soft:#f0f2f1;--ac:#1f6f5c;--ok:#1a7a43;--pa:#a36100;--fa:#b3261e;--warn-bg:#fdf1dc;--warn-fg:#6e4400;color-scheme:light}}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--fg);font:15px/1.5 var(--body)}
main{max-width:1000px;margin:0 auto;padding-block:24px;padding-inline:16px}
a{color:var(--ac);text-decoration:none;overflow-wrap:anywhere}a:hover,a:focus-visible{text-decoration:underline}a.src{font-size:11px;color:var(--mut)}
h1,h2,h3{font-family:var(--display);text-wrap:balance;letter-spacing:-.01em}
h1{font-size:28px;margin:0 0 4px}h2{font-size:23px;margin:4px 0}h3{font-size:16px;margin:24px 0 8px;padding-bottom:4px;border-bottom:2px solid var(--bd)}
h4{font-size:12px;margin:14px 0 6px;color:var(--mut);text-transform:uppercase;letter-spacing:.06em;font-family:var(--body)}
table{width:100%;border-collapse:collapse;font-size:13px;margin-bottom:6px;font-variant-numeric:tabular-nums}th,td{text-align:left;padding:5px 6px;border-bottom:1px solid var(--bd);vertical-align:top}
th{background:var(--soft);font-weight:600}.wrap{overflow-x:auto}
.muted,.sub{color:var(--mut)}.vazio{color:var(--mut);font-style:italic;margin:2px 0 8px}
.ficha{border-top:3px solid var(--ac);padding-top:14px;margin-top:36px}
.pos{font:600 13px var(--mono);color:var(--mut)}.eixo{font-size:11px;padding:2px 8px;border-radius:10px;background:var(--soft);border:1px solid var(--bd)}
.eixo.mcmv{color:var(--ok)}.eixo.medio{color:var(--ac)}
.kpis{display:grid;grid-template-columns:repeat(5,minmax(0,1fr));gap:8px;margin:12px 0}
.kpis div{background:var(--soft);border-radius:6px;padding:8px 10px}.kpis b{font:600 19px var(--mono);display:block}.kpis span{font-size:11px;color:var(--mut)}
.contato{background:var(--soft);padding:10px 14px;border-radius:6px}.contato h3{border:0;margin:0 0 4px;padding:0;color:var(--ok)}
.selo{font-size:11px;white-space:nowrap}.selo.ok,.ic.ok{color:var(--ok)}.selo.parcial,.ic.parcial{color:var(--pa)}.selo.falha,.ic.falha{color:var(--fa)}.selo.nd,.ic.nd{color:var(--mut)}
.ic{font-weight:700}table.val td:first-child{width:22px;text-align:center}
.alertas{background:var(--warn-bg);color:var(--warn-fg);border-radius:6px;padding:8px 8px 8px 26px}
.alerta{color:var(--fa)}img.print{max-width:100%;border:1px solid var(--bd);border-radius:6px}
.semprint{border:1px dashed var(--bd);padding:14px;color:var(--mut);border-radius:6px;font-size:12px}
code{font:12px var(--mono)}.rodape{font-size:11px;color:var(--mut);margin-top:14px}
.rank td:nth-child(n+3):nth-child(-n+6){white-space:nowrap}.rank td:nth-child(7){min-width:180px}
@media (max-width:700px){.kpis{grid-template-columns:repeat(2,minmax(0,1fr))}table{display:block;overflow-x:auto}}
@page{size:A4;margin:12mm}
@media print{.ficha{break-before:page;margin-top:0;border-top:0}h3,h4{break-after:avoid}tr,img{break-inside:avoid}a.src{display:none}main{padding:0}.voltar{display:none}}
"""

FONTES = ('<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wght@600;700'
          '&family=JetBrains+Mono:wght@400;600&family=Source+Sans+3:wght@400;600;700&display=swap">')

def pagina(titulo, corpo, esqueleto=True):
    """esqueleto=False: sem doctype/head, para a pagina principal do Artifact."""
    miolo = f"<title>{e(titulo)}</title>{FONTES}<style>{CSS}</style><main>{corpo}</main>"
    if not esqueleto:
        return miolo
    return f"""<!doctype html><html lang="pt-BR"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">{miolo.replace("<main>", "</head><body><main>", 1)}</body></html>"""

def main():
    itens = []
    for b in SEL:
        p = pesquisa(b["dominio"])
        v = validadores(b, p)
        ad = num(g(p, "aderencia_hadron", "nota_0a10"), 0)
        cf = num(g(p, "confianca_geral_0a10"), 0)
        prioridade = round(0.5 * ad * 10 + 0.3 * cf * 10 + 0.2 * pct(v), 1)
        itens.append((prioridade, b, p, v))
    itens.sort(key=lambda t: -t[0])

    linhas = []
    for i, (pr, b, p, v) in enumerate(itens, 1):
        cr = g(p, "contato_recomendado") or {}
        fone = next((fmt_fone(t["numero"]) for t in g(p, "telefones", default=[]) if t.get("validado") == "confirmado"), "")
        linhas.append([str(i), f'<a href="{e(b["dominio"])}.html"><b>{e(g(p, "nome_comercial") or b["nome"])}</b></a><br>'
                       f'<span class="muted">{e(b["dominio"])}</span>',
                       "MCMV" if b["eixo"] == "mcmv" else "Médio", str(pr),
                       e(g(p, "aderencia_hadron", "nota_0a10", default="–")), f"{pct(v)}%",
                       e(cr.get("nome") or "—") + (f'<br><span class="muted">{e(cr.get("cargo"))}</span>' if cr.get("cargo") else ""),
                       e(fone)])
    n_pesq = sum(1 for _, _, p, _ in itens if p)
    intro = f"""
<h1>Construtoras-alvo · RMBH</h1>
<p class="sub">Mapeamento para apresentar projetos novos · gerado em {HOJE} · {len(itens)} fichas ({n_pesq} com pesquisa web)</p>
<h3>Critérios (conversa do grupo Hadron – Estratégico)</h3>
<ol><li>Prédios com mais de 36 unidades</li><li>Venda entre R$ 10 mil e R$ 14 mil/m² (sem alto padrão), ou</li>
<li>MCMV em BH, Contagem, Betim e Ribeirão das Neves</li><li>Empresa com site</li><li>Área construída acima de 3.000 m²</li>
<li>Bairros sugeridos: Serra, Sion, Buritis, Palmeiras, Estoril, Ouro Preto, Paquetá, Santa Terezinha, Manacás, Engenho Nogueira,
Grajaú, Nova Suíça, Gameleira, Alto Vera Cruz, Boa Vista, Pompéia, São Geraldo, Esplanada, Taquaril e Saudade</li></ol>
<h3>Como a lista foi feita</h3>
<p>1) Base da Receita de jul/2026 (15.681 CNPJs de construção e incorporação em BH), agrupada pelo domínio do site: cada grupo
reúne a construtora e as SPEs dela (2.103 grupos). 2) Retirados os contatos de contador: telefones e e-mails que se repetem em 5 ou mais grupos
sem relação (192 telefones e 164 e-mails), provedores de e-mail e domínios de contabilidade. 3) Pontuação por volume de SPEs,
SPEs abertas desde 2023, padrão médio ou econômico/MCMV, bairros-alvo, site que bate com o nome, Instagram e coesão dos sócios. Gigantes com
projeto interno (MRV, Direcional, Cyrela, Patrimar, Emccamp) foram rebaixados. 4) Das 100 primeiras, 30 foram escolhidas
(10 MCMV e 20 de padrão médio). Cada uma foi pesquisada na web: site, Instagram, LinkedIn, sócios e controladores, decisores,
empreendimentos, Reclame Aqui, processos e notícias.</p>
<p><b>Prioridade</b> = 50% aderência ao perfil Hadron + 30% confiança dos dados + 20% validadores atendidos.</p>
<h3>Ranking</h3>
<div class="wrap">{tabela(['#', 'Construtora', 'Eixo', 'Prioridade', 'Aderência', 'Validação', 'Contato recomendado', 'Telefone confirmado'], linhas, 'rank')}</div>
<h3>Limites desta versão</h3>
<ul><li>O ambiente não tinha acesso direto aos sites. A pesquisa usou o buscador, e "site no ar" e as capturas de tela ficam
pendentes até rodar <code>scripts/04_capturar_sites.js</code> com a rede liberada.</li>
<li>Sócios vêm da Receita de jul/2026. S/A não lista acionistas: nesses casos o controlador vem de notícia ou de site.</li>
<li>O preço/m² só aparece quando algum portal ou notícia publicou. Onde está vazio, precisa ser conferido com corretor ou estande.</li>
<li>A base marca bairros por substring ("sion" casa com "profissional"). Por isso a citação de bairro pesou pouco na nota.</li></ul>"""

    anexo = tabela(["#", "Grupo (domínio)", "Nome na Receita", "SPEs", "desde 2023", "Padrão (site)", "MCMV", "Nota base"],
                   [[str(i), e(t["dominio"]), e(t["nome"]), str(t["n_spe"]), str(t["spe_desde_2023"]), e(t["padrao"]),
                     "sim" if t["mcmv"] else "", str(t["score"])] for i, t in enumerate(TOP, 1)])
    anexo_html = f'<section class="ficha"><h2>Anexo · 100 grupos mapeados pela base</h2><p class="sub">Ordenados pela nota automática. As 30 fichas saíram daqui.</p><div class="wrap">{anexo}</div></section>'

    out = R / "fichas"
    out.mkdir(exist_ok=True)
    fichas = [ficha(b, p, i) for i, (_, b, p, _) in enumerate(itens, 1)]
    for (_, b, p, _), f in zip(itens, fichas):
        (out / f"{b['dominio']}.html").write_text(
            pagina(g(p, "nome_comercial") or b["nome"], '<p class="voltar"><a href="index.html">← voltar ao ranking</a></p>' + f), encoding="utf-8")
    (out / "index.html").write_text(pagina("Construtoras-alvo RMBH", intro + anexo_html), encoding="utf-8")
    (out / "relatorio.html").write_text(pagina("Construtoras-alvo RMBH", intro + "".join(fichas) + anexo_html), encoding="utf-8")
    (out / "artifact_index.html").write_text(pagina("Construtoras-alvo RMBH", intro + anexo_html, esqueleto=False), encoding="utf-8")
    print(f"{len(fichas)} fichas ({n_pesq} com pesquisa) -> {out}")

if __name__ == "__main__":
    main()
