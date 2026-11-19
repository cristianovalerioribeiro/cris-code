# Guia de redação dos capítulos (livro em PDF)

O livro "Símbolos de proteção, limpeza e prosperidade para a porta de casa" é montado por `build.py` a partir de fragmentos HTML em `reports/build/chapters/NN_nome.html`. Cada fragmento é UM capítulo. O leitor é um pesquisador brasileiro exigente, que confronta bibliografias; quer profundidade, precisão e didática.

## Regras de conteúdo (inegociáveis)

1. Escreva em português do Brasil, prosa clara e didática: explique cada termo técnico na primeira vez, dê o porquê de cada regra, use exemplos concretos. Frases completas; nada de estilo telegráfico.
2. Só afirme como fato o que as notas verificadas marcam [LIDO NA FONTE]. O que é [SÓ BUSCA] pode entrar com a ressalva "segundo trecho de busca, não conferido no original". O que é [NÃO VERIFICADO] só entra se for indispensável, e sempre com `<span class="nv">(não verificado no original)</span>`.
3. Nunca invente citação literal, página, data, autor ou URL. Citações literais só as que estão nas notas verificadas, com a referência exata que elas dão.
4. Separe sempre três camadas: o que a fonte primária/acadêmica atesta; o costume popular documentado; a leitura esotérica moderna (com autor e data de quem a criou).
5. Registre divergências entre autores com nomes: quem diz o quê.
6. Não prometa eficácia. Descreva o que cada tradição afirma, com verbos como "atribui-se", "a tradição afirma", "o texto promete".
7. Respeite práticas fechadas (mezuzá, pontos riscados, tronqueira, objetos consagrados): descreva e explique, não ensine a reproduzir. Não desenhe nem reproduza pontos riscados de entidades específicas.
8. Não ensine a desenhar símbolos de ódio como decoração; os alertas ficam claros.
9. Cada capítulo deve ser substancial (em geral 2.500 a 4.500 palavras), com fichas para cada símbolo relevante.
10. Use as correções listadas ao fim das notas verificadas ("Correções à rodada anterior"): elas prevalecem sobre o relatório antigo em `reports/Símbolos de proteção para a porta.md`, que serve só de pano de fundo.

## Estrutura do fragmento

Não inclua `<html>`, `<head>`, `<body>` nem `<section>`; o script acrescenta. Comece assim:

```html
<h1>Título do capítulo</h1>
<p class="lead">Uma ou duas frases que dizem a conclusão principal do capítulo.</p>
<h2>Seção</h2>
<p>…</p>
```

Use `<h2>` para seções (entram no sumário), `<h3>` para subseções. Não numere títulos à mão.

### Componentes disponíveis (classes CSS já definidas)

- Etiquetas de classificação, sempre junto ao nome do símbolo:
  `<span class="tag atestado">Atestado</span>` (fonte primária, arqueológica ou acadêmica),
  `<span class="tag costume">Costume popular</span>`,
  `<span class="tag moderno">Moderno</span>` (séculos XIX–XXI),
  `<span class="tag fechada">Prática fechada</span>`, `<span class="tag aberto">Aberto</span>`, `<span class="tag orientacao">Pede orientação</span>`;
  funções: `<span class="tag protecao">Proteção</span>`, `<span class="tag limpeza">Limpeza</span>`, `<span class="tag prosperidade">Prosperidade</span>`.
- Ficha de símbolo (use uma por símbolo importante):

```html
<div class="ficha">
  <h3>Nome do símbolo <span class="tag atestado">Atestado</span> <span class="tag protecao">Proteção</span></h3>
  <dl>
    <dt>O que é</dt><dd>…</dd>
    <dt>Fonte</dt><dd>… com <a href="URL">link</a></dd>
    <dt>Na porta</dt><dd>lado, altura, direção — e se há fonte para isso</dd>
    <dt>Datação</dt><dd>…</dd>
    <dt>Leitura moderna</dt><dd>quem criou, quando</dd>
    <dt>Divergências</dt><dd>…</dd>
    <dt>Abertura</dt><dd>aberto / pede orientação / fechado, e por quê</dd>
  </dl>
</div>
```

- Caixas: `<div class="box didatico"><strong>Para entender</strong><p>…</p></div>`; outras variantes: `box atestado`, `box moderno`, `box alerta`, `box fechada`, ou só `box` (nota geral).
- Citação de fonte: `<blockquote class="fonte">texto literal<cite>Autor, obra, referência exata</cite></blockquote>`.
- Tabelas: `<table><thead><tr><th>…</th></tr></thead><tbody>…</tbody></table>` (até 5 colunas; texto curto nas células).
- Hebraico: `<span class="heb">שדי</span>`. Não use caracteres chineses, japoneses, devanágari, tibetanos nem rúnicos Unicode: as fontes do PDF não os têm. Escreva a transliteração (ex.: "Fu", "Om") e, se precisar do desenho, faça em SVG com traços.
- Fim do capítulo: lista das fontes efetivamente usadas:

```html
<div class="fontes"><h3>Fontes deste capítulo</h3><ol>
  <li>Autor, <em>Obra</em>, ano. <a href="URL">URL</a> — lido na íntegra / só trecho de busca.</li>
</ol></div>
```

### Diagramas

Diagramas prontos (use com `<figure class="diagrama"><img src="assets/diagrams/NOME.svg"><figcaption>legenda</figcaption></figure>`):
`futhark.svg` (24 runas com nomes), `geometria.svg` (pentagrama, hexagrama, hexafólio), `quadrados.svg` (SATOR e kamea de Júpiter 4×4), `bagua.svg` (Céu Anterior e Céu Posterior), `leoes.svg` (posição dos leões guardiões vista de cima), `mezuza.svg` (posição e inclinação), `nomes72.svg` (construção dos 72 trigramas), `tres_camadas.svg` (síntese da porta).

Crie de 2 a 4 diagramas NOVOS por capítulo quando ajudarem a entender (esquemas de posição na porta, linhas do tempo de datação, estrutura de um símbolo, tabelas visuais de correspondência). Escreva-os como SVG inline dentro de `<figure class="diagrama">…<figcaption>…</figcaption></figure>`, com `viewBox`, largura até 780, `font-family="DejaVu Sans, sans-serif"`, textos de 9 a 13 px, cores da paleta: tinta `#1d1b18`, vinho `#7a2e1d`, ouro `#a8791f`, verde `#2f6b4a`, azul `#2b4f7a`, roxo `#5a3b7a`, vermelho `#a12a2a`, cinza `#6b645a`, linha `#d9d2c5`, fundo `#fffdf9`. Geometria tem de estar correta e os textos não podem se sobrepor nem sair da área. Confira renderizando: salve o capítulo, rode `cd /home/user/cris-code/reports/build && python3 build.py NN_nome` (gera só a prévia do seu capítulo em `reports/_previa_NN_nome.pdf`; NÃO rode sem argumento, outros redatores trabalham em paralelo) e inspecione as páginas com `pdftoppm -r 60 -png "<pdf>" <scratch>/prefixo` + Read das imagens. Apague a prévia (`_previa_*.html` e `.pdf`) ao terminar. Corrija sobreposições.

### Fotografias

As fotos são inseridas depois por outra etapa. Onde uma fotografia ajudaria, deixe um marcador numa linha própria, descrevendo o que mostrar:

```html
<!--FOTO: mezuzá afixada no umbral de uma porta-->
```

Coloque de 4 a 10 marcadores por capítulo, junto do trecho que a foto ilustra. Temas com foto provável: mezuzá, hamsa, nazar, 72 Nomes (manuscrito), shiviti, cornicello, figa, pedra rúnica, bracteata, Vegvísir (manuscrito Huld), Ægishjálmur, Mjölnir, witch marks/hexafólio entalhado, garrafa de bruxa, ferradura em porta, hex sign, cruz de Brígida, triskelion de Newgrange, giz da Epifania C+M+B, Medalha de São Bento, pia de água benta, Sagrado Coração, Exu/assentamento, espada-de-são-jorge, arruda, guiné, comigo-ninguém-pode, fitas do Bonfim, balangandã, defumador, sal grosso, quadrado SATOR, pantáculo de Salomão (manuscrito), pentagrama de Agrippa/Lévi, udjat, Bes, Abracadabra, gorgoneion, Flor da Vida (Osireion), Sigillum Dei, pêndulo/forquilha de radiestesia, aparelho radiônico, Menshen, Fu invertido, chunlian, leões guardiões, espelho bagua, Shigandang, Pixiu, Jin Chan, Zhong Kui, kolam/rangoli, toran, nimbu-mirchi, drishti bommai, suástica hindu no Diwali, Sri Yantra, Ganesha sobre porta, bandeiras de oração, monograma do Kalachakra, ofuda, shimenawa, kadomatsu, morijio, maneki-neko, shisa, Jano, herma, lamassu, Páscoa/sangue nos umbrais.

## Ao terminar

Devolva: nome do(s) arquivo(s) gravado(s), contagem aproximada de palavras, lista dos diagramas novos e qualquer dúvida de conteúdo que tenha ficado sem fonte.
