# Home solta

`index.html` é a home do site: uma página única em capítulos (hero, história, modelagem 3D, por que modelar,
vertentes, por onde começar, método, ao seu lado, quem, perguntas, contato). Veio do artefato
https://claude.ai/artifact/XWjSjAxnPVr2FE8mbRHekM e foi adaptada: fontes locais (Manrope e Inter em
`assets/fonts/`), cena 3D e modelagem pelos arquivos `assets/js/cena3d.js` e `assets/js/modelagem.js`
(em vez de cópias inline), cabeçalho de SEO preenchido pelo `build.py`.

O `build.py` publica este arquivo na raiz (`/`) e move a home gerada das páginas para `/anterior/`
(noindex), para comparação. Marcadores que o build preenche: `{{ROBOTS}}`, `{{DOMINIO}}`, `{{JSON_LD}}`.
