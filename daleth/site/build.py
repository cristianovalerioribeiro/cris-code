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
HOME_SOLTA = RAIZ / "home" / "index.html"   # página única na raiz; a home gerada vai para /anterior/

DOMINIO = "https://daleth.iajudite.com.br"

# Decisões que continuam com o Cristiano (ver PENDENCIAS.md). Enquanto PREVIA for
# True, todas as páginas saem com noindex e o rodapé avisa que o site é preliminar.
PREVIA = True
# Faixa "versão preliminar" no rodapé. O site já está no ar (GitHub Pages); o noindex
# continua enquanto o domínio definitivo não for escolhido (Caderno 1.3).
AVISO_PREVIA = False

# Canal de contato (Caderno 1.1). Preencha e o site passa a mostrar/usar o que existir.
CONTATO = {
    "email": "",        # recebe o formulário quando FORMULARIO = "email"
    "whatsapp": "",     # só números, com DDI e DDD: 5531999999999
    "linkedin": "",     # URL do perfil; também entra no schema Person (sameAs)
}
# Como o formulário envia:
#   ""         ainda não envia e diz isso com clareza (padrão até o canal ser definido)
#   "email"    abre o e-mail de quem escreve já preenchido para CONTATO["email"] (funciona em qualquer hospedagem)
#   "netlify"  Netlify Forms (só quando o site estiver hospedado no Netlify)
FORMULARIO = ""

SLOGAN = "Ao seu lado na construção da sua história."

# Ordem das vertentes: a do menu e das Regras (Empresas · Empreendimentos · Capital).
# A ordem final ainda está em aberto no Caderno de Definições (2.3); se mudar, muda só aqui.
VERTENTES = [
    ("/empresas/", "Empresas"),
    ("/empreendimentos/", "Empreendimentos"),
    ("/capital/", "Capital"),
]
# Submenus das vertentes (a vertente continua visível no topo; os filhos abrem no hover/foco).
SUBMENUS = {
    "/empresas/": [("/empresas/", "Gestão, financeiro e societário"),
                   ("/empresas/preparacao-para-credito/", "Preparação para crédito")],
    "/empreendimentos/": [("/empreendimentos/", "Do terreno à entrega"),
                          ("/empreendimentos/estudo-de-viabilidade/", "Estudo de viabilidade"),
                          ("/empreendimentos/permuta-de-terreno/", "Vender, permutar ou incorporar"),
                          ("/empreendimentos/obra-parada/", "Obras paradas")],
    "/capital/": [("/capital/", "Crédito e capital"),
                  ("/capital/financiamento-a-producao/", "Financiamento à produção")],
    "/metodo/": [("/metodo/", "Os quatro movimentos"),
                 ("/metodo/modelagem/", "Modelagem: tudo conectado"),
                 ("/metodo/modelagens/", "As nove modelagens")],
}
# Ferramentas no topo: decisão do Cristiano em 28/09 (são a prova mais forte do site).
FERRAMENTAS = [
    ("/empreendimentos/simulador/", "Simulador de exposição de caixa"),
    ("/empreendimentos/permuta-de-terreno/#comp-t", "Comparador vender × permutar × incorporar"),
    ("/ferramentas/radar/", "Radar de estruturação"),
]
MENU_APOIO = [
    ("/inteligencia/", "Inteligência"),
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


# Variantes de copy em teste (variantes/vN/*.html): publicadas em /vN/..., com barra para alternar.
# Quando a escolha for feita, os textos escolhidos vão para paginas/ e as pastas somem.
VARIANTES = [("m1", "Trajetória"), ("m2", "Fachada"), ("m3", "Passagem")]
# uma linha por variante, para a página /variantes/
VARIANTES_DESC = {
    "m1": "Executar levou você até aqui. A frase vencedora dos júris como espinha; prova e método no corpo; fecho de parceria.",
    "m2": "O que sustenta um prédio não aparece na fachada. As decisões invisíveis, com a conta e as três alternativas; hero centrado.",
    "m3": "Oportunidade se enxerga. Realização se estrutura. O território potencial → estrutura → realização; hero claro; o nome em Sobre.",
}


def _ler(arq):
    bruto = arq.read_text(encoding="utf-8")
    m = re.match(r"\s*<!--meta\s*(\{.*?\})\s*-->\s*", bruto, re.S)
    if not m:
        sys.exit(f"{arq.name}: falta o bloco <!--meta {{...}} -->")
    meta = json.loads(m.group(1))
    meta["corpo"] = bruto[m.end():]
    meta.setdefault("caminho", "/")
    return meta


def ler_paginas():
    paginas = [_ler(a) for a in sorted((RAIZ / "paginas").glob("*.html"))]
    for v, nome in VARIANTES:
        pasta = RAIZ / "variantes" / v
        if not pasta.is_dir():
            continue
        for arq in sorted(pasta.glob("*.html")):   # só a pasta da variante, não as anteriores
            pg = _ler(arq)
            pg["variante"] = v
            pg["caminho_base"] = pg["caminho"]
            pg["caminho"] = "/" + v + pg["caminho"]
            pg["noindex"] = True
            paginas.append(pg)
    return paginas


def esc(t):
    return html.escape(t, quote=True)


# ---------------------------------------------------------------- links

def relativizador(caminho, local, raiz="/"):
    """Devolve uma função que converte '/x/y/' no link certo para a página.

    local: links relativos com index.html (abre do disco ou em qualquer pasta).
    raiz:  prefixo das URLs limpas, para publicar num subcaminho (GitHub Pages: /cris-code/).
    """
    if not local:
        if raiz == "/":
            return lambda alvo: alvo
        return lambda alvo: (raiz + alvo[1:]) if alvo.startswith("/") and not alvo.startswith("//") else alvo
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
    def troca(m):
        if m.group(1) == "srcset":
            # cada candidato ("/url 1280w, /url2 1672w") é reescrito separadamente
            partes = [c.strip() for c in m.group(2).split(",")]
            novas = []
            for c in partes:
                url, _, desc = c.partition(" ")
                url = rel(url) if url.startswith("/") else url
                novas.append((url + " " + desc).strip())
            return f'srcset="{", ".join(novas)}"'
        return f'{m.group(1)}="{rel(m.group(2))}"'
    return re.sub(r'(href|src|action|srcset)="(/[^"]*)"', troca, texto)


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

    def com_sub(alvo, rotulo, filhos, classe):
        base = item(alvo, rotulo, classe)[:-5]   # tira o </li>
        subs = "".join(f'<li><a href="{a}">{esc(r)}</a></li>' for a, r in filhos)
        return (base.replace("<li>", '<li class="tem-sub">', 1)
                + f'<ul class="sub" aria-label="{esc(rotulo)}">{subs}</ul></li>')

    vert = "".join(com_sub(a, r, SUBMENUS[a], "nav-vertente") if a in SUBMENUS
                   else item(a, r, "nav-vertente") for a, r in VERTENTES)
    ferr = ('<li class="tem-sub"><a href="/empreendimentos/simulador/" class="'
            + ('ativo' if atual.startswith(("/ferramentas/", "/empreendimentos/simulador/")) else '')
            + '">Ferramentas</a><ul class="sub" aria-label="Ferramentas">'
            + "".join(f'<li><a href="{a}">{esc(r)}</a></li>' for a, r in FERRAMENTAS) + "</ul></li>")
    apoio = ferr + "".join(com_sub(a, r, SUBMENUS[a], "") if a in SUBMENUS else item(a, r) for a, r in MENU_APOIO)
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
      <a class="btn btn-primario menu-cta" href="/contato/">{esc(pg.get("cta", CTA))}</a>
    </nav>
  </div>
</header>
<a class="barra-cta" href="/contato/" hidden>{esc(pg.get("cta", CTA))}<span>Conversa de enquadramento, sem custo</span></a>
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
  <div class="palco-3d fecho-3d" aria-hidden="true"><canvas data-cena="rede"></canvas></div>
  <div class="wrap">
    <p class="rotulo">{esc(f.get("rotulo", "Como começa"))}</p>
    <h2 id="fecho-titulo">{esc(f["titulo"])}</h2>
    <p class="lead">{f["texto"]}</p>
    <div class="acoes">
      <a class="btn btn-ouro" href="{contato}">{esc(f.get("botao", pg.get("cta", CTA)))}</a>
      {secundario}
    </div>
    {garantias}
    <div class="fecho-depois" aria-label="O que acontece depois">
      <ol>
        <li><span><strong>Conversa de enquadramento</strong>Sem custo e sem compromisso.</span></li>
        <li><span><strong>Diagnóstico de estruturação</strong>Só se fizer sentido para os dois lados.</span></li>
        <li><span><strong>Escopo escrito</strong>Prazo e entregas definidos antes de começar.</span></li>
      </ol>
    </div>
  </div>
</section>"""


def bloco_variantes(pg):
    """Barra para alternar entre a versão publicada e as variantes de copy (só nas páginas que têm variante)."""
    base = pg.get("caminho_base", pg["caminho"])
    existe = {v for v, _ in VARIANTES if (RAIZ / "variantes" / v).is_dir()
              and any(_ler(a)["caminho"] == base for a in (RAIZ / "variantes" / v).glob("*.html"))}
    if not existe:
        return ""
    atual = pg.get("variante", "")
    marca = ' aria-current="page"'
    itens = [f'<a href="{base}"{marca if not atual else ""}>Atual</a>']
    for v, nome in VARIANTES:
        if v in existe:
            itens.append(f'<a href="/{v}{base}"{marca if v == atual else ""}>{v.upper()}<span>{esc(nome)}</span></a>')
    return ('<nav class="seletor-variantes" aria-label="Versões de texto"><span class="sv-rot">Texto</span>'
            + "".join(itens) + '<a class="sv-caderno" href="/variantes/">Comparar</a></nav>')


def pagina_comparacao(paginas):
    """/variantes/: H1 e lead de cada página, na versão atual e em cada variante, para escolher."""
    por = {}
    for pg in paginas:
        base = pg.get("caminho_base", pg["caminho"])
        por.setdefault(base, {})[pg.get("variante", "atual")] = pg
    existe = [v for v, _ in VARIANTES if any(v in d for d in por.values())]
    if not existe:
        return None
    nomes = dict(VARIANTES)
    limpar = lambda t: re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", t or "")).strip()

    def resumo(pg):
        h1 = re.search(r"<h1[^>]*>(.*?)</h1>", pg["corpo"], re.S)
        lead = re.search(r'<p class="lead[^"]*">(.*?)</p>', pg["corpo"], re.S)
        cta = re.search(r'<a class="btn[^"]*"[^>]*>(.*?)</a>', pg["corpo"], re.S)
        return limpar(h1.group(1) if h1 else ""), limpar(lead.group(1) if lead else ""), limpar(cta.group(1) if cta else "")

    blocos = []
    for base, d in por.items():
        if not any(v in d for v in existe):
            continue
        cartoes = []
        for chave, rotulo in [("atual", "Atual, no ar")] + [(v, f"{v.upper()} · {nomes[v]}") for v in existe]:
            pg = d.get(chave)
            if not pg:
                cartoes.append(f'<article><p class="cp-rot">{esc(rotulo)}</p><p>Sem versão.</p></article>')
                continue
            h1, lead, cta = resumo(pg)
            cartoes.append(f'<article class="{"atual" if chave == "atual" else ""}"><p class="cp-rot">{esc(rotulo)}</p>'
                           f'<h3>{esc(h1)}</h3><p>{esc(lead)}</p>'
                           + (f'<p><strong>Botão:</strong> {esc(cta)}</p>' if cta else "")
                           + f'<a class="link" href="{pg["caminho"]}">Abrir a página</a></article>')
        titulo = d.get("atual", next(iter(d.values())))["titulo"]
        blocos.append(f'<div class="comparacao-pagina"><h2>{esc(titulo)}</h2><div class="comparacao-grade">{"".join(cartoes)}</div></div>')
    notas = "".join(f'<li><a href="/{v}/NOTAS.md">Notas da {v.upper()} · {esc(nomes[v])}</a></li>'
                    for v in existe if (RAIZ / "variantes" / v / "NOTAS.md").exists())
    corpo = f"""<section class="abertura"><div class="wrap">
  <p class="rotulo">Prévia · Para escolher</p>
  <h1>Três versões de texto, o mesmo site</h1>
  <p class="lead">Cada versão conta a mesma história com uma estratégia diferente. Compare página a página pelo título e pela primeira frase, abra cada uma e marque no caderno o que fica.</p>
  <ul class="lista-traco">{"".join(f'<li><strong>{v.upper()} · {esc(nomes[v])}:</strong> {esc(VARIANTES_DESC.get(v, ""))}</li>' for v in existe)}</ul>
  <p class="microcopy">A barra no canto da tela troca de versão em qualquer página que tenha variante. Esta página e as pastas das versões saem do ar quando a escolha for feita.</p>
</div></section>
<section class="secao"><div class="wrap comparacao">{"".join(blocos)}</div></section>
""" + (f'<section class="secao papel"><div class="wrap"><div class="cabeca"><p class="rotulo">Bastidores</p><h2 id="notas">Notas de cada versão</h2></div><ul class="lista-traco">{notas}</ul><p class="nota">Análise completa do texto atual: <a href="/variantes/ANALISE-COPY.md">ANALISE-COPY.md</a>.</p></div></section>' if notas else "")
    return {"caminho": "/variantes/", "titulo": "Versões de texto para escolher", "noindex": True,
            "descricao": "Prévia: três versões de texto do site DALETH, lado a lado, para escolher.",
            "migalhas": [["Versões de texto", "/variantes/"]], "corpo": corpo}


def bloco_rodape():
    itens = []
    if CONTATO["email"]:
        itens.append(f'<li><a href="mailto:{esc(CONTATO["email"])}">{esc(CONTATO["email"])}</a></li>')
    if CONTATO["whatsapp"]:
        itens.append(f'<li><a href="https://wa.me/{esc(CONTATO["whatsapp"])}" rel="noopener">WhatsApp</a></li>')
    if CONTATO["linkedin"]:
        itens.append(f'<li><a href="{esc(CONTATO["linkedin"])}" rel="noopener">LinkedIn</a></li>')
    contatos = f'<ul class="rodape-contatos">{"".join(itens)}</ul>' if itens else ""
    vert = "".join(f'<li><a href="{a}">{r}</a></li>' for a, r in VERTENTES)
    previa = ('<p class="aviso-previa">Versão preliminar do site, em construção.</p>'
              if AVISO_PREVIA else "")
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
        <li><a href="/empreendimentos/estudo-de-viabilidade/">Estudo de viabilidade</a></li>
        <li><a href="/capital/financiamento-a-producao/">Financiamento à produção</a></li>
        <li><a href="/empresas/preparacao-para-credito/">Preparação para crédito</a></li>
        <li><a href="/empreendimentos/obra-parada/">Obras paradas</a></li>
      </ul>
    </nav>
    <nav aria-label="Ferramentas e método">
      <p class="rotulo">Para decidir</p>
      <ul>
        <li><a href="/empreendimentos/simulador/">Simulador de exposição de caixa</a></li>
        <li><a href="/empreendimentos/permuta-de-terreno/">Vender, permutar ou incorporar um terreno</a></li>
        <li><a href="/ferramentas/radar/">Radar de estruturação</a></li>
        <li><a href="/metodo/">Método</a></li>
        <li><a href="/metodo/modelagem/">Modelagem: tudo conectado</a></li>
        <li><a href="/metodo/modelagens/">As nove modelagens</a></li>
        <li><a href="/inteligencia/">Inteligência</a></li>
      </ul>
    </nav>
    <nav aria-label="Institucional">
      <p class="rotulo">DALETH</p>
      <ul>
        <li><a href="/como-comeca/">Como começa um trabalho</a></li>
        <li><a href="/sobre/">Sobre</a></li>
        <li><a href="/contato/">Contato</a></li>
        <li><a href="/privacidade/">Privacidade</a></li>
      </ul>
      {contatos}
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
        pessoa = {"@type": "Person", "name": "Cristiano Valério Ribeiro",
                  "jobTitle": "Fundador", "worksFor": {"@id": DOMINIO + "/#org"}}
        if CONTATO["linkedin"]:
            pessoa["sameAs"] = [CONTATO["linkedin"]]
        grafo.append(pessoa)
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


def inserir_imagem(pg, corpo):
    """Prancha 3D renderizada da própria cena (assets/img/<nome>-3d.jpg), logo abaixo da abertura."""
    img = pg.get("imagem")
    if not img:
        return corpo
    nome, alt = img["arquivo"], esc(img["alt"])
    claro = " clara" if img.get("clara") else ""
    figura = (f'<figure class="prancha-3d{claro}"><picture>'
              f'<source media="(max-width: 600px)" srcset="/assets/img/{nome}-m.jpg">'
              f'<img src="/assets/img/{nome}.jpg" alt="{alt}" width="1600" height="520" decoding="async">'
              f'</picture></figure>')
    fim = corpo.find("</section>")
    return corpo if fim < 0 else corpo[:fim + 10] + "\n" + figura + corpo[fim + 10:]


def montar(pg, local, raiz="/"):
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
    corpo = inserir_imagem(pg, corpo)
    if "{{FORM_ATRIBUTOS}}" in corpo:
        modo = FORMULARIO if (FORMULARIO != "email" or CONTATO["email"]) else ""
        if modo == "netlify":
            attrs = ('name="contato" method="POST" data-netlify="true" '
                     'netlify-honeypot="bot-field" action="/contato/recebido/"')
            aviso = ""
        elif modo == "email":
            attrs = f'data-envio="email" data-destino="{esc(CONTATO["email"])}" method="post"'
            aviso = ('<p class="aviso-form" id="aviso-form">Ao enviar, o seu programa de e-mail abre com a mensagem '
                     'pronta. É só confirmar o envio.</p>')
        else:
            attrs = 'data-inativo="true" method="post"'
            aviso = ('<p class="aviso-form" id="aviso-form">O envio por aqui está em configuração e entra nos próximos dias.</p>')
        corpo = corpo.replace("{{FORM_ATRIBUTOS}}", attrs)
        corpo = corpo.replace("{{FORM_AVISO}}", aviso)
    classe = pg.get("classe_body", "")
    if "tema-claro-hero" in classe:
        corpo = corpo.replace('<canvas data-cena="heroi"', '<canvas data-cena="heroi" data-tema="claro"', 1)
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
<script src="/assets/js/cena3d.js" defer></script>
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
{bloco_variantes(pg)}
</body>
</html>
"""
    if pg.get("variante"):
        v = pg["variante"]
        proprias = {_ler(a)["caminho"] for a in (RAIZ / "variantes" / v).glob("*.html")}
        pagina = re.sub(r'href="(/[^"#?]*/)([#?][^"]*)?"',
                        lambda m: f'href="/{v}{m.group(1)}{m.group(2) or ""}"' if m.group(1) in proprias and not m.group(1).startswith("/" + v + "/") else m.group(0),
                        pagina)
    base = "/" if pg.get("arquivo") else pg["caminho"]   # 404.html fica na raiz
    return reescrever_links(pagina, relativizador(base, local, raiz))


def montar_home_solta(local, raiz="/", arquivo=None, caminho="/"):
    """A home é um arquivo pronto (home/index.html); aqui entram só robots, domínio, dados
    estruturados e os links reescritos para o modo local ou para a raiz publicada.
    Outros arquivos em home/ (ex.: v2.html) saem em /v2/, sem indexação: versões de teste."""
    texto = (arquivo or HOME_SOLTA).read_text(encoding="utf-8")
    robots = '<meta name="robots" content="noindex, nofollow">' if (PREVIA or caminho != "/") else ""
    pg = {"caminho": caminho, "corpo": texto, "pessoa": True}
    texto = (texto.replace("{{ROBOTS}}", robots).replace("{{DOMINIO}}", DOMINIO)
                  .replace("{{JSON_LD}}", json_ld(pg, DOMINIO + caminho)))
    return reescrever_links(texto, relativizador(caminho, local, raiz))


def paginas_de_redirecionamento(local, raiz):
    """Endereços antigos (_redirects) também viram páginas que levam ao novo endereço,
    para hospedagens sem regra de redirecionamento (GitHub Pages)."""
    arq = RAIZ / "_redirects"
    if not arq.exists():
        return 0
    n = 0
    for linha in arq.read_text(encoding="utf-8").splitlines():
        partes = linha.split()
        if len(partes) < 2 or linha.startswith("#") or not partes[0].endswith("/"):
            continue
        de, para = partes[0], partes[1]
        destino = DIST / de.strip("/") / "index.html"
        if destino.exists():
            continue
        alvo = relativizador(de, local, raiz)(para)
        destino.parent.mkdir(parents=True, exist_ok=True)
        destino.write_text(
            f'<!doctype html><html lang="pt-BR"><head><meta charset="utf-8">'
            f'<meta name="robots" content="noindex"><link rel="canonical" href="{DOMINIO}{para}">'
            f'<meta http-equiv="refresh" content="0; url={alvo}"><title>Endereço novo · DALETH</title></head>'
            f'<body><p>Esta página mudou de endereço: <a href="{alvo}">continuar</a>.</p></body></html>\n',
            encoding="utf-8")
        n += 1
    return n


def gerar(local=False, raiz="/"):
    if DIST.exists():
        shutil.rmtree(DIST)
    shutil.copytree(RAIZ / "assets", DIST / "assets")
    paginas = ler_paginas()
    home_solta = HOME_SOLTA.exists()
    if home_solta:
        for pg in paginas:
            if pg["caminho"] == "/" and not pg.get("variante"):
                pg["caminho"] = "/anterior/"
                pg["noindex"] = True
                pg["titulo"] = pg["titulo"] + " (home anterior)"
                pg["sem_sufixo"] = False
    comparacao = pagina_comparacao(paginas)
    if comparacao:
        paginas.append(comparacao)
        for v, _ in VARIANTES:   # as notas e a análise, para ler pelo navegador
            for arq in (RAIZ / "variantes" / v).glob("*.md"):
                (DIST / v).mkdir(parents=True, exist_ok=True)
                shutil.copy(arq, DIST / v / arq.name)
        for arq in (RAIZ / "variantes").glob("*.md"):
            (DIST / "variantes").mkdir(parents=True, exist_ok=True)
            shutil.copy(arq, DIST / "variantes" / arq.name)
    for pg in paginas:
        destino = DIST / pg["caminho"].strip("/") / "index.html"
        if pg.get("arquivo"):
            destino = DIST / pg["arquivo"]
        destino.parent.mkdir(parents=True, exist_ok=True)
        destino.write_text(montar(pg, local, raiz), encoding="utf-8")
    if home_solta:
        (DIST / "index.html").write_text(montar_home_solta(local, raiz), encoding="utf-8")
        for arq in sorted(HOME_SOLTA.parent.glob("*.html")):
            if arq.name == "index.html":
                continue
            destino = DIST / arq.stem / "index.html"
            destino.parent.mkdir(parents=True, exist_ok=True)
            destino.write_text(montar_home_solta(local, raiz, arq, f"/{arq.stem}/"), encoding="utf-8")
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
        + (f"  <url><loc>{DOMINIO}/</loc></url>\n" if home_solta else "")
        + "".join(f"  <url><loc>{DOMINIO}{p['caminho']}</loc></url>\n" for p in urls)
        + "</urlset>\n", encoding="utf-8")
    redirecionadas = paginas_de_redirecionamento(local, raiz)
    (DIST / ".nojekyll").write_text("", encoding="utf-8")   # GitHub Pages: servir as pastas como estão
    print(f"{len(paginas)} páginas geradas em {DIST.relative_to(RAIZ.parent.parent)}"
          + (" (modo local)" if local else "") + (f" sob {raiz}" if raiz != "/" else "")
          + (f", {redirecionadas} endereços antigos redirecionados" if redirecionadas else ""))


if __name__ == "__main__":
    raiz = next((a.split("=", 1)[1] for a in sys.argv if a.startswith("--raiz=")), "/")
    if not raiz.endswith("/"):
        raiz += "/"
    gerar(local="--local" in sys.argv, raiz=raiz)
