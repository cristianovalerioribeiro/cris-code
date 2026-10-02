# Variantes de copy do site DALETH (para escolha do Cristiano)

Três versões completas das 6 páginas centrais, sobre o MESMO layout cinematográfico já aprovado.
Cada variante vive em `variantes/vN/` com os mesmos nomes de arquivo de `paginas/`
(00-inicio, 10-empresas, 20-empreendimentos, 30-capital, 60-como-comeca, 70-sobre).
O build publica as três em /v1/, /v2/ e /v3/, com uma barra para alternar.

## O que NÃO muda (estrutura obrigatória)
- O meta JSON no topo: mesmo `caminho`, mesmos ids de âncora usados por outras páginas
  (/capital/#analise, /capital/#recurso-definido, /capital/#investidor, /empreendimentos/#quando etc.),
  `{{QUADRO}}` e `{{CENARIO}}` onde existem, `"imagem"` no meta, `"scripts"` se houver.
- Na home: a `section.hero-cine` com o `canvas data-cena="heroi"`, a `section.aproxima` com o
  `canvas data-cena="jornada"` e as 3 `.batida`, o `{{QUADRO}}`, a `.vitrine`, os cards de artigo
  (`.artigos-grade`) e o `.fecho` no meta. Pode mudar TODOS os textos dentro deles, os rótulos
  `data-rotulos` dos canvases (6 palavras separadas por |) e a ordem das seções do meio.
- As regras inegociáveis de `docs/COMPONENTES.md` (sem preço, sem promessa, sem GERIC, sem caso
  inventado, sem exclamação, "você", frases curtas).
- CTA principal: cada variante pode propor o seu rótulo, mas use o MESMO em toda a variante.

## O que PODE mudar
- Todo o texto: H1, leads, títulos das seções, parágrafos, FAQs, microcopy, rótulos, fechos.
- A ordem e o número das seções do meio da home (mínimo 6, máximo 9).
- Variações leves de layout via classe no `classe_body` do meta da home: a variante pode pedir
  `"tema-claro-hero"` (hero com fundo névoa e 3D claro) ou `"hero-centrado"` (H1 centralizado e
  3D atrás). O build/CSS já prevê essas duas classes; não invente outras.
- Os rótulos da rede 3D (`data-rotulos`): escolha 6 palavras que contem a história da variante.

## Material
- Textos atuais: `paginas/*.html` (versão em produção, modelo B).
- Caderno de definições: scratchpad `caderno-v02.md`. Relatórios: `docs/revisao-estrutura/09-copy.md`,
  `docs/revisao-layout/45-brand.md`. Componentes: `docs/COMPONENTES.md`.
- Fatos permitidos sobre o Cristiano: engenharia de produção, economia, MBA em gestão de negócios de
  incorporação e construção; atuou nos dois lados do crédito imobiliário (análise e estruturação);
  acompanhou ciclos completos de incorporação. Nada além disso. Sem número de experiência.
- Slogan fixo: "Ao seu lado na construção da sua história." (já sai no topo; não repetir no corpo).

## Conferência
`python3 build.py --local && python3 qa/qa.py` (o QA cobre as variantes). Corrija o que apontar nas suas páginas.
