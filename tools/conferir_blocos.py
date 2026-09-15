#!/usr/bin/env python3
"""
Mostra quais luminarias cada bloco do painel realmente pega.

    python3 tools/conferir_blocos.py

Roda os filtros do painel contra config/casa_exemplo.yaml e lista, bloco por
bloco, as luzes que caem nele. E como conferir se 'luzes:' e 'excluir:'
separaram o que deviam — por exemplo, se a Lavanderia saiu da Cozinha.

Avisa quando:
  * o toque no mestre pegaria luzes diferentes das que o bloco mostra
    (o script do package e o painel fora de sincronia);
  * um bloco fica sem nenhuma luz (padrao errado, ou rele nao identificado);
  * uma luz aparece em dois blocos (falta um 'excluir:' no bloco principal);
  * uma luz da casa nao aparece em bloco nenhum (esquecida no painel).
"""

from __future__ import annotations

import argparse
import ast
import sys
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))
from ha_mock import Casa  # noqa: E402
from ha_mock import expandir_auto_entities  # noqa: E402

RAIZ = Path(__file__).resolve().parent.parent


def alvos_do_script(dados: dict, casa: Casa, variaveis: list[dict]) -> set[str]:
    """Roda o Jinja do script de apoio e devolve as luzes que ele apagaria.

    Le os templates direto de packages/painel_novo.yaml, entao se o script e o
    painel sairem de sincronia o teste acusa.
    """
    env = casa.ambiente()
    contexto = dict(dados)
    for par in variaveis:
        for nome, tpl in par.items():
            bruto = env.from_string(tpl).render(**contexto).strip()
            try:
                contexto[nome] = ast.literal_eval(bruto)
            except (ValueError, SyntaxError):
                contexto[nome] = bruto
    return set(contexto.get("alvos") or [])


def variaveis_do_package(caminho: Path) -> list[dict]:
    dados = yaml.safe_load(caminho.read_text(encoding="utf-8")) or {}
    seq = dados["script"]["alternar_luzes_do_bloco"]["sequence"]
    brutas = next(p["variables"] for p in seq if "variables" in p)
    return [{k: v} for k, v in brutas.items()]


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
            mestre = next((c for c in cards
                           if (c.get("tap_action") or {}).get("perform_action")
                           == "script.alternar_luzes_do_bloco"), None)
            dados = (mestre or {}).get("tap_action", {}).get("data") or {}
            saida.append((view.get("title", "?"), nome, auto, dados))
    return saida


def sugerir_etiquetas(cfg: dict, casa: Casa) -> list[str]:
    """Linhas de 'temperatura:'/'umidade:' que faltam nos blocos.

    Com o sensor no titulo o bloco perde um card de largura inteira e fica ~56px
    mais baixo, e a leitura do ambiente sobe para junto do nome do comodo.
    """
    linhas: list[str] = []
    for pav in cfg.get("pavimentos") or [{"comodos": cfg.get("comodos") or []}]:
        for bloco in pav.get("comodos") or []:
            area = bloco.get("area")
            if not area or not bloco.get("sensores", True):
                continue
            achados = {}
            for eid in casa.area_entities(area):
                ent = casa.por_id[eid]
                if ent.dominio != "sensor":
                    continue
                if "C" in ent.unidade and "temperatura" not in achados:
                    achados["temperatura"] = eid
                elif "%" in ent.unidade and "umidade" not in achados:
                    achados["umidade"] = eid
            faltando = {k: v for k, v in achados.items() if not bloco.get(k)}
            if faltando:
                nome = bloco.get("nome") or area
                linhas.append(f"  # {nome}")
                linhas += [f"    {k}: {v}" for k, v in sorted(faltando.items())]
    return linhas


def main(argv=None) -> int:
    p = argparse.ArgumentParser(description="Confere os filtros de luz dos blocos.")
    p.add_argument("--painel", type=Path, default=RAIZ / "dashboards" / "painel-novo.yaml")
    p.add_argument("--casa", type=Path, default=RAIZ / "config" / "casa_exemplo.yaml")
    p.add_argument("--config", type=Path, default=RAIZ / "config" / "comodos.yaml")
    p.add_argument("--package", type=Path, default=RAIZ / "packages" / "painel_novo.yaml")
    args = p.parse_args(argv)

    dash = yaml.safe_load(args.painel.read_text(encoding="utf-8"))
    casa = Casa.carregar(args.casa)

    todas = {e.entity_id for e in casa.entidades if e.dominio == "light"}
    usadas: dict[str, list[str]] = {}
    vazios: list[str] = []
    pav_atual = None

    variaveis = variaveis_do_package(args.package)
    divergentes: list[str] = []

    for pav, nome, auto, dados in blocos_do_painel(dash):
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
        # O toque no mestre precisa agir exatamente nestas luzes. Comparar o
        # que o script calcularia com o que o painel mostra e o unico jeito de
        # garantir que apagar a "Lavanderia" nao apague a cozinha inteira.
        marca = ""
        if dados:
            do_script = alvos_do_script(dados, casa, variaveis)
            if do_script != set(ids):
                sobra = ", ".join(sorted(do_script - set(ids))) or "-"
                falta = ", ".join(sorted(set(ids) - do_script)) or "-"
                divergentes.append(f"{nome}: o mestre pegaria a mais [{sobra}] "
                                   f"e a menos [{falta}]")
                marca = "  <-- MESTRE DIVERGE"

        if not ids:
            vazios.append(nome)
            print(f"  {nome:26} VAZIO")
        else:
            nomes = ", ".join(casa.por_id[i].name for i in ids)
            print(f"  {nome:26} {len(ids)}x  {nomes}{marca}")

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
    for d in divergentes:
        print(f"ERRO: {d}")
        problemas += 1

    if not problemas:
        print(f"ok: {len(usadas)} luz(es) distribuidas em blocos, nenhuma repetida "
              "e nenhuma esquecida")
        print("ok: em todos os blocos o toque no mestre age exatamente nas luzes "
              "que o bloco mostra")

    if args.config.exists():
        cfg = yaml.safe_load(args.config.read_text(encoding="utf-8")) or {}
        sugestoes = sugerir_etiquetas(cfg, casa)
        if sugestoes:
            print("\nsugestao: estes blocos tem sensor de temperatura ou umidade na area,")
            print("mas nao o declaram. Declarado, o sensor vira etiqueta no titulo em vez")
            print("de card de largura inteira. Medido na casa de exemplo, declarar todos")
            print("encurtou a aba Terreo de 1175px para 929px no desktop (-21%) e de")
            print("2989px para 2483px no celular (-17%):\n")
            print("\n".join(sugestoes))

    return 1 if (vazios or divergentes) else 0


if __name__ == "__main__":
    raise SystemExit(main())
