#!/usr/bin/env python3
"""
Mostra quais luminarias cada bloco do painel realmente pega.

    python3 tools/conferir_blocos.py

Roda os filtros do painel contra config/casa_exemplo.yaml e lista, bloco por
bloco, as luzes que caem nele. E como conferir se 'luzes:' e 'excluir:'
separaram o que deviam — por exemplo, se a Lavanderia saiu da Cozinha.

Avisa quando:
  * um bloco fica sem nenhuma luz (padrao errado, ou rele nao identificado);
  * uma luz aparece em dois blocos (falta um 'excluir:' no bloco principal);
  * uma luz da casa nao aparece em bloco nenhum (esquecida no painel).
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))
from ha_mock import Casa  # noqa: E402
from ha_mock import expandir_auto_entities  # noqa: E402

RAIZ = Path(__file__).resolve().parent.parent


def blocos_do_painel(dash: dict) -> list[tuple[str, str, list[str]]]:
    """(pavimento, bloco, entity_ids) para cada secao das views de pavimento."""
    saida = []
    for view in dash.get("views") or []:
        if view.get("subview") or view.get("path") in ("casa", "luzes"):
            continue
        for secao in view.get("sections") or []:
            cards = secao.get("cards") or []
            nome = next((c.get("heading") for c in cards if c.get("type") == "heading"), "?")
            auto = next((c for c in cards if c.get("type") == "custom:auto-entities"
                         and any(r.get("domain") == "light"
                                 for r in (c.get("filter") or {}).get("include") or [])), None)
            saida.append((view.get("title", "?"), nome, auto))
    return saida


def main(argv=None) -> int:
    p = argparse.ArgumentParser(description="Confere os filtros de luz dos blocos.")
    p.add_argument("--painel", type=Path, default=RAIZ / "dashboards" / "painel-novo.yaml")
    p.add_argument("--casa", type=Path, default=RAIZ / "config" / "casa_exemplo.yaml")
    args = p.parse_args(argv)

    dash = yaml.safe_load(args.painel.read_text(encoding="utf-8"))
    casa = Casa.carregar(args.casa)

    todas = {e.entity_id for e in casa.entidades if e.dominio == "light"}
    usadas: dict[str, list[str]] = {}
    vazios: list[str] = []
    pav_atual = None

    for pav, nome, auto in blocos_do_painel(dash):
        if pav != pav_atual:
            print(f"\n=== {pav} ===")
            pav_atual = pav
        if auto is None:
            print(f"  {nome:26} (sem filtro de luz)")
            continue
        interno = expandir_auto_entities(auto, casa)
        ids = [c["entity"] for c in (interno or {}).get("chips", [])
               + (interno or {}).get("cards", [])]
        for i in ids:
            usadas.setdefault(i, []).append(nome)
        if not ids:
            vazios.append(nome)
            print(f"  {nome:26} VAZIO")
        else:
            nomes = ", ".join(casa.por_id[i].name for i in ids)
            print(f"  {nome:26} {len(ids)}x  {nomes}")

    print()
    problemas = 0
    for nome in vazios:
        print(f"aviso: bloco '{nome}' nao pegou nenhuma luz — confira 'luzes:'")
        problemas += 1
    for eid, onde in sorted(usadas.items()):
        if len(onde) > 1:
            print(f"aviso: {eid} aparece em {len(onde)} blocos ({', '.join(onde)}) — "
                  "falta 'excluir:' no principal")
            problemas += 1
    for eid in sorted(todas - set(usadas)):
        print(f"aviso: {eid} ({casa.por_id[eid].name}) nao aparece em nenhum bloco")
        problemas += 1

    if not problemas:
        print(f"ok: {len(usadas)} luz(es) distribuidas em blocos, nenhuma repetida "
              "e nenhuma esquecida")
    return 1 if vazios else 0


if __name__ == "__main__":
    raise SystemExit(main())
