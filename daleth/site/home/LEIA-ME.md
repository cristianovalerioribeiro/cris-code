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
