# Instalação passo a passo

O painel é **adicionado ao lado** do que você já tem. Nada do painel atual é
alterado, sobrescrito ou removido.

---

## 1. Instale os cards no HACS

**HACS → Frontend → Explorar e baixar repositórios**, e baixe:

- `auto-entities` (thomasloven/lovelace-auto-entities)
- `Mushroom` (piitaya/lovelace-mushroom)
- `card-mod` (thomasloven/lovelace-card-mod)

Depois **recarregue o navegador com Ctrl+Shift+R** (ou limpe o cache do app).
Se um card não estiver instalado, o painel mostra um retângulo vermelho no lugar
dele — o resto continua funcionando.

---

## 2. Confira os nomes das áreas

O painel liga cada cômodo a uma **área** do Home Assistant, pelo nome exato.

Vá em **Ferramentas de Desenvolvedor → Modelo** e cole:

```jinja
{% for a in areas() %}
{{ area_name(a) }}  ->  {{ a }}  ->  {{ area_entities(a) | select('match', 'light\.') | list | count }} luz(es)
{% endfor %}
```

O resultado mostra, para cada área: **nome**, **id** e **quantas luzes** ela tem.

- A coluna do **nome** é o que vai em `area:` no `config/comodos.yaml`.
- Se alguma área mostrar **0 luzes** mas você sabe que tem, as lâmpadas não
  estão atribuídas àquela área — corrija em **Configurações → Áreas** ou nas
  próprias entidades. É aí que o painel busca.

---

## 3. Instale o package (recomendado)

Ele dá o comportamento "apaga tudo se tiver alguma acesa, senão acende tudo" no
card mestre de cada cômodo.

Em `configuration.yaml`:

```yaml
homeassistant:
  packages: !include_dir_named packages
```

Copie `packages/painel_novo.yaml` para `<config>/packages/painel_novo.yaml` e
**reinicie o Home Assistant**.

> **Sem package?** Coloque `usar_script_inteligente: false` em
> `config/comodos.yaml` e rode `python3 tools/gerar_painel.py` de novo. O painel
> passa a usar `light.toggle`, que com metade das luzes acesas inverte cada uma
> em vez de apagar todas. Nesse modo o `area_id` importa: se o id da sua área não
> for o nome "slugificado" (`Sala de Estar` → `sala_de_estar`), informe o
> `area_id:` real no config, usando a saída do passo 2.

---

## 4. Crie um grupo de luz por cômodo (só se as lâmpadas forem dimerizáveis)

> **Pule este passo** se as suas lâmpadas são comuns de liga/desliga, que é o
> padrão deste repositório (`brilho: nunca`). O card mestre já acende e apaga o
> cômodo inteiro sem grupo nenhum; o grupo só acrescentaria um slider de brilho
> que as suas lâmpadas não usam.


**Configurações → Dispositivos e serviços → Ajudantes → Criar ajudante → Grupo
→ Grupo de luzes.** Selecione as luminárias do cômodo e dê um nome
(ex.: `Luzes da sala`).

Informe a entidade resultante em `grupo:` no config. O card mestre daquele
cômodo deixa de ser só um contador e vira um controle de verdade, com **slider
de brilho, temperatura de cor e roda de cores do cômodo inteiro**.

Sem `grupo:`, o mestre ainda funciona — mostra "3 de 5 acesas" e alterna tudo no
toque — mas sem os controles de brilho e cor.

> Não precisa listar as luminárias no painel por causa disso: o grupo é só para
> o controle mestre. As luminárias individuais continuam sendo descobertas
> sozinhas pela área.

---

## 5. Ajuste os cômodos e gere o painel

```bash
$EDITOR config/comodos.yaml     # um bloco por cômodo
python3 tools/gerar_painel.py   # gera dashboards/painel-novo.yaml
python3 tools/validar.py        # confere o YAML
python3 tools/preview.py        # veja como ficou antes de instalar
```

`tools/preview.py` abre nada e instala nada: ele grava HTML e PNG em `preview/`.
Abra `preview/casa-1440.html` no navegador para navegar, ou olhe os PNGs.

Para a pré-visualização refletir a **sua** casa, edite
`config/casa_exemplo.yaml` com as suas áreas e entidades.

---

## 6. Registre o painel novo no Home Assistant

Escolha **uma** das duas formas.

### Forma A — pela interface (mais simples)

1. **Configurações → Painéis → + Adicionar painel → Novo painel do zero**
2. Dê o título `Casa` e **anote a URL** que ele criar.
3. Abra o painel → menu ⋮ → **Editar painel** → ⋮ → **Editor de YAML bruto**.
4. Apague o conteúdo e cole **tudo** de `dashboards/painel-novo.yaml`.
5. Salve.

> A URL precisa bater com `painel.url` do `config/comodos.yaml` (padrão:
> `painel-novo`), senão os toques que abrem a página do cômodo dão 404. Se a URL
> criada for outra, ajuste `painel.url`, regere e cole de novo.

### Forma B — por YAML (versionado no git)

Em `configuration.yaml`:

```yaml
lovelace:
  mode: storage          # mantém o painel ATUAL funcionando como está
  dashboards:
    painel-novo:
      mode: yaml
      title: Casa
      icon: mdi:home-heart
      show_in_sidebar: true
      filename: dashboards/painel-novo.yaml
```

Copie `dashboards/painel-novo.yaml` para `<config>/dashboards/painel-novo.yaml`
e reinicie. Depois disso, cada vez que regerar o arquivo basta recarregá-lo em
**Ferramentas de Desenvolvedor → YAML → Recarregar dashboards do Lovelace** —
sem reiniciar.

A Forma B é a que permite versionar o painel neste repositório.

---

## Se algo não aparecer

| Sintoma | Causa provável |
|---|---|
| Cômodo aparece, mas sem nenhuma luminária | As luzes não estão atribuídas àquela área (passo 2) |
| Retângulo vermelho "Custom element doesn't exist" | Card do HACS faltando ou navegador com cache — Ctrl+Shift+R |
| Card mestre não faz nada ao tocar | Package não instalado; use `usar_script_inteligente: false` |
| Tocar no cômodo dá 404 | `painel.url` diferente da URL real do painel |
| Uma luz aparece duplicada | É um grupo de luz; adicione o `entity_id` em `globais.excluir_luzes` (o grupo indicado em `grupo:` já é excluído sozinho) |
| Título "Sensores"/"Clima"/"Mídia" vazio na página do cômodo | Normal: o título é fixo, a lista some quando a área não tem nada daquele tipo |
| Cômodos fora de ordem no desktop | É o empacotamento denso preenchendo os vãos. Use `densidade: false` para a ordem exata do config |
| Tela principal muito alta | Ponha `cor_na_tela_inicial: false`, ou `estilo_luzes: botoes` se você tinha mudado para `cards` |
| Mestre do cômodo sem slider de brilho | Esperado com `brilho: nunca`. Com `brilho: auto`, falta o `grupo:` daquele cômodo — ver passo 4 |
| Porcentagem aparecendo numa lâmpada que não dimeriza | O Home Assistant mostra o estado que a lâmpada reporta. Se ela reporta brilho mas você não usa, `brilho: nunca` tira os controles |
| Caixas grandes e vazias ao lado dos cards de luz | `brilho: auto` com `colunas_luzes: 2`. Use `colunas_luzes: 1`, ou `brilho: nunca` |
