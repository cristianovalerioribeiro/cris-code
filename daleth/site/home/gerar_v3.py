#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera as três versões de teste da home (v3a, v3b, v3c) a partir de blocos comuns.
Base visual: home/v2.html (CSS, abertura, cena 3D, rodapé). Roteiro: scratchpad v3 (07/10/2026).
Rodar de daleth/site:  python3 home/gerar_v3.py   → home/v3a.html, v3b.html, v3c.html (build.py publica em /v3a/ etc.)"""
import re, pathlib
AQUI = pathlib.Path(__file__).resolve().parent
v2 = (AQUI / "v2.html").read_text(encoding="utf-8")

def entre(s, a, b, inclusivo=True):
    i = s.index(a); j = s.index(b, i) + (len(b) if inclusivo else 0)
    return s[i:j]

HEAD = v2[:v2.index("</head>")]
HEAD = HEAD.replace("<title>DALETH · Estruturação de Negócios Imobiliários (v2)</title>", "<title>DALETH · Estruturação de Negócios Imobiliários</title>")
LOGO = entre(v2, '<a class="marca" href="#inicio" aria-label="DALETH, início">', '</a>')
RODAPE = entre(v2, "<footer>", "</footer>")
TRI = entre(v2, '<svg class="tri"', "</svg>")
SCRIPTS = v2[v2.index("<script>\n// Slogan digitado"):v2.index("</body>")]
SCRIPTS = SCRIPTS.replace('document.querySelectorAll(".vertice[data-frente]")', 'document.querySelectorAll("[data-frente]")')

CSS_V3 = """
/* v3: correções de contraste e foco, barra de CTA no celular, entregas, perguntas da modelagem */
:root{--foco:#7A5A2C}
@media (prefers-color-scheme: dark){:root:not([data-theme="light"]){--foco:#CAA972}}
:root[data-theme="dark"]{--foco:#CAA972}
.btn-linha{border-color:var(--tinta-2);color:var(--tinta)}
.cap .btn-linha,.modelar .btn-linha{border-color:var(--cap-txt-2);color:var(--cap-txt)}
.cap,.modelar{--foco:#D4B37C}
@media (max-width:1100px){.topo nav:not(.menu-movel){gap:16px;font-size:13px}}
@media (max-width:1023px){.mp-palco{height:min(88vw,420px)}.mp-controles{order:0;margin:16px 0 0}.mp-ficha{order:1}.modelar-prancha .cab{order:-1}}

.topo .btn{display:inline-flex}
@media (max-width:860px){.topo .btn{display:inline-flex;padding:9px 14px;font-size:14px}.topo .wrap{gap:10px}}
.abertura .clareza{font-size:clamp(15px,1.5vw,18px);color:var(--cap-txt-2);max-width:40ch;margin:0}
@media (max-width:860px){.abertura{align-items:flex-end}.abertura::before{background:linear-gradient(180deg,rgba(8,37,56,.25) 0%,rgba(8,37,56,.55) 45%,rgba(8,37,56,.94) 100%)}}
.tese2 .micro{font-size:13px;color:var(--tinta-2);margin-top:-8px}
.apoio-cta{font-size:13px;color:var(--tinta-2)}
.cap .apoio-cta{color:var(--cap-txt-2)}
/* ficha estática (antes do JS) */
.mp-ficha .mf-sub li{margin:0}
/* perguntas que as frentes respondem */
.perguntas-frentes{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:20px;margin-top:clamp(28px,4vw,40px);padding-top:24px;border-top:1px solid var(--m-fio)}
.perguntas-frentes div{min-width:0}
.perguntas-frentes h3{font-size:18px;font-weight:700;color:var(--m-branco);margin-bottom:10px}
.perguntas-frentes p{display:flex;flex-wrap:wrap;gap:6px;margin:0}
.perguntas-frentes button{font:500 13px/1 var(--f-txt);min-height:44px;padding:0 14px;border:1px solid rgba(212,179,124,.45);border-radius:999px;background:rgba(255,255,255,.04);color:var(--m-branco);cursor:pointer}
.perguntas-frentes button:hover{border-color:var(--m-dourado-claro)}
.modelar .fecho-mod{margin-top:20px;color:var(--m-gelo);font-size:15px;max-width:62ch}
@media (max-width:860px){.perguntas-frentes{grid-template-columns:minmax(0,1fr)}}
/* entregas */
.recebe-sec{background:var(--papel-2)}
.recebe-sec.papel{background:var(--papel)}
.entregas-grade{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:20px 32px}
.entrega{display:flex;flex-direction:column;gap:8px;min-width:0;padding-top:16px;border-top:2px solid var(--tinta)}
.entrega:nth-child(2){border-top-color:var(--ouro-marca)}
.entrega .num{font-family:var(--f-disp);font-weight:700;font-size:12px;letter-spacing:.12em;color:var(--ouro)}
.entrega h3{font-size:22px;font-weight:700}
.entrega p{font-size:15px;color:var(--tinta-2)}
.entrega p b{color:var(--tinta);font-weight:600}
.recebe-sec .nota{margin-top:24px}
@media (max-width:760px){.entregas-grade{grid-template-columns:minmax(0,1fr)}}
/* passos: "você recebe" curto */
.passos .recebe{font-size:14px}
/* quem: papéis em linha */
.papeis-linha{margin-top:20px;font-family:var(--f-disp);font-weight:600;font-size:17px;color:var(--tinta)}
.papeis-linha em{font-style:normal;color:var(--ouro)}
/* barra de CTA no celular, depois da abertura */
.cta-movel{display:none}
@media (max-width:860px){
  .cta-movel{display:block;position:fixed;left:0;right:0;bottom:0;z-index:19;padding:10px var(--gut) calc(10px + env(safe-area-inset-bottom,0px));background:var(--papel);border-top:1px solid var(--linha);transform:translateY(110%);transition:transform .25s}
  .cta-movel.visivel{transform:none}
  .cta-movel .btn{width:100%;justify-content:center}
  body.com-cta-movel{padding-bottom:72px}
}
.oculto{position:absolute!important;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}
.pular{position:absolute;left:16px;top:-48px;z-index:30;background:var(--tinta);color:var(--papel);padding:10px 14px;border-radius:2px;text-decoration:none;font-weight:600}
.pular:focus{top:12px}
"""

def header(itens):
    nav = "".join(f'      <a href="#{a}">{t}</a>\n' for a, t in itens)
    movel = "".join(f'<a href="#{a}">{t}</a>' for a, t in itens) + '<a href="#contato">Conversar</a>'
    return f'''<a class="pular" href="#main">Ir para o conteúdo</a>
<header class="topo">
  <div class="wrap">
    {LOGO}
    <nav aria-label="Seções">
{nav}    </nav>
    <a class="btn btn-tinta" href="#contato">Conversar</a>
    <button type="button" class="menu-bt" aria-expanded="false" aria-controls="menu-movel" aria-label="Abrir o menu"><span></span><span></span><span></span></button>
  </div>
  <nav class="menu-movel" id="menu-movel" aria-label="Seções, menu do celular" hidden>
    {movel}
  </nav>
</header>
'''

ABERTURA = '''<section class="cap abertura" id="inicio" aria-label="Abertura">
  <div class="palco-3d" aria-hidden="true"><canvas data-cena="heroi"></canvas></div>
  <div class="wrap">
    <p class="sobre">DALETH · Estruturação de Negócios Imobiliários</p>
    <p class="assina-grande" id="assina" aria-label="Ao seu lado na construção de sua história."><span class="l1" aria-hidden="true">Ao seu lado na construção</span><span class="l2" aria-hidden="true"><em>de sua história.</em></span></p>
    <p class="clareza">Estruturação de empresas e empreendimentos imobiliários: comparamos os caminhos antes da decisão e ficamos ao lado na implantação.</p>
    <a class="desce" href="#tese" aria-label="Descer para a tese"><i aria-hidden="true">↓</i><span>A tese</span></a>
  </div>
</section>
'''

TESE = f'''<section class="tese2" id="tese">
  <div class="wrap">
    <div class="tese2-grade">
      <div class="hero-txt">
        <p class="sobre">A tese</p>
        <h1>A estrutura certa muda o tamanho do que você <em>pode construir.</em></h1>
        <p class="hero-nota">Muitas construtoras crescem pela capacidade de executar. O próximo crescimento depende da capacidade de estruturar.</p>
        <div class="acoes">
          <a class="btn btn-tinta" href="#contato">Conversar sobre uma oportunidade</a>
          <a class="btn btn-linha" href="#modelagem">Ver a modelagem</a>
        </div>
        <p class="micro apoio-cta">A primeira conversa não tem custo.</p>
      </div>
      <div class="tri-caixa">
{TRI}
        <p class="tri-legenda">Empresa, empreendimento e capital se decidem juntos.</p>
      </div>
    </div>
    {{PONTE}}
  </div>
</section>
'''

FICHA_ESTATICA = '''<p class="mf-num">00 · Modelagem do empreendimento</p><h3 class="mf-nome">Tudo conectado</h3><p class="mf-frase">Mudar uma frente muda as outras. Cada caminho é comparado antes da escolha.</p><ul class="mf-sub"><li>Terreno</li><li>Produto e mercado</li><li>Técnica</li><li>Jurídico</li><li>Societário</li><li>Tributário</li><li>Econômico-financeiro</li><li>Capital e funding</li><li>Comercialização</li><li>Risco e retorno</li></ul>'''

def modelagem(titulo, ponte=""):
    return f'''<section class="modelar modelar-prancha" id="modelagem" data-modelar="prancha" aria-labelledby="mod-t" tabindex="-1">
  <div class="wrap">
    <div class="cab">
      <p class="sobre">Modelar · o centro do método</p>
      <h2 class="h2" id="mod-t">{titulo}</h2>
      <p class="lead">O mesmo terreno pode ser vendido, permutado ou incorporado. Cada caminho muda risco, caixa e captura. Comparamos antes de escolher.</p>
    </div>
    <div class="mp-palco">
      <canvas data-cena="modelagem" data-lado="esquerda" data-reserva-direita="0.36" data-reserva-baixo="0.06" data-rotulos="Terreno|Produto e mercado|Técnica|Jurídico|Societário|Tributário|Econômico-financeiro|Capital e funding|Comercialização|Risco e retorno" aria-hidden="true"></canvas>
      <div class="cena-rotulos"></div>
      <p class="mp-titulo">Modelagem do empreendimento</p>
      <div class="mp-ficha" aria-live="polite">{FICHA_ESTATICA}</div>
    </div>
    <div class="mp-controles">
      <button type="button" class="mp-seta" data-passo="-1" aria-label="Frente anterior">←</button>
      <div class="mp-trilho" role="group" aria-label="Frentes da modelagem"></div>
      <button type="button" class="mp-seta" data-passo="1" aria-label="Próxima frente">→</button>
      <button type="button" class="mp-auto" aria-pressed="false">Percorrer as frentes</button>
    </div>
    <p class="mp-dica">Os nomes em dourado na ficha levam às frentes que cada uma move. <a href="/assets/docs/DALETH-Modelagem-do-Empreendimento.pdf" download>Este capítulo em PDF</a>.</p>
    <div class="perguntas-frentes" aria-label="As frentes, pela pergunta que respondem">
      <div><h3>O que este terreno pode ser?</h3><p><button type="button" data-frente="terreno">Terreno</button><button type="button" data-frente="produto">Produto e mercado</button><button type="button" data-frente="tecnica">Técnica</button></p></div>
      <div><h3>Em que forma o negócio existe?</h3><p><button type="button" data-frente="juridico">Jurídico e regulatório</button><button type="button" data-frente="societario">Societário e governança</button><button type="button" data-frente="tributario">Tributário</button></p></div>
      <div><h3>Como o dinheiro entra, sai e volta?</h3><p><button type="button" data-frente="financeiro">Econômico-financeiro</button><button type="button" data-frente="capital">Capital e funding</button><button type="button" data-frente="comercial">Comercialização</button><button type="button" data-frente="risco">Risco e retorno</button></p></div>
    </div>
    <p class="fecho-mod">O projeto fica com o arquiteto, a empresa com o contador, o capital com o banco. Alguém precisa olhar os três juntos.</p>
    {ponte}
  </div>
</section>
'''

def metodo(recebe_longo=False, ponte="", com_recebe=True):
    R = {
      "mapear": ("O retrato escrito: ativos, restrições, premissas e os caminhos que merecem comparação.",
                 "Um retrato escrito: ativos, recursos, restrições, riscos, premissas e oportunidades. As perguntas abertas, por urgência. Os caminhos que merecem comparação, e os que não, com o motivo."),
      "modelar": ("Dois ou três caminhos lado a lado, com premissas, caixa, exposição e a decisão registrada.",
                  "Os caminhos lado a lado: premissas escritas, caixa e exposição de cada um, risco assumido, valor capturado, o que exigem da empresa. Nossa indicação e o porquê. A escolha fica registrada."),
      "estruturar": ("A operação por escrito: sociedade, terreno, contratos, caixa alvo e dossiê para quem financia.",
                     "A operação por escrito: sociedade e passos de constituição, forma de aquisição do terreno, contratos com responsável por cada um, caixa alvo com pontos de controle, dossiê pronto para banco, investidor ou sócio. Quem aprova é o financiador."),
      "conduzir": ("Presença nos pontos de controle, com uma leitura escrita do que mudou e do que fazer.",
                   "Presença nos pontos de controle definidos na estruturação. A cada ponto, uma leitura escrita do que mudou e do que fazer. A execução continua com a sua empresa."),
    }
    k = 1 if recebe_longo else 0
    def rec(ch): return f'<p class="recebe"><b>Você recebe</b>{R[ch][k]}</p>' if com_recebe else ''
    return f'''<section class="metodo" id="metodo" aria-labelledby="met-t">
  <div class="wrap">
    <div class="cab">
      <p class="sobre">Como trabalhamos</p>
      <h2 class="h2" id="met-t">Quatro movimentos. Cada um termina com uma decisão sua.</h2>
      <p class="lead">Começa com uma conversa sem custo. Nada avança sem algo escrito e lido com você.</p>
    </div>
    <ol class="passos">
      <li class="entrada">
        <span class="num">PORTA DE ENTRADA</span>
        <h3>Conversa de enquadramento</h3>
        <p class="recebe">Você conta o terreno, a empresa ou a necessidade de capital. Saímos sabendo se há caso e por onde ele começa.</p>
        <span class="selo">sem custo</span>
      </li>
      <li><span class="num">01</span><h3>Mapear</h3><p class="para">para compreender</p><p class="frase">Mapear a situação real, antes de recomendar.</p>{rec("mapear")}</li>
      <li><span class="num">02</span><h3>Modelar</h3><p class="para">para enxergar</p><p class="frase">Comparar os caminhos antes de comprometer o capital.</p>{rec("modelar")}</li>
      <li><span class="num">03</span><h3>Estruturar</h3><p class="para">para tornar executável</p><p class="frase">Transformar o caminho escolhido em operação.</p>{rec("estruturar")}</li>
      <li><span class="num">04</span><h3>Conduzir</h3><p class="para">para funcionar</p><p class="frase">Acompanhar a implantação ao lado de quem executa.</p>{rec("conduzir")}</li>
    </ol>
    {ponte}
  </div>
</section>
'''

def entregas(fundo_papel=False, ponte=""):
    return f'''<section class="recebe-sec{' papel' if fundo_papel else ''}" id="entregas" aria-labelledby="ent-t">
  <div class="wrap">
    <div class="cab">
      <p class="sobre">O que você recebe</p>
      <h2 class="h2" id="ent-t">O que fica na sua mão, do primeiro retrato à obra.</h2>
      <p class="lead">Quatro entregas, uma por movimento. Nenhuma delas é a obra.</p>
    </div>
    <div class="entregas-grade">
      <div class="entrega"><span class="num">01 · MAPEAR</span><h3>Um retrato escrito</h3><p>Ativos, recursos, restrições, riscos, premissas e oportunidades. As perguntas abertas, por urgência. Os caminhos que merecem comparação, e os que não, com o motivo. <b>Você decide se vale modelar.</b></p></div>
      <div class="entrega"><span class="num">02 · MODELAR</span><h3>Os caminhos lado a lado</h3><p>Premissas escritas, caixa e exposição de cada um, risco assumido, valor capturado, o que exigem da empresa. Nossa indicação e o porquê. <b>Você escolhe, e a escolha fica registrada.</b></p></div>
      <div class="entrega"><span class="num">03 · ESTRUTURAR</span><h3>A operação por escrito</h3><p>Sociedade e passos de constituição, forma de aquisição do terreno, contratos com responsável por cada um, caixa alvo com pontos de controle, dossiê pronto para banco, investidor ou sócio. <b>Quem aprova é o financiador.</b></p></div>
      <div class="entrega"><span class="num">04 · CONDUZIR</span><h3>Presença nos pontos de controle</h3><p>Definidos na estruturação. A cada ponto, uma leitura escrita do que mudou em relação à premissa e do que fazer. <b>A execução continua com a sua empresa.</b></p></div>
    </div>
    {ponte}
  </div>
</section>
'''

def lado(ponte=""):
    return f'''<section class="cap lado" id="ao-seu-lado" aria-labelledby="lado-t">
  <div class="wrap">
    <div class="cab">
      <p class="sobre">Ao seu lado</p>
      <h2 class="grande" id="lado-t">Uma coisa é dizer o que fazer. Outra é estar lá enquanto é feito.</h2>
      <p class="lead">Mostramos os caminhos e dizemos qual tomaríamos. A decisão é sua. A obra é da sua empresa. A rota, acompanhamos juntos.</p>
    </div>
    <div class="papeis">
      <div><b>O cliente</b><p>decide.<small>Com os caminhos e os números na mesa.</small></p></div>
      <div><b>A empresa</b><p>executa.<small>Quem constrói continua construindo.</small></p></div>
      <div><b>A DALETH</b><p>conduz.<small>Verifica, cobra o combinado e corrige a rota.</small></p></div>
    </div>
    <div class="comp">
      <div class="prop">
        <p class="sobre">Por que existimos</p>
        <p class="p-txt">Dar estrutura para que bons empreendimentos imobiliários realizem seu potencial.</p>
      </div>
      <div>
        <p class="sobre" style="margin-bottom:6px">Três compromissos</p>
        <ol>
          <li>Mapear a situação real antes de recomendar.</li>
          <li>Mostrar os caminhos lado a lado, com as premissas escritas.</li>
          <li>Dizer o que os números dizem, mesmo quando o caminho preferido não fecha.</li>
        </ol>
      </div>
    </div>
    {ponte}
  </div>
</section>
'''

def quem(com_papeis=False, ponte=""):
    papeis = '<p class="papeis-linha">O cliente decide. A empresa executa. <em>A DALETH conduz.</em></p>' if com_papeis else ''
    return f'''<section class="quem" id="quem" aria-labelledby="quem-t">
  <div class="wrap">
    <div class="cab" style="margin-bottom:0">
      <p class="sobre">Quem conduz</p>
      <h2 class="h2" id="quem-t">Cristiano Valério Ribeiro</h2>
      <p class="meta">Engenharia de produção · Economia · MBA em gestão de negócios de incorporação e construção</p>
    </div>
    <div class="txt">
      <p class="lead">Atuou nos dois lados do crédito imobiliário, analisando e estruturando operações. Acompanhou ciclos completos de incorporação, do terreno à entrega.</p>
      <div class="provas">
        <p class="num">R$ 324 mi<small>em VGV (valor geral de vendas) de operações de financiamento à produção trabalhadas, na trajetória do fundador, via TRAL3.</small></p>
        <p class="num">30<small>operações de financiamento à produção.</small></p>
        <p class="num">19<small>construtoras e incorporadoras atendidas nessas operações.</small></p>
      </div>
      {papeis}
    </div>
    {ponte}
  </div>
</section>
'''

FAQ = '''<section class="faq" id="perguntas" aria-labelledby="faq-t">
  <div class="wrap">
    <div class="cab">
      <p class="sobre">Antes de escrever</p>
      <h2 class="h2" id="faq-t">O que costumam perguntar antes de escrever.</h2>
      <p class="lead">Respostas curtas. O resto cabe na conversa de enquadramento.</p>
    </div>
    <div class="faq-lista">
      <details><summary>Quanto custa?</summary><p>Caso a caso. O escopo sai da conversa de enquadramento, que não tem custo. Valor, prazo e entregas ficam escritos na proposta antes de qualquer trabalho começar.</p></details>
      <details><summary>Vocês decidem por mim?</summary><p>Não. Mostramos os caminhos lado a lado, com as consequências de cada um, e dizemos qual tomaríamos. A decisão é sua e fica registrada com a premissa que a sustenta.</p></details>
      <details><summary>Vocês recebem comissão do banco?</summary><p>Não. Não somos correspondentes bancários nem recebemos de instituição financeira. Isso nos deixa livres para comparar qualquer fonte de capital. Quem aprova o crédito é o financiador.</p></details>
      <details><summary>Já tenho contador, advogado e arquiteto. Faz sentido?</summary><p>Faz, e não substituímos nenhum deles. Trabalhamos ao lado do seu time. O que costuma faltar é alguém olhando empresa, empreendimento e capital juntos.</p></details>
      <details><summary>Minha obra parou. É caso para vocês?</summary><p>Pode ser. Obra parada mexe nos três lados ao mesmo tempo. A conversa de enquadramento diz se há caminho e qual seria o primeiro passo.</p></details>
      <details><summary>Atendem fora de Minas Gerais?</summary><p>Sim. A base é Belo Horizonte e a atuação é nacional, à distância, com presença quando o caso pede. Documentos e decisões circulam por escrito.</p></details>
      <details><summary>O que vocês não fazem?</summary><p>Não captamos recursos, não damos curso, não terceirizamos rotinas (BPO) e não assumimos a execução. É estruturação.</p></details>
    </div>
  </div>
</section>
'''

CONVERSA = '''<section class="cap contato" id="contato" aria-labelledby="conv-t">
  <div class="wrap">
    <div class="cab" style="margin-bottom:0">
      <p class="sobre">Começa com uma conversa</p>
      <h2 id="conv-t">Conte o terreno, a empresa ou a obra.</h2>
      <p class="lead">Uma conversa basta para saber se há caso. Se houver, a proposta diz escopo, prazo e valor.</p>
      <ol class="degraus">
        <li><b>Conversa de enquadramento</b><span>Sem custo e sem compromisso.</span></li>
        <li><b>Mapeamento</b><span>O primeiro trabalho, só se fizer sentido para os dois lados.</span></li>
        <li><b>Escopo escrito</b><span>Prazo, entregas e valor antes de começar.</span></li>
      </ol>
    </div>
    <div class="canal">
      <b>Canal de contato · em breve</b>
      <p>A conversa de enquadramento já vale como está: sem custo e confidencial desde a primeira mensagem.</p>
      <p>Belo Horizonte · atuação nacional</p>
    </div>
  </div>
</section>
'''

CTA_MOVEL = '''<div class="cta-movel" id="cta-movel" aria-hidden="true"><a class="btn btn-tinta" href="#contato" tabindex="-1">Conversar sobre uma oportunidade</a></div>
'''
JS_V3 = '''<script>
// Barra de CTA no celular: aparece depois da abertura, some perto do fecho
(function(){
  var barra=document.getElementById("cta-movel"), ab=document.getElementById("tese"), fim=document.getElementById("contato");
  if(!barra||!ab||!fim||!("IntersectionObserver" in window)) return;
  document.body.classList.add("com-cta-movel");
  var passouAbertura=false, noFim=false;
  function ajustar(){ var v=passouAbertura&&!noFim; barra.classList.toggle("visivel",v); barra.setAttribute("aria-hidden",String(!v)); barra.querySelector("a").tabIndex=v?0:-1; }
  new IntersectionObserver(function(es){ es.forEach(function(e){ passouAbertura=!e.isIntersecting && e.boundingClientRect.bottom<0; }); ajustar(); },{threshold:0}).observe(ab);
  new IntersectionObserver(function(es){ es.forEach(function(e){ noFim=e.isIntersecting; }); ajustar(); },{threshold:0.1}).observe(fim);
})();
</script>
'''

def ponte(alvo, texto):
    return f'<a class="ponte" href="#{alvo}"><span>{texto}</span><i aria-hidden="true">↓</i></a>'

VERSOES = {
  "v3a": dict(
    nome="A · Direta",
    nav=[("modelagem","Modelagem"),("metodo","Como trabalhamos"),("quem","Quem conduz"),("perguntas","Perguntas")],
    corpo=lambda: [ABERTURA, TESE.replace("{PONTE}",""), modelagem("Toda oportunidade guarda mais de um negócio."),
                   metodo(recebe_longo=True), quem(com_papeis=True), FAQ, CONVERSA]),
  "v3b": dict(
    nome="B · Narrativa",
    nav=[("modelagem","Modelagem"),("metodo","Como trabalhamos"),("entregas","O que você recebe"),("ao-seu-lado","Ao seu lado"),("quem","Quem conduz")],
    corpo=lambda: [ABERTURA, TESE.replace("{PONTE}", ponte("modelagem","Como enxergar os três lados juntos antes de decidir.")),
                   modelagem("Toda oportunidade guarda mais de um negócio.", ponte("metodo","A sequência, do primeiro retrato à obra.")),
                   metodo(ponte=ponte("entregas","O que fica na sua mão em cada passo."), com_recebe=False),
                   entregas(fundo_papel=True, ponte=ponte("ao-seu-lado","A decisão é sua. E depois dela?")),
                   lado(), quem(), FAQ, CONVERSA]),
  "v3c": dict(
    nome="C · Entregas primeiro",
    nav=[("entregas","O que você recebe"),("modelagem","Modelagem"),("metodo","Como trabalhamos"),("quem","Quem conduz")],
    corpo=lambda: [ABERTURA, TESE.replace("{PONTE}",""), entregas(),
                   modelagem("Toda oportunidade guarda mais de um negócio."), metodo(com_recebe=False), quem(com_papeis=True), FAQ, CONVERSA]),
}

# ---------------------------------------------------------------- v4 (mesa de decisão, 07/10): hero novo + prova no topo; assinatura depois da tese
CSS_V4 = """
/* v4: hero com rótulos na cena, barra de prova, assinatura depois da tese */
.heroi-v4{min-height:0;height:clamp(600px,calc(100svh - 64px - 150px),860px);padding-block:clamp(48px,6vw,80px)}
@media (max-width:860px){.heroi-v4{height:auto;min-height:calc(100svh - 64px - 120px)}}
.heroi-v4::before{display:none}
.heroi-v4 .palco-3d{z-index:-1}
.heroi-v4 .palco-3d.foto{background:#082538;overflow:hidden}
.heroi-v4 .foto-img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:72% 55%;transform-origin:72% 62%;animation:kb 38s ease-in-out infinite alternate}
@keyframes kb{from{transform:scale(1.02)}to{transform:scale(1.10) translate(-1.6%,-1.2%)}}
.heroi-v4 .tracos{position:absolute;inset:0;width:100%;height:100%;z-index:2;pointer-events:none;font-family:var(--f-txt)}
.heroi-v4 .tracos .rede line{stroke:rgba(212,179,124,.42);stroke-width:1;stroke-dasharray:600;stroke-dashoffset:600;animation:tracar 2.2s 1.2s cubic-bezier(.4,0,.2,1) forwards}
.heroi-v4 .tracos .lote{fill:rgba(212,179,124,.06);stroke:rgba(212,179,124,.85);stroke-width:1.5;stroke-linejoin:round;stroke-dasharray:1200;stroke-dashoffset:1200;animation:tracar 2.4s .6s cubic-bezier(.4,0,.2,1) forwards}
.heroi-v4 .tracos .lote-l{fill:none;stroke:rgba(212,179,124,.55);stroke-width:1;stroke-dasharray:3 6;opacity:0;animation:surge 1.4s 2.6s forwards}
.heroi-v4 .tracos .pino line{stroke:rgba(255,255,255,.75);stroke-width:1;stroke-dasharray:400;stroke-dashoffset:400;animation:tracar 1.1s calc(1.8s + var(--i) * .22s) cubic-bezier(.4,0,.2,1) forwards}
.heroi-v4 .tracos .pino .ponto{fill:#FFE9B8}
.heroi-v4 .tracos .pino .base{fill:url(#g-no);animation:pulsa 3.6s calc(2.4s + var(--i) * .5s) ease-in-out infinite}
.heroi-v4 .tracos .pino .alto{fill:#fff}
.heroi-v4 .tracos .pino text{fill:#fff;font-size:12px;font-weight:600;letter-spacing:.12em}
.heroi-v4 .tracos .pino .rot-fundo{fill:rgba(8,37,56,.78);stroke:rgba(212,179,124,.55);stroke-width:1}
.heroi-v4 .tracos .pino .alto,.heroi-v4 .tracos .pino text,.heroi-v4 .tracos .pino .rot-fundo{opacity:0;animation:surge .7s calc(2.7s + var(--i) * .22s) forwards}
@keyframes tracar{to{stroke-dashoffset:0}}
@keyframes surge{to{opacity:1}}
@keyframes pulsa{0%,100%{transform:scale(.7);opacity:.55}50%{transform:scale(1.25);opacity:1}}
.heroi-v4 .tracos .pino .base{transform-box:fill-box;transform-origin:center}
.heroi-v4 .palco-3d::after{z-index:1}
@media (max-width:860px){.heroi-v4 .foto-img{object-position:center top;animation-duration:30s}.heroi-v4 .tracos{display:none}}
@media (prefers-reduced-motion:reduce){.heroi-v4 .foto-img{animation:none}.heroi-v4 .tracos *{animation:none!important;stroke-dashoffset:0;opacity:1}}
.heroi-v4 .palco-3d::after{content:"";position:absolute;inset:0;z-index:0;pointer-events:none;background:linear-gradient(90deg,rgba(8,37,56,.98) 0%,rgba(8,37,56,.96) 30%,rgba(8,37,56,.70) 52%,rgba(8,37,56,.10) 100%)}
.heroi-v4 .palco-3d .cena-rotulos{z-index:1}
.heroi-v4 .wrap{gap:22px;max-width:var(--larg)}
.heroi-v4 h1{font-family:var(--f-disp);font-weight:800;font-size:clamp(34px,5.6vw,72px);line-height:1.04;letter-spacing:-.03em;color:var(--cap-txt);margin:0;max-width:14ch;text-wrap:balance}
.heroi-v4 h1 em{font-style:normal;color:var(--ouro-cap)}
.heroi-v4 .lead-h{font-size:clamp(16px,1.6vw,20px);line-height:1.5;color:var(--cap-txt-2);max-width:52ch;margin:0}
.heroi-v4 .acoes{display:flex;flex-wrap:wrap;gap:12px 20px;align-items:center}
.heroi-v4 .cena-rotulos span{font-size:11px}
@media (max-width:860px){.heroi-v4{align-items:flex-end}.heroi-v4 .palco-3d::after{background:linear-gradient(180deg,rgba(8,37,56,.30) 0%,rgba(8,37,56,.62) 45%,rgba(8,37,56,.96) 100%)}.heroi-v4 .cena-rotulos{display:none}}
/* ritmo: seções mais curtas na v4 */
main > section:not(.heroi-v4):not(.prova):not(.assina-sec){padding-block:clamp(48px,6.5vw,84px)}
.tese2.fecha{padding-block:clamp(48px,6.5vw,84px)}
.tese2 .hero-txt{gap:18px}
@media (min-width:1024px){.modelar .mp-palco{aspect-ratio:16/8;max-height:540px;min-height:380px}}
.modelar .perguntas-frentes{margin-top:24px;padding-top:18px}
.modelar .fecho-mod{margin-top:14px}
@media (max-width:860px){.modelar .perguntas-frentes{gap:10px;padding-top:14px}.modelar .perguntas-frentes h3{font-size:16px;margin-bottom:0}.modelar .perguntas-frentes p{display:none}}
.faq summary{padding:14px 40px 14px 0;font-size:17px}
.faq summary::after{top:10px}
.faq details p{padding-bottom:14px}
.passos h3{font-size:22px}
.passos .frase{font-size:16px}
@media (max-width:980px){
  /* passos em trilho horizontal no celular: uma tela em vez de duas e meia */
  .passos{display:flex;overflow-x:auto;scroll-snap-type:x mandatory;gap:14px;padding:4px var(--gut) 14px;margin:0 calc(-1 * var(--gut));scrollbar-width:thin}
  .passos li,.passos li+li{flex:0 0 min(78vw,320px);scroll-snap-align:start;padding:18px 18px 20px;border:1px solid var(--linha);border-left:3px solid var(--ouro-marca);background:var(--papel)}
  .passos li::before{display:none}
  .passos h3{font-size:20px}
  .passos .frase{font-size:15px}
  .passos .recebe{font-size:13px}
}
/* prova: quatro números sob o hero */
.prova{padding-block:0;background:var(--tinta);color:var(--papel);border-top:1px solid rgba(212,179,124,.35)}
.prova .wrap{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:24px 32px;padding-block:clamp(28px,3.5vw,44px)}
.prova .num{font-family:var(--f-disp);font-weight:800;font-size:clamp(30px,3.6vw,46px);line-height:1;letter-spacing:-.02em;color:#D4B37C;font-variant-numeric:tabular-nums;margin:0}
.prova .num small{font-size:.42em;font-weight:600;letter-spacing:0;margin-left:.2em;color:#D4B37C}
.prova .leg{font:600 11px/1.5 var(--f-txt);letter-spacing:.14em;text-transform:uppercase;color:rgba(255,255,255,.78);margin:10px 0 0}
.prova .celula{min-width:0;padding-left:20px;border-left:1px solid rgba(255,255,255,.14)}
.prova .celula:first-child{padding-left:0;border-left:0}
.prova .celula.local .num{font-size:clamp(18px,1.8vw,22px);font-weight:700;letter-spacing:.06em;text-transform:uppercase;color:#D4B37C;line-height:1.3}
@media (max-width:860px){.prova .wrap{grid-template-columns:repeat(2,minmax(0,1fr))}.prova .celula:nth-child(3){padding-left:0;border-left:0}}
/* tese em segundo plano: título continua grande, mas é h2 */
.tese2 .como-h1{font-size:clamp(36px,5vw,58px);font-weight:800;line-height:1.06;letter-spacing:-.025em;color:var(--tinta)}
.tese2 .como-h1 em{font-style:normal;color:var(--ouro)}
.tese2.fecha{padding-bottom:clamp(56px,8vw,96px)}
/* assinatura: a palavra "construção" é a chave; traço dourado se ergue sob ela como uma viga */
.assina-sec{min-height:min(62svh,560px);padding-block:clamp(56px,7vw,88px);text-align:center;justify-content:center}
.assina-sec .wrap{align-items:center}
.assina-sec::before{background:linear-gradient(180deg,rgba(8,37,56,.90) 0%,rgba(8,37,56,.72) 50%,rgba(8,37,56,.92) 100%)}
.assina-sec .assina-grande{align-items:center;font-size:clamp(34px,6vw,84px)}
.assina-sec .chave{position:relative;display:inline-block;color:var(--ouro-cap);font-style:normal}
.assina-sec .chave::after{content:"";position:absolute;left:0;right:0;bottom:-.08em;height:.055em;background:var(--ouro-cap);transform-origin:left;transform:scaleX(0);animation:viga 1.1s .5s cubic-bezier(.2,.7,.2,1) forwards}
@keyframes viga{to{transform:scaleX(1)}}
.assina-sec .clareza{text-align:center;max-width:46ch}
@media (prefers-reduced-motion:reduce){.assina-sec .chave::after{animation:none;transform:none}}
"""

HERO_V4 = '''<section class="cap abertura heroi-v4" id="inicio" aria-label="Abertura">
  <div class="palco-3d foto" role="img" aria-label="Vista de uma cidade ao entardecer, com uma obra em andamento e plantas sobre a laje">
    <picture><source media="(max-width:860px)" srcset="/assets/img/heroi-foto-m.jpg"><img class="foto-img" src="/assets/img/heroi-foto.jpg" srcset="/assets/img/heroi-foto-1280.jpg 1280w, /assets/img/heroi-foto.jpg 1672w" sizes="100vw" alt="" fetchpriority="high" decoding="async"></picture>
    <svg class="tracos" viewBox="0 0 1600 900" preserveAspectRatio="xMidYMid slice" aria-hidden="true">
      <defs><radialGradient id="g-no"><stop offset="0" stop-color="#FFE9B8" stop-opacity="1"/><stop offset=".45" stop-color="#D4B37C" stop-opacity=".9"/><stop offset="1" stop-color="#D4B37C" stop-opacity="0"/></radialGradient></defs>
      <g class="rede">
        <line x1="846" y1="588" x2="968" y2="540"/>
        <line x1="968" y1="540" x2="1086" y2="556"/>
        <line x1="1086" y1="556" x2="1206" y2="572"/>
        <line x1="1206" y1="572" x2="1330" y2="548"/>
        <line x1="1330" y1="548" x2="1456" y2="524"/>
        <line x1="846" y1="588" x2="1086" y2="556"/>
        <line x1="968" y1="540" x2="1206" y2="572"/>
        <line x1="1086" y1="556" x2="1330" y2="548"/>
        <line x1="1206" y1="572" x2="1456" y2="524"/>
        <line x1="968" y1="540" x2="1330" y2="548"/>
      </g>
      <path class="lote" d="M980 622 L1250 574 L1372 636 L1080 702 Z"/>
      <path class="lote-l" d="M980 622 L980 480 M1250 574 L1250 432 M1372 636 L1372 494 M1080 702 L1080 560 M980 480 L1250 432 L1372 494 L1080 560 Z"/>
      <g class="pino" style="--i:0"><line x1="846" y1="588" x2="846" y2="334"/><circle class="base" cx="846" cy="588" r="9"/><circle class="ponto" cx="846" cy="588" r="3"/><circle class="alto" cx="846" cy="334" r="2.5"/><rect class="rot-fundo" x="801" y="302" width="89" height="22" rx="11"/><text x="846" y="317" text-anchor="middle">TERRENO</text></g>
      <g class="pino" style="--i:1"><line x1="968" y1="540" x2="968" y2="292"/><circle class="base" cx="968" cy="540" r="9"/><circle class="ponto" cx="968" cy="540" r="3"/><circle class="alto" cx="968" cy="292" r="2.5"/><rect class="rot-fundo" x="923" y="260" width="89" height="22" rx="11"/><text x="968" y="275" text-anchor="middle">PRODUTO</text></g>
      <g class="pino" style="--i:2"><line x1="1086" y1="556" x2="1086" y2="310"/><circle class="base" cx="1086" cy="556" r="9"/><circle class="ponto" cx="1086" cy="556" r="3"/><circle class="alto" cx="1086" cy="310" r="2.5"/><rect class="rot-fundo" x="1022" y="278" width="128" height="22" rx="11"/><text x="1086" y="293" text-anchor="middle">VIABILIDADE</text></g>
      <g class="pino" style="--i:3"><line x1="1206" y1="572" x2="1206" y2="330"/><circle class="base" cx="1206" cy="572" r="9"/><circle class="ponto" cx="1206" cy="572" r="3"/><circle class="alto" cx="1206" cy="330" r="2.5"/><rect class="rot-fundo" x="1152" y="298" width="108" height="22" rx="11"/><text x="1206" y="313" text-anchor="middle">PROCESSOS</text></g>
      <g class="pino" style="--i:4"><line x1="1330" y1="548" x2="1330" y2="300"/><circle class="base" cx="1330" cy="548" r="9"/><circle class="ponto" cx="1330" cy="548" r="3"/><circle class="alto" cx="1330" cy="300" r="2.5"/><rect class="rot-fundo" x="1233" y="268" width="195" height="22" rx="11"/><text x="1330" y="283" text-anchor="middle">ESTRUTURA JURÍDICA</text></g>
      <g class="pino" style="--i:5"><line x1="1456" y1="524" x2="1456" y2="282"/><circle class="base" cx="1456" cy="524" r="9"/><circle class="ponto" cx="1456" cy="524" r="3"/><circle class="alto" cx="1456" cy="282" r="2.5"/><rect class="rot-fundo" x="1411" y="250" width="89" height="22" rx="11"/><text x="1456" y="265" text-anchor="middle">CAPITAL</text></g>
    </svg>
  </div>
  <div class="wrap">
    <p class="sobre">Estruturação de Negócios Imobiliários</p>
    <h1>Transformamos oportunidades imobiliárias <em>em negócios estruturados para acontecer.</em></h1>
    <p class="lead-h">Terreno, produto, viabilidade, processos, estrutura jurídica e capital integrados em uma única visão do negócio.</p>
    <div class="acoes">
      <a class="btn btn-tinta" href="#contato">Conversar sobre uma oportunidade</a>
      <a class="btn btn-linha" href="#metodo">Conhecer como atuamos</a>
    </div>
  </div>
</section>
<section class="prova" aria-label="Números da trajetória">
  <div class="wrap">
    <div class="celula"><p class="num">R$ 524<small>milhões</small></p><p class="leg">VGV de operações trabalhadas</p></div>
    <div class="celula"><p class="num">40</p><p class="leg">Operações de financiamento à produção</p></div>
    <div class="celula"><p class="num">6.320+</p><p class="leg">Unidades estruturadas</p></div>
    <div class="celula local"><p class="num">Atuação nacional</p><p class="leg">Base em Belo Horizonte</p></div>
  </div>
</section>
'''

ASSINATURA_V4 = '''<section class="cap abertura assina-sec" id="assinatura" aria-label="Assinatura">
  <div class="palco-3d" aria-hidden="true"><canvas data-cena="rede"></canvas></div>
  <div class="wrap">
    <p class="sobre">Nossa assinatura</p>
    <p class="assina-grande" id="assina" aria-label="Ao seu lado na construção de sua história."><span class="l1" aria-hidden="true">Ao seu lado na <em class="chave">construção</em> de</span><span class="l2" aria-hidden="true"><em>sua história.</em></span></p>
    <p class="clareza">Construção é a palavra que une o que fazemos: do empreendimento, da empresa, do capital. E da história de quem decide.</p>
    <a class="desce" href="#modelagem" aria-label="Descer para a modelagem"><i aria-hidden="true">↓</i><span>A modelagem</span></a>
  </div>
</section>
'''

TESE_V4 = (TESE.replace("<h1>", '<h2 class="como-h1">').replace("</h1>", "</h2>")
           .replace('<section class="tese2" id="tese">', '<section class="tese2 fecha" id="tese">').replace("{PONTE}", ""))

def quem_v4():
    return (quem(com_papeis=True)
            .replace("R$ 324 mi<small>", "R$ 524 mi<small>")
            .replace(">30<small>operações", ">40<small>operações"))

VERSOES["v4"] = dict(
    nome="v4 · Mesa de decisão",
    css_extra=CSS_V4,
    scripts_sub=[('var fins=["de seu projeto", "de seu empreendimento", "de seu legado", "de sua história."];', 'var fins=["seu projeto", "seu empreendimento", "sua história."];')],
    nav=[("modelagem","O que fazemos"),("metodo","Como estruturamos"),("quem","Sobre a DALETH"),("perguntas","Perguntas")],
    corpo=lambda: [HERO_V4, TESE_V4, ASSINATURA_V4, modelagem("Toda oportunidade guarda mais de um negócio."),
                   metodo(recebe_longo=True), quem_v4(), FAQ, CONVERSA])

# ---------------------------------------------------------------- v5 (PDF "Reconstrução da Homepage v4" + pedidos do Cristiano, 07/10 noite)
CSS_V5 = """
/* v5: oito capítulos; método em fluxo; assinatura à esquerda depois do método; quem sem números; CTA único */
.modelar-v5 .cab .lead{max-width:62ch}
.mp-dica{margin-top:14px}
/* método em fluxo */
.metodo-v5 .fluxo{position:relative;margin-top:clamp(28px,4vw,44px)}
.metodo-v5 .fio{position:relative;height:14px;margin:0 0 30px}
.metodo-v5 .fio-base,.metodo-v5 .fio-vivo{position:absolute;left:0;right:0;top:6px;height:2px;background:var(--linha)}
.metodo-v5 .fio-vivo{background:var(--ouro-marca);transform-origin:left;transform:scaleX(0);transition:transform 2.4s cubic-bezier(.4,0,.2,1)}
.metodo-v5 .fluxo.visto .fio-vivo{transform:scaleX(1)}
.metodo-v5 .fio i{position:absolute;top:0;left:calc(var(--p) * 33.333%);width:14px;height:14px;margin-left:-7px;border-radius:50%;background:var(--papel);border:2px solid var(--tinta);box-sizing:border-box;transition:background .4s calc(var(--p) * .6s),border-color .4s calc(var(--p) * .6s)}
.metodo-v5 .fio i:last-child{left:100%}
.metodo-v5 .fluxo.visto .fio i{background:var(--ouro-marca);border-color:var(--ouro-marca)}
.metodo-v5 .passos{grid-template-columns:repeat(4,minmax(0,1fr));padding-top:0}
.metodo-v5 .passos li{gap:10px}
.metodo-v5 .passos h3{font-size:24px}
.metodo-v5 .passos .frase{font-size:17px;color:var(--tinta)}
.metodo-v5 .passos .detalhe{font-size:16px;line-height:1.5;color:var(--tinta)}
.metodo-v5 .linha-comercial{margin-top:18px;padding-top:18px;border-top:1px solid var(--linha);font-size:15px;color:var(--tinta-2);max-width:72ch}
.metodo-v5 .linha-comercial b{color:var(--tinta);font-weight:600}
.modelar-v5 .cab .lead b{color:var(--m-branco);font-weight:600}
.metodo-v5 .passos .papel{display:flex;flex-direction:column;gap:2px;margin-top:6px;padding-top:10px;border-top:1px solid var(--linha);font-size:13px;color:var(--tinta-2)}
.metodo-v5 .passos .papel b{color:var(--tinta);font-weight:600}
.metodo-v5 .passos .papel em{font-style:normal;color:var(--ouro)}
.metodo-v5 .pergunta{font-family:var(--f-disp);font-weight:600;font-size:13px;letter-spacing:.06em;text-transform:uppercase;color:var(--ouro)}
.metodo-v5 .papeis-linha{margin-top:clamp(28px,4vw,40px);font-size:clamp(18px,2vw,22px)}
.metodo-v5 .papeis-linha em{color:var(--ouro)}
@media (max-width:980px){.metodo-v5 .fio{display:none}}
/* assinatura à esquerda, depois do método, como clímax */
.assina-sec.esquerda{text-align:left;justify-content:center;min-height:min(66svh,640px)}
.assina-sec.esquerda .wrap{align-items:flex-start}
.assina-sec.esquerda .assina-grande{align-items:flex-start;font-size:clamp(36px,6.2vw,92px)}
.assina-sec.esquerda .clareza{text-align:left;max-width:52ch;font-size:clamp(16px,1.5vw,19px)}
.assina-sec.esquerda::before{background:linear-gradient(90deg,rgba(8,37,56,.96) 0%,rgba(8,37,56,.82) 55%,rgba(8,37,56,.55) 100%)}
.assina-sec .chave::after{animation:none;transform:scaleX(0)}
.assina-sec .fixo .chave::after{animation:viga 1.1s .15s cubic-bezier(.2,.7,.2,1) forwards}
.assina-sec .fixo .l2 em{animation:realce 1.4s .2s ease-out both}
@keyframes realce{0%{text-shadow:0 0 0 rgba(212,179,124,0)}35%{text-shadow:0 0 28px rgba(212,179,124,.75)}100%{text-shadow:0 0 0 rgba(212,179,124,0)}}
@media (prefers-reduced-motion:reduce){.assina-sec .chave::after{transform:none}.assina-sec .fixo .l2 em{animation:none}}
/* quem está ao seu lado */
.quem-v5 .txt .lead{font-size:clamp(18px,1.7vw,21px);max-width:60ch}
.quem-v5 .meta{margin-top:10px}
.quem-v5 .apoio{margin-top:14px;font-size:14px;color:var(--tinta-2);max-width:60ch}
/* CTA final: uma ação */
.cta-final .wrap{display:flex;flex-direction:column;align-items:flex-start;gap:18px;max-width:var(--larg)}
.cta-final .wrap>*{max-width:880px}
.cta-final h2{font-size:clamp(32px,4.6vw,56px);font-weight:800;line-height:1.06;letter-spacing:-.02em}
.cta-final .lead{max-width:60ch}
.cta-final .acoes{display:flex;flex-wrap:wrap;gap:12px 20px;align-items:center;margin-top:8px}
.cta-final .micro{font-size:13px;color:var(--cap-txt-2)}
footer .slogan{display:none}
"""

def modelagem_v5():
    m = modelagem("Uma decisão muda várias frentes ao mesmo tempo.")
    m = m.replace('<section class="modelar modelar-prancha"', '<section class="modelar modelar-prancha modelar-v5"')
    m = m.replace('O mesmo terreno pode ser vendido, permutado ou incorporado. Cada caminho muda risco, caixa e captura. Comparamos antes de escolher.',
                  'É por isso que modelamos o negócio como um sistema: <b>ativo e produto</b>, <b>estrutura da empresa e do negócio</b>, <b>capital, caixa e retorno</b>. As dez frentes estão no componente abaixo.')
    m = m.replace('<p class="sobre">Modelar · o centro do método</p>', '<p class="sobre">O que enxergamos</p>')
    a = m.index('    <div class="perguntas-frentes"'); b = m.index('</p>\n', m.index('<p class="fecho-mod">')) + 5
    m = m[:a] + m[b:]
    return m

METODO_V5 = """<section class="metodo metodo-v5" id="metodo" aria-labelledby="met-t">
  <div class="wrap">
    <div class="cab">
      <p class="sobre">Como a DALETH entra</p>
      <h2 class="h2" id="met-t">Do diagnóstico à implantação, em quatro movimentos.</h2>
      <p class="lead">A porta de entrada é o negócio, não um produto. Podemos começar por um terreno, um empreendimento, uma empresa ou uma necessidade de capital. O mapeamento mostra quais frentes precisam ser estruturadas.</p>
    </div>
    <div class="fluxo" id="fluxo">
      <div class="fio" aria-hidden="true"><span class="fio-base"></span><span class="fio-vivo"></span><i style="--p:0"></i><i style="--p:1"></i><i style="--p:2"></i><i style="--p:3"></i></div>
      <ol class="passos">
        <li><span class="num">01</span><h3>Mapear</h3><p class="pergunta">Onde estamos?</p><p class="detalhe">Ler ativos, premissas, restrições, riscos, recursos e oportunidades.</p><p class="papel"><em>A DALETH mapeia.</em><b>Você valida o retrato.</b></p></li>
        <li><span class="num">02</span><h3>Modelar</h3><p class="pergunta">Quais caminhos existem?</p><p class="detalhe">Comparar cenários, caixa, capital, risco, retorno e impacto sobre a empresa.</p><p class="papel"><em>A DALETH compara.</em><b>Você escolhe.</b></p></li>
        <li><span class="num">03</span><h3>Estruturar</h3><p class="pergunta">Como o caminho vira operação?</p><p class="detalhe">Organizar sociedade, contratos, funding, cronograma, responsabilidades e pontos de controle.</p><p class="papel"><em>A DALETH estrutura.</em><b>Você aprova.</b></p></li>
        <li><span class="num">04</span><h3>Acompanhar</h3><p class="pergunta">O que mudou no caminho?</p><p class="detalhe">Confrontar o realizado com o estruturado e sinalizar desvios relevantes.</p><p class="papel"><em>A DALETH acompanha.</em><b>Você decide os ajustes.</b></p></li>
      </ol>
    </div>
    <p class="papeis-linha">O cliente decide. A empresa executa. <em>A DALETH estrutura e acompanha.</em></p>
    <p class="linha-comercial"><b>Começamos por uma conversa de enquadramento.</b> Se houver aderência, escopo, prazo, responsabilidades e honorários ficam definidos em proposta antes do início do trabalho.</p>
  </div>
</section>
"""

ASSINATURA_V5 = ASSINATURA_V4.replace('class="cap abertura assina-sec" id="assinatura" aria-label="Assinatura"', 'class="cap abertura assina-sec esquerda" id="ao-seu-lado" aria-label="Ao seu lado"') \
    .replace('<p class="sobre">Nossa assinatura</p>', '<p class="sobre">Ao seu lado</p>') \
    .replace('Construção é a palavra que une o que fazemos: do empreendimento, da empresa, do capital. E da história de quem decide.',
             'Estruturar define o caminho. Acompanhar ajuda a preservar sua lógica enquanto o negócio acontece.') \
    .replace('    <a class="desce" href="#modelagem" aria-label="Descer para a modelagem"><i aria-hidden="true">↓</i><span>A modelagem</span></a>\n', '')

QUEM_V5 = """<section class="quem quem-v5" id="quem" aria-labelledby="quem-t">
  <div class="wrap">
    <div class="cab" style="margin-bottom:0">
      <p class="sobre">Quem está ao seu lado</p>
      <h2 class="h2" id="quem-t">Cristiano Valério Ribeiro</h2>
      <p class="meta">Engenharia de produção · Economia · MBA em gestão de negócios de incorporação e construção</p>
    </div>
    <div class="txt">
      <p class="lead">Experiência na estruturação de empreendimentos, financiamento à produção e organização de operações imobiliárias, atuando na interface entre empresa, empreendimento e capital.</p>
    </div>
  </div>
</section>
"""

CTA_V5 = """<section class="cap contato cta-final" id="contato" aria-labelledby="conv-t">
  <div class="wrap">
    <p class="sobre">Toda oportunidade começa com uma decisão.</p>
    <h2 id="conv-t">Vamos entender qual negócio existe nela.</h2>
    <p class="lead">Conte o terreno, o empreendimento, a empresa ou o desafio de capital. A primeira conversa serve para entender o cenário e identificar por onde começar.</p>
    <div class="acoes"><a class="btn btn-tinta" href="/contato/">Conversar sobre uma oportunidade</a></div>
    <p class="micro">Conversa de enquadramento · confidencial · sem custo · Belo Horizonte, atuação nacional</p>
  </div>
</section>
"""

JS_V5 = """<script>
// Método: o fio dourado acende quando a seção entra na tela
(function(){
  var f=document.getElementById("fluxo"); if(!f) return;
  if(!("IntersectionObserver" in window)){ f.classList.add("visto"); return; }
  new IntersectionObserver(function(es,o){ es.forEach(function(e){ if(e.isIntersecting){ f.classList.add("visto"); o.disconnect(); } }); },{threshold:0.35}).observe(f);
})();
</script>
"""

a_=TESE_V4.index('        <div class="acoes">'); b_=TESE_V4.index('</p>\n', TESE_V4.index('<p class="micro apoio-cta">'))+5
TESE_V5 = TESE_V4[:a_] + TESE_V4[b_:]

VERSOES["v5"] = dict(
    nome="v5 · Reconstrução",
    titulo_limpo=True,
    css_extra=CSS_V4 + CSS_V5,
    js_extra=JS_V5,
    nav=[("modelagem","O que fazemos"),("metodo","Como entramos"),("quem","Quem somos"),("contato","Conversa")],
    scripts_sub=[
      ('var fins=["de seu projeto", "de seu empreendimento", "de seu legado", "de sua história."];', 'var fins=["seu projeto", "seu empreendimento", "sua história."];'),
      ('alvo.innerHTML=final; p.classList.remove("digitando");', 'alvo.innerHTML=final; p.classList.remove("digitando"); p.classList.add("fixo");'),
      ('  espera(900,digitar);\n', '  if("IntersectionObserver" in window){ new IntersectionObserver(function(es,o){ es.forEach(function(e){ if(e.isIntersecting){ o.disconnect(); espera(500,digitar); } }); },{threshold:0.4}).observe(p); } else { espera(900,digitar); }\n'),
    ],
    corpo=lambda: [HERO_V4, TESE_V5, modelagem_v5(), METODO_V5, ASSINATURA_V5, QUEM_V5, CTA_V5])

for chave, v in VERSOES.items():
    corpo = "".join(v["corpo"]())
    scripts = SCRIPTS
    for a, b in v.get("scripts_sub", []):
        assert a in scripts, a
        scripts = scripts.replace(a, b)
    html = (HEAD.replace("</style>", CSS_V3 + v.get("css_extra","") + "</style>")
            .replace("<title>DALETH · Estruturação de Negócios Imobiliários</title>", "<title>DALETH · Estruturação de Negócios Imobiliários</title>" if v.get("titulo_limpo") else f"<title>DALETH · Estruturação de Negócios Imobiliários (teste {v['nome']})</title>")
            + "</head>\n<body>\n" + header(v["nav"]) + "\n<main id=\"main\">\n" + corpo + "</main>\n\n" + RODAPE + "\n" + CTA_MOVEL + scripts + JS_V3 + v.get("js_extra","") + "</body>\n</html>\n")
    (AQUI / f"{chave}.html").write_text(html, encoding="utf-8")
    print(chave, len(html)//1024, "KB", "seções:", corpo.count("<section"))
