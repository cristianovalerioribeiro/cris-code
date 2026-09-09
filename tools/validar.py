#!/usr/bin/env python3
"""
Confere o dashboard gerado antes de voce colar no Home Assistant.

    python3 tools/validar.py [ARQUIVO]

Verifica:
  * o YAML e valido;
  * todos os caminhos de view sao unicos (paths duplicados quebram a navegacao);
  * todo navigation_path aponta para uma view que existe;
  * todos os templates Jinja compilam;
  * so sao usados custom cards conhecidos (evita erro de digitacao no HACS).
"""

from __future__ import annotations

import sys
from pathlib import Path

import yaml
from jinja2 import Environment
from jinja2 import TemplateSyntaxError

RAIZ = Path(__file__).resolve().parent.parent
PADRAO = RAIZ / "dashboards" / "painel-novo.yaml"

# Custom cards que este painel usa. Cada um precisa estar instalado via HACS.
CARDS_CONHECIDOS = {
    "custom:auto-entities",
    "custom:mushroom-light-card",
    "custom:mushroom-template-card",
    "custom:mushroom-chips-card",
    "custom:mushroom-cover-card",
}

# Filtros/funcoes do Home Assistant que o Jinja puro nao conhece.
EXTRAS_HA = {
    "area_entities": lambda *a: [],
    "states": {},
    "is_state": lambda *a: False,
    "expand": lambda *a: [],
}


def caminhar(no, trilha="raiz"):
    """Gera (trilha, chave, valor) para cada par chave/valor da arvore."""
    if isinstance(no, dict):
        for k, v in no.items():
            yield trilha, k, v
            yield from caminhar(v, f"{trilha}.{k}")
    elif isinstance(no, list):
        for i, v in enumerate(no):
            yield from caminhar(v, f"{trilha}[{i}]")


def main(argv: list[str]) -> int:
    alvo = Path(argv[1]) if len(argv) > 1 else PADRAO
    if not alvo.exists():
        print(f"erro: arquivo nao encontrado: {alvo}", file=sys.stderr)
        return 2

    try:
        dash = yaml.safe_load(alvo.read_text(encoding="utf-8"))
    except yaml.YAMLError as exc:
        print(f"erro: YAML invalido: {exc}", file=sys.stderr)
        return 1

    problemas: list[str] = []
    views = (dash or {}).get("views") or []
    if not views:
        problemas.append("nenhuma view encontrada")

    # 1. paths unicos
    paths: list[str] = []
    for v in views:
        p = v.get("path")
        if not p:
            problemas.append(f"view '{v.get('title')}' sem 'path'")
        elif p in paths:
            problemas.append(f"path duplicado: '{p}'")
        else:
            paths.append(p)

    # 2. navigation_path aponta para view existente
    for trilha, chave, valor in caminhar(dash):
        if chave == "navigation_path" and isinstance(valor, str):
            destino = valor.rstrip("/").rsplit("/", 1)[-1]
            if destino and destino not in paths:
                problemas.append(f"{trilha}: navigation_path '{valor}' nao existe no painel")

    # 3. templates Jinja compilam
    env = Environment()
    for nome in EXTRAS_HA:
        env.globals[nome] = EXTRAS_HA[nome]
    env.filters.setdefault("is_state", lambda *a: False)
    env.tests.setdefault("is_state", lambda *a: False)
    env.filters.setdefault("match", lambda *a: False)
    env.tests.setdefault("match", lambda *a: False)

    n_templates = 0
    for trilha, chave, valor in caminhar(dash):
        if isinstance(valor, str) and ("{{" in valor or "{%" in valor):
            n_templates += 1
            try:
                env.parse(valor)
            except TemplateSyntaxError as exc:
                problemas.append(f"{trilha}.{chave}: template invalido — {exc}")

    # 4. custom cards conhecidos
    usados = set()
    for _, chave, valor in caminhar(dash):
        if chave == "type" and isinstance(valor, str) and valor.startswith("custom:"):
            usados.add(valor)
    for card in sorted(usados - CARDS_CONHECIDOS):
        problemas.append(f"custom card desconhecido: {card}")

    if problemas:
        for p in problemas:
            print(f"erro: {p}", file=sys.stderr)
        return 1

    print(f"ok: {alvo.name}")
    print(f"  {len(views)} view(s), {len(paths)} caminho(s) unico(s)")
    print(f"  {n_templates} template(s) Jinja compilam")
    print(f"  custom cards usados: {', '.join(sorted(usados)) or 'nenhum'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
