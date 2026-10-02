// DALETH · radar de estruturação
// Seis respostas (0 a 3) viram um hexágono. A frente com menor nota é a de maior alavanca:
// é por ela que a conversa começa. Nada sai do navegador.
(function () {
  "use strict";
  var form = document.getElementById("radar");
  var svg = document.getElementById("radar-svg");
  if (!form || !svg) return;

  var EIXOS = [
    { id: "empresa", rot: "Empresa" },
    { id: "terreno", rot: "Terreno" },
    { id: "caixa", rot: "Caixa" },
    { id: "capital", rot: "Capital" },
    { id: "sociedade", rot: "Sociedade" },
    { id: "execucao", rot: "Execução" }
  ];
  // empate: começa pelo que mais pesa no caixa
  var PRIORIDADE = ["execucao", "caixa", "capital", "terreno", "sociedade", "empresa"];
  var FRENTES = {
    empresa: { nome: "Empresas: gestão e decisão", momento: "empresa",
      texto: "A maior alavanca está em como a empresa decide: números no tempo certo, papéis claros e rotina. É a base para crescer de projeto em projeto.",
      links: [["/empresas/", "Gestão, financeiro e societário"], ["/empresas/preparacao-para-credito/", "Preparação para crédito"]] },
    terreno: { nome: "Empreendimentos: terreno e produto", momento: "terreno",
      texto: "A maior alavanca está antes do projeto: o que o terreno comporta e qual produto faz o negócio fechar melhor.",
      links: [["/empreendimentos/permuta-de-terreno/", "Vender, permutar ou incorporar"], ["/empreendimentos/estudo-de-viabilidade/", "Estudo de viabilidade"]] },
    caixa: { nome: "Empreendimentos: viabilidade e caixa", momento: "empreendimento",
      texto: "A maior alavanca está no caixa: saber quanto capital a obra pede, em que mês, e comparar estruturas que diminuem esse pico.",
      links: [["/empreendimentos/simulador/", "Simulador de exposição de caixa"], ["/empreendimentos/estudo-de-viabilidade/", "Estudo de viabilidade"]] },
    capital: { nome: "Capital: crédito e investidor", momento: "capital",
      texto: "A maior alavanca está nas fontes de recurso: preparar a operação para chegar pronta ao banco ou ao investidor.",
      links: [["/capital/", "Crédito e capital"], ["/capital/financiamento-a-producao/", "Financiamento à produção"]] },
    sociedade: { nome: "Estrutura societária da operação", momento: "empreendimento",
      texto: "A maior alavanca está na forma: como sócios, empresas e investidores se organizam em cada operação, com risco e tributo à vista.",
      links: [["/inteligencia/spe-holding-ou-scp/", "SPE, holding ou SCP?"], ["/capital/#recurso-definido", "Quando o recurso já está definido"]] },
    execucao: { nome: "Conduzir a implantação", momento: "empreendimento",
      texto: "A maior alavanca está em transformar o plano em rotina: cronograma, orçamento e acompanhamento com quem executa.",
      links: [["/metodo/", "O método"], ["/empreendimentos/", "Do terreno à entrega"]] },
    parada: { nome: "Obras paradas", momento: "obra-parada",
      texto: "Primeiro, um caminho para retomar: entender por que parou, quanto falta e quais arranjos ainda estão na mesa.",
      links: [["/empreendimentos/obra-parada/", "Obras paradas"], ["/empreendimentos/simulador/", "Simulador de exposição de caixa"]] },
    pronto: { nome: "Pronto para um passo maior", momento: "empreendimento",
      texto: "A base está estruturada nas seis frentes. A conversa pode começar pela próxima operação, maior do que as anteriores.",
      links: [["/empreendimentos/estudo-de-viabilidade/", "Estudo de viabilidade"], ["/capital/", "Crédito e capital"]] }
  };

  var NS = "http://www.w3.org/2000/svg";
  var CX = 170, CY = 150, R = 96;
  function no(tag, a, txt) {
    var n = document.createElementNS(NS, tag);
    for (var k in a) n.setAttribute(k, a[k]);
    if (txt) n.textContent = txt;
    return n;
  }
  function pt(i, v) {
    var ang = -Math.PI / 2 + i * Math.PI / 3, r = R * v;
    return [CX + Math.cos(ang) * r, CY + Math.sin(ang) * r];
  }
  function poli(vals) { return vals.map(function (v, i) { return pt(i, v).map(function (n) { return n.toFixed(1); }).join(","); }).join(" "); }

  function desenhar(notas) {
    while (svg.firstChild) svg.removeChild(svg.firstChild);
    [1, 2, 3].forEach(function (n) {
      svg.appendChild(no("polygon", { points: poli([n, n, n, n, n, n].map(function (x) { return x / 3; })),
        fill: "none", stroke: "#24465F", "stroke-width": 1 }));
    });
    EIXOS.forEach(function (e, i) {
      var p = pt(i, 1), l = pt(i, 1.22);
      svg.appendChild(no("line", { x1: CX, y1: CY, x2: p[0], y2: p[1], stroke: "#24465F" }));
      var anc = Math.abs(l[0] - CX) < 4 ? "middle" : l[0] > CX ? "start" : "end";
      svg.appendChild(no("text", { x: l[0], y: l[1] + 4, "text-anchor": anc, fill: "#B9C8D4",
        "font-size": 12, "font-family": "Inter, sans-serif" }, e.rot));
    });
    var vals = EIXOS.map(function (e) { return notas[e.id] == null ? 0 : (notas[e.id] + 0.35) / 3.35; });
    var algum = EIXOS.some(function (e) { return notas[e.id] != null; });
    if (algum) {
      svg.appendChild(no("polygon", { points: poli(vals), fill: "rgba(212,179,124,.22)", stroke: "#D4B37C",
        "stroke-width": 2, "stroke-linejoin": "round" }));
      EIXOS.forEach(function (e, i) {
        if (notas[e.id] == null) return;
        var p = pt(i, vals[i]);
        svg.appendChild(no("circle", { cx: p[0], cy: p[1], r: 4, fill: "#B58A44", stroke: "#fff", "stroke-width": 1.5 }));
      });
    }
  }

  function ler() {
    var n = {};
    EIXOS.forEach(function (e) {
      var m = form.querySelector('input[name="' + e.id + '"]:checked');
      n[e.id] = m ? parseInt(m.value, 10) : null;
    });
    return n;
  }

  function escolherFrente(n) {
    if (n.execucao === 0) return "parada";
    var menor = Math.min.apply(null, EIXOS.map(function (e) { return n[e.id]; }));
    if (menor === 3) return "pronto";
    for (var i = 0; i < PRIORIDADE.length; i++) if (n[PRIORIDADE[i]] === menor) return PRIORIDADE[i];
    return "caixa";
  }

  function atualizar() {
    var n = ler();
    desenhar(n);
    var feitas = EIXOS.filter(function (e) { return n[e.id] != null; }).length;
    var status = document.getElementById("radar-status");
    var res = document.getElementById("radar-resultado");
    var resumo = EIXOS.map(function (e) { return e.rot + " " + (n[e.id] == null ? "sem resposta" : n[e.id] + " de 3"); }).join("; ");
    svg.setAttribute("aria-label", "Radar de estruturação. " + resumo + ".");
    if (feitas < EIXOS.length) {
      status.textContent = feitas ? "Faltam " + (EIXOS.length - feitas) + (EIXOS.length - feitas === 1 ? " resposta." : " respostas.")
        : "Responda as seis perguntas. O desenho se completa a cada resposta.";
      res.hidden = true;
      return;
    }
    var chave = escolherFrente(n), f = FRENTES[chave];
    status.textContent = "Radar completo.";
    document.getElementById("radar-vertente").textContent = f.nome;
    document.getElementById("radar-texto").textContent = f.texto;
    var ul = document.getElementById("radar-links");
    ul.innerHTML = "";
    f.links.forEach(function (l) {
      var li = document.createElement("li"), a = document.createElement("a");
      a.href = rel(l[0]); a.textContent = l[1];
      li.appendChild(a); ul.appendChild(li);
    });
    var msg = "Radar de estruturação: " + resumo + ". Por onde começar: " + f.nome + ".";
    var levar = document.getElementById("radar-levar");
    var base = levar.getAttribute("href").split("?")[0];
    levar.setAttribute("href", base + "?momento=" + f.momento + "&origem=radar&msg=" + encodeURIComponent(msg));
    res.hidden = false;
  }

  // na prévia local os links são relativos (../../x/index.html); o botão já vem no formato certo
  var exemplo = document.getElementById("radar-levar").getAttribute("href");
  var prefixo = (exemplo.match(/^((?:\.\.\/)*)/) || ["", ""])[1];
  var local = /index\.html/.test(exemplo);
  function rel(alvo) {
    if (!local) return alvo;
    var partes = alvo.split("#");
    return prefixo + partes[0].replace(/^\//, "") + "index.html" + (partes[1] ? "#" + partes[1] : "");
  }

  form.addEventListener("change", atualizar);
  form.addEventListener("submit", function (e) { e.preventDefault(); });
  atualizar();
})();
