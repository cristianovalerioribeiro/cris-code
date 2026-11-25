# -*- coding: utf-8 -*-
"""Mapa de quebras: as 19 ocorrências da auditoria inicial (ed. 9, 137 páginas) e o estado final."""
import json, re, pymupdf
A = json.load(open("pages/audit_breaks.json")); n = A["pages"]
doc = pymupdf.open("Manual_de_Radiestesia_Terapeutica.pdf")
ID = re.compile(r"^(G\d{1,3}b?|C[1-7]-(?:sinais|emocoes|corpo))$")
BEFORE = [("13", "título “Perguntas” sozinho no pé", "título preso ao primeiro bloco (trecho curto virou bloco simples)"),
 ("21", "uma linha (“6.”) no alto antes do par G15/G28", "item final de lista preso ao anterior"),
 ("31", "uma linha (“5.”) no alto antes de “Passo 5”", "idem"),
 ("34, 37, 40, 46, 49", "cabeçalho C2-sinais … C7-sinais sozinho no pé", "cabeçalho da lista preso à interpretação e às 3 primeiras linhas"),
 ("43", "título “Passo 1b · Sinais” sozinho no pé", "título movido para dentro do bloco da lista"),
 ("54", "duas linhas de “Base” no alto antes de G20b", "“Base” passou a vir antes da tabela nos pares"),
 ("62", "cabeçalho G33 sozinho no pé", "cabeçalho da lista preso ao conteúdo"),
 ("83", "cabeçalho G45 sozinho no pé (exemplo enviado)", "idem"),
 ("93", "duas linhas no alto antes de “Pós-sessão”", "mínimo de 3 linhas por página (viúvas/órfãs)"),
 ("104", "duas linhas de “Base” antes de “Objetos perdidos”", "“Base” antes da tabela"),
 ("107", "título “Ficha de atendimento: campos” sozinho no pé", "título preso à tabela"),
 ("109", "uma linha (“6.”) no alto antes de G84", "item final preso ao anterior"),
 ("110", "três linhas de “Base” antes de “Alternativas”", "“Base” antes da tabela"),
 ("118", "título “Ferramentas desta seção” sozinho no pé", "tabela em largura total, título preso a ela"),
 ("126", "cabeçalho G104 sozinho no pé", "cabeçalho da lista preso ao conteúdo")]
L = ["# Mapa de quebras — pente fino final", "", f"Edição 9 auditada: 137 páginas, 19 quebras ruins, 22 caudas vazias. Edição 10: {n} páginas, {len(A['report'])} quebras ruins, {len(A['tails'])} caudas.", "",
     "## As 19 quebras encontradas na auditoria inicial", "", "| Página (ed. 9) | Problema | Correção aplicada |", "|---|---|---|"]
for pg, prob, fix in BEFORE: L.append(f"| {pg} | {prob} | {fix} |")
L += ["", "## O que ainda resta", "", "### Quebras ruins", ""]
if A["report"]:
    L += ["| Página | Tipo | O quê | Observação |", "|---|---|---|---|"]
    for pg, tipo, k, txt, obs in A["report"]: L.append(f"| {pg} | {tipo} | {txt} | {obs} |")
else: L.append("Nenhuma.")
L += ["", "### Caudas vazias (mais de 45 mm livres no fim da página)", "", "| Página | Livre (mm) | O que começa na página seguinte | Por que não coube |", "|---|---|---|---|"]
for pg, t in A["tails"]:
    if pg >= n: L.append(f"| {pg} | {t} | fim do manual | — |"); continue
    p = doc[pg]; W = p.rect.width
    bl = sorted([b for b in p.get_text("blocks") if b[4].strip() and b[0] < W - 45 and b[1] > 30], key=lambda b: (round(b[1]/6), b[0]))
    first = bl[0][4].strip().split("\n")[0][:40] if bl else ""
    ids = [s["text"].strip() for b in p.get_text("dict")["blocks"] for l in b.get("lines", []) for s in l["spans"] if 10.8 < s["size"] < 12.4 and ID.match(s["text"].strip()) and s["bbox"][1] < 160]
    if ids:
        what = " e ".join(ids[:2]); why = "bloco de desenho indivisível (90 a 150 mm) maior que o espaço livre; encolher o suficiente deixaria os rótulos abaixo de 5 pt"
    else:
        what = first; why = "abertura de Parte em página nova" if first.startswith("PA R T E") or first.startswith("Mapa") else "bloco indivisível seguinte (cartão, ficha ou tabela) maior que o espaço livre"
    L.append(f"| {pg} | {t} | {what} | {why} |")
L += ["", "## Regras de diagramação que passaram a valer", "",
      "- Cabeçalho de lista pendulável (G9, G45, G104…) preso à interpretação e às três primeiras linhas; o resto da lista quebra livremente.",
      "- Título de seção no fim de um trecho vai para dentro do bloco indivisível do gráfico seguinte (linha extra na tabela do desenho ou no bloco da lista), nunca fica sozinho.",
      "- Título com parágrafo (até 700 caracteres), tabela curta (até 420) ou primeiro item de lista presos num bloco pequeno; listas longas são divididas para isso, mantendo a numeração.",
      "- Trechos curtos deixam de ser multicoluna (o motor ignora proteções de quebra dentro de multicoluna).",
      "- Mínimo de três linhas de um parágrafo em cada página; último item de lista e linha “Base” não começam página.",
      "- Nos pares, a linha “Base” vem antes da tabela, para a célula terminar em linhas de tabela.",
      "- Chakras: se o par emoções | corpo saltou de página deixando 45 mm ou mais, as tabelas de crenças (3b) e de Hay sobem para o texto antes do par.",
      "- Bloco que saltou de página: todas as linhas de resultado vão para a tabela larga (divisível) e o desenho encolhe até 22 % (par: 20 %) para caber; o cálculo desconta o título colado ao bloco.",
      "- Apêndices A, B, C e D removidos; o Glossário ficou, emendado ao fim da Parte XVI."]
open("Mapa_de_quebras.md", "w", encoding="utf-8").write("\n".join(L)); print("mapa ok")
