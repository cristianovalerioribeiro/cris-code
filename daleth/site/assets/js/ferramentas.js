// DALETH · simulador de exposição de caixa
// Simulação ilustrativa, com as premissas fixas escritas na própria página.
// O mesmo modelo existe em modelo.py, que monta o quadro de alternativas da home:
// se mudar uma premissa aqui, mude lá também.
(function () {
  "use strict";
  var el = function (id) { return document.getElementById(id); };
  var curva = el("curva");
  if (!curva) return;

  var MESES = 30, OBRA = 24, CUSTO = 0.55, DESPESAS = 0.12, REPASSE = 3;
  var campos = ["vgv", "terreno", "permuta", "planta", "credito"];
  var faltando = campos.concat(["k-exposicao", "k-mes", "k-resultado"]).filter(function (id) { return !el(id); });
  if (faltando.length) return;   // fica o aviso estático, sem quebrar a página

  var FALA = {
    vgv: function (v) { return "R$ " + v + " milhões"; },
    terreno: function (v) { return v + " por cento do VGV"; },
    permuta: function (v) { return v + " por cento do terreno"; },
    planta: function (v) { return v + " por cento do VGV"; },
    credito: function (v) { return v + " por cento do custo da obra"; }
  };
  var MOSTRA = {
    vgv: function (v) { return "R$ " + v + " mi"; },
    terreno: function (v) { return v + "%"; }, permuta: function (v) { return v + "%"; },
    planta: function (v) { return v + "%"; }, credito: function (v) { return v + "%"; }
  };

  function moeda(v) {
    var mi = v / 1e6;
    return "R$ " + mi.toFixed(Math.abs(mi) >= 10 ? 1 : 2).replace(".", ",") + " mi";
  }

  function calcular(p) {
    var vgv = p.vgv * 1e6;
    var custoObra = vgv * CUSTO, despesas = vgv * DESPESAS;
    var terreno = vgv * p.terreno / 100;
    var terrenoDinheiro = terreno * (1 - p.permuta / 100);
    var vgvDisponivel = vgv - terreno * p.permuta / 100;   // a permuta paga em unidades
    var credito = custoObra * p.credito / 100;
    var planta = vgvDisponivel * p.planta / 100;
    var entrega = vgvDisponivel - planta;
    var saldo = 0, serie = [], pior = 0, mesPior = -1;
    for (var m = 0; m <= MESES; m++) {
      var f = 0;
      if (m === 0) f -= terrenoDinheiro;
      if (m >= 1 && m <= OBRA) f += (credito + planta - custoObra - despesas) / OBRA;
      if (m === OBRA + REPASSE) f += entrega - credito;
      saldo += f;
      serie.push(saldo);
      if (saldo < pior - 1) { pior = saldo; mesPior = m; }
    }
    return { serie: serie, exposicao: -pior, mes: mesPior, sem: mesPior < 0, resultado: saldo };
  }

  var NS = "http://www.w3.org/2000/svg";
  function no(tag, attrs, texto) {
    var n = document.createElementNS(NS, tag);
    for (var k in attrs) n.setAttribute(k, attrs[k]);
    if (texto) n.textContent = texto;
    return n;
  }

  function desenhar(r) {
    // o SVG encolhe no celular: o texto cresce na mesma proporção para ficar com ~12px na tela
    var k = Math.max(1, 640 / (curva.clientWidth || 640));
    var fs = Math.round(12 * k), fsDestaque = Math.round(13 * k);
    var w = 640, h = 300 + Math.round(20 * (k - 1)), e = 22 + Math.round(30 * k), d = 16, t = 26, b = 18 + Math.round(16 * k);
    curva.setAttribute("viewBox", "0 0 " + w + " " + h);
    var vals = r.serie.concat([0]);
    var max = Math.max.apply(null, vals), min = Math.min.apply(null, vals);
    var amp = (max - min) || 1;
    var x = function (i) { return e + i / (r.serie.length - 1) * (w - e - d); };
    var y = function (v) { return t + (max - v) / amp * (h - t - b); };
    while (curva.firstChild) curva.removeChild(curva.firstChild);
    var cinza = "#5E6E7D";
    // eixo do tempo
    [0, 6, 12, 18, 24, 30].forEach(function (m) {
      curva.appendChild(no("line", { x1: x(m), x2: x(m), y1: t, y2: h - b, stroke: "#E9EEF2" }));
      curva.appendChild(no("text", { x: x(m), y: h - 12, "text-anchor": "middle", fill: cinza,
        "font-size": fs, "font-family": "Inter, sans-serif" }, m === 0 ? "mês 0" : String(m)));
    });
    // faixa da obra
    curva.appendChild(no("rect", { x: x(1), y: h - b + 4, width: x(OBRA) - x(1), height: 4, fill: "#D6DEE6", rx: 2 }));
    // linha do zero
    var z = y(0);
    curva.appendChild(no("line", { x1: e, x2: w - d, y1: z, y2: z, stroke: "#082538", "stroke-width": 1, "stroke-dasharray": "4 4" }));
    // eixo do saldo, em R$ mi
    var passoMi = amp / 1e6 > 24 ? 10 : amp / 1e6 > 10 ? 5 : amp / 1e6 > 4 ? 2 : 1;
    for (var v = Math.ceil(min / 1e6 / passoMi) * passoMi; v <= max / 1e6; v += passoMi) {
      var yy = y(v * 1e6);
      if (v !== 0) curva.appendChild(no("line", { x1: e, x2: w - d, y1: yy, y2: yy, stroke: "#F2F5F8" }));
      curva.appendChild(no("text", { x: e - 8, y: yy + 4, "text-anchor": "end", fill: cinza, "font-size": fs,
        "font-family": "Inter, sans-serif" }, v === 0 ? "0" : String(v)));
    }
    curva.appendChild(no("text", { x: e - 8, y: t - 10, "text-anchor": "end", fill: cinza, "font-size": fs,
      "font-family": "Inter, sans-serif" }, "R$ mi"));
    // área negativa e curva
    var caminho = r.serie.map(function (v, i) { return (i ? "L" : "M") + x(i).toFixed(1) + " " + y(v).toFixed(1); }).join(" ");
    curva.appendChild(no("path", { d: caminho + " L" + x(r.serie.length - 1) + " " + z + " L" + x(0) + " " + z + " Z",
      fill: "#082538", opacity: ".07" }));
    curva.appendChild(no("path", { d: caminho, fill: "none", stroke: "#082538", "stroke-width": 2.5,
      "stroke-linejoin": "round", "stroke-linecap": "round" }));
    if (!r.sem) {
      var px = x(r.mes), py = y(-r.exposicao), direita = px > w * 0.6;
      curva.appendChild(no("circle", { cx: px, cy: py, r: 6, fill: "#B58A44", stroke: "#fff", "stroke-width": 2 }));
      curva.appendChild(no("text", { x: direita ? px - 10 : px + 10, y: Math.max(py - 14, t + 14),
        "text-anchor": direita ? "end" : "start", fill: "#7A5A28", "font-size": fsDestaque, "font-weight": 700,
        "font-family": "Inter, sans-serif", stroke: "#fff", "stroke-width": 4, "paint-order": "stroke",
        "stroke-linejoin": "round" }, "pico: " + moeda(r.exposicao) + " no mês " + r.mes));
      var xr = x(OBRA + REPASSE);
      curva.appendChild(no("text", { x: xr - 6, y: t + 4 + fs, "text-anchor": "end", fill: cinza, "font-size": fs,
        "font-family": "Inter, sans-serif" }, "entrega e repasse"));
    } else {
      curva.appendChild(no("text", { x: e + 6, y: t + 14, fill: "#7A5A28", "font-size": fsDestaque, "font-weight": 700,
        "font-family": "Inter, sans-serif" }, "o caixa não fica negativo nesta combinação"));
    }
    curva.setAttribute("aria-label", "Saldo de caixa acumulado ao longo de 30 meses. " +
      (r.sem ? "O saldo não fica negativo. " : "Pico negativo de " + moeda(r.exposicao) + " no mês " + r.mes + ". ") +
      "Resultado ao fim do ciclo: " + moeda(r.resultado) + ".");
  }

  var espera;
  function anunciar(r) {
    clearTimeout(espera);
    espera = setTimeout(function () {
      var alvo = el("sim-resumo");
      if (alvo) alvo.textContent = (r.sem ? "Sem exposição de caixa nesta combinação. "
        : "Exposição máxima de " + moeda(r.exposicao) + " no mês " + r.mes + ". ") +
        "Resultado ao fim do ciclo: " + moeda(r.resultado) + ".";
    }, 500);
  }

  function atualizar() {
    var p = {};
    campos.forEach(function (c) {
      p[c] = parseFloat(el(c).value);
      el(c).setAttribute("aria-valuetext", FALA[c](p[c]));
      el("o-" + c).textContent = MOSTRA[c](p[c]);
    });
    var r = calcular(p);
    el("k-exposicao").textContent = r.sem ? "R$ 0" : moeda(r.exposicao);
    el("k-mes").textContent = r.sem ? "sem pico" : "mês " + r.mes;
    el("k-resultado").textContent = moeda(r.resultado);
    desenhar(r);
    anunciar(r);
  }

  var CENARIOS = {
    proprio: { vgv: 20, terreno: 15, permuta: 0, planta: 0, credito: 0 },
    planta: { vgv: 20, terreno: 15, permuta: 0, planta: 40, credito: 0 },
    permuta: { vgv: 20, terreno: 15, permuta: 70, planta: 0, credito: 0 },
    combinada: { vgv: 20, terreno: 15, permuta: 70, planta: 35, credito: 55 }
  };
  var botoes = document.querySelectorAll("[data-cenario]");
  function escolher(nome) {
    botoes.forEach(function (b) { b.setAttribute("aria-pressed", String(b.dataset.cenario === nome)); });
    var c = CENARIOS[nome];
    campos.forEach(function (k) { el(k).value = c[k]; });
    var alvo = document.querySelector('[data-cenario="' + nome + '"]');
    var nota = el("nota-cenario");
    if (nota && alvo && alvo.dataset.nota) nota.textContent = alvo.dataset.nota;
    atualizar();
  }
  botoes.forEach(function (b) { b.addEventListener("click", function () { escolher(b.dataset.cenario); }); });
  campos.forEach(function (c) {
    el(c).addEventListener("input", function () {
      botoes.forEach(function (b) { b.setAttribute("aria-pressed", "false"); });
      var nota = el("nota-cenario");
      if (nota) nota.textContent = "Combinação própria: você ajustou os controles à mão. Volte a um dos quatro arranjos quando quiser.";
      atualizar();
    });
  });

  // a home e as páginas internas podem abrir o simulador num arranjo: ?arranjo=combinada
  var largura = curva.clientWidth;
  window.addEventListener("resize", function () {
    if (Math.abs(curva.clientWidth - largura) > 40) { largura = curva.clientWidth; atualizar(); }
  });

  var pedido = (location.search.match(/arranjo=(\w+)/) || [])[1];
  escolher(CENARIOS[pedido] ? pedido : "proprio");
  var caixa = el("sim");
  if (caixa) caixa.setAttribute("data-sim", "ativo");
})();
