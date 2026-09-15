#!/usr/bin/env python3
"""
Descobre os entity_id reais da sua casa.

    python3 tools/descobrir.py            # imprime o template para colar no HA
    python3 tools/descobrir.py --testar   # confere o template contra a casa de exemplo

Como usar:

  1. Rode o comando e copie o template inteiro.
  2. No Home Assistant: Ferramentas de Desenvolvedor > Modelo.
  3. Cole no campo da esquerda. O resultado aparece a direita.
  4. Copie o resultado e salve em config/casa_exemplo.yaml.

A partir dai a pre-visualizacao passa a ser a SUA casa, e o
tools/conferir_blocos.py passa a conferir os padroes de 'luzes:' contra os
seus entity_id de verdade — e a dizer qual bloco ficou vazio porque o rele
ainda nao foi identificado.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))
from ha_mock import Casa  # noqa: E402

RAIZ = Path(__file__).resolve().parent.parent

DOMINIOS = ("light", "cover", "sensor", "binary_sensor",
            "climate", "fan", "media_player", "switch", "lock")

TEMPLATE = """\
{%- set dominios = ['""" + "', '".join(DOMINIOS) + """'] -%}
areas:
{%- for a in areas() %}
{%- set itens = area_entities(a) | select('match', '(' ~ dominios | join('|') ~ ')\\\\.') | sort | list %}
{%- if itens %}
  "{{ area_name(a) }}":
{%- for e in itens %}
{%- set modos = state_attr(e, 'supported_color_modes') or [] %}
    - {id: {{ e }}, nome: "{{ (state_attr(e, 'friendly_name') or e) | replace('"', '') }}", estado: "{{ states(e) }}"
      {#- #}{% if state_attr(e, 'unit_of_measurement') %}, unidade: "{{ state_attr(e, 'unit_of_measurement') }}"{% endif %}
      {#- #}{% if state_attr(e, 'device_class') %}, classe: {{ state_attr(e, 'device_class') }}{% endif %}
      {#- #}{% if state_attr(e, 'current_position') is not none %}, posicao: {{ state_attr(e, 'current_position') }}{% endif %}
      {#- #}{% if e.startswith('light.') and modos and modos != ['onoff'] %}, dimeriza: true{% endif %}}
{%- endfor %}
{%- endif %}
{%- endfor %}
"""

RESUMO = """\
{%- for a in areas() %}
{{ area_name(a) }} -> {{ a }} -> {{ area_entities(a) | select('match', 'light\\\\.') | list | count }} luz(es)
{%- endfor %}
"""


def testar() -> int:
    """Roda o template contra a casa de exemplo e confere se o YAML volta igual."""
    origem = RAIZ / "config" / "casa_exemplo.yaml"
    casa = Casa.carregar(origem)
    saida = casa.ambiente().from_string(TEMPLATE).render()

    try:
        voltou = yaml.safe_load(saida)
    except yaml.YAMLError as exc:
        print("erro: o template gerou YAML invalido:", exc, file=sys.stderr)
        print("\n--- saida ---\n" + saida, file=sys.stderr)
        return 1

    esperado = yaml.safe_load(origem.read_text(encoding="utf-8"))
    n_orig = sum(len(v) for v in esperado["areas"].values())
    n_novo = sum(len(v) for v in (voltou or {}).get("areas", {}).values())

    print(f"areas: {len(esperado['areas'])} -> {len((voltou or {}).get('areas', {}))}")
    print(f"entidades: {n_orig} -> {n_novo}")

    problemas = []
    for area, itens in esperado["areas"].items():
        novos = {i["id"]: i for i in (voltou or {}).get("areas", {}).get(area, [])}
        for it in itens:
            n = novos.get(it["id"])
            if n is None:
                problemas.append(f"{it['id']} nao voltou")
            elif n.get("nome") != it.get("nome"):
                problemas.append(f"{it['id']}: nome '{n.get('nome')}' != '{it.get('nome')}'")
    for p in problemas[:10]:
        print("  divergencia:", p, file=sys.stderr)
    if problemas:
        print(f"erro: {len(problemas)} divergencia(s)", file=sys.stderr)
        return 1
    print("ok: o template reproduz a casa de exemplo sem perder nada")
    return 0


def main(argv=None) -> int:
    p = argparse.ArgumentParser(description="Descobre os entity_id da sua casa.")
    p.add_argument("--testar", action="store_true",
                   help="roda o template contra a casa de exemplo")
    p.add_argument("--resumo", action="store_true",
                   help="imprime um template curto: area, id e numero de luzes")
    args = p.parse_args(argv)

    if args.testar:
        return testar()

    if args.resumo:
        print("# Cole em Ferramentas de Desenvolvedor > Modelo para ver as areas:\n")
        print(RESUMO)
        return 0

    print("# ============================================================")
    print("# Cole em: Home Assistant > Ferramentas de Desenvolvedor > Modelo")
    print("# Copie o RESULTADO e salve em config/casa_exemplo.yaml")
    print("# ============================================================\n")
    print(TEMPLATE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
