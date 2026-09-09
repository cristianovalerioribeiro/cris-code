# Painel Novo — dashboard responsivo por cômodo (Home Assistant)

Um painel **novo e independente**, criado do zero ao lado do painel existente.
Ele não toca em nada do que você já tem: é adicionado como uma URL separada, você
usa os dois em paralelo e apaga o antigo quando quiser.

## O problema que ele resolve

Cada cômodo tem uma quantidade diferente de luminárias, e listar lâmpada por
lâmpada no YAML significa reeditar o painel toda vez que uma muda de lugar.

Aqui **nenhuma luminária é listada**. Cada cômodo aponta para uma **área** do
Home Assistant e o painel descobre em tempo real todas as luzes daquela área.
Trocou uma lâmpada, adicionou uma arandela, moveu um abajur de cômodo? O painel
já mostra certo no próximo carregamento, sem editar YAML.

## Como o layout se comporta

- **View `sections`** (nativa do HA): as colunas se reorganizam sozinhas conforme
  a largura da tela — 4 colunas no desktop, 1 no celular, sem media query.
- **Cômodo com 1 luminária** ocupa um bloco pequeno; **cômodo com 10** cresce
  verticalmente. Com `dense_section_placement`, os blocos curtos preenchem os
  buracos em vez de deixar espaço morto.
- **Alvos de toque grandes**: cada cômodo tem um card mestre de largura total,
  com o nome, o ícone e o texto "3 de 5 acesa(s)" — dá para ler e acertar o
  toque sem mirar.
- **Controles escondidos quando não servem**: o slider de brilho e a cor só
  aparecem com a luz acesa (`collapsible_controls`), o que deixa a tela limpa.

## As três telas

| Tela | Para quê |
|---|---|
| **Casa** | Visão geral. Um bloco por cômodo, com mestre + grade de luminárias. |
| **Luzes** | Compacta. Por cômodo, uma linha de botões redondos — um por luminária. |
| **&lt;Cômodo&gt;** | Página de detalhe (subview). Iluminação, clima, sensores e o resto da área. |

Toque no card mestre alterna o cômodo inteiro; segure para abrir a página do
cômodo. Toque no título do cômodo também abre a página dele.

## Estrutura do repositório

```
config/comodos.yaml        <- o ÚNICO arquivo que você edita
tools/gerar_painel.py      <- gera o dashboard a partir do config
tools/validar.py           <- confere o YAML gerado antes de colar no HA
dashboards/painel-novo.yaml <- GERADO. não edite à mão
packages/painel_novo.yaml  <- script de apoio (alternância inteligente)
docs/INSTALACAO.md         <- passo a passo de instalação
```

## Uso

```bash
# 1. edite os cômodos
$EDITOR config/comodos.yaml

# 2. gere o painel
python3 tools/gerar_painel.py

# 3. confira antes de colar no Home Assistant
python3 tools/validar.py
```

`config/comodos.yaml` só pede, por cômodo, o **nome exato da área** e um ícone.
Temperatura, umidade e entidades extras (ar-condicionado, ventilador, cortina)
são opcionais.

O gerador recusa configurações quebradas em vez de produzir um painel torto:
área faltando, dois cômodos que gerariam a mesma URL, ou um cômodo com nome
reservado (`Casa`, `Luzes`).

`tools/gerar_painel.py --check` não escreve nada e falha se o YAML gerado estiver
desatualizado em relação ao config — útil para não commitar os dois fora de sincronia.

## Pré-requisitos (HACS)

Instale estes quatro cards em **HACS → Frontend** e recarregue o navegador:

| Card | Repositório | Para quê |
|---|---|---|
| `auto-entities` | thomasloven/lovelace-auto-entities | Descobre as luzes de cada área |
| `Mushroom` | piitaya/lovelace-mushroom | Cards de luz, chips e templates |
| `card-mod` | thomasloven/lovelace-card-mod | Dependência do Mushroom |

E, opcionalmente, o package `packages/painel_novo.yaml` — ver
[docs/INSTALACAO.md](docs/INSTALACAO.md).

Requer Home Assistant **2024.11 ou mais novo** (views `sections`, card `heading`
com badges, `grid_options`, sintaxe `perform-action`).
