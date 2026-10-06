// DALETH · Modelagem do empreendimento: dez frentes na mesma rede
// Duas apresentações do mesmo conteúdo (data-modelar="prancha" | "percurso"):
//   prancha   palco largo com ficha ancorada; frentes numeradas embaixo; setas e teclado
//   percurso  cena fixa de um lado, as frentes rolam como capítulos do outro
// Ao mudar de frente, as palavras dela entram nos nós da rede 3D (canvas.cena3d.rotular).
(function () {
  "use strict";
  var raiz = document.querySelector("[data-modelar]");
  var tela = document.querySelector('canvas[data-cena="modelagem"]');
  if (!raiz || !tela) return;
  var modo = raiz.getAttribute("data-modelar");
  var reduzir = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  var FRENTES = [
    { id: "tudo", num: "00", nome: "Tudo conectado", curto: "Tudo",
      frase: "Dez frentes, uma decisão. Mudar uma muda as outras. Por isso modelamos antes de escolher.",
      sub: ["Terreno", "Produto e mercado", "Técnica", "Jurídico", "Societário", "Tributário", "Econômico-financeiro", "Capital e funding", "Comercialização", "Risco e retorno"],
      move: [] },
    { id: "terreno", num: "01", nome: "Terreno", curto: "Terreno",
      frase: "Estruturar o terreno é definir a base jurídica, econômica e negocial sobre a qual todo o empreendimento será construído.",
      sub: ["Compra", "Permuta", "Opção", "Parceria", "Aporte", "Prazo", "Due diligence", "Regularização"],
      move: ["produto", "juridico", "capital"] },
    { id: "produto", num: "02", nome: "Produto e mercado", curto: "Produto",
      frase: "Estruturar o produto é transformar o potencial do terreno em uma oferta aderente à demanda, ao preço e à capacidade de absorção do mercado.",
      sub: ["Público", "Tipologia", "Mix", "Área", "Ticket", "Preço por m²", "VGV", "Demanda", "Absorção", "Lançamento"],
      move: ["tecnica", "comercial", "financeiro"] },
    { id: "tecnica", num: "03", nome: "Técnica", curto: "Técnica",
      frase: "Estruturar tecnicamente é converter o produto idealizado em uma solução executável, eficiente e compatível com custo, prazo e qualidade.",
      sub: ["Implantação", "Eficiência", "Projetos", "Sistema construtivo", "Compatibilização", "Infraestrutura", "Fases", "Orçamento", "Cronograma"],
      move: ["financeiro", "produto", "comercial"] },
    { id: "juridico", num: "04", nome: "Jurídico e regulatório", curto: "Jurídico",
      frase: "Estruturar juridicamente é criar segurança para desenvolver, contratar, financiar, comercializar e concluir o empreendimento.",
      sub: ["Matrícula", "Licenças", "Incorporação", "Memorial", "Contratos", "Permutas", "Parcerias", "Garantias", "Registros"],
      move: ["societario", "capital", "comercial"] },
    { id: "societario", num: "05", nome: "Societário e governança", curto: "Societário",
      frase: "Estruturar a sociedade é definir quem participa, quanto aporta, como decide, como assume riscos e como recebe resultados.",
      sub: ["SPE", "SCP", "Holding", "Sócios", "Investidores", "Participações", "Aportes", "Governança", "Saída", "Isolamento de risco"],
      move: ["tributario", "risco", "capital"] },
    { id: "tributario", num: "06", nome: "Tributário", curto: "Tributário",
      frase: "Estruturar a tributação é adequar a operação ao regime mais eficiente e coerente com o modelo societário, comercial e financeiro.",
      sub: ["RET", "Presumido", "Real", "Afetação", "Permuta", "Integralização", "Ganho de capital", "Distribuição"],
      move: ["financeiro", "societario", "terreno"] },
    { id: "financeiro", num: "07", nome: "Econômico-financeiro", curto: "Financeiro",
      frase: "Estruturar financeiramente é medir capital, retorno, exposição e sensibilidade para saber se o empreendimento cria valor e suporta seus riscos.",
      sub: ["Fluxo de caixa", "Exposição", "Capital necessário", "Margem", "TIR", "VPL", "Payback", "Break-even", "Sensibilidades", "Cenários"],
      move: ["capital", "comercial", "risco"] },
    { id: "capital", num: "08", nome: "Capital e funding", curto: "Funding",
      frase: "Estruturar o funding é combinar as fontes de capital certas, no momento certo, com custo, prazo, garantias e risco compatíveis com o projeto.",
      sub: ["Capital próprio", "Sócios", "Investidor", "Equity", "Dívida", "Caixa", "Bancos", "Recebíveis", "CRI", "Mercado de capitais"],
      move: ["risco", "juridico", "financeiro"] },
    { id: "comercial", num: "09", nome: "Comercialização", curto: "Comercial",
      frase: "Estruturar a comercialização é transformar produto em receita, equilibrando preço, velocidade de vendas e geração de caixa.",
      sub: ["Preço", "Tabela", "Entrada", "Parcelamento", "Velocidade", "Pré-venda", "Associativo", "Repasse", "Estoque", "Canais"],
      move: ["financeiro", "capital", "produto"] },
    { id: "risco", num: "10", nome: "Risco e retorno", curto: "Risco",
      frase: "Estruturar risco e retorno é equilibrar proteção, exposição e remuneração entre empreendedor, investidores, financiadores e demais partes.",
      sub: ["Riscos", "Garantias", "Covenants", "Contingência", "Participações", "Preferência", "Waterfall", "Distribuição", "Exit"],
      move: ["societario", "capital", "juridico"] }
  ];
  var POR_ID = {};
  FRENTES.forEach(function (f) { POR_ID[f.id] = f; });

  var atual = "tudo";
  var ouvintes = [];
  function mostrar(id, origem) {
    var f = POR_ID[id];
    if (!f) return;
    atual = id;
    if (tela.cena3d) tela.cena3d.rotular(f.sub);
    else tela.setAttribute("data-rotulos", f.sub.join("|"));
    ouvintes.forEach(function (fn) { fn(f, origem); });
  }
  function el(tag, cls, texto) {
    var e = document.createElement(tag);
    if (cls) e.className = cls;
    if (texto != null) e.textContent = texto;
    return e;
  }
  // a ficha de uma frente: número, nome, frase, decisões, o que ela move
  function preencherFicha(caixa, f) {
    caixa.innerHTML = "";
    var cab = el("p", "mf-num", f.num + " · " + (f.id === "tudo" ? "Modelagem do empreendimento" : "Frente"));
    var nome = el("h3", "mf-nome", f.nome);
    var frase = el("p", "mf-frase", f.frase);
    var sub = el("ul", "mf-sub");
    f.sub.forEach(function (s) { sub.appendChild(el("li", null, s)); });
    caixa.appendChild(cab); caixa.appendChild(nome); caixa.appendChild(frase); caixa.appendChild(sub);
    if (f.move.length) {
      var mv = el("p", "mf-move");
      mv.appendChild(el("span", "mf-move-rot", "Também move"));
      f.move.forEach(function (id) {
        var b = el("button", "mf-link", POR_ID[id].nome);
        b.type = "button"; b.dataset.ir = id;
        b.addEventListener("click", function () { mostrar(id, "ligacao"); });
        mv.appendChild(b);
      });
      caixa.appendChild(mv);
    }
  }

  // ------------------------------------------------------------ prancha
  if (modo === "prancha") {
    var trilho = raiz.querySelector(".mp-trilho");
    var ficha = raiz.querySelector(".mp-ficha");
    var palco = raiz.querySelector(".mp-palco");
    // em telas estreitas a ficha sai de dentro do palco e vem logo abaixo dele
    var estreita = window.matchMedia("(max-width: 1023px)");
    function acomodar() {
      if (estreita.matches) { if (ficha.parentNode === palco) palco.parentNode.insertBefore(ficha, palco.nextSibling); }
      else if (ficha.parentNode !== palco) palco.appendChild(ficha);
    }
    acomodar();
    if (estreita.addEventListener) estreita.addEventListener("change", acomodar);
    var botoes = [];
    FRENTES.forEach(function (f) {
      var b = el("button", "mp-frente");
      b.type = "button"; b.dataset.frente = f.id; b.setAttribute("aria-pressed", "false");
      b.appendChild(el("span", "n", f.num)); b.appendChild(el("span", "t", f.curto));
      b.addEventListener("click", function () { parar(); mostrar(f.id, "botao"); });
      trilho.appendChild(b); botoes.push(b);
    });
    var espera = null, autoBtn = raiz.querySelector(".mp-auto");
    function parar() {
      if (espera) { clearInterval(espera); espera = null; }
      if (autoBtn) { autoBtn.setAttribute("aria-pressed", "false"); autoBtn.textContent = "Passear pelas frentes"; }
    }
    function passear() {
      parar();
      espera = setInterval(function () {
        var i = FRENTES.findIndex(function (f) { return f.id === atual; });
        mostrar(FRENTES[(i + 1) % FRENTES.length].id, "auto");
      }, 5000);
      if (autoBtn) { autoBtn.setAttribute("aria-pressed", "true"); autoBtn.textContent = "Parar o passeio"; }
    }
    if (autoBtn) autoBtn.addEventListener("click", function () { if (espera) parar(); else passear(); });
    raiz.querySelectorAll("[data-passo]").forEach(function (seta) {
      seta.addEventListener("click", function () {
        parar();
        var i = FRENTES.findIndex(function (f) { return f.id === atual; });
        var n = (i + parseInt(seta.dataset.passo, 10) + FRENTES.length) % FRENTES.length;
        mostrar(FRENTES[n].id, "seta");
      });
    });
    raiz.addEventListener("keydown", function (e) {
      if (e.key !== "ArrowRight" && e.key !== "ArrowLeft") return;
      e.preventDefault(); parar();
      var i = FRENTES.findIndex(function (f) { return f.id === atual; });
      var n = (i + (e.key === "ArrowRight" ? 1 : -1) + FRENTES.length) % FRENTES.length;
      mostrar(FRENTES[n].id, "tecla");
      var b = botoes[n]; if (b) b.focus();
    });
    ouvintes.push(function (f, origem) {
      botoes.forEach(function (b) { b.setAttribute("aria-pressed", String(b.dataset.frente === f.id)); });
      ficha.classList.remove("troca"); void ficha.offsetWidth; ficha.classList.add("troca");
      preencherFicha(ficha, f);
      var b = botoes[FRENTES.indexOf(f)];
      if (b && origem !== "auto" && b.scrollIntoView) b.scrollIntoView({ block: "nearest", inline: "center", behavior: reduzir ? "auto" : "smooth" });
      if (origem === "ligacao" && window.innerWidth < 1024) ficha.scrollIntoView({ block: "nearest", behavior: reduzir ? "auto" : "smooth" });
    });
    mostrar("tudo", "inicio");
    if (!reduzir && "IntersectionObserver" in window) {
      var tocado = false;
      raiz.addEventListener("pointerdown", function () { tocado = true; }, { once: true });
      new IntersectionObserver(function (es) {
        es.forEach(function (e) {
          if (e.isIntersecting && !espera && !tocado) passear();
          if (!e.isIntersecting && espera) parar();
        });
      }, { threshold: 0.35 }).observe(raiz.querySelector(".mp-palco"));
    }
  }

  // ------------------------------------------------------------ percurso
  if (modo === "percurso") {
    var lista = raiz.querySelector(".mq-capitulos");
    var pontos = raiz.querySelector(".mq-pontos");
    var cartoes = [];
    FRENTES.forEach(function (f) {
      var art = el("article", "mq-cap");
      art.id = "frente-" + f.id; art.dataset.frente = f.id;
      preencherFicha(art, f);
      lista.appendChild(art); cartoes.push(art);
      if (pontos) {
        var p = el("a", "mq-ponto"); p.href = "#frente-" + f.id; p.setAttribute("aria-label", f.num + " " + f.nome);
        p.appendChild(el("span", null, f.num));
        pontos.appendChild(p);
      }
    });
    var marcas = pontos ? Array.prototype.slice.call(pontos.children) : [];
    var titulo = raiz.querySelector(".mq-atual");
    ouvintes.push(function (f) {
      cartoes.forEach(function (c) { c.classList.toggle("ativa", c.dataset.frente === f.id); });
      marcas.forEach(function (m, i) { m.classList.toggle("ativa", FRENTES[i].id === f.id); m.classList.toggle("passada", FRENTES.indexOf(f) > i); });
      if (titulo) { titulo.textContent = f.num + " · " + f.nome; }
    });
    // os links "também move" rolam até o capítulo
    ouvintes.push(function (f, origem) {
      if (origem === "ligacao") {
        var alvo = document.getElementById("frente-" + f.id);
        if (alvo) alvo.scrollIntoView({ block: "center", behavior: reduzir ? "auto" : "smooth" });
      }
    });
    if ("IntersectionObserver" in window) {
      var obs = new IntersectionObserver(function (es) {
        es.forEach(function (e) { if (e.isIntersecting) mostrar(e.target.dataset.frente, "rolagem"); });
      }, { rootMargin: "-45% 0px -45% 0px", threshold: 0 });
      cartoes.forEach(function (c) { obs.observe(c); });
    }
    mostrar("tudo", "inicio");
  }
})();
