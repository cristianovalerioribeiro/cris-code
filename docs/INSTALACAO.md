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

## 4. Ajuste os cômodos e gere o painel

```bash
$EDITOR config/comodos.yaml     # um bloco por cômodo
python3 tools/gerar_painel.py   # gera dashboards/painel-novo.yaml
python3 tools/validar.py        # confere antes de colar
```

---

## 5. Registre o painel novo no Home Assistant

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
| Uma luz aparece duplicada | É um grupo de luz; adicione o `entity_id` em `globais.excluir_luzes` |
| Título "Sensores"/"Outros" vazio na página do cômodo | Normal: o título é fixo, a lista some quando a área não tem nada daquele tipo |
