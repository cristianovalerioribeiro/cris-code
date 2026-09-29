#!/usr/bin/env python3
"""Separa as 30 finais (curadoria sobre o top100) e monta, para cada uma,
o pacote de dados da base que os agentes de pesquisa recebem."""
import csv, json, re, sys
from pathlib import Path
from importlib.machinery import SourceFileLoader

AQUI = Path(__file__).resolve().parent.parent
BASE = "/home/user/construtoras-bh/data/input/construtoras_bh_2026-07_enriquecido.csv"

# Curadoria: 10 do eixo MCMV/economico (BH, Contagem, Betim, Neves) e 20 do eixo
# medio (R$ 10-14 mil/m2). Ficaram fora: gigantes com projeto interno (MRV,
# Direcional, Cyrela, Patrimar, Emccamp), loteadoras (Parcelar, Gran Viver) e
# dominios de SPE unica sem site proprio.
MCMV = ["neocasabrasil.com.br", "construtoraformula.com.br", "construtoravoce.com.br",
        "viasul.com", "magmaconstrucoes.com.br", "sonharconstrutora.com.br",
        "rdrengenharia.com", "argonengenharia.com", "maislar.com", "conquestconstrutora.com.br"]
MEDIO = ["prodomoconstrutora.com.br", "vivaquartzo.com.br", "construtoraqbhz.com.br",
         "petraeng.com.br", "construtoralage.com.br", "sudoeste.com.br", "somattos.com.br",
         "portoegomes.com.br", "construtoralive.com.br", "incorpe.com.br", "canopus.com.br",
         "mipconstrutora.com.br", "line4engenharia.com.br", "fbrinc.com.br",
         "phvengenharia.com.br", "terrazzas.com.br", "geraesconstrutora.com.br",
         "valadaresgontijo.com.br", "construtoracrd.com.br", "capanema.com"]

top = {s["dominio"]: s for s in json.load(open(AQUI / "dados/top100.json"))}
rows = list(csv.DictReader(open(BASE, encoding="utf-8-sig"), delimiter=";"))
dom = lambda s: re.sub(r"^https?://(www\.)?", "", s or "").split("/")[0].lower()

pacotes = []
for eixo, lista in (("mcmv", MCMV), ("medio", MEDIO)):
    for d in lista:
        g = dict(top[d]); g["eixo"] = eixo
        rs = sorted((r for r in rows if dom(r["site"]) == d), key=lambda r: r["inicio_atividade"], reverse=True)
        g["cnpjs"] = [{k: r[k] for k in ("cnpj", "razao_social", "nome_fantasia", "cnae", "porte",
                       "capital_social", "bairro", "inicio_atividade", "socios", "telefone", "email")}
                      for r in rs[:25]]
        pacotes.append(g)
(AQUI / "dados/pesquisa").mkdir(exist_ok=True)
json.dump(pacotes, open(AQUI / "dados/selecao30.json", "w"), ensure_ascii=False, indent=1)
print(len(pacotes), "selecionadas")
