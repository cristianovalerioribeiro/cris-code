// DALETH · cenas 3D (WebGL puro, sem biblioteca)
//
// Uma só cena, contada de três jeitos:
//   heroi    o terreno de pontos que respira, o lote em dourado, as quatro hastes do símbolo D
//            erguidas em linha e, em volta, uma rede de decisões conectadas com pulsos de dados
//   jornada  a mesma cena guiada pela rolagem (.aproxima): primeiro só o lote, depois as
//            alternativas tracejadas, por fim a escolhida de pé e a rede ligando tudo
//   rede     só a rede, discreta, atrás do fecho marinho das páginas
// data-tema="claro" desenha em marinho e dourado sobre fundo claro (modelo C).
//
// Cuidados: pausa fora da tela e em aba oculta; com "reduzir movimento", um quadro parado;
// menos pontos e resolução limitada no celular; sem WebGL, fica o que estiver no HTML (SVG
// ou pôster), porque a classe .cena-viva só entra quando a cena desenhou de fato.
(function () {
  "use strict";
  var telas = Array.prototype.slice.call(document.querySelectorAll("canvas[data-cena]"));
  if (!telas.length) return;
  var reduzir = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var ponteiroFino = window.matchMedia("(pointer: fine)").matches;
  var leve = Math.min(screen.width, screen.height) < 700 || (navigator.hardwareConcurrency || 8) <= 4;

  // ------------------------------------------------------------ matemática
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
  function mult(a, b) {
    var r = new Array(16);
    for (var c = 0; c < 4; c++) for (var l = 0; l < 4; l++) {
      r[c * 4 + l] = a[l] * b[c * 4] + a[4 + l] * b[c * 4 + 1] + a[8 + l] * b[c * 4 + 2] + a[12 + l] * b[c * 4 + 3];
    }
    return r;
  }
  function aplicar(m, p) {
    return [m[0] * p[0] + m[4] * p[1] + m[8] * p[2] + m[12], m[1] * p[0] + m[5] * p[1] + m[9] * p[2] + m[13],
            m[2] * p[0] + m[6] * p[1] + m[10] * p[2] + m[14], m[3] * p[0] + m[7] * p[1] + m[11] * p[2] + m[15]];
  }
  function suave(a, b, x) { var t = Math.min(Math.max((x - a) / (b - a), 0), 1); return t * t * (3 - 2 * t); }
  function semente(n) { return function () { n = (n * 16807) % 2147483647; return (n - 1) / 2147483646; }; }

  // ------------------------------------------------------------ shaders
  var COMUM = [
    "uniform mat4 vp; uniform vec2 desloc; uniform vec3 olho;",
    "uniform float tempo, cresce, fantasma, rede, anel, claro, escala;",
    "const vec3 GELO = vec3(.725,.784,.831); const vec3 BRANCO = vec3(1.);",
    "const vec3 OURO_C = vec3(.831,.702,.486); const vec3 OURO_F = vec3(.612,.459,.208);",
    "const vec3 MARINHO = vec3(.031,.145,.22); const vec3 GRAFITE = vec3(.278,.345,.416); const vec3 FIO = vec3(.49,.553,.608);",
    "float relevo(vec2 q){ return .26*sin(q.x*.55+tempo*.22)*cos(q.y*.47-tempo*.17) + .12*sin(q.x*1.25+q.y*.85+tempo*.31) + .05*sin(q.x*2.9-q.y*2.1+tempo*.5); }",
    "float nevoa(float d){ return smoothstep(26., 7., d); }",
    "vec4 projetar(vec3 p){ vec4 c = vp*vec4(p,1.); c.xy += desloc*c.w; return c; }"
  ].join("\n");

  var VS_PONTOS = COMUM + [
    "attribute vec3 p; attribute vec3 e;",
    "varying vec4 vCor; varying float vClaro;",
    "void main(){",
    "  vec3 q = p; float t = e.x, s = e.y, a = 1.; vec3 cor = GELO;",
    "  if (t < .5) {",                                  // terreno
    "    float d = length(q.xz);",
    "    q.y = relevo(q.xz) * (1. - smoothstep(3.4, 1.7, d));",
    "    a = smoothstep(10., 5.5, d) * (.7 + .3*sin(tempo*1.1 + s*60.));",
    "    cor = claro > .5 ? FIO : mix(GELO, BRANCO, smoothstep(.12, .4, q.y));\n    if (claro > .5) a *= .75;",
    "  } else if (t < 1.5) {",                          // lote
    "    a = .85 * (.8 + .2*sin(tempo*2. + s*30.)); cor = claro > .5 ? OURO_F : OURO_C;",
    "  } else if (t < 2.5) {",                          // faces das torres: janelas que acendem
    "    q.y *= cresce;",
    "    float luz = step(.88, fract(s*13. + tempo*.06));",
    "    a = cresce * (.22 + .7*luz);",
    "    cor = claro > .5 ? MARINHO : mix(GELO, BRANCO, luz);",
    "  } else if (t < 3.5) {",                          // nó com rótulo / topo das torres
    "    a = rede; cor = claro > .5 ? OURO_F : OURO_C;",
    "  } else if (t < 4.5) {",                          // nó da rede
    "    a = rede * .85; cor = claro > .5 ? MARINHO : BRANCO;",
    "  } else {",                                       // pulso de dados
    "    a = rede; cor = claro > .5 ? OURO_F : mix(OURO_C, BRANCO, .35);",
    "  }",
    "  gl_Position = projetar(q);",
    "  float d = distance(q, olho);",
    "  gl_PointSize = clamp(e.z * escala / d * (claro > .5 ? .48 : 1.), 1., 56.);",
    "  vCor = vec4(cor, a * nevoa(d)); vClaro = claro;",
    "}"
  ].join("\n");
  var FS_PONTOS = [
    "precision mediump float;",
    "varying vec4 vCor; varying float vClaro;",
    "void main(){",
    "  vec2 q = gl_PointCoord - .5; float r = length(q) * 2.;",
    "  if (r > 1.) discard;",
    "  float a = vClaro > .5 ? smoothstep(1., .55, r) : (pow(1. - r, 2.) * .6 + smoothstep(.38, 0., r) * .6);",
    "  gl_FragColor = vec4(vCor.rgb, vCor.a * a);",
    "}"
  ].join("\n");

  var VS_LINHAS = COMUM + [
    "attribute vec3 p; attribute vec3 e;",
    "varying vec4 vCor; varying float vT; varying float vTr;",
    "void main(){",
    "  vec3 q = p; float t = e.x, a = e.z, tr = 0.; vec3 cor = GELO;",
    "  if (t < 10.5) { cor = claro > .5 ? OURO_F : OURO_C; tr = 1.; }",                       // contorno do lote
    "  else if (t < 11.5) { q.y *= cresce; a *= cresce * .85; cor = claro > .5 ? MARINHO : BRANCO; }", // torres
    "  else if (t < 12.5) { a *= fantasma * .9; cor = claro > .5 ? OURO_F : OURO_C; tr = 1.; }",     // alternativas
    "  else if (t < 13.5) { q.xz *= .6 + anel * 9.; a *= (1. - anel) * .5; cor = claro > .5 ? OURO_F : OURO_C; }", // anel
    "  else if (t < 14.5) { a *= rede; cor = claro > .5 ? GRAFITE : mix(GELO, OURO_C, e.y); }",       // rede
    "  else { a *= .18; cor = claro > .5 ? FIO : GELO; }",                                       // grade do chão
    "  gl_Position = projetar(q);",
    "  vCor = vec4(cor, a * nevoa(distance(q, olho))); vT = e.y; vTr = tr;",
    "}"
  ].join("\n");
  var FS_LINHAS = [
    "precision mediump float;",
    "varying vec4 vCor; varying float vT; varying float vTr;",
    "void main(){",
    "  if (vTr > .5 && fract(vT * 3.2) > .56) discard;",
    "  gl_FragColor = vCor;",
    "}"
  ].join("\n");

  // ------------------------------------------------------------ geometria
  var LOTE = 1.35;
  var TORRES = [{ x: -0.93, h: 1.35 }, { x: -0.33, h: 1.85 }, { x: 0.27, h: 2.4 }, { x: 0.87, h: 3.0 }];
  var TW = 0.21, TZ0 = -0.42, TZ1 = 0.58;

  function caixa(L, x0, x1, z0, z1, h, tipo, andar) {
    var arestas = [
      [[x0, 0, z0], [x0, h, z0]], [[x1, 0, z0], [x1, h, z0]], [[x1, 0, z1], [x1, h, z1]], [[x0, 0, z1], [x0, h, z1]],
      [[x0, h, z0], [x1, h, z0]], [[x1, h, z0], [x1, h, z1]], [[x1, h, z1], [x0, h, z1]], [[x0, h, z1], [x0, h, z0]],
      [[x0, 0, z0], [x1, 0, z0]], [[x1, 0, z0], [x1, 0, z1]], [[x1, 0, z1], [x0, 0, z1]], [[x0, 0, z1], [x0, 0, z0]]
    ];
    arestas.forEach(function (ar) { segmento(L, ar[0], ar[1], tipo, 1); });
    if (andar) {
      for (var y = andar; y < h - 0.05; y += andar) {
        segmento(L, [x0, y, z1], [x1, y, z1], tipo, 0.28);
        segmento(L, [x1, y, z0], [x1, y, z1], tipo, 0.28);
        segmento(L, [x0, y, z0], [x0, y, z1], tipo, 0.16);
        segmento(L, [x0, y, z0], [x1, y, z0], tipo, 0.16);
      }
    }
  }
  function segmento(L, a, b, tipo, alfa, t0) {
    var comp = Math.hypot(b[0] - a[0], b[1] - a[1], b[2] - a[2]);
    t0 = t0 || 0;
    L.push(a[0], a[1], a[2], tipo, t0, alfa, b[0], b[1], b[2], tipo, t0 + comp, alfa);
  }

  function construir(cfg) {
    var rnd = semente(cfg.semente || 7), P = [], L = [];
    var passo = cfg.leve ? 0.2 : 0.135;
    if (cfg.terreno) {
      for (var x = -10; x <= 10; x += passo) {
        for (var z = -10; z <= 10; z += passo) {
          var jx = x + (rnd() - 0.5) * passo * 0.6, jz = z + (rnd() - 0.5) * passo * 0.6;
          if (jx * jx + jz * jz > 100) continue;
          if (Math.abs(jx) < LOTE + 0.08 && Math.abs(jz) < LOTE + 0.08) continue;
          P.push(jx, 0, jz, 0, rnd(), 2.8);
        }
      }
      for (var lx = -LOTE + 0.1; lx < LOTE; lx += 0.19) {
        for (var lz = -LOTE + 0.1; lz < LOTE; lz += 0.19) P.push(lx, 0.005, lz, 1, rnd(), 1.5);
      }
      // grade de prancha no chão, apagando para as bordas
      for (var k = -9; k <= 9; k += 1.5) {
        for (var s = -9; s < 9; s += 1) {
          var f1 = suave(9.5, 3, Math.hypot(k, s)), f2 = suave(9.5, 3, Math.hypot(k, s + 1));
          if (f1 + f2 < 0.02) continue;
          L.push(k, 0, s, 15, 0, f1, k, 0, s + 1, 15, 0, f2);
          L.push(s, 0, k, 15, 0, f1, s + 1, 0, k, 15, 0, f2);
        }
      }
      // contorno tracejado do lote e o anel que varre o terreno
      var c = [[-LOTE, 0, -LOTE], [LOTE, 0, -LOTE], [LOTE, 0, LOTE], [-LOTE, 0, LOTE]];
      for (var i = 0; i < 4; i++) segmento(L, c[i], c[(i + 1) % 4], 10, 1, i * 2 * LOTE);
      for (var g = 0; g < 96; g++) {
        var a0 = g / 96 * Math.PI * 2, a1 = (g + 1) / 96 * Math.PI * 2;
        L.push(Math.cos(a0), 0.01, Math.sin(a0), 13, 0, 1, Math.cos(a1), 0.01, Math.sin(a1), 13, 0, 1);
      }
    }
    if (cfg.torres) {
      TORRES.forEach(function (t) {
        caixa(L, t.x - TW, t.x + TW, TZ0, TZ1, t.h, 11, 0.2);
        var n = Math.round((cfg.leve ? 110 : 220) * t.h / 3);
        for (var j = 0; j < n; j++) {
          var face = rnd(), y = rnd() * t.h, u = rnd();
          if (face < 0.4) P.push(t.x - TW + u * 2 * TW, y, TZ1, 2, rnd(), 1.5);
          else if (face < 0.8) P.push(t.x + TW, y, TZ0 + u * (TZ1 - TZ0), 2, rnd(), 1.5);
          else P.push(t.x - TW + u * 2 * TW, t.h, TZ0 + rnd() * (TZ1 - TZ0), 2, rnd(), 1.3);
        }
      });
      // as alternativas que não foram escolhidas: uma torre só, alta; uma laje baixa e larga
      caixa(L, -1.1, -0.15, -1.0, 0.9, 3.7, 12, 0);
      caixa(L, -1.2, 1.2, -1.15, 1.15, 0.95, 12, 0);
    }
    return { pontos: new Float32Array(P), linhas: new Float32Array(L) };
  }

  // rede de decisões: nós em órbita lenta; os seis primeiros carregam rótulo
  function criarRede(cfg) {
    var rnd = semente(31), nos = [];
    var n = cfg.denso ? (cfg.leve ? 34 : 64) : (cfg.leve ? 22 : 40);
    for (var i = 0; i < n; i++) {
      if (i < 6) {
        nos.push({ r: 3.6 + (i % 2) * 0.5, th: i * Math.PI / 3 + 0.35, y: 2.0 + (i % 3) * 0.6, w: 0.03, fase: rnd() * 6, rot: true });
      } else {
        nos.push({ r: 2.0 + rnd() * 3.8, th: rnd() * Math.PI * 2, y: 0.5 + rnd() * 3.8,
          w: (rnd() < 0.5 ? -1 : 1) * (0.015 + rnd() * 0.045), fase: rnd() * 6, rot: false });
      }
    }
    return { nos: nos, pulsos: [], rnd: rnd };
  }

  // ------------------------------------------------------------ programa
  function compilar(gl, vs, fs) {
    function sh(tipo, src) {
      var s = gl.createShader(tipo);
      gl.shaderSource(s, src); gl.compileShader(s);
      if (!gl.getShaderParameter(s, gl.COMPILE_STATUS)) throw new Error(gl.getShaderInfoLog(s));
      return s;
    }
    var p = gl.createProgram();
    gl.attachShader(p, sh(gl.VERTEX_SHADER, vs));
    gl.attachShader(p, sh(gl.FRAGMENT_SHADER, fs));
    gl.linkProgram(p);
    if (!gl.getProgramParameter(p, gl.LINK_STATUS)) throw new Error(gl.getProgramInfoLog(p));
    var u = {};
    ["vp", "desloc", "olho", "tempo", "cresce", "fantasma", "rede", "anel", "claro", "escala"].forEach(function (k) {
      u[k] = gl.getUniformLocation(p, k);
    });
    return { p: p, u: u, aP: gl.getAttribLocation(p, "p"), aE: gl.getAttribLocation(p, "e") };
  }

  // ------------------------------------------------------------ uma cena por canvas
  function Cena(tela) {
    var tipo = tela.getAttribute("data-cena");
    var claro = tela.getAttribute("data-tema") === "claro";
    var host = tela.closest("section") || tela.parentElement;
    var gl = tela.getContext("webgl", { alpha: claro, premultipliedAlpha: false, antialias: !leve,
      powerPreference: "low-power", preserveDrawingBuffer: tela.hasAttribute("data-captura") });
    if (!gl) return null;
    var cfg = { leve: leve, terreno: tipo !== "rede", torres: tipo !== "rede", denso: tipo === "rede", semente: 7 };
    var geo = construir(cfg), rede = criarRede(cfg);
    var progPontos, progLinhas;
    try {
      progPontos = compilar(gl, VS_PONTOS, FS_PONTOS);
      progLinhas = compilar(gl, VS_LINHAS, FS_LINHAS);
    } catch (e) { return null; }

    function buffer(dados, dinamico) {
      var b = gl.createBuffer();
      gl.bindBuffer(gl.ARRAY_BUFFER, b);
      gl.bufferData(gl.ARRAY_BUFFER, dados, dinamico ? gl.DYNAMIC_DRAW : gl.STATIC_DRAW);
      return b;
    }
    var bPontos = buffer(geo.pontos), bLinhas = buffer(geo.linhas);
    var MAX_ARESTAS = 260, MAX_PULSOS = cfg.leve ? 10 : 18;
    var dLinhas = new Float32Array(MAX_ARESTAS * 12), dPontos = new Float32Array((rede.nos.length + 4 + MAX_PULSOS) * 6);
    var bdLinhas = buffer(dLinhas, true), bdPontos = buffer(dPontos, true);

    // rótulos HTML que acompanham os nós projetados
    var rotulos = [], caixaRot = tela.parentElement.querySelector(".cena-rotulos");
    var nomes = (tela.getAttribute("data-rotulos") || "").split("|").filter(Boolean);
    if (caixaRot && claro) caixaRot.classList.add("claro");
    if (caixaRot && nomes.length) {
      nomes.slice(0, 6).forEach(function (nome) {
        var s = document.createElement("span");
        s.textContent = nome;
        caixaRot.appendChild(s);
        rotulos.push(s);
      });
    }

    var DPR = Math.min(window.devicePixelRatio || 1, leve ? 1.5 : 1.75);
    var W = 1, H = 1, cssW = 1, cssH = 1;
    function medir() {
      cssW = tela.clientWidth; cssH = tela.clientHeight;
      if (!cssW || !cssH) return;
      W = Math.round(cssW * DPR); H = Math.round(cssH * DPR);
      if (tela.width !== W || tela.height !== H) { tela.width = W; tela.height = H; }
      gl.viewport(0, 0, W, H);
    }

    var inicio = performance.now(), ultimo = inicio;
    var mx = 0, my = 0, smx = 0, smy = 0;
    var estado = { rolagem: 0, z: 0 };

    function camera(t, asp) {
      // hero escuro: no desktop a cena vai para a direita do texto, seja qual for a proporção;
      // no celular (faixa acima do texto) fica centrada
      var largo = tipo === "heroi" && !claro ? cssW >= 900 : asp > 1.3;
      var k = estado.rolagem, z = estado.z;
      if (tipo === "heroi") {
        var ang = 0.32 + t * 0.03 + smx * 0.22, elev = 0.4 + smy * 0.05 - k * 0.08;
        // telas largas mas não tanto (notebook pequeno, tablet deitado): afasta e empurra para a direita
        var aperto = largo && !claro ? Math.max(0, Math.min(1.5, (1.78 - asp) / 0.45)) : 0;
        var dist = (largo ? 12 + aperto * 3.2 : claro ? 10.4 : 9.2) - k * 4.6;
        if (centrada) {
          return { ang: ang, elev: elev + 0.12, dist: dist + 5, alvo: [0, 0.9, 0], desloc: [0, -0.42], fov: 0.72 };
        }
        return { ang: ang, elev: elev, dist: dist, alvo: [0, 1.15 + k * 0.4, 0],
          desloc: largo ? [0.36 + aperto * 0.16, -0.03] : [0, claro ? -0.02 : -0.06], fov: 0.72 };
      }
      if (tipo === "jornada") {
        return { ang: 0.4 + (1 - z) * 1.7 + t * 0.012 + smx * 0.1, elev: 0.62 - z * 0.24, dist: 12.6 - z * 4.8,
          alvo: [0, 0.7 + z * 0.75, 0], desloc: largo ? [-0.34, 0] : [0, 0.3], fov: asp < 0.8 ? 0.95 : 0.72 };
      }
      return { ang: t * 0.05 + smx * 0.2, elev: 0.22, dist: 7.6, alvo: [0, 2.2, 0],
        desloc: largo ? [0.3, 0] : [0, 0.1], fov: 0.8 };
    }

    var centro = tela.hasAttribute("data-centro");
    // hero centrado (texto no meio): a cena fica atrás, mais afastada e mais baixa
    var centrada = tipo === "heroi" && document.body.classList.contains("hero-centrado");
    var giro = parseFloat(tela.getAttribute("data-angulo")) || 0;   // pranchas renderizadas: cada página com seu ângulo
    var cameraBase = camera;
    camera = function (t, asp) {
      var c = cameraBase(t, asp);
      if (centro || host.classList.contains("estatica")) c.desloc = [0, 0];
      if (giro) c.ang += giro;
      return c;
    };

    function parametros(t) {
      if (tipo === "jornada") {
        var z = estado.z;
        return { cresce: suave(0.6, 0.86, z), fantasma: suave(0.28, 0.42, z) * (1 - suave(0.64, 0.8, z)),
          rede: suave(0.74, 0.98, z), anel: (t / 7) % 1 };
      }
      if (tipo === "rede") return { cresce: 0, fantasma: 0, rede: 1, anel: 0 };
      return { cresce: reduzir ? 1 : suave(0.25, 2.6, t), fantasma: 0, rede: reduzir ? 1 : suave(1.4, 3.6, t), anel: (t / 7) % 1 };
    }

    function atualizarRede(t, dt, prm, vp) {
      var nos = rede.nos, pos = [], i, j;
      for (i = 0; i < nos.length; i++) {
        var n = nos[i], th = n.th + n.w * t;
        pos.push([Math.cos(th) * n.r, n.y + Math.sin(t * 0.6 + n.fase) * 0.18, Math.sin(th) * n.r]);
      }
      var ancoras = [];
      if (cfg.torres) TORRES.forEach(function (tr) { ancoras.push([tr.x, tr.h * prm.cresce + 0.02, (TZ0 + TZ1) / 2]); });
      var todos = pos.concat(ancoras), nA = 0, LIM = 3.3;
      var viz = [];
      for (i = 0; i < todos.length; i++) viz.push([]);
      for (i = 0; i < todos.length && nA < MAX_ARESTAS; i++) {
        for (j = i + 1; j < todos.length && nA < MAX_ARESTAS; j++) {
          var ehAncora = j >= pos.length;
          if (i >= pos.length && ehAncora) continue;
          var lim = ehAncora ? 3.8 : LIM;
          if (ehAncora && prm.cresce < 0.3) continue;
          var a = todos[i], b = todos[j], d = Math.hypot(a[0] - b[0], a[1] - b[1], a[2] - b[2]);
          if (d > lim) continue;
          var al = Math.pow(1 - d / lim, 1.1) * (ehAncora ? 0.9 : 0.8);
          var ouro = (i < 6 || ehAncora) ? 1 : 0;
          var o = nA * 12;
          dLinhas[o] = a[0]; dLinhas[o + 1] = a[1]; dLinhas[o + 2] = a[2]; dLinhas[o + 3] = 14; dLinhas[o + 4] = ouro; dLinhas[o + 5] = al;
          dLinhas[o + 6] = b[0]; dLinhas[o + 7] = b[1]; dLinhas[o + 8] = b[2]; dLinhas[o + 9] = 14; dLinhas[o + 10] = ouro; dLinhas[o + 11] = al;
          viz[i].push(j); viz[j].push(i);
          nA++;
        }
      }
      // pulsos: correm por uma aresta e escolhem a seguinte
      var ps = rede.pulsos, rnd = rede.rnd;
      while (ps.length < MAX_PULSOS) ps.push({ i: -1, j: -1, u: 1, v: 0.5 });
      ps.forEach(function (p) {
        p.u += dt * p.v;
        var valido = p.i >= 0 && viz[p.i] && viz[p.i].indexOf(p.j) >= 0;
        if (p.u >= 1 || !valido) {
          var de = p.u >= 1 && valido ? p.j : Math.floor(rnd() * todos.length);
          if (!viz[de] || !viz[de].length) { p.i = -1; return; }
          p.i = de; p.j = viz[de][Math.floor(rnd() * viz[de].length)]; p.u = 0; p.v = 0.35 + rnd() * 0.5;
        }
      });
      var k = 0;
      for (i = 0; i < todos.length; i++) {
        var q = todos[i], rot = i < 6 && nos[i] && nos[i].rot, anc = i >= pos.length;
        if (anc && prm.cresce < 0.3) continue;
        dPontos.set([q[0], q[1], q[2], rot || anc ? 3 : 4, 0, rot ? 13 : anc ? 10 : 8], k * 6); k++;
      }
      ps.forEach(function (p) {
        if (p.i < 0) return;
        var a = todos[p.i], b = todos[p.j], u = p.u;
        dPontos.set([a[0] + (b[0] - a[0]) * u, a[1] + (b[1] - a[1]) * u, a[2] + (b[2] - a[2]) * u, 5, 0, 10], k * 6); k++;
      });
      // rótulos (um rótulo que encostaria noutro já posto fica escondido neste quadro)
      var postos = [];
      for (i = 0; i < rotulos.length; i++) {
        var c = aplicar(vp, pos[i]);
        var el = rotulos[i];
        if (c[3] <= 0.1 || prm.rede < 0.05) { el.style.opacity = "0"; continue; }
        var cam = camAtual.desloc;
        var nx = c[0] / c[3] + cam[0], ny = c[1] / c[3] + cam[1];
        var sx = (nx * 0.5 + 0.5) * cssW, sy = (1 - (ny * 0.5 + 0.5)) * cssH;
        var largoR = cssW / cssH > 1.3;
        var lw = el._w || (el._w = el.offsetWidth || 100);
        var dentro = sx > 8 && sx + 14 + lw < cssW - 4 && sy > 14 && sy < cssH - 14;
        if (largoR && !centro && tipo === "heroi" && !claro && !centrada && sx < cssW * 0.58) dentro = false;
        if (centrada && sy < cssH * 0.72) dentro = false;
        if (largoR && !centro && tipo === "jornada" && sx > cssW * 0.5) dentro = false;
        var prof = Math.max(0, Math.min(1, (16 - c[3]) / 8));
        if (dentro) {
          var cx0 = sx + 12, cy0 = sy - 12, cx1 = cx0 + lw, cy1 = sy + 12;
          for (var pi = 0; pi < postos.length; pi++) {
            var o = postos[pi];
            if (cx0 < o[2] + 6 && cx1 + 6 > o[0] && cy0 < o[3] + 4 && cy1 + 4 > o[1]) { dentro = false; break; }
          }
          if (dentro) postos.push([cx0, cy0, cx1, cy1]);
        }
        el.style.opacity = dentro ? String((prm.rede * (0.35 + 0.65 * prof)).toFixed(3)) : "0";
        el.style.transform = "translate3d(" + sx.toFixed(1) + "px," + sy.toFixed(1) + "px,0)";
      }
      return { arestas: nA, pontos: k };
    }

    var camAtual = null;
    function usar(prog, buf, vp, olho, prm, t, desloc, esc) {
      gl.useProgram(prog.p);
      gl.bindBuffer(gl.ARRAY_BUFFER, buf);
      gl.enableVertexAttribArray(prog.aP); gl.vertexAttribPointer(prog.aP, 3, gl.FLOAT, false, 24, 0);
      gl.enableVertexAttribArray(prog.aE); gl.vertexAttribPointer(prog.aE, 3, gl.FLOAT, false, 24, 12);
      var u = prog.u;
      gl.uniformMatrix4fv(u.vp, false, new Float32Array(vp));
      gl.uniform2f(u.desloc, desloc[0], desloc[1]);
      gl.uniform3fv(u.olho, olho);
      gl.uniform1f(u.tempo, t); gl.uniform1f(u.cresce, prm.cresce); gl.uniform1f(u.fantasma, prm.fantasma);
      gl.uniform1f(u.rede, prm.rede); gl.uniform1f(u.anel, prm.anel); gl.uniform1f(u.claro, claro ? 1 : 0);
      gl.uniform1f(u.escala, esc);
    }

    function desenhar(agora) {
      var t = reduzir ? 9 : (agora - inicio) / 1000, dt = Math.min(0.05, (agora - ultimo) / 1000);
      ultimo = agora;
      if (reduzir) dt = 0;
      smx += (mx - smx) * 0.04; smy += (my - smy) * 0.04;
      var asp = W / H, cam = camAtual = camera(t, asp), prm = parametros(t);
      var olho = [cam.alvo[0] + cam.dist * Math.cos(cam.elev) * Math.sin(cam.ang), cam.alvo[1] + cam.dist * Math.sin(cam.elev),
                  cam.alvo[2] + cam.dist * Math.cos(cam.elev) * Math.cos(cam.ang)];
      var vp = mult(perspectiva(cam.fov, asp, 0.1, 60), olharPara(olho, cam.alvo));
      var n = atualizarRede(t, dt, prm, vp);
      var esc = 21 * DPR * Math.min(1.25, Math.max(0.75, H / (720 * DPR)));

      if (claro) { gl.clearColor(0, 0, 0, 0); gl.enable(gl.BLEND); gl.blendFuncSeparate(gl.SRC_ALPHA, gl.ONE_MINUS_SRC_ALPHA, gl.ONE, gl.ONE_MINUS_SRC_ALPHA); }
      else { gl.clearColor(8 / 255, 37 / 255, 56 / 255, 1); gl.enable(gl.BLEND); gl.blendFunc(gl.SRC_ALPHA, gl.ONE); }
      gl.clear(gl.COLOR_BUFFER_BIT);

      if (geo.linhas.length) { usar(progLinhas, bLinhas, vp, olho, prm, t, cam.desloc, esc); gl.drawArrays(gl.LINES, 0, geo.linhas.length / 6); }
      if (geo.pontos.length) { usar(progPontos, bPontos, vp, olho, prm, t, cam.desloc, esc); gl.drawArrays(gl.POINTS, 0, geo.pontos.length / 6); }
      if (prm.rede > 0.01) {
        gl.bindBuffer(gl.ARRAY_BUFFER, bdLinhas); gl.bufferSubData(gl.ARRAY_BUFFER, 0, dLinhas.subarray(0, n.arestas * 12));
        usar(progLinhas, bdLinhas, vp, olho, prm, t, cam.desloc, esc); gl.drawArrays(gl.LINES, 0, n.arestas * 2);
        gl.bindBuffer(gl.ARRAY_BUFFER, bdPontos); gl.bufferSubData(gl.ARRAY_BUFFER, 0, dPontos.subarray(0, n.pontos * 6));
        usar(progPontos, bdPontos, vp, olho, prm, t, cam.desloc, esc); gl.drawArrays(gl.POINTS, 0, n.pontos);
      }
    }

    // ---- ciclo de vida
    var rodando = false, visivel = false, viva = false;
    function laco(agora) {
      if (!rodando) return;
      ler();
      desenhar(agora);
      requestAnimationFrame(laco);
    }
    function ligar() {
      if (rodando || !visivel || document.hidden) return;
      if (reduzir) { ler(); desenhar(performance.now()); return; }
      rodando = true; ultimo = performance.now();
      requestAnimationFrame(laco);
    }
    function desligar() { rodando = false; }
    function ler() {
      if (tipo === "heroi") {
        var r = host.getBoundingClientRect();
        estado.rolagem = reduzir ? 0 : Math.min(Math.max(-r.top / (r.height || 1), 0), 1);
      } else if (tipo === "jornada") {
        var z = parseFloat(host.style.getPropertyValue("--z"));
        estado.z = reduzir || host.classList.contains("estatica") ? 1 : (isNaN(z) ? 0 : z);
      }
    }

    medir();
    ler();
    desenhar(performance.now());
    viva = true;
    host.classList.add("cena-viva");

    if (window.ResizeObserver) {
      new ResizeObserver(function () { medir(); if (!rodando) { ler(); desenhar(performance.now()); } }).observe(tela);
    } else {
      window.addEventListener("resize", medir);
    }
    if (ponteiroFino && !reduzir) {
      window.addEventListener("pointermove", function (e) {
        if (!rodando) return;
        var r = tela.getBoundingClientRect();
        mx = Math.max(-1, Math.min(1, ((e.clientX - r.left) / r.width - 0.5) * 2));
        my = Math.max(-1, Math.min(1, ((e.clientY - r.top) / r.height - 0.5) * -2));
      }, { passive: true });
    }
    if (reduzir && tipo === "jornada") {
      window.addEventListener("scroll", function () { if (visivel) { ler(); desenhar(performance.now()); } }, { passive: true });
    }
    document.addEventListener("visibilitychange", function () { if (document.hidden) desligar(); else ligar(); });
    tela.addEventListener("webglcontextlost", function (e) {
      e.preventDefault(); desligar(); viva = false; host.classList.remove("cena-viva");
    });
    return {
      visivel: function (v) { visivel = v; if (v) ligar(); else desligar(); },
      viva: function () { return viva; }
    };
  }

  // ------------------------------------------------------------ montagem preguiçosa
  // o hero monta na hora; as outras cenas só quando chegam perto da tela
  var cenas = new Map();
  function montar(tela) {
    if (cenas.has(tela)) return cenas.get(tela);
    var c = null;
    try { c = Cena(tela); } catch (e) { c = null; }
    cenas.set(tela, c);
    return c;
  }
  if (!("IntersectionObserver" in window)) {
    telas.forEach(function (t) { var c = montar(t); if (c) c.visivel(true); });
    return;
  }
  var obs = new IntersectionObserver(function (es) {
    es.forEach(function (e) {
      var c = e.isIntersecting || cenas.has(e.target) ? montar(e.target) : null;
      if (c) c.visivel(e.isIntersecting);
    });
  }, { rootMargin: "120px 0px" });
  telas.forEach(function (t) {
    if (t.getAttribute("data-cena") === "heroi") montar(t);
    obs.observe(t);
  });
})();
