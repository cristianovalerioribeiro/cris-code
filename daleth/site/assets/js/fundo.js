// DALETH · fundo vivo do hero (modelo B)
// Um terreno feito de pontos que respira devagar; no meio dele, um lote em dourado e as
// quatro hastes crescentes do símbolo D. A rolagem aproxima a câmera do lote e o mouse
// desloca o ponto de vista de leve. WebGL puro, sem biblioteca (o Miravo usa three.js, ~600 KB).
// Sem WebGL, o CSS mostra uma malha de pontos estática; com movimento reduzido, um quadro parado.
(function () {
  "use strict";
  var tela = document.querySelector(".fundo-vivo");
  if (!tela) return;
  var hero = tela.parentElement;
  var reduzir = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var gl = tela.getContext("webgl", { antialias: false, alpha: false, premultipliedAlpha: false, powerPreference: "low-power" });
  if (!gl) return;

  var celular = Math.min(window.innerWidth, window.innerHeight) < 700;
  var DPR = Math.min(window.devicePixelRatio || 1, celular ? 1.5 : 1.75);

  // ---------------------------------------------------------------- geometria
  var LOTE = { x: -1.7, z: 3.4, w: 1.5, d: 1.5 };
  var passo = celular ? 0.17 : 0.115;
  var dados = [];
  for (var x = -7; x <= 7; x += passo) {
    for (var z = -1; z <= 15; z += passo) {
      var dentro = x > LOTE.x - LOTE.w / 2 && x < LOTE.x + LOTE.w / 2 && z > LOTE.z - LOTE.d / 2 && z < LOTE.z + LOTE.d / 2;
      dados.push(x + (Math.random() - 0.5) * passo * 0.35, 0, z + (Math.random() - 0.5) * passo * 0.35, dentro ? 1 : 0);
    }
  }
  // contorno do lote, mais denso, como o tracejado da prancha
  for (var i = 0; i < 160; i++) {
    var t = i / 160, lado = Math.floor(t * 4), f = (t * 4) % 1;
    var x0 = LOTE.x - LOTE.w / 2, z0 = LOTE.z - LOTE.d / 2;
    if ((i % 4) === 3) continue;   // falhas regulares: tracejado
    var px = lado === 0 ? x0 + f * LOTE.w : lado === 1 ? x0 + LOTE.w : lado === 2 ? x0 + LOTE.w - f * LOTE.w : x0;
    var pz = lado === 0 ? z0 : lado === 1 ? z0 + f * LOTE.d : lado === 2 ? z0 + LOTE.d : z0 + LOTE.d - f * LOTE.d;
    dados.push(px, 0, pz, 1.5);
  }
  // as quatro hastes do D: colunas de pontos, alturas crescentes
  [0.55, 0.8, 1.05, 1.3].forEach(function (h, k) {
    var bx = LOTE.x - 0.5 + k * 0.33, bz = LOTE.z + 0.1;
    for (var y = 0; y <= h; y += 0.03) {
      for (var a = 0; a < 4; a++) {
        for (var b = 0; b < 3; b++) dados.push(bx + a * 0.05, y, bz + b * 0.07, 2);
      }
    }
  });
  var N = dados.length / 4;

  // ---------------------------------------------------------------- shaders
  var vs = [
    "attribute vec4 a;",
    "uniform mat4 vp; uniform vec3 olho; uniform float t, tam, sobe;",
    "varying float vAlfa; varying float vTipo;",
    "float relevo(vec2 p){",
    "  return .30*sin(p.x*.55+t*.22)*cos(p.y*.42-t*.17)+.14*sin(p.x*1.3+p.y*.9+t*.31)+.05*sin(p.x*3.1-p.y*2.2+t*.5);",
    "}",
    "void main(){",
    "  vec3 p = a.xyz; float tipo = a.w;",
    "  vec2 c = vec2(" + LOTE.x.toFixed(2) + "," + LOTE.z.toFixed(2) + ");",
    "  float plano = smoothstep(2.4, .9, distance(p.xz, c));",   // o terreno se assenta perto do lote
    "  float h = relevo(p.xz) * (1. - .92*plano);",
    "  if (tipo > 1.9) { p.y = p.y * sobe + relevo(c)*(.08); } else { p.y = h; }",
    "  gl_Position = vp * vec4(p, 1.);",
    "  float dist = distance(p, olho);",
    "  float base = tipo > 1.9 ? 1.25 : tipo > .9 ? 1.35 : 1.;",
    "  gl_PointSize = max(1., tam * base / dist);",
    "  vAlfa = smoothstep(16., 3., dist) * smoothstep(.2, 1.2, dist);",
    "  vTipo = tipo;",
    "}"
  ].join("\n");
  var fs = [
    "precision mediump float;",
    "varying float vAlfa; varying float vTipo;",
    "void main(){",
    "  vec2 q = gl_PointCoord - .5; float r = dot(q,q);",
    "  if (r > .25) discard;",
    "  float suave = smoothstep(.25, .05, r);",
    "  vec3 gelo = vec3(.725,.784,.831), ouro = vec3(.831,.702,.486), branco = vec3(1.);",
    "  vec3 cor = vTipo > 1.9 ? branco : vTipo > .9 ? ouro : gelo;",
    "  float a = vTipo > .9 ? 1. : .62;",
    "  gl_FragColor = vec4(cor, a * suave * vAlfa);",
    "}"
  ].join("\n");

  function compilar(tipo, src) {
    var s = gl.createShader(tipo);
    gl.shaderSource(s, src);
    gl.compileShader(s);
    if (!gl.getShaderParameter(s, gl.COMPILE_STATUS)) throw new Error(gl.getShaderInfoLog(s));
    return s;
  }
  var prog;
  try {
    prog = gl.createProgram();
    gl.attachShader(prog, compilar(gl.VERTEX_SHADER, vs));
    gl.attachShader(prog, compilar(gl.FRAGMENT_SHADER, fs));
    gl.linkProgram(prog);
    if (!gl.getProgramParameter(prog, gl.LINK_STATUS)) throw new Error(gl.getProgramInfoLog(prog));
  } catch (e) { return; }   // fica a malha estática do CSS
  gl.useProgram(prog);
  var buf = gl.createBuffer();
  gl.bindBuffer(gl.ARRAY_BUFFER, buf);
  gl.bufferData(gl.ARRAY_BUFFER, new Float32Array(dados), gl.STATIC_DRAW);
  var locA = gl.getAttribLocation(prog, "a");
  gl.enableVertexAttribArray(locA);
  gl.vertexAttribPointer(locA, 4, gl.FLOAT, false, 0, 0);
  var U = {};
  ["vp", "olho", "t", "tam", "sobe"].forEach(function (n) { U[n] = gl.getUniformLocation(prog, n); });
  gl.enable(gl.BLEND);
  gl.blendFunc(gl.SRC_ALPHA, gl.ONE_MINUS_SRC_ALPHA);
  gl.clearColor(8 / 255, 37 / 255, 56 / 255, 1);

  // ---------------------------------------------------------------- câmera
  function perspectiva(fov, asp, perto, longe) {
    var f = 1 / Math.tan(fov / 2), nf = 1 / (perto - longe);
    return [f / asp, 0, 0, 0, 0, f, 0, 0, 0, 0, (longe + perto) * nf, -1, 0, 0, 2 * longe * perto * nf, 0];
  }
  function sub(a, b) { return [a[0] - b[0], a[1] - b[1], a[2] - b[2]]; }
  function cruz(a, b) { return [a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0]]; }
  function norm(a) { var l = Math.hypot(a[0], a[1], a[2]) || 1; return [a[0] / l, a[1] / l, a[2] / l]; }
  function ponto(a, b) { return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]; }
  function olharPara(o, alvo) {
    var z = norm(sub(o, alvo)), x = norm(cruz([0, 1, 0], z)), y = cruz(z, x);
    return [x[0], y[0], z[0], 0, x[1], y[1], z[1], 0, x[2], y[2], z[2], 0, -ponto(x, o), -ponto(y, o), -ponto(z, o), 1];
  }
  function mult(a, b) {   // a * b, colunas
    var r = new Array(16);
    for (var c = 0; c < 4; c++) for (var l = 0; l < 4; l++) {
      r[c * 4 + l] = a[l] * b[c * 4] + a[4 + l] * b[c * 4 + 1] + a[8 + l] * b[c * 4 + 2] + a[12 + l] * b[c * 4 + 3];
    }
    return r;
  }
  function mistura(a, b, k) { return [a[0] + (b[0] - a[0]) * k, a[1] + (b[1] - a[1]) * k, a[2] + (b[2] - a[2]) * k]; }

  // ---------------------------------------------------------------- estado
  var largura = 1, altura = 1, rolagem = 0, mx = 0, my = 0, smx = 0, smy = 0, rodando = false, visivel = true;
  var inicio = performance.now(), sobe = reduzir ? 1 : 0;

  function medir() {
    var w = tela.clientWidth, h = tela.clientHeight;
    if (!w || !h) return;
    largura = Math.round(w * DPR); altura = Math.round(h * DPR);
    if (tela.width !== largura || tela.height !== altura) { tela.width = largura; tela.height = altura; }
    gl.viewport(0, 0, largura, altura);
  }

  function quadro(agora) {
    var t = reduzir ? 8 : (agora - inicio) / 1000;
    if (!reduzir) sobe = Math.min(1, sobe + 0.012);
    smx += (mx - smx) * 0.05; smy += (my - smy) * 0.05;
    var asp = largura / altura, retrato = asp < 1;
    var k = rolagem * rolagem * (3 - 2 * rolagem);   // suaviza a aproximação
    var lote = [LOTE.x, 0.3, LOTE.z];
    // de longe: o lote à direita do texto (no celular, acima dele); de perto: dentro do lote
    var estreito = asp < 1.7;   // celular e tablet em pé: o lote no centro da faixa
    var olho0 = estreito ? [LOTE.x + 0.3, 2.0, -1.4] : [0.6, 2.3, -2.6];
    var alvo0 = estreito ? [LOTE.x, 0.0, 5.0] : [0.5, -0.1, 5.2];
    var olho1 = [LOTE.x + 0.25, 1.05, LOTE.z - 1.9];
    var olho = mistura(olho0, olho1, k), alvo = mistura(alvo0, lote, k);
    olho[0] -= smx * 0.45; olho[1] += smy * 0.2;
    var vp = mult(perspectiva(retrato ? 1.0 : 0.8, asp, 0.05, 40), olharPara(olho, alvo));
    gl.clear(gl.COLOR_BUFFER_BIT);
    gl.uniformMatrix4fv(U.vp, false, new Float32Array(vp));
    gl.uniform3fv(U.olho, olho);
    gl.uniform1f(U.t, t);
    gl.uniform1f(U.tam, (celular ? 11 : 13) * DPR);
    gl.uniform1f(U.sobe, 1 - Math.pow(1 - sobe, 3));
    gl.drawArrays(gl.POINTS, 0, N);
  }

  function laco(agora) {
    if (!rodando) return;
    quadro(agora);
    requestAnimationFrame(laco);
  }
  function ligar() {
    if (reduzir || rodando || !visivel || document.hidden) return;
    rodando = true;
    requestAnimationFrame(laco);
  }
  function desligar() { rodando = false; }

  medir();
  quadro(performance.now());
  hero.classList.add("vivo");

  if (window.ResizeObserver) new ResizeObserver(function () { medir(); if (!rodando) quadro(performance.now()); }).observe(tela);
  else window.addEventListener("resize", function () { medir(); });

  if (!reduzir) {
    window.addEventListener("scroll", function () {
      rolagem = Math.min(Math.max(window.scrollY / (hero.offsetHeight || 1), 0), 1);
    }, { passive: true });
    if (window.matchMedia("(pointer: fine)").matches) {
      hero.addEventListener("pointermove", function (e) {
        var r = hero.getBoundingClientRect();
        mx = ((e.clientX - r.left) / r.width - 0.5) * 2;
        my = ((e.clientY - r.top) / r.height - 0.5) * -2;
      });
      hero.addEventListener("pointerleave", function () { mx = 0; my = 0; });
    }
    if ("IntersectionObserver" in window) {
      new IntersectionObserver(function (es) {
        visivel = es[0].isIntersecting;
        if (visivel) ligar(); else desligar();
      }).observe(hero);
    }
    document.addEventListener("visibilitychange", function () { if (document.hidden) desligar(); else ligar(); });
    ligar();
  }

  tela.addEventListener("webglcontextlost", function (e) { e.preventDefault(); desligar(); hero.classList.remove("vivo"); });
})();
