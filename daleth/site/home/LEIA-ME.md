# Home solta

`index.html` é a home do site: uma página única em capítulos (hero, história, modelagem 3D, por que modelar,
vertentes, por onde começar, método, ao seu lado, quem, perguntas, contato). Veio do artefato
https://claude.ai/artifact/XWjSjAxnPVr2FE8mbRHekM e foi adaptada: fontes locais (Manrope e Inter em
`assets/fonts/`), cena 3D e modelagem pelos arquivos `assets/js/cena3d.js` e `assets/js/modelagem.js`
(em vez de cópias inline), cabeçalho de SEO preenchido pelo `build.py`.

O `build.py` publica este arquivo na raiz (`/`) e move a home gerada das páginas para `/anterior/`
(noindex), para comparação. Marcadores que o build preenche: `{{ROBOTS}}`, `{{DOMINIO}}`, `{{JSON_LD}}`.

## Versões de teste v3 (07/10/2026)

`home/gerar_v3.py` gera `v3a.html`, `v3b.html` e `v3c.html` a partir de blocos comuns (abertura e tese aprovadas,
cena 3D da modelagem, método, FAQ, conversa) e publica em `/v3a/`, `/v3b/` e `/v3c/` (noindex). Diferem na ordem e
no peso dos capítulos: A direta (7), B narrativa com pontes e "Ao seu lado" (9), C com "o que você recebe" logo após
a tese (8). Para mudar texto, edite o gerador e rode `python3 home/gerar_v3.py` antes do build. O acervo de frases
retiradas está em `home/acervo/`.

## v4 · a partir da mesa de decisão (07/10/2026)

A mesa de decisão (artefato privado no claude.ai) registra, capítulo a capítulo, qual versão entra e o que mudar.
A primeira rodada pediu: hero novo no topo ("Transformamos oportunidades imobiliárias em negócios estruturados para
acontecer.") com os seis eixos como rótulos na cena 3D; barra de prova logo abaixo (R$ 524 mi · 40 operações ·
6.320+ unidades · atuação nacional); tese em A; e a assinatura "Ao seu lado na construção…" movida para depois da
tese, com a palavra construção como chave visual. O mesmo gerador produz `v4.html` (`VERSOES["v4"]`, com
`css_extra`), publicado em `/v4/` (noindex). Os capítulos ainda sem decisão seguem a versão A. Os números da seção
"Quem conduz" foram alinhados aos da barra de prova.

## v5 · reconstrução (07/10/2026, noite)

Segue o PDF "DALETH_Reconstrucao_Homepage_v4" (Drive, pasta 50 BRIEFING NOVO SITE) e os pedidos da mesa: oito
capítulos, Hero → Prova → Tese → Modelagem → Como a DALETH entra → Ao seu lado → Quem está ao seu lado → CTA.
Saem da home a FAQ, os blocos "você recebe", a "conversa de enquadramento" como quinto passo, o fecho do
arquiteto na modelagem, os números repetidos em "Quem" e o slogan no rodapé. "Conduzir" vira "Acompanhar";
papéis: "O cliente decide. A empresa executa. A DALETH estrutura e acompanha." A assinatura fica à esquerda,
depois do método, digita três variações e destaca a final. O CTA único leva a /contato/. Hero com rótulos em
pílulas escuras e pinos à direita do texto. `VERSOES["v5"]` no mesmo gerador, publicado em `/v5/` (noindex).
