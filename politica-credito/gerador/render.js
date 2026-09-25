const fs = require('fs');
const path = require('path');
const {
  Document, Packer, Paragraph, TextRun, AlignmentType, Table, TableRow, TableCell, WidthType,
  ShadingType, LevelFormat, BorderStyle, Footer, PageNumber, VerticalAlign, HeightRule,
} = require('docx');
const { C, E, docs } = require('./conteudo');

const OUT = process.argv[2];
const FONT = 'Arial';
const W = 10206; // A4 (11906) com margens de 1,5 cm
const NONE = { style: BorderStyle.NONE, size: 0, color: 'FFFFFF' };
const noBorders = { top: NONE, bottom: NONE, left: NONE, right: NONE };
const line = (c = 'BFBFBF', s = 4) => ({ style: BorderStyle.SINGLE, size: s, color: c });

// **negrito** -> [{text, bold}]
const parse = (s) => s.split(/(\*\*[^*]+\*\*)/).filter(Boolean).map((x) => (x.startsWith('**') ? { text: x.slice(2, -2), bold: true } : { text: x }));

// ---------------------------------------------------------------- Word
const R = (s, o = {}) => parse(s).map((x) => new TextRun({ text: x.text, bold: x.bold || o.bold, font: FONT, size: o.size || 20, color: o.color }));
const P = (s, o = {}) => new Paragraph({ children: R(s, o), alignment: o.align || AlignmentType.LEFT, spacing: { before: o.before || 0, after: o.after ?? 80, line: 264 }, keepNext: o.keepNext, numbering: o.numbering });
const lines = (s, o) => s.split('\n').map((l) => P(l, { ...o, after: 20 }));
const cell = (children, o = {}) => new TableCell({
  children, width: { size: o.w, type: WidthType.DXA }, verticalAlign: o.valign || VerticalAlign.TOP,
  shading: o.fill ? { type: ShadingType.CLEAR, color: 'auto', fill: o.fill } : undefined,
  borders: o.borders || { top: line(), bottom: line(), left: line(), right: line() },
  margins: { top: o.pad ?? 80, bottom: o.pad ?? 80, left: 120, right: 120 },
});
const tbl = (widths, rows) => new Table({ width: { size: W, type: WidthType.DXA }, columnWidths: widths, rows });
const pct = (ws) => { const r = ws.map((w) => Math.round((W * w) / 100)); r[r.length - 1] += W - r.reduce((a, b) => a + b, 0); return r; };
const gap = (n = 120) => new Paragraph({ children: [], spacing: { after: n } });

function evenCols(n, gutter = 160) {
  const w = Math.floor((W - gutter * (n - 1)) / n);
  const cols = [];
  for (let i = 0; i < n; i++) { cols.push(w); if (i < n - 1) cols.push(gutter); }
  cols[cols.length - 1] += W - cols.reduce((a, b) => a + b, 0);
  return cols;
}

function toDocx(b) {
  switch (b.t) {
    case 'banner':
      return [tbl([W], [new TableRow({ children: [cell([
        P(b.title, { bold: true, size: 36, color: 'FFFFFF', after: 40 }),
        P(b.sub, { size: 18, color: 'D9E1F2', after: 0 }),
      ], { w: W, fill: C.navy, borders: noBorders, pad: 200 })] })]), gap(160)];
    case 'h':
      return [new Paragraph({ keepNext: true, spacing: { before: 240, after: 100 }, border: { bottom: line(C.navy, 8) }, children: R(b.text, { bold: true, size: 24, color: C.navy }) })];
    case 'p': return [P(b.text, { after: 100 })];
    case 'small': return [P(b.text, { size: 17, color: '595959', after: 100 })];
    case 'callout': {
      const body = b.list ? b.list.map((x) => P(x, { numbering: { reference: 'bul', level: 0 }, after: 50 })) : [P(b.text, { after: 0 })];
      return [tbl([W], [new TableRow({ cantSplit: true, children: [cell(body, { w: W, fill: C[b.color], borders: { ...noBorders, left: line(E[b.color], 24) }, pad: 120 })] })]), gap()];
    }
    case 'cards': case 'tiles': {
      const cols = evenCols(b.items.length);
      const cells = [];
      b.items.forEach((it, i) => {
        const kids = b.t === 'tiles'
          ? [P(it.big, { bold: true, size: 40, color: E[it.color], align: AlignmentType.CENTER, after: 20 }), P(it.label, { size: 17, align: AlignmentType.CENTER, after: 0 })]
          : [P(it.title, { bold: true, size: 19, color: E[it.color], after: 60 }), ...it.body.map((x) => P(x, { size: 18, after: 30, numbering: x.startsWith('→') ? undefined : { reference: 'bul', level: 0 } }))];
        cells.push(cell(kids, { w: cols[i * 2], fill: C[it.color], borders: { ...noBorders, top: line(E[it.color], 18) }, pad: 120 }));
        if (i < b.items.length - 1) cells.push(cell([new Paragraph({ children: [] })], { w: cols[i * 2 + 1], borders: noBorders }));
      });
      return [tbl(cols, [new TableRow({ cantSplit: true, children: cells })]), gap()];
    }
    case 'table': {
      const ws = pct(b.widths);
      const head = new TableRow({ tableHeader: true, children: b.head.map((h, j) => cell([P(h, { bold: true, size: 18, color: 'FFFFFF', after: 0 })], { w: ws[j], fill: C.navy })) });
      const rows = b.rows.map((r) => new TableRow({ cantSplit: true, children: r.cells.map((c, j) => cell(lines(c, { size: 18, bold: b.boldFirst && j === 0 }), { w: ws[j], fill: r.color ? C[r.color] : undefined })) }));
      return [tbl(ws, [head, ...rows]), gap()];
    }
    case 'bullets': return b.items.map((x) => P(x, { numbering: { reference: 'bul', level: 0 }, after: 50 }));
    case 'numlist': return b.items.map((x) => P(x, { numbering: { reference: `num${b._id}`, level: 0 }, after: 70 }));
    case 'form': {
      const ws = pct([18, 32, 18, 32]);
      return [tbl(ws, b.rows.map((r, i) => new TableRow({ children: r.flatMap(([label, val]) => [
        cell([P(label, { bold: true, size: 17, color: C.navy, after: 0 })], { w: ws[0], fill: (b.head && i === 0) ? C.blue : C.gray }),
        cell([P(val || ' ', { size: 18, after: 0 })], { w: ws[1] }),
      ]) }))), gap(80)];
    }
    case 'steps': {
      const n = b.items.length; const arrow = 360;
      const w = Math.floor((W - arrow * (n - 1)) / n);
      const cols = []; b.items.forEach((_, i) => { cols.push(w); if (i < n - 1) cols.push(arrow); });
      cols[cols.length - 1] += W - cols.reduce((a, c) => a + c, 0);
      const cells = [];
      b.items.forEach((it, i) => {
        cells.push(cell([P(it.title, { bold: true, size: 20, color: E.blue, align: AlignmentType.CENTER, after: 30 }), P(it.body, { size: 17, align: AlignmentType.CENTER, after: 0 })], { w: cols[i * 2], fill: C.blue, borders: noBorders, pad: 110, valign: VerticalAlign.CENTER }));
        if (i < n - 1) cells.push(cell([P('►', { size: 22, color: E.blue, align: AlignmentType.CENTER, after: 0 })], { w: arrow, borders: noBorders, valign: VerticalAlign.CENTER, pad: 0 }));
      });
      return [tbl(cols, [new TableRow({ cantSplit: true, children: cells })]), gap(60)];
    }
    case 'sign': {
      const cols = evenCols(2, 600);
      const rows = [];
      for (let i = 0; i < b.names.length; i += 2) {
        rows.push(new TableRow({ cantSplit: true, children: [0, 1].flatMap((k) => {
          const [name, doc] = b.names[i + k];
          const c = cell(name ? [
            new Paragraph({ children: [], spacing: { before: 520, after: 0 }, border: { bottom: line('404040', 6) } }),
            P(name, { bold: true, size: 18, after: 0, before: 40 }),
            P(`${doc}: ____________________`, { size: 17, after: 0 }),
          ] : [new Paragraph({ children: [] })], { w: cols[k * 2], borders: noBorders, pad: 40 });
          return k === 0 ? [c, cell([new Paragraph({ children: [] })], { w: cols[1], borders: noBorders })] : [c];
        }) }));
      }
      return [tbl(cols, rows)];
    }
    default: throw new Error('bloco desconhecido: ' + b.t);
  }
}

async function writeDocx(d) {
  let id = 0;
  d.blocks.forEach((b) => { if (b.t === 'numlist') b._id = id++; });
  const numbering = { config: [
    { reference: 'bul', levels: [{ level: 0, format: LevelFormat.BULLET, text: '•', alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 300, hanging: 200 } } } }] },
    ...Array.from({ length: id }, (_, i) => ({ reference: `num${i}`, levels: [{ level: 0, format: LevelFormat.DECIMAL, text: '%1.', alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 400, hanging: 300 } }, run: { bold: true, color: C.navy } } }] })),
  ] };
  const fr = (s) => new TextRun({ text: s, font: FONT, size: 15, color: '808080' });
  const doc = new Document({
    styles: { default: { document: { run: { font: FONT, size: 20 } } } },
    numbering,
    sections: [{
      properties: { page: { size: { width: 11906, height: 16838 }, margin: { top: 850, bottom: 850, left: 850, right: 850 } } },
      footers: { default: new Footer({ children: [new Paragraph({ alignment: AlignmentType.CENTER, children: [fr(d.footer + '  ·  página '), new TextRun({ children: [PageNumber.CURRENT], font: FONT, size: 15, color: '808080' }), fr(' de '), new TextRun({ children: [PageNumber.TOTAL_PAGES], font: FONT, size: 15, color: '808080' })] })] }) },
      children: d.blocks.flatMap(toDocx),
    }],
  });
  fs.writeFileSync(path.join(OUT, d.file + '.docx'), await Packer.toBuffer(doc));
}

// ---------------------------------------------------------------- HTML (vira PDF)
const esc = (s) => s.replace(/&/g, '&amp;').replace(/</g, '&lt;');
const H = (s) => parse(s).map((x) => (x.bold ? `<b>${esc(x.text)}</b>` : esc(x.text))).join('').replace(/\n/g, '<br>');
const hex = (c) => '#' + c;

function toHtml(b) {
  switch (b.t) {
    case 'banner': return `<div class="banner"><div class="bt">${H(b.title)}</div><div class="bs">${H(b.sub)}</div></div>`;
    case 'h': return `<h2>${H(b.text)}</h2>`;
    case 'p': return `<p>${H(b.text)}</p>`;
    case 'small': return `<p class="small">${H(b.text)}</p>`;
    case 'callout': return `<div class="callout" style="background:${hex(C[b.color])};border-left-color:${hex(E[b.color])}">${b.list ? `<ul>${b.list.map((x) => `<li>${H(x)}</li>`).join('')}</ul>` : H(b.text)}</div>`;
    case 'cards': return `<div class="row">${b.items.map((it) => `<div class="card" style="background:${hex(C[it.color])};border-top-color:${hex(E[it.color])}"><div class="ct" style="color:${hex(E[it.color])}">${H(it.title)}</div><ul>${it.body.map((x) => (x.startsWith('→') ? `<li class="note">${H(x)}</li>` : `<li>${H(x)}</li>`)).join('')}</ul></div>`).join('')}</div>`;
    case 'tiles': return `<div class="row">${b.items.map((it) => `<div class="card tile" style="background:${hex(C[it.color])};border-top-color:${hex(E[it.color])}"><div class="big" style="color:${hex(E[it.color])}">${it.big}</div><div>${H(it.label)}</div></div>`).join('')}</div>`;
    case 'table': return `<table><colgroup>${b.widths.map((w) => `<col style="width:${w}%">`).join('')}</colgroup><thead><tr>${b.head.map((h) => `<th>${H(h)}</th>`).join('')}</tr></thead><tbody>${b.rows.map((r) => `<tr${r.color ? ` style="background:${hex(C[r.color])}"` : ''}>${r.cells.map((c, j) => `<td${b.boldFirst && j === 0 ? ' class="b"' : ''}>${H(c)}&nbsp;</td>`).join('')}</tr>`).join('')}</tbody></table>`;
    case 'bullets': return `<ul class="list">${b.items.map((x) => `<li>${H(x)}</li>`).join('')}</ul>`;
    case 'numlist': return `<ol>${b.items.map((x) => `<li>${H(x)}</li>`).join('')}</ol>`;
    case 'form': return `<table class="form"><colgroup><col style="width:18%"><col style="width:32%"><col style="width:18%"><col style="width:32%"></colgroup>${b.rows.map((r, i) => `<tr>${r.map(([l, v]) => `<td class="fl" style="background:${hex((b.head && i === 0) ? C.blue : C.gray)}">${H(l)}</td><td>${H(v || '')}</td>`).join('')}</tr>`).join('')}</table>`;
    case 'steps': return `<div class="steps">${b.items.map((it, i) => `<div class="step"><b>${H(it.title)}</b><span>${H(it.body)}</span></div>${i < b.items.length - 1 ? '<div class="arrow">►</div>' : ''}`).join('')}</div>`;
    case 'sign': return `<div class="sign">${b.names.map(([n, d]) => (n ? `<div class="sig"><div class="sl"></div><b>${H(n)}</b><span>${d}: ____________________</span></div>` : '<div></div>')).join('')}</div>`;
    default: throw new Error('bloco desconhecido: ' + b.t);
  }
}

const CSS = `
@page { size: A4; margin: 15mm 15mm 16mm 15mm; }
* { box-sizing: border-box; -webkit-print-color-adjust: exact; print-color-adjust: exact; }
body { font-family: Arial, Helvetica, sans-serif; font-size: 9.5pt; color: #1a1a1a; line-height: 1.3; margin: 0; }
.banner { background: #${C.navy}; color: #fff; padding: 12px 16px; margin-bottom: 10px; }
.bt { font-size: 18pt; font-weight: bold; } .bs { font-size: 9pt; color: #D9E1F2; margin-top: 3px; }
h2 { font-size: 12pt; color: #${C.navy}; border-bottom: 1.5px solid #${C.navy}; padding-bottom: 3px; margin: 12px 0 6px; break-after: avoid; }
p { margin: 0 0 6px; } .small { font-size: 8.5pt; color: #595959; }
.callout { border-left: 4px solid; padding: 8px 12px; margin: 4px 0 9px; break-inside: avoid; }
.callout ul { margin: 0; padding-left: 16px; } .callout li { margin-bottom: 3px; }
.row { display: flex; gap: 8px; margin: 4px 0 9px; break-inside: avoid; }
.card { flex: 1; border-top: 3px solid; padding: 6px 9px; font-size: 9pt; }
.ct { font-weight: bold; font-size: 9.5pt; margin-bottom: 4px; }
.card ul { margin: 0; padding-left: 14px; } .card li { margin-bottom: 2px; } .card li.note { list-style: none; margin-left: -14px; }
.tile { text-align: center; } .big { font-size: 20pt; font-weight: bold; }
table { width: 100%; border-collapse: collapse; margin: 4px 0 9px; font-size: 9pt; }
th { background: #${C.navy}; color: #fff; text-align: left; padding: 5px 7px; }
td { border: 1px solid #BFBFBF; padding: 4px 7px; vertical-align: top; } td.b { font-weight: bold; }
tr { break-inside: avoid; }
table.form td { height: 22px; } td.fl { font-weight: bold; color: #${C.navy}; font-size: 8.5pt; }
ol { margin: 0 0 6px; padding-left: 20px; } ol li { margin-bottom: 4px; } ol li::marker { font-weight: bold; color: #${C.navy}; }
ul.list { margin: 0 0 6px; padding-left: 18px; } ul.list li { margin-bottom: 3px; }
.steps { display: flex; align-items: stretch; gap: 4px; margin: 4px 0 6px; break-inside: avoid; }
.step { flex: 1; background: #${C.blue}; padding: 7px; text-align: center; font-size: 8.5pt; display: flex; flex-direction: column; justify-content: center; }
.step b { color: #${E.blue}; font-size: 10pt; margin-bottom: 2px; } .arrow { align-self: center; color: #${E.blue}; }
.sign { display: grid; grid-template-columns: 1fr 1fr; column-gap: 40px; row-gap: 6px; break-inside: avoid; }
.sig { padding-top: 34px; font-size: 9pt; } .sig .sl { border-bottom: 1px solid #404040; margin-bottom: 3px; } .sig span { display: block; }
`;

function writeHtml(d) {
  const html = `<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><title>${d.file}</title><style>${CSS}</style></head><body>${d.blocks.map(toHtml).join('\n')}</body></html>`;
  fs.writeFileSync(path.join(OUT, d.file + '.html'), html);
  fs.writeFileSync(path.join(OUT, d.file + '.footer.txt'), d.footer);
}

(async () => {
  for (const d of docs) { await writeDocx(d); writeHtml(d); }
  console.log('ok');
})();
