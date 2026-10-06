// DALETH · página Modelagem: tudo conectado
// Oito frentes de modelagem. Ao escolher uma, as palavras dela entram nos nós da rede 3D,
// enquanto a cena continua girando: a mesma rede, outra camada da decisão.
(function () {
  "use strict";
  var tela = document.querySelector('canvas[data-cena="modelagem"]');
  var botoes = document.querySelectorAll("[data-frente]");
  if (!tela || !botoes.length) return;
  var reduzir = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  var FRENTES = {
    tudo: { nome: "Tudo conectado",
      texto: "Oito frentes, uma decisão. Mudar uma muda as outras. Por isso modelamos antes de escolher.",
      palavras: ["Societária", "Documental", "Tributária", "Financeira", "Funding", "Terreno", "Técnica", "Produto e mercado"] },
    societaria: { nome: "Societária",
      texto: "Quem entra, com que risco e com que direito. A forma da sociedade muda o tributo, o funding e a saída.",
      palavras: ["SPE", "SCP", "Holding", "Acordo de cotistas", "Investidor", "Isolamento de risco"] },
    documental: { nome: "Documental",
      texto: "O que precisa existir no papel para o negócio andar, do registro às garantias.",
      palavras: ["Incorporação", "Memorial", "Matrícula", "Licenças", "Contratos", "Garantias", "Permuta e parceria", "Due diligence"] },
    tributaria: { nome: "Tributária",
      texto: "O regime e o tratamento de cada operação mudam o resultado, e dependem da forma societária e do produto.",
      palavras: ["RET", "Lucro presumido", "Lucro real", "Tratamento da permuta", "Distribuição"] },
    financeira: { nome: "Financeira",
      texto: "Quanto entra, quanto sai e em que mês. É onde todas as outras escolhas aparecem como número.",
      palavras: ["Fluxo de caixa", "Exposição", "Cenários", "Preço", "Ritmo de vendas", "TIR", "VPL", "Ponto de equilíbrio"] },
    funding: { nome: "Funding",
      texto: "De onde vem o recurso e em que condições. Quem aprova é o financiador; a estrutura prepara a operação.",
      palavras: ["Crédito bancário", "Caixa", "Investidor", "Grupo de investidores", "CRI", "Mercado de capitais", "Recursos próprios"] },
    terreno: { nome: "Terreno",
      texto: "Como o terreno entra no negócio muda o caixa do primeiro mês e o produto possível.",
      palavras: ["Permuta física", "Permuta financeira", "Permuta mista", "Opção de compra", "Pagamento a prazo", "Parceria com o proprietário", "Contrato", "Diligência"] },
    tecnica: { nome: "Técnica",
      texto: "O que se constrói, como e em quantas etapas. Cada escolha técnica aparece no orçamento e no cronograma.",
      palavras: ["Eficiência de área", "Soluções construtivas", "Faseamento", "Compatibilização", "Impacto no custo", "Orçamento", "Torres e quadras", "Etapas"] },
    produto: { nome: "Produto e mercado",
      texto: "Para quem, a que preço e em que ritmo. O produto define o orçamento, e a venda define o caixa.",
      palavras: ["Produto", "Público", "Preço", "Lançamento", "Estratégia de vendas"] }
  };
  var ORDEM = ["tudo", "societaria", "documental", "tributaria", "financeira", "funding", "terreno", "tecnica", "produto"];

  var nomeEl = document.getElementById("frente-nome");
  var textoEl = document.getElementById("frente-texto");
  var chipsEl = document.getElementById("frente-palavras");
  var atual = "tudo", espera = null;

  function mostrar(chave) {
    var f = FRENTES[chave];
    if (!f) return;
    atual = chave;
    botoes.forEach(function (b) { b.setAttribute("aria-pressed", String(b.dataset.frente === chave)); });
    if (nomeEl) nomeEl.textContent = f.nome;
    if (textoEl) textoEl.textContent = f.texto;
    if (chipsEl) {
      chipsEl.innerHTML = "";
      f.palavras.forEach(function (p) {
        var li = document.createElement("li");
        li.textContent = p;
        chipsEl.appendChild(li);
      });
    }
    if (tela.cena3d) tela.cena3d.rotular(f.palavras);
    else tela.setAttribute("data-rotulos", f.palavras.join("|"));   // a cena ainda não montou: nasce com estas palavras
  }

  botoes.forEach(function (b) {
    b.addEventListener("click", function () {
      parar();
      mostrar(b.dataset.frente);
      // no celular os botões ficam acima do palco: leva a cena para a tela
      var palco = tela.closest(".modelar-palco");
      if (palco && window.innerWidth < 1024) {
        var r = palco.getBoundingClientRect();
        if (r.top > window.innerHeight * 0.55 || r.bottom < 120) palco.scrollIntoView({ behavior: reduzir ? "auto" : "smooth", block: "start" });
      }
    });
  });

  // passeia pelas frentes sozinho até a primeira interação (não quando o visitante pediu menos movimento)
  function proxima() {
    var i = (ORDEM.indexOf(atual) + 1) % ORDEM.length;
    mostrar(ORDEM[i]);
  }
  function parar() {
    if (espera) { clearInterval(espera); espera = null; }
    var auto = document.getElementById("frente-auto");
    if (auto) { auto.setAttribute("aria-pressed", "false"); auto.textContent = "Passear pelas frentes"; }
  }
  function passear() {
    parar();
    espera = setInterval(proxima, 4500);
    var auto = document.getElementById("frente-auto");
    if (auto) { auto.setAttribute("aria-pressed", "true"); auto.textContent = "Parar o passeio"; }
  }
  var botaoAuto = document.getElementById("frente-auto");
  if (botaoAuto) botaoAuto.addEventListener("click", function () { if (espera) parar(); else passear(); });

  mostrar("tudo");
  if (!reduzir && "IntersectionObserver" in window) {
    var palco = tela.closest(".modelar-palco") || tela;
    var obs = new IntersectionObserver(function (es) {
      es.forEach(function (e) {
        if (e.isIntersecting && !espera && !palco.dataset.tocado) passear();
        if (!e.isIntersecting && espera) parar();
      });
    }, { threshold: 0.4 });
    obs.observe(palco);
    palco.addEventListener("pointerdown", function () { palco.dataset.tocado = "1"; }, { once: true });
  }
})();
