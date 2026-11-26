// Gera o Word do manual a partir de word/ir.json (estrutura extraída do HTML final).
// A4 deitado, margens 10/11,5/10/10 mm, Inter, cabeçalho e rodapé como no PDF, âncoras + "vá para (p. N)" por campos PAGEREF.
const fs = require("fs");
const path = require("path");
const d = require("docx");
const {
  Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell, ImageRun, Bookmark, InternalHyperlink, SimpleField,
  PageBreak, PageNumber, AlignmentType, BorderStyle, WidthType, ShadingType, TabStopType, LeaderType, Tab, PageOrientation,
  SectionType, HeadingLevel, LevelFormat, VerticalAlign, TableLayoutType, Header, Footer, LineRuleType,
} = d;

const ROOT = path.resolve(__dirname, "..");
let IR = JSON.parse(fs.readFileSync(path.join(__dirname, "ir.json"), "utf8")).blocks;
if (process.env.IR_LIMIT) IR = IR.slice(0, parseInt(process.env.IR_LIMIT, 10));
const PAGES = JSON.parse(fs.readFileSync(path.join(__dirname, "pages.json"), "utf8"));

// ---- medidas ----
const mm = (x) => Math.round((x / 25.4) * 1440);        // mm → twips
const pt = (x) => Math.round(x * 20);                   // pt → twips (espaçamento)
const hp = (x) => Math.round(x * 2);                    // pt → meios-pontos (corpo)
const px = (mmv) => Math.round((mmv / 25.4) * 96);      // mm → px (imagens, 96 dpi)
const PAGE_W = 16838, PAGE_H = 11906;
const M_TOP = mm(10), M_BOT = mm(10), M_LEFT = mm(10), M_RIGHT = mm(11.5);
const TEXT_W = PAGE_W - M_LEFT - M_RIGHT;               // 15619 twips = 275,5 mm
const BLUE = "1F4E8C", INK = "111111", GREY = "444444", LINE = "9A9A9A";
const FONT = "Inter";

// ---- numeração (listas) ----
const numbering = { config: [{ reference: "bul", levels: [{ level: 0, format: LevelFormat.BULLET, text: "•", alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: pt(12), hanging: pt(8) } } } }] }] };
let nOl = 0;
function olRef(start) {
  nOl += 1; const ref = `ol${nOl}`;
  numbering.config.push({ reference: ref, levels: [{ level: 0, format: LevelFormat.DECIMAL, text: "%1.", start, alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: pt(12), hanging: pt(9) } } } }] });
  return ref;
}

// ---- runs ----
let pendingAnchors = [];
function bookmarkRuns(runs) {
  if (!pendingAnchors.length) return runs;
  const bms = pendingAnchors.map((id) => new Bookmark({ id, children: [new TextRun({ text: "", font: FONT })] }));
  pendingAnchors = [];
  return bms.concat(runs);
}
function mkRun(r, ctx) {
  const o = { text: r.text, font: FONT, size: hp(r.size || ctx.fs), bold: !!r.b || !!ctx.bold, italics: !!r.i };
  if (r.color) o.color = r.color; else if (ctx.color) o.color = ctx.color;
  if (r.shade) o.shading = { type: ShadingType.CLEAR, fill: r.shade, color: "auto" };
  if (r.sup) o.superScript = true;
  if (r.br) return new TextRun({ break: 1, font: FONT, size: hp(ctx.fs) });
  return new TextRun(o);
}
function mkRuns(runs, ctx) {
  const out = [];
  for (const r of runs) {
    if (r.pageref) {
      const cached = PAGES[r.pageref] != null ? String(PAGES[r.pageref]) : "0";
      out.push(new TextRun({ text: " (p. ", font: FONT, size: hp(ctx.fs), color: GREY }));
      out.push(new SimpleField(`PAGEREF ${r.pageref} \\h`, cached));
      out.push(new TextRun({ text: ")", font: FONT, size: hp(ctx.fs), color: GREY }));
      continue;
    }
    if (r.link) { out.push(new InternalHyperlink({ anchor: r.link, children: [mkRun(r, ctx)] })); continue; }
    out.push(mkRun(r, ctx));
  }
  return out;
}

// ---- parágrafos ----
function para(runs, opts, ctx) {
  const o = Object.assign({ spacing: { after: pt(3), line: 305, lineRule: LineRuleType.AUTO }, keepLines: false }, opts || {});
  o.children = bookmarkRuns(runs);
  return new Paragraph(o);
}
const BLUE_RULE = (sizeEighths, color) => ({ style: BorderStyle.SINGLE, size: sizeEighths, color, space: 1 });

function pBlock(b, ctx) {
  const cls = b.cls || "";
  let fs = ctx.fs, opts = { spacing: { after: pt(3), line: 305, lineRule: LineRuleType.AUTO } }, color = null, runsBase = b.runs;
  if (b.interp || ctx.interp) { fs = ctx.fsInterp || 7.7; opts.spacing = { before: pt(1), after: pt(2), line: 305, lineRule: LineRuleType.AUTO }; }
  if (cls === "kicker") {
    return para(b.runs.map((r) => new TextRun({ text: r.text.toUpperCase(), font: FONT, size: hp(6.8), color: BLUE, characterSpacing: 22 })), { spacing: { before: 0, after: pt(2), line: 240, lineRule: LineRuleType.AUTO }, keepNext: true }, ctx);
  }
  if (cls === "rota") { fs = 7.3; opts = { spacing: { before: pt(3), after: pt(3), line: 290, lineRule: LineRuleType.AUTO }, shading: { type: ShadingType.CLEAR, fill: "F3F6FB", color: "auto" }, border: { left: { style: BorderStyle.SINGLE, size: 16, color: BLUE, space: 4 } }, indent: { left: pt(5) } }; }
  else if (cls === "base") { fs = 7.2; color = GREY; opts.spacing = { before: pt(2), after: pt(2), line: 290, lineRule: LineRuleType.AUTO }; }
  else if (cls === "pergunta-block") { opts = { spacing: { before: pt(2), after: pt(3), line: 290, lineRule: LineRuleType.AUTO }, border: { left: { style: BorderStyle.SINGLE, size: 16, color: BLUE, space: 4 } }, indent: { left: pt(5) } }; }
  else if (cls === "cellhead") { fs = 8.4; opts = { spacing: { before: 0, after: pt(2), line: 260, lineRule: LineRuleType.AUTO }, keepNext: true }; runsBase = b.runs.map((r) => Object.assign({}, r, { b: true, color: BLUE })); }
  else if (cls === "pi-id") { opts = { spacing: { before: pt(5), after: pt(1), line: 260, lineRule: LineRuleType.AUTO }, keepNext: true }; }
  else if (cls === "box-title") { opts = { spacing: { before: 0, after: pt(1.5), line: 240, lineRule: LineRuleType.AUTO }, keepNext: true }; runsBase = b.runs.map((r) => Object.assign({}, r, { b: true, size: 7 })); return para(runsBase.map((r) => new TextRun({ text: r.text.toUpperCase(), font: FONT, size: hp(7), bold: true, characterSpacing: 14 })), opts, ctx); }
  else if (cls === "intro") { opts.spacing = { after: pt(3), line: 305, lineRule: LineRuleType.AUTO }; if (b.narrow) opts.indent = { right: Math.round(TEXT_W * 0.36) }; }
  if (ctx.gloss) { fs = 7.3; opts.spacing = { after: pt(2), line: 290, lineRule: LineRuleType.AUTO }; opts.keepLines = true; }
  if (ctx.inCell && !cls) opts.spacing = { before: 0, after: pt(0.6), line: 293, lineRule: LineRuleType.AUTO };
  if (ctx.narrowRight) opts.indent = Object.assign({}, opts.indent || {}, { right: ctx.narrowRight });
  if (b.keep_with_next) opts.keepNext = true;
  if (b.id) pendingAnchors.push(b.id);
  return para(mkRuns(runsBase, Object.assign({}, ctx, { fs, color })), opts, ctx);
}

function heading(b, ctx) {
  if (b.id) pendingAnchors.push(b.id);
  if (b.t === "h1") {
    const runs = [new TextRun({ text: b.text, font: FONT, size: hp(15), bold: true, color: INK })];
    return para(runs, { heading: HeadingLevel.HEADING_1, spacing: { before: 0, after: pt(4), line: 264, lineRule: LineRuleType.AUTO }, keepNext: !ctx.noKeep }, ctx);
  }
  if (b.t === "h2") {
    const o = { heading: HeadingLevel.HEADING_2, spacing: { before: pt(6), after: pt(2), line: 276, lineRule: LineRuleType.AUTO }, keepNext: !ctx.noKeep, border: { bottom: { style: BorderStyle.SINGLE, size: 3, color: "C9D2E0", space: 1 } } };
    if (ctx.narrowRight) o.indent = { right: ctx.narrowRight };
    return para(mkRuns(b.runs.map((r) => Object.assign({ b: true, color: BLUE, size: ctx.beside ? 9.4 : 10.2 }, r, { b: true, color: r.color || BLUE })), ctx), o, ctx);
  }
  const o = { heading: HeadingLevel.HEADING_3, spacing: { before: pt(5), after: pt(1.5), line: 260, lineRule: LineRuleType.AUTO }, keepNext: !ctx.noKeep };
  if (ctx.narrowRight) o.indent = { right: ctx.narrowRight };
  return para(mkRuns(b.runs.map((r) => Object.assign({ b: true, color: BLUE, size: 8.8 }, r, { b: true, color: r.color || BLUE })), ctx), o, ctx);
}

function chartHead(b, ctx) {
  // id à esquerda (11,5 pt, azul), título à direita (8,8 pt), filete preto embaixo
  if (b.id) pendingAnchors.push(b.id);
  const width = ctx.avail || TEXT_W;
  const idRun = new TextRun({ text: b.cid, font: FONT, size: hp(11.5), bold: true, color: BLUE });
  const children = [idRun, new TextRun({ children: [new Tab()], font: FONT, size: hp(8.8) }), new TextRun({ text: b.title, font: FONT, size: hp(b.long ? 7.6 : 8.8), bold: true })];
  return para(children, { spacing: { before: pt(2), after: pt(3), line: 264, lineRule: LineRuleType.AUTO }, keepNext: !ctx.noKeep, tabStops: [{ type: TabStopType.RIGHT, position: width }], border: { bottom: { style: BorderStyle.SINGLE, size: 8, color: INK, space: 1 } } }, ctx);
}

function listBlock(b, ctx) {
  const out = [];
  const ref = b.ordered ? olRef(b.start || 1) : "bul";
  const fs = ctx.interp ? (ctx.fsInterp || 7.7) : ctx.fs;
  b.items.forEach((it, i) => {
    const o = { numbering: { reference: ref, level: 0 }, spacing: { after: pt(b.cls && b.cls.includes("steps") ? 2 : 1.2), line: 305, lineRule: LineRuleType.AUTO } };
    if (ctx.narrowRight) o.indent = { right: ctx.narrowRight };
    if (i === b.items.length - 1 && b.items.length > 1) o.keepNext = false;
    out.push(para(mkRuns(it.runs, Object.assign({}, ctx, { fs })), o, ctx));
  });
  return out;
}

// ---- imagens ----
function imageBlock(b, ctx) {
  const buf = fs.readFileSync(path.join(ROOT, b.path));
  let wmm = (ctx.avail || TEXT_W) / 1440 * 25.4;
  if (b.thumb) wmm = 22;
  if (ctx.imgScale) wmm *= ctx.imgScale;
  if (!(wmm > 12)) { console.log('imagem estreita:', b.path, 'avail', ctx.avail, '→ 40 mm'); wmm = 40; }
  const w = px(wmm), h = Math.round(w * b.hpx / b.wpx);
  return para([new ImageRun({ type: "png", data: buf, transformation: { width: w, height: h } })], { spacing: { before: 0, after: pt(2) }, keepNext: false }, ctx);
}

// ---- tabelas ----
const NOB = { style: BorderStyle.NONE, size: 0, color: "FFFFFF" };
const NOBORDERS = { top: NOB, bottom: NOB, left: NOB, right: NOB, insideHorizontal: NOB, insideVertical: NOB };
const THIN = { style: BorderStyle.SINGLE, size: 3, color: LINE };
const THINB = { top: THIN, bottom: THIN, left: THIN, right: THIN, insideHorizontal: THIN, insideVertical: THIN };

function colWidths(tb, avail, ctx) {
  const ncol = Math.max(...tb.rows.map((r) => r.cells.reduce((a, c) => a + (c.colspan || 1), 0)));
  const explicit = tb.rows.find((r) => r.cells.some((c) => c.w != null));
  if (tb.cls === "cb" || tb.cls === "gi" || tb.cls === "two") {
    // larguras do HTML: td.l com width:%, td.gap 5 mm (grp) ou 4 % (two), td.r o resto; usa a linha com mais células
    const row = tb.rows.reduce((a, r) => (r.cells.length > a.cells.length ? r : a), tb.rows[0]); const ws = []; let used = 0; let nRest = 0;
    row.cells.forEach((c) => {
      if (c.cls.includes("gap")) { const g = tb.cls === "two" ? Math.round(avail * 0.04) : mm(5); ws.push(g); used += g; }
      else if (c.w != null) { const w = Math.round(avail * c.w / 100); ws.push(w); used += w; }
      else if (tb.cls === "two") { const w = Math.round(avail * 0.48); ws.push(w); used += w; }
      else { ws.push(null); nRest += 1; }
    });
    const rest = Math.max(avail - used, mm(20));
    return ws.map((w) => (w == null ? Math.round(rest / Math.max(nRest, 1)) : w));
  }
  if (tb.cls === "legend") {
    const p = ctx.inCbRight ? [24, 34, 42] : (ctx.inCols ? [22, 33, 45] : [14, 36, 50]);
    if (ncol === 3) return p.map((x) => Math.round(avail * x / 100));
  }
  if (tb.cls === "lista") return Array(ncol).fill(Math.round(avail / ncol));
  // genérica: proporcional ao tamanho médio do texto por coluna (limitado)
  const lens = Array(ncol).fill(0), cnt = Array(ncol).fill(0);
  tb.rows.forEach((r) => { let i = 0; r.cells.forEach((c) => { const L = JSON.stringify(c.blocks).replace(/"[a-z_]+":/g, "").length; lens[i] += L; cnt[i] += 1; i += c.colspan || 1; }); });
  let sc = lens.map((L, i) => Math.min(Math.max(L / Math.max(cnt[i], 1), 60), 1200));
  const tot = sc.reduce((a, b) => a + b, 0);
  const ws = sc.map((x) => Math.round(avail * x / tot));
  ws[ws.length - 1] += avail - ws.reduce((a, b) => a + b, 0);
  return ws;
}

function tableBlock(tb, ctx) {
  const avail = ctx.avail || TEXT_W;
  const ws = colWidths(tb, avail, ctx);
  const total = ws.reduce((a, b) => a + b, 0);
  const bare = ["cb", "gi", "two", "lista"].includes(tb.cls);
  const fsTable = tb.cls === "small" ? (ctx.inDcard ? 6.7 : 7.0) : tb.cls === "lista" ? 8.0 : tb.cls === "legend" ? (ctx.interp ? 7.8 : 7.3) : (ctx.inBeside ? 7.4 : 7.5);
  const rows = tb.rows.map((r) => {
    let ci = 0;
    const cells = r.cells.map((c) => {
      const span = c.colspan || 1; const w = ws.slice(ci, ci + span).reduce((a, b) => a + b, 0); ci += span;
      const isL = c.cls.includes("l"), isR = c.cls.includes("r"), isGap = c.cls.includes("gap");
      const inner = Object.assign({}, ctx, { avail: w - (bare ? (isL ? mm(6) : 0) : pt(6)), fs: bare ? ctx.fs : fsTable, interp: bare ? ctx.interp : false, inCbRight: tb.cls === "cb" && isR, inCols: false, keepImg: true, inCell: !bare, bold: !!r.header });
      if (tb.cls === "lista") inner.avail = w - pt(8);
      const kids = [];
      if (!isGap) for (const b of c.blocks) kids.push(...render(b, inner));
      if (!kids.length) kids.push(new Paragraph({ children: [new TextRun({ text: "", font: FONT, size: hp(6) })], spacing: { after: 0, line: 200, lineRule: LineRuleType.AUTO } }));
      const o = { width: { size: w, type: WidthType.DXA }, children: kids, verticalAlign: VerticalAlign.TOP };
      if (bare) {
        o.borders = { top: NOB, bottom: NOB, left: NOB, right: NOB };
        o.margins = { top: 0, bottom: 0, left: 0, right: isL && tb.cls === "cb" ? mm(6) : 0 };
        if (tb.cls === "lista") {
          o.margins = { top: pt(0.9), bottom: pt(0.9), left: pt(4), right: pt(4) };
          if (c.cls.includes("li") && !c.cls.includes("empty")) { o.shading = { type: ShadingType.CLEAR, fill: "FAFBFD", color: "auto" }; o.borders.left = { style: BorderStyle.SINGLE, size: 16, color: c.lborder || LINE }; }
          if (c.cls.includes("lh") && c.shade) o.shading = { type: ShadingType.CLEAR, fill: c.shade, color: "auto" };
          o.verticalAlign = VerticalAlign.CENTER;
        }
      } else {
        o.borders = { top: THIN, bottom: THIN, left: THIN, right: THIN };
        o.margins = { top: pt(1.6), bottom: pt(1.6), left: pt(3), right: pt(3) };
        if (r.header) o.shading = { type: ShadingType.CLEAR, fill: c.cap ? BLUE : "EEF2F7", color: "auto" };
      }
      return new TableCell(o);
    });
    const hasImg = r.cells.some((c) => c.blocks.some((x) => x.t === "image"));
    return new TableRow({ children: cells, cantSplit: !bare || hasImg, tableHeader: !!r.header && !bare });   // linha com desenho é indivisível (como no PDF; e o LibreOffice trava tentando parti-la)
  });
  // cabeçalho: negrito 600 / texto
  const t = new Table({ rows, width: { size: total, type: WidthType.DXA }, columnWidths: ws, layout: TableLayoutType.FIXED, borders: bare ? NOBORDERS : THINB });
  return [t, spacer(bare ? 2 : 4)];
}
function spacer(ptAfter) { return new Paragraph({ children: [new TextRun({ text: "", font: FONT, size: hp(2) })], spacing: { before: 0, after: pt(ptAfter || 0), line: 120, lineRule: LineRuleType.AUTO } }); }

// cabeçalho de tabela em negrito: aplicado via runs (th) — o IR marca a linha como header; aqui reforçamos o peso
function boldHeaderRuns(b) { return b; }

// ---- trilha (chips) ----
function trilha(b, ctx) {
  const kids = [];
  b.chips.forEach((c, i) => {
    if (i) kids.push(new TextRun({ text: " › ", font: FONT, size: hp(9), bold: true, color: BLUE }));
    const bd = { style: BorderStyle.SINGLE, size: 4, color: BLUE, space: 1 };
    const inner = [new TextRun({ text: c.id + " ", font: FONT, size: hp(6.8), bold: true, color: BLUE, border: bd, shading: { type: ShadingType.CLEAR, fill: "FFFFFF", color: "auto" } }),
                   new TextRun({ text: c.label + " · ", font: FONT, size: hp(6.8), color: INK, border: bd, shading: { type: ShadingType.CLEAR, fill: "FFFFFF", color: "auto" } }),
                   new SimpleField(`PAGEREF ${c.anchor} \\h`, PAGES[c.anchor] != null ? String(PAGES[c.anchor]) : "0")];
    kids.push(new InternalHyperlink({ anchor: c.anchor, children: inner }));
  });
  return [para(kids, { spacing: { before: pt(1), after: pt(4), line: 330, lineRule: LineRuleType.AUTO }, shading: { type: ShadingType.CLEAR, fill: "F3F6FB", color: "auto" }, keepNext: true, keepLines: true }, ctx)];
}

// ---- caixas, cartões ----
function box(b, ctx) {
  const avail = ctx.avail || TEXT_W;
  const color = b.cls === "variacao" ? "2E7D32" : b.cls === "alerta" ? "C62828" : BLUE;
  const inner = Object.assign({}, ctx, { avail: avail - pt(12), fs: 8.2, interp: false });
  const kids = []; for (const x of b.blocks) kids.push(...render(x, inner));
  const bd = { style: BorderStyle.SINGLE, size: 5, color };
  const cell = new TableCell({ width: { size: avail, type: WidthType.DXA }, children: kids, borders: { top: bd, bottom: bd, left: bd, right: bd }, margins: { top: pt(3), bottom: pt(1), left: pt(6), right: pt(6) },
    shading: b.cls === "variacao" ? { type: ShadingType.CLEAR, fill: "F3F9F3", color: "auto" } : undefined });
  return [new Table({ rows: [new TableRow({ children: [cell], cantSplit: true })], width: { size: avail, type: WidthType.DXA }, columnWidths: [avail], layout: TableLayoutType.FIXED }), spacer(5)];
}
function dcard(b, ctx) {
  const avail = ctx.avail || TEXT_W; const inner = avail - pt(10);
  if (b.id) pendingAnchors.push(b.id);
  const kids = [];
  // cabeça: miniatura | D-n + pergunta
  const thumbW = mm(22), txtW = inner - thumbW - pt(6);
  const left = []; if (b.thumb) left.push(imageBlock({ path: path.relative(ROOT, path.join(__dirname, "png", "mini_" + path.basename(b.thumb, ".svg") + ".png")), wpx: 0, hpx: 0, thumb: true }, ctx));
  const right = [para([new TextRun({ text: b.did, font: FONT, size: hp(8.4), bold: true, color: BLUE })], { spacing: { after: pt(1), line: 240, lineRule: LineRuleType.AUTO }, keepNext: true }, ctx),
                 para(mkRuns(b.q.map((r) => Object.assign({ i: true, color: BLUE, size: 7.3 }, r)), ctx), { spacing: { after: pt(2), line: 260, lineRule: LineRuleType.AUTO }, keepNext: true }, ctx)];
  const head = new Table({ rows: [new TableRow({ children: [
      new TableCell({ width: { size: thumbW, type: WidthType.DXA }, children: left.length ? left : [spacer(0)], borders: { top: NOB, bottom: NOB, left: NOB, right: NOB }, margins: { top: 0, bottom: 0, left: 0, right: pt(6) } }),
      new TableCell({ width: { size: txtW, type: WidthType.DXA }, children: right, borders: { top: NOB, bottom: NOB, left: NOB, right: NOB }, margins: { top: 0, bottom: 0, left: 0, right: 0 } }) ], cantSplit: true })],
    width: { size: inner, type: WidthType.DXA }, columnWidths: [thumbW, txtW], layout: TableLayoutType.FIXED, borders: NOBORDERS });
  kids.push(head);
  if (b.table) kids.push(...tableBlock(b.table, Object.assign({}, ctx, { avail: inner, inDcard: true, interp: false })));
  const bd = { style: BorderStyle.SINGLE, size: 4, color: "B7C3D6" };
  const cell = new TableCell({ width: { size: avail, type: WidthType.DXA }, children: kids, borders: { top: bd, bottom: bd, left: bd, right: bd }, margins: { top: pt(4), bottom: pt(1), left: pt(5), right: pt(5) }, shading: { type: ShadingType.CLEAR, fill: "FCFDFF", color: "auto" } });
  return [new Table({ rows: [new TableRow({ children: [cell], cantSplit: true })], width: { size: avail, type: WidthType.DXA }, columnWidths: [avail], layout: TableLayoutType.FIXED }), spacer(4)];
}

// ---- miniaturas (dcard) : corrigir dimensões lendo o PNG ----
const PNG_DIM = {};
function pngDim(p) {
  if (!PNG_DIM[p]) { const b = fs.readFileSync(p); PNG_DIM[p] = [b.readUInt32BE(16), b.readUInt32BE(20)]; }
  return PNG_DIM[p];
}
const _imageBlock = imageBlock;
imageBlock = function (b, ctx) { if (!b.wpx) { const [w, h] = pngDim(path.join(ROOT, b.path)); b = Object.assign({}, b, { wpx: w, hpx: h }); } return _imageBlock(b, ctx); };

// ---- despacho ----
function render(b, ctx) {
  switch (b.t) {
    case "p": return [pBlock(b, ctx)];
    case "h1": case "h2": case "h3": case "h4": return [heading(b, ctx)];
    case "list": return listBlock(b, ctx);
    case "table": return tableBlock(b, ctx);
    case "image": return [imageBlock(b, ctx)];
    case "chart-head": return [chartHead(b, ctx)];
    case "anchor": pendingAnchors.push(b.id); return [];
    case "trilha": return trilha(b, ctx);
    case "box": return box(b, ctx);
    case "dcard": return dcard(b, ctx);
    case "pic": { const kids = [imageBlock({ path: path.relative(ROOT, path.join(__dirname, "png", path.basename(b.src, ".svg") + ".png")), wpx: 0, hpx: 0 }, Object.assign({}, ctx, { keepImg: true }))];
      if (b.caption && b.caption.length) kids.push(para(mkRuns(b.caption, Object.assign({}, ctx, { fs: 7.3, color: GREY })), { alignment: AlignmentType.CENTER, spacing: { before: pt(2), after: pt(6), line: 260, lineRule: LineRuleType.AUTO } }, ctx)); return kids; }
    case "one": { const inner = Object.assign({}, ctx, { narrowRight: Math.round((ctx.avail || TEXT_W) * 0.28), avail: Math.round((ctx.avail || TEXT_W) * 0.72) }); const out = []; for (const x of b.blocks) out.push(...render(x, inner)); return out; }
    case "beside": { const inner = Object.assign({}, ctx, { beside: true, inBeside: true }); const out = []; let first = true;
      for (const x of b.blocks) { const r = render(x, inner); if (first && b.rule && r.length && r[0] instanceof Paragraph) { /* filete acima */ } first = false; out.push(...r); } return out; }
    case "gloss": { const inner = Object.assign({}, ctx, { gloss: true, fs: 7.3 }); const out = []; for (const x of b.blocks) out.push(...render(x, inner)); return out; }
    case "tec": { if (b.id) pendingAnchors.push(b.id); const out = []; for (const x of b.blocks) out.push(...render(x, ctx)); return out; }
    case "cols": { const out = []; for (const x of b.blocks) out.push(...render(x, Object.assign({}, ctx, { inCols: true }))); return out; }   // colunas aninhadas: sequencial
    case "pb": return [new Paragraph({ children: [new PageBreak()] })];
    case "chapter": case "cover": case "toc": return [];
    default: throw new Error("bloco não mapeado no Word: " + b.t);
  }
}

// ---- cabeçalho e rodapé ----
function headerDefault() {
  return new Header({ children: [new Paragraph({ tabStops: [{ type: TabStopType.RIGHT, position: TEXT_W }], spacing: { after: 0, line: 240, lineRule: LineRuleType.AUTO },
    children: [new TextRun({ text: "Manual de Radiestesia Terapêutica", font: FONT, size: hp(7.5), color: "555555" }), new TextRun({ children: [new Tab()], font: FONT, size: hp(7.5) }),
               new SimpleField('STYLEREF "heading 1"', "")] })] });
}
function footerOdd() {
  return new Footer({ children: [new Paragraph({ alignment: AlignmentType.RIGHT, border: { top: { style: BorderStyle.SINGLE, size: 4, color: "BBBBBB", space: 4 } }, spacing: { before: 0, after: 0, line: 240, lineRule: LineRuleType.AUTO },
    children: [new SimpleField('STYLEREF "heading 1"', ""), new TextRun({ text: "   ·   ", font: FONT, size: hp(8), bold: true, color: "222222" }), new TextRun({ children: [PageNumber.CURRENT], font: FONT, size: hp(8), bold: true, color: "222222" })] })] });
}
function footerEven() {
  return new Footer({ children: [new Paragraph({ alignment: AlignmentType.LEFT, border: { top: { style: BorderStyle.SINGLE, size: 4, color: "BBBBBB", space: 4 } }, spacing: { before: 0, after: 0, line: 240, lineRule: LineRuleType.AUTO },
    children: [new TextRun({ children: [PageNumber.CURRENT], font: FONT, size: hp(8), bold: true, color: "222222" }), new TextRun({ text: "   ·   ", font: FONT, size: hp(8), bold: true, color: "222222" }), new SimpleField('STYLEREF "heading 1"', "")] })] });
}
const PAGE = { size: { width: PAGE_H, height: PAGE_W, orientation: PageOrientation.LANDSCAPE }, margin: { top: M_TOP, bottom: M_BOT, left: M_LEFT, right: M_RIGHT, header: mm(5), footer: mm(5) } };

// ---- montagem das seções ----
const sections = [];
let cur = null;
function newSection(props, first) {
  cur = { properties: Object.assign({ page: PAGE }, props || {}), children: [] };
  if (first) { cur.headers = { default: headerDefault(), even: headerDefault() }; cur.footers = { default: footerOdd(), even: footerEven() }; }
  sections.push(cur);
}
const baseCtx = { fs: 8.2, avail: TEXT_W };
let prevWasBreak = false;

// capa: seção própria, sem margens
{
  const buf = fs.readFileSync(path.join(__dirname, "png", "cover.png")); const [w, h] = pngDim(path.join(__dirname, "png", "cover.png"));
  sections.push({ properties: { page: { size: { width: PAGE_H, height: PAGE_W, orientation: PageOrientation.LANDSCAPE }, margin: { top: 0, bottom: 0, left: 0, right: 0, header: 0, footer: 0 } }, type: SectionType.NEXT_PAGE },
    headers: { default: new Header({ children: [] }) }, footers: { default: new Footer({ children: [] }), even: new Footer({ children: [] }) },
    children: [new Paragraph({ spacing: { before: 0, after: 0 }, children: [new ImageRun({ type: "png", data: buf, transformation: { width: px(297), height: px(210) } })] })] });
}
newSection({ type: SectionType.NEXT_PAGE }, true);

for (let i = 0; i < IR.length; i++) {
  const b = IR[i];
  if (b.t === "cover") continue;
  if (b.t === "toc") {
    pendingAnchors.push("sumario");
    cur.children.push(para([new TextRun({ text: b.title, font: FONT, size: hp(15), bold: true, color: INK })], { heading: HeadingLevel.HEADING_1, spacing: { before: 0, after: pt(6), line: 264, lineRule: LineRuleType.AUTO }, keepNext: true }, baseCtx));
    newSection({ type: SectionType.CONTINUOUS, column: { count: 3, space: pt(12), equalWidth: true } });
    const colW = Math.round((TEXT_W - 2 * pt(12)) / 3);
    for (const it of b.items) {
      const fs = it.level === 1 ? 7.3 : 6.9;
      cur.children.push(new Paragraph({ tabStops: [{ type: TabStopType.RIGHT, position: colW, leader: LeaderType.DOT }], spacing: { before: it.level === 1 ? pt(2) : 0, after: 0, line: 300, lineRule: LineRuleType.AUTO }, indent: it.level === 2 ? { left: pt(7) } : undefined, keepLines: true,
        children: [new InternalHyperlink({ anchor: it.anchor, children: [new TextRun({ text: it.text, font: FONT, size: hp(fs), bold: it.level === 1, color: it.level === 1 ? INK : "333333" })] }),
                   new TextRun({ children: [new Tab()], font: FONT, size: hp(fs) }), new SimpleField(`PAGEREF ${it.anchor} \\h`, PAGES[it.anchor] != null ? String(PAGES[it.anchor]) : "0")] }));
    }
    newSection({ type: SectionType.CONTINUOUS });
    continue;
  }
  if (b.t === "chapter") {
    if (b.flow) cur.children.push(new Paragraph({ border: { top: { style: BorderStyle.SINGLE, size: 12, color: BLUE, space: 5 } }, spacing: { before: pt(9), after: pt(1), line: 120, lineRule: LineRuleType.AUTO }, children: [new TextRun({ text: "", font: FONT, size: hp(2) })] }));
    else cur.children.push(new Paragraph({ children: [new PageBreak()], spacing: { before: 0, after: 0, line: 120, lineRule: LineRuleType.AUTO } }));
    if (b.id) pendingAnchors.push(b.id);
    continue;
  }
  if (b.t === "cols" && b.n > 1) {
    const gap = b.n === 4 ? mm(5) : b.n === 3 ? mm(8) : (b.grpflow ? mm(7) : mm(9));
    const colW = Math.round((TEXT_W - (b.n - 1) * gap) / b.n);
    newSection({ type: SectionType.CONTINUOUS, column: { count: b.n, space: gap, equalWidth: true, separate: b.n <= 2 } });
    const ctx = Object.assign({}, baseCtx, { avail: colW, inCols: true, noKeep: true });
    for (const x of b.blocks) cur.children.push(...render(x, ctx));
    newSection({ type: SectionType.CONTINUOUS });
    continue;
  }
  cur.children.push(...render(b, baseCtx));
}
if (!process.env.NOBAL) { newSection({ type: SectionType.CONTINUOUS }); cur.children.push(new Paragraph({ children: [new TextRun({ text: "", font: FONT, size: hp(2) })], spacing: { before: 0, after: 0 } })); }
// seções vazias atrapalham: remover as que não têm filhos (mantendo a primeira de conteúdo)
const finalSections = sections.filter((s, i) => i < 2 || s.children.length > 0);

const doc = new Document({
  creator: "Manual de Radiestesia Terapêutica", title: "Manual de Radiestesia Terapêutica",
  features: { updateFields: true },
  evenAndOddHeaderAndFooters: true,
  styles: { default: { document: { run: { font: FONT, size: hp(8.2), color: INK }, paragraph: { spacing: { line: 305, lineRule: LineRuleType.AUTO, after: pt(3) } } } },
    paragraphStyles: [
      { id: "Heading1", name: "heading 1", basedOn: "Normal", next: "Normal", quickFormat: true, run: { font: FONT, size: hp(15), bold: true, color: INK }, paragraph: { spacing: { before: 0, after: pt(4) }, keepNext: true, outlineLevel: 0 } },
      { id: "Heading2", name: "heading 2", basedOn: "Normal", next: "Normal", quickFormat: true, run: { font: FONT, size: hp(10.2), bold: true, color: BLUE }, paragraph: { spacing: { before: pt(6), after: pt(2) }, keepNext: true, outlineLevel: 1 } },
      { id: "Heading3", name: "heading 3", basedOn: "Normal", next: "Normal", quickFormat: true, run: { font: FONT, size: hp(8.8), bold: true, color: BLUE }, paragraph: { spacing: { before: pt(5), after: pt(1.5) }, keepNext: true, outlineLevel: 2 } },
    ] },
  numbering,
  sections: finalSections,
});
Packer.toBuffer(doc).then((buf) => {
  const out = path.join(ROOT, process.env.OUT || "Manual_de_Radiestesia_Terapeutica.docx");
  fs.writeFileSync(out, buf);
  console.log("docx:", Math.round(buf.length / 1024), "KB | seções:", finalSections.length, "| listas numeradas:", nOl);
});
