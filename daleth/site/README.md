# Site DALETH · reconstrução do zero (outubro de 2026)

Site institucional da DALETH, Estruturação de Negócios Imobiliários. Substitui o
site v12 (gerado por `site_build.py`) mantendo os textos já aprovados e corrigindo
os erros estruturais apontados pelas três revisões de 30/09.

Hoje no ar, em prévia: https://daleth.iajudite.com.br (com `noindex`).

## Como rodar

```bash
cd daleth/site
python3 build.py            # produção: gera dist/ com URLs limpas
python3 build.py --local    # prévia: links relativos, abre direto do disco
python3 qa/qa.py            # QA (depois do --local); precisa de: pip install playwright
```

Só a biblioteca padrão do Python para gerar. No Netlify, o `netlify.toml` já
aponta o build e a pasta `dist/`.

## Onde mexer

| Quero mudar | Arquivo |
|---|---|
| Texto de uma página | `paginas/NN-nome.html` (metadados no topo, conteúdo abaixo) |
| Cabeçalho, menu, rodapé, slogan, fecho | `build.py` |
| Visual | `assets/site.css` |
| Simulador | `assets/js/ferramentas.js` **e** `modelo.py` (são gêmeos; o QA confere) |
| Cenário do hero | `cenario.py` |
| Sair da prévia / ligar o formulário | `PREVIA` e `FORMULARIO_ATIVO` no topo do `build.py` |
| Ordem das vertentes no menu | `VERTENTES` no `build.py` |

Nunca editar `dist/` à mão: é saída do build.

## As páginas

| Endereço | Página |
|---|---|
| `/` | Início |
| `/empresas/` | Empresas |
| `/empreendimentos/` | Empreendimentos |
| `/empreendimentos/terreno/` | Vender, permutar ou incorporar |
| `/empreendimentos/simulador/` | Simulador de exposição de caixa |
| `/empreendimentos/obra-parada/` | Obras paradas |
| `/capital/` | Capital |
| `/metodo/` | Método |
| `/repertorio/` | As nove modelagens |
| `/como-comeca/` | Como começa (substitui `/setup/`) |
| `/sobre/` | Sobre e quem conduz |
| `/contato/` e `/contato/recebido/` | Contato |
| `404.html` | Página não encontrada |

Os endereços antigos (`/terreno/`, `/simulador/`, `/obra-parada/`, `/setup/`,
`/recebido/`) redirecionam com 301 (`_redirects`).

## O que mudou em relação ao v12

1. **A home gira em torno do MODELAR**, o único diferencial que a pesquisa de 63
   concorrentes confirmou como inexistente no mercado. Logo depois do hero vem um
   quadro com o mesmo empreendimento em quatro estruturas de capital, com os
   números calculados pelo modelo do simulador no build (nada escrito à mão).
2. **A porta de entrada está na 3ª seção**, e não na 7ª.
3. **O cliente é nomeado no texto visível**: construtoras e incorporadoras.
4. **Afirmação em vez de negação**: os blocos "o que não somos" viraram texto
   afirmativo; a frase de categoria aprovada aparece uma vez só, em /sobre/.
5. **Fechos diferentes em cada página**; as três garantias aparecem só onde pesam.
6. **Migalhas visíveis** e coerentes com a arquitetura: terreno, simulador e obra
   parada vivem dentro de Empreendimentos, também no endereço.
7. **Frases que colidiam com concorrentes** saíram ("Potencial não basta",
   "Um empreendimento começa antes da obra", "Ficamos até funcionar").
8. **Remuneração fora do site**: saiu a FAQ de Capital que citava acompanhamento
   mensal e percentual de êxito.
9. **Atuação nacional** com base em Belo Horizonte (decisão do Caderno §01).
10. **Impressão** com regras próprias (sem branco sobre branco), títulos com
    tamanho mínimo, `scroll-padding-top` para as âncoras e menu mobile que deixa o
    resto da página inerte.

## Regras inegociáveis (resumo do briefing de 30/09)

- Nunca: parecer assinado, laudo, veredito; prometer crédito, captação ou retorno;
  "assumimos a execução"; preço ou modelo de remuneração; "cobramos do cliente,
  nunca do banco"; "Setup de Estruturação"; chave religiosa ou esotérica; inventar
  caso, número, depoimento, preço ou prazo.
- Regra-mãe: partir da ambição do cliente, e não da deficiência.
- Slogan "Ao seu lado na construção da sua história." no topo de todas as páginas.
- Etimologia do nome só em /sobre/, em uso moderado.

O `qa/qa.py` procura esses termos no texto visível de todas as páginas.

Decisões ainda em aberto: ver [PENDENCIAS.md](PENDENCIAS.md).
