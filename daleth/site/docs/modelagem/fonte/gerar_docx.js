const fs = require('fs');
const d = require('docx');
const { Document, Packer, Paragraph, TextRun, ImageRun, Table, TableRow, TableCell, WidthType, ShadingType, AlignmentType,
  HeadingLevel, PageBreak, BorderStyle, Header, Footer, PageNumber, LevelFormat, VerticalAlign, TableLayoutType } = d;
const D = JSON.parse(fs.readFileSync('dados.json', 'utf8'));
const MAR = '082538', DOUR = 'B58A44', DOURT = '7A5A28', NEVOA = 'F2F5F8', FIO = 'D3DCE3', GRAF = '47586A', GELO = 'B9C8D4';
const SERIF = 'Georgia', SANS = 'Arial';
const PAGE_W = 11906, PAGE_H = 16838, M = 1134; // A4, 2cm
const CW = PAGE_W - 2 * M; // 9638
const img = (f) => fs.readFileSync(f);
const porId = {}; D.frentes.forEach(f => porId[f.id] = f);
const DEZ = D.frentes.slice(1);

const nada = { style: BorderStyle.NONE, size: 0, color: 'FFFFFF' };
const semBordas = { top: nada, bottom: nada, left: nada, right: nada, insideHorizontal: nada, insideVertical: nada };

function rotulo(t, cor = DOURT, antes = 240) {
  return new Paragraph({ spacing: { before: antes, after: 80 }, children: [new TextRun({ text: t.toUpperCase(), font: SANS, size: 15, bold: true, color: cor, characterSpacing: 40 })] });
}
function h2(t, cor = MAR) {
  return new Paragraph({ heading: HeadingLevel.HEADING_1, spacing: { before: 80, after: 240 }, children: [new TextRun({ text: t, font: SERIF, size: 40, bold: true, color: cor })] });
}
function h3(t, cor = MAR) {
  return new Paragraph({ heading: HeadingLevel.HEADING_2, spacing: { before: 320, after: 120 }, children: [new TextRun({ text: t, font: SERIF, size: 28, bold: true, color: cor })] });
}
function p(t, o = {}) {
  return new Paragraph({ spacing: { after: o.after ?? 160, line: 300 }, alignment: o.align, children: [new TextRun({ text: t, font: o.font || SANS, size: o.size || 21, color: o.cor || '1B2A36', italics: o.it, bold: o.bold })] });
}
function lead(t, cor) { return p(t, { size: 24, cor: cor || '2C3E4E' }); }
function foto(f, wPx, hPx, wTw) { // keep ratio 1.6
  const w = wTw / 1440 * 96, h = w / (wPx / hPx);
  return new Paragraph({ spacing: { after: 160 }, children: [new ImageRun({ type: 'jpg', data: img(f), transformation: { width: Math.round(w), height: Math.round(h) } })] });
}
function celula(children, w, o = {}) {
  return new TableCell({ children, width: { size: w, type: WidthType.DXA }, borders: o.borders || semBordas, verticalAlign: o.va,
    shading: o.fill ? { type: ShadingType.CLEAR, fill: o.fill, color: 'auto' } : undefined,
    margins: { top: o.pad ?? 120, bottom: o.pad ?? 120, left: o.padx ?? 160, right: o.padx ?? 160 } });
}
function grade(linhas, larguras, o = {}) {
  return new Table({ width: { size: larguras.reduce((a, b) => a + b, 0), type: WidthType.DXA }, columnWidths: larguras, layout: TableLayoutType.FIXED,
    borders: semBordas, rows: linhas.map(cels => new TableRow({ children: cels })) });
}
function chips(lista) { // chips as light cells in a wrapping grid: 4 per row
  const porLinha = 4, w = Math.floor(CW / 2 / porLinha) ; const linhas = [];
  for (let i = 0; i < lista.length; i += porLinha) {
    const fatia = lista.slice(i, i + porLinha);
    while (fatia.length < porLinha) fatia.push('');
    linhas.push(fatia.map(t => celula([new Paragraph({ alignment: AlignmentType.CENTER, children: [new TextRun({ text: t, font: SANS, size: 17, color: MAR })] })], w,
      { fill: t ? NEVOA : undefined, pad: 70, padx: 60 })));
  }
  return grade(linhas, Array(porLinha).fill(w));
}
const topBorder = (cor) => ({ top: { style: BorderStyle.SINGLE, size: 12, color: cor }, bottom: nada, left: nada, right: nada });

const secoes = [];
const cab = (txt) => new Header({ children: [new Paragraph({ tabStops: [{ type: 'right', position: CW }], children: [
  new TextRun({ text: 'MODELAGEM DO EMPREENDIMENTO', font: SANS, size: 14, color: '7D8D9B', characterSpacing: 30 }),
  new TextRun({ text: '\t' + txt.toUpperCase(), font: SANS, size: 14, color: '7D8D9B', characterSpacing: 30 })] })] });
const pe = new Footer({ children: [new Paragraph({ border: { top: { style: BorderStyle.SINGLE, size: 4, color: FIO, space: 6 } }, tabStops: [{ type: 'right', position: CW }], children: [
  new TextRun({ text: 'DALETH', font: SANS, size: 14, bold: true, color: '7D8D9B', characterSpacing: 60 }),
  new TextRun({ text: '\t', font: SANS, size: 14 }), new TextRun({ children: [PageNumber.CURRENT], font: SERIF, size: 18, color: DOURT })] })] });
const pagina = (txt, children) => ({ properties: { page: { size: { width: PAGE_W, height: PAGE_H }, margin: { top: M, bottom: M, left: M, right: M, header: 567, footer: 567 } } },
  headers: { default: cab(txt) }, footers: { default: pe }, children });

// Capa
const capa = { properties: { page: { size: { width: PAGE_W, height: PAGE_H }, margin: { top: M, bottom: M, left: M, right: M } } }, children: [
  new Paragraph({ spacing: { after: 400 }, children: [new ImageRun({ type: 'png', data: img('horizontal-color.png'), transformation: { width: 190, height: 50 } })] }),
  new Paragraph({ spacing: { after: 320 }, children: [new ImageRun({ type: 'jpg', data: img('img/capa.jpg'), transformation: { width: 643, height: 402 } })] }),
  rotulo('Método DALETH · 02 · Modelar', DOURT, 200),
  new Paragraph({ spacing: { after: 240 }, children: [new TextRun({ text: 'Modelagem do empreendimento', font: SERIF, size: 72, bold: true, color: MAR })] }),
  lead('Dez frentes, uma decisão. Mudar uma muda as outras. Por isso modelamos antes de escolher.'),
  new Paragraph({ spacing: { before: 600 }, border: { top: { style: BorderStyle.SINGLE, size: 12, color: DOUR, space: 8 } }, children: [new TextRun({ text: 'ESTRUTURAÇÃO DE NEGÓCIOS IMOBILIÁRIOS · BELO HORIZONTE · ATUAÇÃO NACIONAL', font: SANS, size: 15, color: GRAF, characterSpacing: 40 })] }),
] };
secoes.push(capa);

// O que é modelar
const movW = Math.floor(CW / 4);
const movimentos = grade([D.movimentos.map(([n, v, pp]) => celula([
  new Paragraph({ children: [new TextRun({ text: n, font: SANS, size: 14, bold: true, color: '7D8D9B', characterSpacing: 30 })] }),
  new Paragraph({ children: [new TextRun({ text: v, font: SERIF, size: 24, bold: true, color: n === '02' ? DOURT : MAR })] }),
  new Paragraph({ children: [new TextRun({ text: pp, font: SANS, size: 17, color: GRAF })] })], movW, { borders: topBorder(n === '02' ? DOUR : FIO), padx: 80 }))], Array(4).fill(movW));
const camW = Math.floor(CW / 3);
const caminhos = grade([D.caminhos.map(([t, a, b]) => celula([
  new Paragraph({ spacing: { after: 80 }, children: [new TextRun({ text: t, font: SERIF, size: 26, bold: true, color: MAR })] }),
  p(a, { size: 18, after: 60 }), p(b, { size: 18, cor: GRAF, after: 0 })], camW, { fill: NEVOA, borders: { top: nada, bottom: nada, right: nada, left: { style: BorderStyle.SINGLE, size: 18, color: DOUR } } }))], Array(3).fill(camW));
const cadeia = new Paragraph({ spacing: { before: 120, after: 160 }, children: D.cadeia.flatMap((c, i) => [
  new TextRun({ text: c.toUpperCase(), font: SANS, size: 17, bold: true, color: MAR, characterSpacing: 20 }),
  ...(i < D.cadeia.length - 1 ? [new TextRun({ text: '   →   ', font: SANS, size: 20, color: DOUR })] : [])]) });
secoes.push(pagina('O que é modelar', [
  rotulo('O segundo movimento do método', DOURT, 0),
  h2('Modelar é colocar os caminhos lado a lado, com premissas escritas, antes de comprometer capital.'),
  movimentos,
  new Paragraph({ spacing: { after: 120 } }),
  lead('Mapeamos para compreender, modelamos para enxergar, estruturamos para tornar executável, sustentamos para funcionar. Modelar é o movimento que muda o resultado: é quando o empreendimento ainda cabe inteiro numa planilha e qualquer decisão custa pouco para ser revista.'),
  h3('O mesmo terreno gera negócios diferentes'),
  p('Vender, permutar ou incorporar. Uma torre ou duas fases. SPE ou SCP. Crédito de obra ou investidor. Cada escolha move as outras, e todas aparecem no caixa. Comparamos os caminhos pelos mesmos critérios antes de escolher um.'),
  caminhos,
  h3('Cada decisão muda a seguinte'),
  cadeia,
  p('O produto define o orçamento. O orçamento define o caixa. O caixa define o capital necessário, que define o cronograma, que define as vendas. Modelar é enxergar essa cadeia antes que ela aconteça.', { size: 19, cor: GRAF }),
]));

// Conceito visual
const legW = Math.floor(CW / 2);
const metade = Math.ceil(DEZ.length / 2);
const vtW = Math.floor(CW / 3);
const legenda = grade([D.vertentes.map(([v, dsc, ids]) => celula([
  new Paragraph({ spacing: { after: 40 }, children: [new TextRun({ text: v, font: SERIF, size: 23, bold: true, color: MAR })] }),
  p(dsc, { size: 16, cor: GRAF, after: 120 }),
  ...ids.map(id => new Paragraph({ spacing: { after: 60 }, children: [
    new TextRun({ text: porId[id].num + '   ', font: SANS, size: 16, bold: true, color: DOURT }), new TextRun({ text: porId[id].nome, font: SANS, size: 19, color: MAR })] }))
], vtW, { borders: topBorder(DOUR), padx: 80 }))], Array(3).fill(vtW));
secoes.push(pagina('O conceito visual', [
  rotulo('Tudo conectado', DOURT, 0),
  h2('Um empreendimento se decide em dez frentes ao mesmo tempo.'),
  foto('img/tudo.jpg', 2400, 1500, CW),
  h3('Como ler a imagem'),
  p('No centro, o empreendimento. Em volta, uma rede: cada ponto é uma decisão, cada linha é uma consequência. Nenhuma frente está isolada. Puxar uma delas desloca as vizinhas, e o efeito chega ao caixa.'),
  p('Nas páginas seguintes, a rede troca de palavras a cada frente: as decisões que ela carrega e as outras frentes que ela move.'),
  p('As dez frentes se agrupam em três vertentes: empreendimento, empresa e capital. O projeto costuma ficar com o arquiteto, a empresa com o contador, o capital com o banco. Estruturar é decidir as três de uma vez.'),
  rotulo('As dez frentes, por vertente', DOURT, 200),
  legenda,
]));

// Frentes
const meioW = Math.floor(CW / 2) - 100;
DEZ.forEach(f => {
  const [apoio, pergunta] = D.apoio[f.id];
  const move = f.move.map(m => porId[m].nome).join(' · ');
  secoes.push(pagina('Frente ' + f.num + ' de 10', [
    foto('img/' + f.id + '.jpg', 2400, 1500, CW),
    new Paragraph({ spacing: { before: 120, after: 60 }, children: [
      new TextRun({ text: f.num + '  ', font: SERIF, size: 60, bold: true, color: DOUR }),
      new TextRun({ text: f.nome, font: SERIF, size: 44, bold: true, color: MAR })] }),
    new Paragraph({ spacing: { before: 120, after: 240, line: 300 }, indent: { left: 240 }, border: { left: { style: BorderStyle.SINGLE, size: 18, color: DOUR, space: 12 } },
      children: [new TextRun({ text: f.frase, font: SERIF, size: 26, color: MAR })] }),
    grade([[
      celula([rotulo('O que está em jogo', DOURT, 0), p(apoio, { size: 20 }), rotulo('A pergunta que a modelagem responde'), p(pergunta, { font: SERIF, size: 22, it: true, cor: MAR, after: 0 })], meioW, { padx: 0 }),
      celula([rotulo('Decisões desta frente', DOURT, 0), chips(f.sub), rotulo('Também move'), p(move, { size: 21, bold: true, cor: DOURT, after: 0 })], meioW + 200, { padx: 0, va: VerticalAlign.TOP }),
    ]], [meioW, meioW + 200]),
  ]));
});

// Mapa de conexões
const nomeW = 2600, cW = Math.floor((CW - nomeW) / 10);
const cabec = [celula([new Paragraph('')], nomeW), ...DEZ.map(g => celula([new Paragraph({ alignment: AlignmentType.CENTER, children: [new TextRun({ text: g.curto.toUpperCase(), font: SANS, size: 11, bold: true, color: GRAF })] })], cW,
  { borders: { top: nada, left: nada, right: nada, bottom: { style: BorderStyle.SINGLE, size: 6, color: FIO } }, padx: 20, pad: 60 }))];
const linhasMapa = DEZ.map(f => [
  celula([new Paragraph({ children: [new TextRun({ text: f.num + '  ', font: SANS, size: 15, bold: true, color: DOURT }), new TextRun({ text: f.nome, font: SANS, size: 18, color: MAR })] })], nomeW,
    { borders: { top: nada, left: nada, right: nada, bottom: { style: BorderStyle.SINGLE, size: 4, color: FIO } }, padx: 60, pad: 110 }),
  ...DEZ.map(g => celula([new Paragraph({ alignment: AlignmentType.CENTER, children: [new TextRun({ text: f.move.includes(g.id) ? '●' : '', font: SANS, size: 20, color: DOUR })] })], cW,
    { borders: { top: nada, left: nada, right: nada, bottom: { style: BorderStyle.SINGLE, size: 4, color: FIO } }, fill: g.id === f.id ? NEVOA : undefined, padx: 20, pad: 110 }))]);
const leitW = Math.floor(CW / 3);
const leituras = grade([[
  ['O financeiro recebe quase tudo', 'Produto, técnica, tributário, funding e comercialização desembocam no fluxo de caixa. É onde as frentes viram números comparáveis.'],
  ['Um triângulo de estrutura', 'Jurídico, societário e capital se movem juntos. A forma da sociedade define o que pode ser contratado, financiado e garantido.'],
  ['O terreno é o ponto de partida', 'A forma de acesso ao terreno já escolhe produto, base jurídica e necessidade de capital. Modelar começa ali.'],
].map(([t, x]) => celula([new Paragraph({ spacing: { after: 80 }, children: [new TextRun({ text: t, font: SERIF, size: 23, bold: true, color: MAR })] }), p(x, { size: 18, cor: GRAF, after: 0 })], leitW, { borders: topBorder(DOUR), padx: 80 }))], Array(3).fill(leitW));
secoes.push(pagina('Mapa de conexões', [
  rotulo('Quem move quem', DOURT, 0),
  h2('Nenhuma frente se decide sozinha.'),
  lead('Cada linha mostra as frentes que uma decisão move primeiro. Terreno puxa produto, jurídico e capital. Societário puxa tributário, risco e capital. O financeiro recebe quase todas.'),
  grade([cabec, ...linhasMapa], [nomeW, ...Array(10).fill(cW)]),
  p('Leitura: a frente da linha move as frentes marcadas na coluna. As conexões indicadas são as primeiras, não as únicas: na modelagem, todas chegam ao caixa.', { size: 17, cor: GRAF }),
  new Paragraph({ spacing: { after: 200 } }),
  leituras,
]));

// Entrega e convite
const entW = Math.floor(CW / 2);
const entregas = grade([[0, 1], [2, 3]].map(par => par.map(i => celula([
  new Paragraph({ spacing: { after: 80 }, children: [new TextRun({ text: D.entrega[i][0], font: SERIF, size: 26, bold: true, color: DOURT })] }),
  p(D.entrega[i][1], { size: 19, cor: GRAF, after: 0 })], entW, { borders: topBorder(FIO), padx: 80, pad: 160 }))), [entW, entW]);
secoes.push(pagina('O que a modelagem entrega', [
  rotulo('Do mapa ao seu caso', DOURT, 0),
  h2('Modelar é o que separa uma oportunidade de uma decisão.'),
  entregas,
  new Paragraph({ spacing: { before: 400, after: 400, line: 300 }, indent: { left: 240 }, border: { left: { style: BorderStyle.SINGLE, size: 18, color: DOUR, space: 12 } },
    children: [new TextRun({ text: D.papeis, font: SERIF, size: 26, color: MAR })] }),
  grade([[celula([
    new Paragraph({ spacing: { after: 120 }, children: [new TextRun({ text: 'Modelar o seu empreendimento começa com uma conversa', font: SERIF, size: 28, bold: true, color: 'FFFFFF' })] }),
    p('Conte o terreno, o produto ou a empresa. A primeira conversa é de enquadramento, sem custo, e já mostra por quais frentes o seu caso pede para começar.', { size: 21, cor: GELO }),
    new Paragraph({ children: [new TextRun({ text: D.site + '/metodo/modelagem/', font: SANS, size: 19, bold: true, color: 'D4B37C' })] })], CW, { fill: MAR, pad: 400, padx: 400 })]], [CW]),
  new Paragraph({ spacing: { before: 800 }, children: [new ImageRun({ type: 'png', data: img('horizontal-color.png'), transformation: { width: 152, height: 40 } })] }),
  new Paragraph({ spacing: { before: 120 }, children: [new TextRun({ text: D.slogan, font: SERIF, size: 22, italics: true, color: GRAF })] }),
]));

const doc = new Document({
  creator: 'DALETH', title: 'Modelagem do empreendimento', description: 'Dez frentes, uma decisão. Material de apoio do método DALETH.',
  styles: { default: { document: { run: { font: SANS, size: 21 } } },
    paragraphStyles: [
      { id: 'Heading1', name: 'Heading 1', basedOn: 'Normal', next: 'Normal', quickFormat: true, run: { font: SERIF, size: 40, bold: true, color: MAR } },
      { id: 'Heading2', name: 'Heading 2', basedOn: 'Normal', next: 'Normal', quickFormat: true, run: { font: SERIF, size: 28, bold: true, color: MAR } }] },
  sections: secoes,
});
Packer.toBuffer(doc).then(buf => { fs.writeFileSync('DALETH-Modelagem-do-Empreendimento.docx', buf); console.log('docx', (buf.length / 1024 | 0), 'KB'); });
