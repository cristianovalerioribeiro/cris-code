// DALETH · comportamento comum a todas as páginas
(function () {
  "use strict";
  var doc = document.documentElement;
  doc.classList.add("js");
  var reduzir = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  // ---- menu mobile: o resto da página fica inerte enquanto ele está aberto
  var botao = document.querySelector(".menu-botao");
  var menu = document.getElementById("menu");
  if (botao && menu) {
    var fora = function () {
      return Array.prototype.slice.call(document.querySelectorAll("main, footer, .faixa-slogan, .migalhas, .marca"));
    };
    var fechar = function (devolverFoco) {
      botao.setAttribute("aria-expanded", "false");
      menu.classList.remove("aberto");
      document.body.classList.remove("menu-aberto");
      fora().forEach(function (el) { el.inert = false; });
      if (devolverFoco) botao.focus();
    };
    botao.addEventListener("click", function () {
      var abrir = botao.getAttribute("aria-expanded") !== "true";
      if (!abrir) return fechar(false);
      botao.setAttribute("aria-expanded", "true");
      menu.classList.add("aberto");
      document.body.classList.add("menu-aberto");
      fora().forEach(function (el) { el.inert = true; });
      var primeiro = menu.querySelector("a");
      if (primeiro) primeiro.focus();
    });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && menu.classList.contains("aberto")) fechar(true);
    });
    window.matchMedia("(min-width: 1080px)").addEventListener("change", function (m) {
      if (m.matches) fechar(false);
    });
  }

  // ---- cenário do hero: a página desce, as camadas se aproximam (CSS faz o resto)
  var cenario = document.querySelector(".cenario");
  if (cenario && !reduzir) {
    var hero = cenario.parentElement, pendente = false;
    var medir = function () {
      pendente = false;
      var altura = hero.offsetHeight || 1;
      var p = Math.min(Math.max(window.scrollY / altura, 0), 1);
      cenario.style.setProperty("--p", p.toFixed(3));
    };
    window.addEventListener("scroll", function () {
      if (!pendente) { pendente = true; requestAnimationFrame(medir); }
    }, { passive: true });
    medir();
  }

  // ---- entrada suave dos blocos marcados com .surge
  var surgem = document.querySelectorAll(".surge");
  if (surgem.length && "IntersectionObserver" in window && !reduzir) {
    var obs = new IntersectionObserver(function (entradas) {
      entradas.forEach(function (e) {
        if (e.isIntersecting) { e.target.classList.add("visivel"); obs.unobserve(e.target); }
      });
    }, { rootMargin: "0px 0px -8% 0px" });
    surgem.forEach(function (el) { obs.observe(el); });
  } else {
    surgem.forEach(function (el) { el.classList.add("visivel"); });
  }

  // ---- filtro das nove modelagens
  var filtro = document.querySelector("[data-filtro]");
  if (filtro) {
    var fichas = document.querySelectorAll(".modelagem");
    var contagem = document.getElementById("contagem");
    filtro.addEventListener("click", function (e) {
      var b = e.target.closest("button");
      if (!b) return;
      filtro.querySelectorAll("button").forEach(function (x) { x.setAttribute("aria-pressed", String(x === b)); });
      var f = b.dataset.valor, n = 0;
      fichas.forEach(function (ficha) {
        var mostra = f === "todas" || ficha.dataset.dim.split(" ").indexOf(f) >= 0;
        ficha.hidden = !mostra;
        if (mostra) n++;
      });
      if (contagem) contagem.textContent = n + (n === 1 ? " modelagem" : " modelagens");
    });
  }


  // ---- barra de contato no celular: aparece depois da abertura, some perto do fecho e no contato
  var barra = document.querySelector(".barra-cta");
  var noContato = /\/contato\//.test(location.pathname);
  if (barra && !noContato) {
    var abertura = document.querySelector(".hero, .abertura");
    var fecho = document.querySelector(".fecho");
    var limite = abertura ? abertura.offsetTop + abertura.offsetHeight : 400;
    var mostrar = function () {
      var y = window.scrollY, fim = fecho ? fecho.getBoundingClientRect().top < window.innerHeight : false;
      var visivel = y > limite && !fim && !document.body.classList.contains("menu-aberto");
      barra.hidden = !visivel;
      document.body.classList.toggle("com-barra", visivel);
    };
    window.addEventListener("scroll", mostrar, { passive: true });
    mostrar();
  }

  // ---- contato: momento, origem e mensagem vindos do link (?momento=...&origem=...&msg=...)
  var form2 = document.querySelector("form.form");
  if (form2) {
    var q = {};
    location.search.replace(/^\?/, "").split("&").forEach(function (par) {
      if (!par) return;
      var kv = par.split("=");
      try { q[decodeURIComponent(kv[0])] = decodeURIComponent((kv[1] || "").replace(/\+/g, " ")); } catch (e) {}
    });
    var sel = document.getElementById("momento");
    if (q.momento && sel && sel.querySelector('option[value="' + q.momento + '"]')) sel.value = q.momento;
    var orig = document.getElementById("origem");
    if (orig) orig.value = q.origem || (document.referrer ? "referencia-externa" : "direto");
    var msg = document.getElementById("mensagem");
    var guardada = null;
    try { guardada = sessionStorage.getItem("daleth-cenario"); } catch (e) {}
    if (msg && !msg.value && (q.msg || (q.origem === "simulador" && guardada))) msg.value = q.msg || guardada;
  }

  // ---- formulário de contato enquanto o canal não está definido
  var form = document.querySelector("form[data-inativo]");
  if (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var aviso = document.getElementById("aviso-form");
      if (aviso) {
        aviso.textContent = "Prévia: a mensagem não foi enviada. O envio entra quando o canal de contato for definido.";
        aviso.classList.add("ativo");
        aviso.setAttribute("role", "status");
        aviso.focus && aviso.setAttribute("tabindex", "-1");
        aviso.focus();
      }
    });
  }
})();
