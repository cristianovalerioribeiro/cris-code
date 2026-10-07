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
.btn-linha{border-color:var(--linha);color:var(--tinta)}
.cap .btn-linha,.modelar .btn-linha{border-color:var(--cap-linha);color:var(--cap-txt)}
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
.perguntas-frentes button{font:500 12px/1 var(--f-txt);padding:7px 10px;border:1px solid rgba(212,179,124,.45);border-radius:999px;background:rgba(255,255,255,.04);color:var(--m-branco);cursor:pointer}
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
    return f'''<a class="pular" href="#tese">Ir para o conteúdo</a>
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
    <p class="clareza">Estruturamos empresas e empreendimentos imobiliários para quem decide construir mais.</p>
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
        <p class="tri-legenda">Empresa, empreendimento e capital se decidem juntos. Mexer em um muda os outros dois.</p>
      </div>
    </div>
    {{PONTE}}
  </div>
</section>
'''

FICHA_ESTATICA = '''<p class="mf-num">00 · Modelagem do empreendimento</p><h3 class="mf-nome">Tudo conectado</h3><p class="mf-frase">Mudar uma frente muda as outras. Por isso comparamos antes de escolher.</p><ul class="mf-sub"><li>Terreno</li><li>Produto e mercado</li><li>Técnica</li><li>Jurídico</li><li>Societário</li><li>Tributário</li><li>Econômico-financeiro</li><li>Capital e funding</li><li>Comercialização</li><li>Risco e retorno</li></ul>'''

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
    <p class="mp-dica">Setas percorrem as frentes. Os nomes em dourado levam a quem cada uma move. <a href="/assets/docs/DALETH-Modelagem-do-Empreendimento.pdf" download>Este capítulo em PDF</a>.</p>
    <div class="perguntas-frentes" aria-label="As frentes, pela pergunta que respondem">
      <div><h3>O que este terreno pode ser?</h3><p><button type="button" data-frente="terreno">Terreno e permutas</button><button type="button" data-frente="produto">Produto e mercado</button><button type="button" data-frente="tecnica">Técnica e projeto</button><button type="button" data-frente="comercial">Comercialização</button></p></div>
      <div><h3>Em que forma o negócio existe?</h3><p><button type="button" data-frente="societario">Societário</button><button type="button" data-frente="juridico">Jurídico e documental</button><button type="button" data-frente="tributario">Tributário</button></p></div>
      <div><h3>Como o dinheiro entra, sai e volta?</h3><p><button type="button" data-frente="financeiro">Fluxo e exposição</button><button type="button" data-frente="capital">Capital e funding</button><button type="button" data-frente="risco">Risco e retorno</button></p></div>
    </div>
    <p class="fecho-mod">O projeto fica com o arquiteto, a empresa com o contador, o capital com o banco. Alguém precisa olhar os três juntos.</p>
    {ponte}
  </div>
</section>
'''

def metodo(recebe_longo=False, ponte=""):
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
    return f'''<section class="metodo" id="metodo" aria-labelledby="met-t">
  <div class="wrap">
    <div class="cab">
      <p class="sobre">Como trabalhamos</p>
      <h2 class="h2" id="met-t">Quatro movimentos. Cada um termina com algo escrito na sua mão.</h2>
      <p class="lead">Começa com uma conversa sem custo. Cada movimento entrega algo escrito e pede uma decisão sua.</p>
    </div>
    <ol class="passos">
      <li class="entrada">
        <span class="num">PORTA DE ENTRADA</span>
        <h3>Conversa de enquadramento</h3>
        <p class="recebe">Você conta o terreno, a empresa ou a necessidade de capital. Saímos sabendo se há caso e por onde ele começa.</p>
        <span class="selo">sem custo</span>
      </li>
      <li><span class="num">01</span><h3>Mapear</h3><p class="para">para compreender</p><p class="frase">Mapear a situação real, antes de recomendar.</p><p class="recebe"><b>Você recebe</b>{R["mapear"][k]}</p></li>
      <li><span class="num">02</span><h3>Modelar</h3><p class="para">para enxergar</p><p class="frase">Comparar os caminhos antes de comprometer o capital.</p><p class="recebe"><b>Você recebe</b>{R["modelar"][k]}</p></li>
      <li><span class="num">03</span><h3>Estruturar</h3><p class="para">para tornar executável</p><p class="frase">Transformar o caminho escolhido em operação.</p><p class="recebe"><b>Você recebe</b>{R["estruturar"][k]}</p></li>
      <li><span class="num">04</span><h3>Conduzir</h3><p class="para">para funcionar</p><p class="frase">Acompanhar a implantação ao lado de quem executa.</p><p class="recebe"><b>Você recebe</b>{R["conduzir"][k]}</p></li>
    </ol>
    <p class="nota" style="margin-top:24px">Escopo, prazo e valor de cada movimento ficam na proposta, caso a caso.</p>
    {ponte}
  </div>
</section>
'''

def entregas(fundo_papel=False, ponte=""):
    return f'''<section class="recebe-sec{' papel' if fundo_papel else ''}" id="entregas" aria-labelledby="ent-t">
  <div class="wrap">
    <div class="cab">
      <p class="sobre">O que você recebe</p>
      <h2 class="h2" id="ent-t">O que fica na sua mão em cada movimento.</h2>
      <p class="lead">Nada aqui tem nome de produto. Cada movimento termina com algo escrito, lido com você, e uma decisão sua.</p>
    </div>
    <div class="entregas-grade">
      <div class="entrega"><span class="num">01 · MAPEAR</span><h3>Um retrato escrito</h3><p>Ativos, recursos, restrições, riscos, premissas e oportunidades. As perguntas abertas, por urgência. Os caminhos que merecem comparação, e os que não, com o motivo. <b>Você decide se vale modelar.</b></p></div>
      <div class="entrega"><span class="num">02 · MODELAR</span><h3>Os caminhos lado a lado</h3><p>Premissas escritas, caixa e exposição de cada um, risco assumido, valor capturado, o que exigem da empresa. Nossa indicação e o porquê. <b>Você escolhe, e a escolha fica registrada.</b></p></div>
      <div class="entrega"><span class="num">03 · ESTRUTURAR</span><h3>A operação por escrito</h3><p>Sociedade e passos de constituição, forma de aquisição do terreno, contratos com responsável por cada um, caixa alvo com pontos de controle, dossiê pronto para banco, investidor ou sócio. <b>Quem aprova é o financiador.</b></p></div>
      <div class="entrega"><span class="num">04 · CONDUZIR</span><h3>Presença nos pontos de controle</h3><p>Definidos na estruturação. A cada ponto, uma leitura escrita do que mudou em relação à premissa e do que fazer. <b>A execução continua com a sua empresa.</b></p></div>
    </div>
    <p class="nota">Escopo, prazo e valor de cada movimento ficam na proposta, caso a caso.</p>
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
        <p class="num">R$ 324 mi<small>em VGV de operações de financiamento à produção trabalhadas, na trajetória do fundador, via TRAL3.</small></p>
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
      <details><summary>Minha obra parou. É caso para vocês?</summary><p>Pode ser. Obra parada mexe nos três lados ao mesmo tempo e quase sempre começa pela frente jurídica. A conversa de enquadramento diz se há caminho e por onde ele começa.</p></details>
      <details><summary>Atendem fora de Minas Gerais?</summary><p>Sim. A base é Belo Horizonte e a atuação é nacional, à distância, com presença quando o caso pede. Documentos e decisões circulam por escrito.</p></details>
      <details><summary>O que vocês não fazem?</summary><p>Não captamos recursos, não damos curso, não fazemos BPO e não assumimos a execução. É estruturação.</p></details>
    </div>
  </div>
</section>
'''

CONVERSA = '''<section class="cap contato" id="contato" aria-labelledby="conv-t">
  <div class="wrap">
    <div class="cab" style="margin-bottom:0">
      <p class="sobre">Começa com uma conversa</p>
      <h2 id="conv-t">Conte o terreno, o produto ou a empresa.</h2>
      <p class="lead">Você conta. Saímos sabendo se há caso e por onde ele começa. Escopo, prazo e valor ficam na proposta.</p>
      <ol class="degraus">
        <li><b>Conversa de enquadramento</b><span>Sem custo e sem compromisso.</span></li>
        <li><b>Mapeamento</b><span>O primeiro trabalho, só se fizer sentido para os dois lados.</span></li>
        <li><b>Escopo escrito</b><span>Prazo, entregas e valor antes de começar.</span></li>
      </ol>
    </div>
    <div class="canal">
      <b>Canal de contato</b>
      <p>Em definição: e-mail, WhatsApp ou formulário. Este quadro sai quando o canal estiver escolhido.</p>
      <p>Confidencial desde a primeira mensagem. Belo Horizonte · atuação nacional.</p>
    </div>
  </div>
</section>
'''

CTA_MOVEL = '''<div class="cta-movel" id="cta-movel" aria-hidden="true"><a class="btn btn-tinta" href="#contato" tabindex="-1">Conversar sobre uma oportunidade</a></div>
'''
JS_V3 = '''<script>
// Barra de CTA no celular: aparece depois da abertura, some perto do fecho
(function(){
  var barra=document.getElementById("cta-movel"), ab=document.getElementById("inicio"), fim=document.getElementById("contato");
  if(!barra||!ab||!fim||!("IntersectionObserver" in window)) return;
  document.body.classList.add("com-cta-movel");
  var passouAbertura=false, noFim=false;
  function ajustar(){ var v=passouAbertura&&!noFim; barra.classList.toggle("visivel",v); barra.setAttribute("aria-hidden",String(!v)); barra.querySelector("a").tabIndex=v?0:-1; }
  new IntersectionObserver(function(es){ es.forEach(function(e){ passouAbertura=!e.isIntersecting; }); ajustar(); },{threshold:0.15}).observe(ab);
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
    corpo=lambda: [ABERTURA, TESE.replace("{PONTE}",""), modelagem("Nenhuma frente de um empreendimento se decide sozinha."),
                   metodo(recebe_longo=True), quem(com_papeis=True), FAQ, CONVERSA]),
  "v3b": dict(
    nome="B · Narrativa",
    nav=[("modelagem","Modelagem"),("metodo","Como trabalhamos"),("entregas","O que você recebe"),("ao-seu-lado","Ao seu lado"),("quem","Quem conduz")],
    corpo=lambda: [ABERTURA, TESE.replace("{PONTE}", ponte("modelagem","Se os três lados se movem juntos, como enxergar isso antes de decidir?")),
                   modelagem("Toda oportunidade guarda mais de um negócio.", ponte("metodo","Comparar antes faz sentido. Qual é a sequência?")),
                   metodo(ponte=ponte("entregas","E o que fica na minha mão em cada passo?")),
                   entregas(fundo_papel=True, ponte=ponte("ao-seu-lado","Depois que eu escolher, vocês somem ou ficam?")),
                   lado(), quem(), FAQ, CONVERSA]),
  "v3c": dict(
    nome="C · Entregas primeiro",
    nav=[("entregas","O que você recebe"),("modelagem","Modelagem"),("metodo","Como trabalhamos"),("quem","Quem conduz")],
    corpo=lambda: [ABERTURA, TESE.replace("{PONTE}",""), entregas(),
                   modelagem("Toda oportunidade guarda mais de um negócio."), metodo(), quem(com_papeis=True), FAQ, CONVERSA]),
}

for chave, v in VERSOES.items():
    corpo = "".join(v["corpo"]())
    html = (HEAD.replace("</style>", CSS_V3 + "</style>")
            .replace("<title>DALETH · Estruturação de Negócios Imobiliários</title>", f"<title>DALETH · Estruturação de Negócios Imobiliários (teste {v['nome']})</title>")
            + "</head>\n<body>\n" + header(v["nav"]) + "\n<main>\n" + corpo + "</main>\n\n" + RODAPE + "\n" + CTA_MOVEL + SCRIPTS + JS_V3 + "</body>\n</html>\n")
    (AQUI / f"{chave}.html").write_text(html, encoding="utf-8")
    print(chave, len(html)//1024, "KB", "seções:", corpo.count("<section"))
