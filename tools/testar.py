#!/usr/bin/env python3
"""
Roda todas as conferencias do painel de uma vez.

    python3 tools/testar.py

Use depois de mexer em config/comodos.yaml. Em ordem:

  1. gerar_painel      o config e valido e o dashboard e regerado
  2. gerar_painel -c   o dashboard versionado esta em dia com o config
  3. validar           o YAML gerado esta consistente
  4. conferir_blocos   as separacoes de luz fazem o que deviam
  5. conferir --reles  as separacoes se sustentam so pelo nome amigavel,
                       mesmo com entity_id sem sentido (light.rele_07)
  6. descobrir -t      o template de descoberta nao perde entidades
  7. fora dos pav.     um comodo nao declarado aparece no painel em vez de sumir
  8. package           o YAML do script de apoio e valido

Sai com codigo 1 se qualquer etapa falhar, entao serve em gancho de commit.
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
PY = sys.executable

ETAPAS = [
    ("gera o painel", [PY, "tools/gerar_painel.py"]),
    ("painel em dia com o config", [PY, "tools/gerar_painel.py", "--check"]),
    ("YAML gerado consistente", [PY, "tools/validar.py"]),
    ("separacoes de luz", [PY, "tools/conferir_blocos.py"]),
    ("separacoes com entity_id opaco", [PY, "tools/conferir_blocos.py", "--reles"]),
    ("template de descoberta", [PY, "tools/descobrir.py", "--testar"]),
]


def fora_dos_pavimentos() -> tuple[bool, str]:
    """A secao 'Fora dos pavimentos' acusa comodo que o config ainda nao conhece.

    Testa os dois estados: casa toda classificada (deve dizer que esta tudo
    certo) e casa com uma area a mais (deve acusar, nomear a area e mostrar as
    luzes). E a rede de seguranca para um pavimento inteiro nao sumir do painel.
    """
    import copy
    import sys

    import yaml

    sys.path.insert(0, str(RAIZ / "tools"))
    from ha_mock import Casa, expandir_auto_entities

    dash = yaml.safe_load((RAIZ / "dashboards" / "painel-novo.yaml").read_text("utf-8"))
    try:
        secao = next(s for v in dash["views"] if v.get("path") == "casa"
                     for s in v.get("sections") or []
                     if any(c.get("heading") == "Fora dos pavimentos"
                            for c in s.get("cards") or []))
    except StopIteration:
        return False, "a secao nao existe no painel"

    card = next(c for c in secao["cards"] if c.get("type") == "custom:mushroom-template-card")
    auto = next(c for c in secao["cards"] if c.get("type") == "custom:auto-entities")
    bruto = yaml.safe_load((RAIZ / "config" / "casa_exemplo.yaml").read_text("utf-8"))

    limpa = Casa(copy.deepcopy(bruto))
    if "Tudo classificado" not in limpa.render(card["primary"]):
        return False, f"casa completa deveria dizer 'Tudo classificado', "\
                      f"disse '{limpa.render(card['primary'])}'"

    com_extra = copy.deepcopy(bruto)
    com_extra["areas"]["Area Nao Declarada"] = [
        {"id": "light.teste_fora_1", "nome": "Teto", "estado": "off"},
        {"id": "light.teste_fora_2", "nome": "Sanca", "estado": "on"},
    ]
    suja = Casa(com_extra)
    texto = suja.render(card["primary"])
    if "2 luzes fora" not in texto:
        return False, f"deveria acusar 2 luzes fora, disse '{texto}'"
    if "Area Nao Declarada" not in suja.render(card["secondary"]):
        return False, "nao nomeou a area nao declarada"
    interno = expandir_auto_entities(auto, suja)
    ids = {c["entity"] for c in (interno or {}).get("chips", [])}
    if ids != {"light.teste_fora_1", "light.teste_fora_2"}:
        return False, f"os botoes mostrados nao batem: {sorted(ids)}"
    return True, "acusa comodo nao declarado e some quando tudo esta classificado"


def package_valido() -> tuple[bool, str]:
    import yaml

    arq = RAIZ / "packages" / "painel_novo.yaml"
    if not arq.exists():
        return False, f"{arq.name} nao encontrado"
    try:
        dados = yaml.safe_load(arq.read_text(encoding="utf-8")) or {}
    except yaml.YAMLError as exc:
        return False, f"YAML invalido: {exc}"
    scripts = (dados.get("script") or {})
    if "alternar_luzes_do_bloco" not in scripts:
        return False, "falta o script alternar_luzes_do_bloco"
    return True, f"script com campos {list(scripts['alternar_luzes_do_bloco']['fields'])}"


def main() -> int:
    falhas = []
    for i, (nome, cmd) in enumerate(ETAPAS, start=1):
        r = subprocess.run(cmd, cwd=RAIZ, capture_output=True, text=True)
        marca = "ok  " if r.returncode == 0 else "FALHA"
        ultima = [l for l in (r.stdout or "").strip().split("\n") if l.strip()]
        print(f"{marca} {i}. {nome}" + (f" — {ultima[-1]}" if ultima else ""))
        if r.returncode != 0:
            falhas.append(nome)
            for linha in (r.stderr or r.stdout or "").strip().split("\n")[-8:]:
                print(f"        {linha}")

    for n, (nome, fn) in enumerate([("secao fora dos pavimentos", fora_dos_pavimentos),
                                    ("package de apoio", package_valido)],
                                   start=len(ETAPAS) + 1):
        ok, detalhe = fn()
        print(f"{'ok  ' if ok else 'FALHA'} {n}. {nome} — {detalhe}")
        if not ok:
            falhas.append(nome)

    print()
    if falhas:
        print(f"{len(falhas)} etapa(s) com problema: {', '.join(falhas)}")
        return 1
    print("tudo certo. Para ver como ficou:  python3 tools/preview.py --metricas")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
