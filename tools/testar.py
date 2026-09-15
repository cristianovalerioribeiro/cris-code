#!/usr/bin/env python3
"""
Roda todas as conferencias do painel de uma vez.

    python3 tools/testar.py

Use depois de mexer em config/comodos.yaml. Em ordem:

  1. gerar_painel      o config e valido e o dashboard e regerado
  2. gerar_painel -c   o dashboard versionado esta em dia com o config
  3. validar           o YAML gerado esta consistente
  4. conferir_blocos   as separacoes de luz fazem o que deviam
  5. descobrir -t      o template de descoberta nao perde entidades
  6. package           o YAML do script de apoio e valido

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
    ("template de descoberta", [PY, "tools/descobrir.py", "--testar"]),
]


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

    ok, detalhe = package_valido()
    print(f"{'ok  ' if ok else 'FALHA'} {len(ETAPAS) + 1}. package de apoio — {detalhe}")
    if not ok:
        falhas.append("package de apoio")

    print()
    if falhas:
        print(f"{len(falhas)} etapa(s) com problema: {', '.join(falhas)}")
        return 1
    print("tudo certo. Para ver como ficou:  python3 tools/preview.py --metricas")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
