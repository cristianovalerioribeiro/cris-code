#!/usr/bin/env python3
"""
Extrai os SVG dos icones MDI usados pelo painel para tools/icones.json.

    npm pack @mdi/js@7.4.47 && tar xzf mdi-js-7.4.47.tgz
    python3 tools/extrair_icones.py package/mdi.js

So os icones realmente usados sao guardados, para a pre-visualizacao
funcionar offline sem carregar uma biblioteca inteira.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
SAIDA = RAIZ / "tools" / "icones.json"

# Icones que a pre-visualizacao usa mesmo que nao apareçam no config.
SEMPRE = """
mdi:home mdi:home-heart mdi:lightbulb mdi:lightbulb-outline mdi:lightbulb-group
mdi:lightbulb-off-outline mdi:lightbulb-on mdi:ceiling-light mdi:floor-lamp
mdi:wall-sconce-flat mdi:led-strip-variant mdi:sofa mdi:countertop mdi:bed-double
mdi:bed-single mdi:desk mdi:shower mdi:tree mdi:thermostat mdi:gauge
mdi:dots-horizontal mdi:window-shutter mdi:window-shutter-open mdi:curtains
mdi:blinds-horizontal mdi:thermometer mdi:water-percent mdi:motion-sensor
mdi:window-closed-variant mdi:door mdi:gas-cylinder mdi:air-conditioner
mdi:fan mdi:television mdi:coffee-maker mdi:power mdi:chevron-right
mdi:arrow-up mdi:arrow-down mdi:stop mdi:palette mdi:brightness-6
mdi:eye mdi:toggle-switch-variant mdi:sofa-outline
""".split()


def camel(nome: str) -> str:
    partes = nome.removeprefix("mdi:").split("-")
    return "mdi" + "".join(p.capitalize() for p in partes)


def main(argv: list[str]) -> int:
    if len(argv) < 2:
        print("uso: extrair_icones.py CAMINHO/mdi.js", file=sys.stderr)
        return 2
    fonte = Path(argv[1])
    if not fonte.exists():
        print(f"erro: {fonte} nao encontrado", file=sys.stderr)
        return 2

    bruto = fonte.read_text(encoding="utf-8")
    caminhos = dict(re.findall(r'export var (mdi\w+) = "([^"]+)"', bruto))

    usados = set(SEMPRE)
    for arq in (RAIZ / "config").glob("*.yaml"):
        usados |= set(re.findall(r"mdi:[a-z0-9-]+", arq.read_text(encoding="utf-8")))
    for arq in (RAIZ / "tools").glob("*.py"):
        usados |= set(re.findall(r"mdi:[a-z0-9-]+", arq.read_text(encoding="utf-8")))

    saida, faltando = {}, []
    for nome in sorted(usados):
        d = caminhos.get(camel(nome))
        if d:
            saida[nome] = d
        else:
            faltando.append(nome)

    SAIDA.write_text(json.dumps(saida, indent=0, sort_keys=True), encoding="utf-8")
    print(f"gravado: {SAIDA.relative_to(RAIZ)} ({len(saida)} icones, {SAIDA.stat().st_size} bytes)")
    if faltando:
        print("nao encontrados em @mdi/js: " + ", ".join(faltando), file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
