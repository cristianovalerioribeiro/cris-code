#!/usr/bin/env python3
"""Gerador do site DALETH.

Cada página vive em paginas/<nome>.html: um bloco de metadados em JSON no topo
(<!--meta {...} -->) e o conteúdo do <main> logo abaixo. Este script monta o
resto (cabeçalho, faixa do slogan, migalhas, fecho, rodapé, SEO e dados
estruturados) e grava o site pronto em dist/.

Uso:
    python3 build.py              # produção: URLs limpas (/empresas/)
    python3 build.py --local      # prévia: links relativos com index.html,
                                  # abre direto do disco ou em qualquer hospedagem

Sem dependências fora da biblioteca padrão.
"""
import html
import json
import re
import shutil
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent
DIST = RAIZ / "dist"

DOMINIO = "https://daleth.iajudite.com.br"

# Decisões que continuam com o Cristiano (ver PENDENCIAS.md). Enquanto PREVIA for
# True, todas as páginas saem com noindex e o rodapé avisa que o site é preliminar.
PREVIA = True
# O canal de contato ainda não foi definido. Com False, o formulário não envia e
# diz isso com clareza; com True, passa a usar o Netlify Forms.
FORMULARIO_ATIVO = False

SLOGAN = "Ao seu lado na construção da sua história."

# Ordem das vertentes: a do menu e das Regras (Empresas · Empreendimentos · Capital).
# A ordem final ainda está em aberto no Caderno de Definições (2.3); se mudar, muda só aqui.
VERTENTES = [
    ("/empresas/", "Empresas"),
    ("/empreendimentos/", "Empreendimentos"),
    ("/capital/", "Capital"),
]
# Simulador no topo: decisão do Cristiano em 28/09 (é a prova mais forte do site).
MENU_APOIO = [
    ("/empreendimentos/simulador/", "Simulador"),
    ("/metodo/", "Método"),
    ("/sobre/", "Sobre"),
]
CTA = "Analisar meu caso"   # um rótulo só para a ação principal, em todo o site

# Fecho padrão de quem ainda não decidiu: as três garantias aparecem só nas
# páginas que pedem (para não repetir a mesma frase em todas).
GARANTIAS = """<ul class="garantias">
<li><strong>Sem compromisso.</strong> A conversa de enquadramento não obriga a nada, e o diagnóstico não obriga a seguir adiante.</li>
<li><strong>Escopo escrito.</strong> Prazo e valor definidos caso a caso, antes de começar.</li>
<li><strong>Confidencialidade.</strong> Documentos e números do cliente não circulam fora do trabalho.</li>
</ul>"""


def ler_paginas():
    paginas = []
    for arq in sorted((RAIZ / "paginas").glob("*.html")):
        bruto = arq.read_text(encoding="utf-8")
        m = re.match(r"\s*<!--meta\s*(\{.*?\})\s*-->\s*", bruto, re.S)
        if not m:
            sys.exit(f"{arq.name}: falta o bloco <!--meta {{...}} -->")
        meta = json.loads(m.group(1))
        meta["corpo"] = bruto[m.end():]
        meta.setdefault("caminho", "/")
        paginas.append(meta)
    return paginas


def esc(t):
    return html.escape(t, quote=True)


# ---------------------------------------------------------------- links

def relativizador(caminho, local):
    """Devolve uma função que converte '/x/y/' no link certo para a página."""
    if not local:
        return lambda alvo: alvo
    profundidade = caminho.strip("/").count("/") + 1 if caminho.strip("/") else 0
    prefixo = "../" * profundidade

    def rel(alvo):
        if not alvo.startswith("/") or alvo.startswith("//"):
            return alvo
        base, _, ancora = alvo.partition("#")
        base, _, consulta = base.partition("?")
        base = base.lstrip("/")
        if base == "" or base.endswith("/"):
            base += "index.html"
        return prefixo + base + ("?" + consulta if consulta else "") + ("#" + ancora if ancora else "")
    return rel


def reescrever_links(texto, rel):
    return re.sub(r'(href|src|action)="(/[^"]*)"',
                  lambda m: f'{m.group(1)}="{rel(m.group(2))}"', texto)


# ---------------------------------------------------------------- blocos

def bloco_migalhas(pg):
    trilha = pg.get("migalhas")
    if not trilha:
        return ""
    itens = ['<li><a href="/">Início</a></li>']
    for rotulo, alvo in trilha[:-1]:
        itens.append(f'<li><a href="{alvo}">{esc(rotulo)}</a></li>')
    itens.append(f'<li aria-current="page">{esc(trilha[-1][0])}</li>')
    return ('<nav class="migalhas" aria-label="Você está em"><div class="wrap"><ol>'
            + "".join(itens) + "</ol></div></nav>")


def bloco_cabecalho(pg):
    atual = pg["caminho"]

    def item(alvo, rotulo, classe=""):
        ativo = atual == alvo or (alvo != "/" and atual.startswith(alvo))
        if alvo == "/empreendimentos/" and atual.startswith("/empreendimentos/simulador/"):
            ativo = False
        marca = ' aria-current="page"' if ativo else ""
        return f'<li><a href="{alvo}"{marca} class="{classe}">{rotulo}</a></li>'

    vert = "".join(item(a, r, "nav-vertente") for a, r in VERTENTES)
    apoio = "".join(item(a, r) for a, r in MENU_APOIO)
    return f"""<a class="pular" href="#conteudo">Pular para o conteúdo</a>
<header class="topo" id="topo">
  <div class="wrap topo-linha">
    <a class="marca" href="/" aria-label="DALETH, Estruturação de Negócios: página inicial">
      <img src="/assets/marca/horizontal-color.svg" alt="" width="190" height="50">
    </a>
    <a class="btn btn-primario cta-movel" href="/contato/">Conversar</a>
    <button class="menu-botao" type="button" aria-expanded="false" aria-controls="menu">
      <span class="menu-icone" aria-hidden="true"></span><span class="menu-texto">Menu</span>
    </button>
    <nav class="menu" id="menu" aria-label="Principal">
      <ul class="menu-vertentes">{vert}</ul>
      <ul class="menu-apoio">{apoio}</ul>
      <a class="btn btn-primario menu-cta" href="/contato/">{CTA}</a>
    </nav>
  </div>
</header>
<a class="barra-cta" href="/contato/" hidden>{CTA}<span>Conversa de enquadramento, sem custo</span></a>
<div class="faixa-slogan" role="note" aria-label="Assinatura">
  <div class="wrap"><p>{SLOGAN}</p></div>
</div>"""


def bloco_fecho(pg):
    f = pg.get("fecho")
    if not f:
        return ""
    garantias = GARANTIAS if f.get("garantias") else ""
    secundario = ""
    if f.get("secundario"):
        alvo, rotulo = f["secundario"]
        secundario = f'<a class="link" href="{alvo}">{esc(rotulo)}</a>'
    contato = "/contato/" + (f"?momento={pg['momento']}&amp;origem={pg['caminho'].strip('/').replace('/', '-') or 'inicio'}"
                             if pg.get("momento") else "")
    return f"""<section class="fecho" aria-labelledby="fecho-titulo">
  <div class="wrap">
    <p class="rotulo">{esc(f.get("rotulo", "Como começa"))}</p>
    <h2 id="fecho-titulo">{esc(f["titulo"])}</h2>
    <p class="lead">{f["texto"]}</p>
    <div class="acoes">
      <a class="btn btn-ouro" href="{contato}">{esc(f.get("botao", CTA))}</a>
      {secundario}
    </div>
    {garantias}
  </div>
</section>"""


def bloco_rodape():
    vert = "".join(f'<li><a href="{a}">{r}</a></li>' for a, r in VERTENTES)
    previa = ('<p class="aviso-previa">Versão preliminar do site, em construção.</p>'
              if PREVIA else "")
    return f"""<footer class="rodape">
  <div class="wrap rodape-grade">
    <div class="rodape-marca">
      <img src="/assets/marca/horizontal-color.svg" alt="DALETH, Estruturação de Negócios" width="180" height="48">
      <p>Estruturação de negócios imobiliários para construtoras, incorporadoras, investidores e proprietários.</p>
      <p class="rodape-slogan">{SLOGAN}</p>
    </div>
    <nav aria-label="Atuação">
      <p class="rotulo">Atuação</p>
      <ul>{vert}
        <li><a href="/empreendimentos/obra-parada/">Obras paradas</a></li>
      </ul>
    </nav>
    <nav aria-label="Ferramentas e método">
      <p class="rotulo">Para decidir</p>
      <ul>
        <li><a href="/empreendimentos/simulador/">Simulador de exposição de caixa</a></li>
        <li><a href="/empreendimentos/permuta-de-terreno/">Vender, permutar ou incorporar um terreno</a></li>
        <li><a href="/metodo/">Método</a></li>
        <li><a href="/metodo/modelagens/">As nove modelagens</a></li>
      </ul>
    </nav>
    <nav aria-label="Institucional">
      <p class="rotulo">DALETH</p>
      <ul>
        <li><a href="/como-comeca/">Como começa um trabalho</a></li>
        <li><a href="/sobre/">Sobre</a></li>
        <li><a href="/contato/">Contato</a></li>
      </ul>
      <p class="rodape-local">Belo Horizonte · atuação nacional</p>
    </nav>
  </div>
  <div class="wrap"><div class="rodape-base">
    <p>© 2026 DALETH. Os números das ferramentas são exemplos ilustrativos, e não leitura de um projeto real.</p>
    {previa}
  </div></div>
</footer>"""


# ---------------------------------------------------------------- SEO

def json_ld(pg, url):
    grafo = [{
        "@type": "Organization",
        "@id": DOMINIO + "/#org",
        "name": "DALETH",
        "description": "Estruturação de negócios imobiliários",
        "url": DOMINIO + "/",
        "logo": DOMINIO + "/assets/marca/vertical-color.svg",
        "slogan": SLOGAN,
        "areaServed": "BR",
        "address": {"@type": "PostalAddress", "addressLocality": "Belo Horizonte",
                    "addressRegion": "MG", "addressCountry": "BR"},
    }]
    if pg.get("migalhas"):
        itens = [{"@type": "ListItem", "position": 1, "name": "Início", "item": DOMINIO + "/"}]
        for i, (rotulo, alvo) in enumerate(pg["migalhas"], start=2):
            itens.append({"@type": "ListItem", "position": i, "name": rotulo,
                          "item": DOMINIO + alvo})
        grafo.append({"@type": "BreadcrumbList", "itemListElement": itens})
    if pg.get("servico"):
        grafo.append({"@type": "Service", "name": pg["servico"], "url": url,
                      "provider": {"@id": DOMINIO + "/#org"}, "areaServed": "BR"})
    if pg.get("pessoa"):
        # sem sameAs enquanto o LinkedIn não for definido (Caderno de Definições 1.3)
        grafo.append({"@type": "Person", "name": "Cristiano Valério Ribeiro",
                      "jobTitle": "Fundador", "worksFor": {"@id": DOMINIO + "/#org"}})
    faqs = re.findall(r'<details class="faq">\s*<summary>(.*?)</summary>\s*(.*?)</details>',
                      pg["corpo"], re.S)
    if faqs:
        limpar = lambda t: re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", t)).strip()
        grafo.append({"@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": limpar(q),
             "acceptedAnswer": {"@type": "Answer", "text": limpar(r)}} for q, r in faqs]})
    dados = {"@context": "https://schema.org", "@graph": grafo}
    return ('<script type="application/ld+json">'
            + json.dumps(dados, ensure_ascii=False, separators=(",", ":")) + "</script>")


def inserir_indice(corpo):
    """Na abertura das páginas internas, um índice com os H2 da página (só aparece no desktop)."""
    m = re.search(r'(<section class="abertura">\s*<div class="wrap">)(.*?)(</div>\s*</section>)', corpo, re.S)
    if not m:
        return corpo
    titulos = re.findall(r'<h2 id="([^"]+)"(?: class="(?!oculto)[^"]*")?>(.*?)</h2>', corpo[m.end():], re.S)
    titulos = [(i, re.sub(r"<[^>]+>", "", t).strip()) for i, t in titulos if i != "fecho-titulo"][:6]
    if len(titulos) < 3:
        indice = ""
    else:
        itens = "".join(f'<li><a href="#{i}">{t}</a></li>' for i, t in titulos)
        indice = f'<nav class="indice" aria-label="Nesta página"><p class="rotulo">Nesta página</p><ol>{itens}</ol></nav>'
    return (corpo[:m.start()] + m.group(1) + '<div class="abertura-texto">' + m.group(2) + "</div>"
            + indice + m.group(3) + corpo[m.end():])


def montar(pg, local):
    url = DOMINIO + pg["caminho"]
    titulo = pg["titulo"] if pg["caminho"] == "/" or pg.get("sem_sufixo") else f'{pg["titulo"]} · DALETH'
    robots = '<meta name="robots" content="noindex, nofollow">' if PREVIA or pg.get(
        "noindex") else ""
    scripts = "".join(f'<script src="/assets/js/{s}" defer></script>'
                      for s in pg.get("scripts", []))
    corpo = pg["corpo"]
    if "{{CENARIO}}" in corpo:
        import cenario
        corpo = corpo.replace("{{CENARIO}}", cenario.svg())
    if "{{QUADRO}}" in corpo:
        import modelo
        corpo = corpo.replace("{{QUADRO}}", modelo.quadro())
    corpo = inserir_indice(corpo)
    if "{{FORM_ATRIBUTOS}}" in corpo:
        attrs = ('name="contato" method="POST" data-netlify="true" '
                 'netlify-honeypot="bot-field" action="/contato/recebido/"'
                 if FORMULARIO_ATIVO else 'data-inativo="true" method="post"')
        corpo = corpo.replace("{{FORM_ATRIBUTOS}}", attrs)
        corpo = corpo.replace("{{FORM_AVISO}}", "" if FORMULARIO_ATIVO else (
            '<p class="aviso-form" id="aviso-form">Prévia: o envio ainda não está ligado. '
            'O canal de contato entra quando for definido.</p>'))
    classe = pg.get("classe_body", "")
    pagina = f"""<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(titulo)}</title>
<meta name="description" content="{esc(pg["descricao"])}">
{robots}
<link rel="canonical" href="{url}">
<meta property="og:type" content="website">
<meta property="og:locale" content="pt_BR">
<meta property="og:site_name" content="DALETH">
<meta property="og:title" content="{esc(pg.get("og_titulo", pg["titulo"]))}">
<meta property="og:description" content="{esc(pg["descricao"])}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{DOMINIO}/assets/og.png">
<meta name="theme-color" content="#082538">
<link rel="icon" href="/assets/favicon.svg" type="image/svg+xml">
<link rel="preload" href="/assets/fonts/source-serif-4-normal-latin.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="/assets/fonts/inter-latin.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/assets/site.css">
{json_ld(pg, url)}
<script src="/assets/js/site.js" defer></script>
{scripts}
</head>
<body class="{classe}">
{bloco_cabecalho(pg)}
{bloco_migalhas(pg)}
<main id="conteudo" tabindex="-1">
{corpo}
{bloco_fecho(pg)}
</main>
{bloco_rodape()}
</body>
</html>
"""
    base = "/" if pg.get("arquivo") else pg["caminho"]   # 404.html fica na raiz
    return reescrever_links(pagina, relativizador(base, local))


def gerar(local=False):
    if DIST.exists():
        shutil.rmtree(DIST)
    shutil.copytree(RAIZ / "assets", DIST / "assets")
    paginas = ler_paginas()
    for pg in paginas:
        destino = DIST / pg["caminho"].strip("/") / "index.html"
        if pg.get("arquivo"):
            destino = DIST / pg["arquivo"]
        destino.parent.mkdir(parents=True, exist_ok=True)
        destino.write_text(montar(pg, local), encoding="utf-8")
    # arquivos de servidor (Netlify)
    for nome in ("_headers", "_redirects"):
        if (RAIZ / nome).exists():
            shutil.copy(RAIZ / nome, DIST / nome)
    robots = "User-agent: *\nDisallow: /\n" if PREVIA else (
        f"User-agent: *\nAllow: /\n\nSitemap: {DOMINIO}/sitemap.xml\n")
    (DIST / "robots.txt").write_text(robots, encoding="utf-8")
    urls = [p for p in paginas if not p.get("noindex") and not p.get("arquivo")]
    (DIST / "sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        + "".join(f"  <url><loc>{DOMINIO}{p['caminho']}</loc></url>\n" for p in urls)
        + "</urlset>\n", encoding="utf-8")
    print(f"{len(paginas)} páginas geradas em {DIST.relative_to(RAIZ.parent.parent)}"
          + (" (modo local)" if local else ""))


if __name__ == "__main__":
    gerar(local="--local" in sys.argv)
