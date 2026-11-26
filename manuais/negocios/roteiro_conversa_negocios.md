# Roteiro para a próxima conversa (Manual de Radiestesia para Negócios)

Cole o texto abaixo como primeira mensagem de uma conversa nova aberta no repositório `cris-code`.

---

Esta conversa continua o Manual de Radiestesia para Negócios (edição 1, 66 páginas, 60 gráficos, quatorze Partes), feito com o mesmo motor do Manual de Radiestesia Terapêutica. Responda sempre em português. Economize tokens: use o modelo mais leve que resolva cada passo.

## Onde está tudo

- **Google Drive**, pasta `0) CRISTIANO SA / MANUAL_RAD / Radiestesia Empresarial`: os três PDFs (manual, gráficos para impressão, fichas) e, na subpasta `Fontes e notas`, o `negocios_fontes.zip` (pasta `manuais/negocios/` inteira, sem os arquivos gerados pela montagem), o `README_ESTADO.md`, a nota de pesquisa `14_radiestesia_negocios_mapeamento.md` e este roteiro. A pasta `MANUAL_RAD` acima guarda o manual terapêutico (`manuais_fontes.zip`, PDFs e `README_ESTADO.md` dele).
- **Repositório** `cristianovalerioribeiro/cris-code`, ramo `claude/laughing-cerf-dojlh4`, PR nº 3 (rascunho): `manuais/radiestesia/` (terapêutico), `manuais/negocios/` (negócios), `manuais/research_notes/`. Se o ramo não existir mais, extraia os dois zips do Drive na raiz do repositório: `manuais_fontes.zip` cria `manuais/radiestesia/` e `manuais/research_notes/`; `negocios_fontes.zip` cria `manuais/negocios/`.

## Antes de mexer

Leia inteiros `manuais/negocios/README_ESTADO.md` e `manuais/radiestesia/README_ESTADO.md` (regras do motor). Numeração dos gráficos é compartilhada entre os dois manuais: gráfico novo recebe **G138** em diante; cartão novo, **D16**. Desenhos existentes não mudam.

## Montar

Dependências: Python 3 com weasyprint, pymupdf, bs4, pillow, pyphen; fonte Inter. Em `manuais/negocios/`: `python3 gen_charts.py` (precisa de `../radiestesia/charts/` para copiar os gráficos reaproveitados), `python3 build_book.py` (seis passagens, ~8 min), `python3 check_all.py`, `python3 audit_breaks.py`, `python3 build_fichas.py`, `python3 build_print.py` (precisa de `../radiestesia/gen_charts.py` para as listas em paisagem).

## Estado em 26/11/2026

Partes: I fundamentos; II decisão; III a empresa; IV sócios; V propostas; VI projetos e preços; VII pessoas; VIII interferências; IX espaços, ponto, terreno e empreendimento; X finanças; XI a pessoa; XII coaching (rodas, foco, metas, sabotadores, desbloqueio, desafio de 28 dias); XIII estratégia (seletor, carteira, SWOT, funil, abordagem e expectativas, atores e investidores, abrir caminhos e dívida, roda do líder); XIV registro; glossário. Gráficos próprios: G111 a G137. Vetos fixos: nada sobre terceiros sem consentimento, nada de seleção de pessoas, nada de emissor para convencer ou fazer esquecer, nada de promessa de resultado. Pendente: versão Word (pipeline `word/`) e revisão de conteúdo pelo autor antes de imprimir.
