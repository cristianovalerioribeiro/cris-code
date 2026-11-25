import os, csv, sys, re
os.chdir(sys.argv[1])
reg={}
for l in open('livro/registry.tsv',encoding='utf-8'):
    p=l.rstrip('\n').split('\t')
    if len(p)>=3: reg[p[0]]={'title':p[1],'mime':p[2],'size':int(p[3]) if len(p)>3 and p[3].isdigit() else 0,'parent':p[4] if len(p)>4 else ''}
folders={'1L1I1FiTbUzS51GMuL-qqNOdaSJFygZrt':'RADIESTESIA','17PvWETiVEwv09JYZ8YUQEkjJFafpj7bP':'Radiestesia Grupo','1iNvT4HONQgUMgTsG0_ad9mDsI4yWkUzV':'Grafico','1ADMHooohkUczwm57zGVg6j08lskHnl2S':'Livros','1KmSB907CMmQ5cqEc2zrq_DJSTwfWUNaj':'Novo','1jImw4_mmyVJvXz2NJDlYlcE5fc6HtSb4':'Base de Conhecimento GEN','1JD-R6taTR3ejdwVC-w-pulIvpVqbZy7U':'Imprimir','1fse_gVTGmqxpsaGtfCyIFyVkSo7Bs5at':'ESTUDO','19LDXfzKsUJmk_AyyBFu46xJYwMpmjsI_':'Graficos','1CBzKMA_oE_Y777WBXpBcnQAyFbR-A1jj':'OK['}
def link(i): return f'https://drive.google.com/file/d/{i}/view'
def mb(n): return f'{n/1e6:.1f} MB' if n>=1e6 else f'{n//1000} KB'
def esc(s): return s.replace('|','\\|').replace('\n',' ')
disk={f.split('__')[0]:f for f in os.listdir('drive_imagens') if '__' in f}
desc={}
for l in open('livro/desc.tsv',encoding='utf-8'):
    p=l.rstrip('\n').split('\t')
    if len(p)>=5: desc[p[0]]=p
pdfd={}
for l in open('livro/pdfdesc.tsv',encoding='utf-8'):
    p=l.rstrip('\n').split('\t')
    if len(p)>=6: pdfd[p[0]]=p
large=[l.rstrip('\n').split('\t') for l in open('livro/largepdf.tsv',encoding='utf-8') if l.strip()]
imgs=sorted([i for i in disk if not disk[i].endswith('.pdf')], key=lambda i: (desc.get(i,['','z'])[1], reg.get(i,{}).get('title','')))
pdfs=sorted([i for i in disk if disk[i].endswith('.pdf')], key=lambda i: reg.get(i,{}).get('title',''))
out=[]
out.append('# Índice — imagens e PDFs de radiestesia no Google Drive\n')
out.append(f'Gerado em 2026-11-04. Pasta local: `/tmp/claude-0/-home-user-cris-code/3e0792b2-7078-57c8-b2b4-fb04de9efb63/scratchpad/drive_imagens/`\n')
nimg=len([i for i in reg if reg[i]['mime'].startswith('image/')]); npdf=len([i for i in reg if reg[i]['mime']=='application/pdf'])
out.append(f'**Candidatos encontrados (dedup. por id): {len(reg)}** — {nimg} imagens, {npdf} PDFs. **Baixados: {len(imgs)} imagens e {len(pdfs)} PDFs** (nome local = `<id>__<nome>.<ext>`). Imagens não baixadas: 1 (Terreno.jpg, 6,7 MB, excede o limite do conector). PDFs não baixados: {npdf-len(pdfs)} (limite de 40 + arquivos acima de ~6,3 MB, que derrubam o conector); os mais relevantes foram resumidos via `read_file_content` na seção 3.\n')
out.append('Tipos: **leque** (semicírculo/roda com setores), **régua** (escala linear), **tabela**, **mesa** (mesa radiônica composta), **silhueta** (corpo humano), **outro** (gráfico radiônico/símbolo/print).\n')
out.append('## 1. Imagens baixadas\n')
out.append('| arquivo local | nome original | tipo | tema | setores/escala | observação | link do Drive |')
out.append('|---|---|---|---|---|---|---|')
for i in imgs:
    d=desc.get(i); r=reg.get(i,{})
    if d: out.append(f'| `{esc(disk[i])}` | {esc(r.get("title",""))} | {d[1]} | {esc(d[2])} | {esc(d[3])} | {esc(d[4])}; {mb(r.get("size",0))} | [link]({link(i)}) |')
    else: out.append(f'| `{esc(disk[i])}` | {esc(r.get("title",""))} | ? | — | — | sem descrição | [link]({link(i)}) |')
out.append('\n### 1a. Setores detalhados da "Mesa Formação Autodiagnóstico Terapêutico" (1mBFAQzW…)\n')
for l in open('livro/formacao_setores.txt',encoding='utf-8'): out.append('- '+l.strip())
out.append('\n## 2. PDFs baixados\n')
out.append('| arquivo local | nome original | págs | tipo | tema | setores/escala | observação | link do Drive |')
out.append('|---|---|---|---|---|---|---|---|')
for i in pdfs:
    d=pdfd.get(i); r=reg.get(i,{})
    if d: out.append(f'| `{esc(disk[i])}` | {esc(r.get("title",""))} | {d[1]} | {d[2]} | {esc(d[3])} | {esc(d[4])} | {esc(d[5])}; {mb(r.get("size",0))} | [link]({link(i)}) |')
    else: out.append(f'| `{esc(disk[i])}` | {esc(r.get("title",""))} | ? | ? | — | — | sem descrição; {mb(r.get("size",0))} | [link]({link(i)}) |')
out.append('\n## 3. Não baixados, mas lidos/resumidos via read_file_content\n')
out.append('| id | nome original | resumo (setores/escala) | observação | link |')
out.append('|---|---|---|---|---|')
if '14vS8_7aTE0xYyjCcduNMh4UY9g04HE2X' in pdfd:
    d=pdfd['14vS8_7aTE0xYyjCcduNMh4UY9g04HE2X']
    out.append(f'| 14vS8_7a… | Sem nome (420 x 297 mm)_20251029_111406_0000.pdf — **Avaliação Radiestesia (A3, material próprio)** | {esc(d[4])} | {esc(d[5])} | [link]({link("14vS8_7aTE0xYyjCcduNMh4UY9g04HE2X")}) |')
for p in large:
    out.append(f'| {p[0][:8]}… | {esc(p[1])} | {esc(p[2])} | {esc(p[3])} | [link]({link(p[0])}) |')
out.append('| 1qJJeqdy… | Terreno.jpg (imagem, 6,7 MB) | foto/planta de terreno (não aberta) | excede limite do conector | [link](https://drive.google.com/file/d/1qJJeqdywLuYaZfIGwt2wTR-wgRJsqRNq/view) |')
out.append('\n## 4. Demais PDFs candidatos não baixados (apenas registrados)\n')
missing=[i for i in reg if reg[i]['mime']=='application/pdf' and i not in disk and i not in {p[0] for p in large} and i!='14vS8_7aTE0xYyjCcduNMh4UY9g04HE2X']
byf={}
for i in missing: byf.setdefault(folders.get(reg[i]['parent'],'outras pastas'),[]).append(i)
for f in sorted(byf, key=lambda k:(k=='outras pastas',k)):
    out.append(f'\n**Pasta {f}** ({len(byf[f])} arquivos)\n')
    for i in sorted(byf[f], key=lambda x: reg[x]['title'].lower()):
        out.append(f'- {esc(reg[i]["title"])} ({mb(reg[i]["size"])}) — [link]({link(i)})')
out.append('\n## 5. Outros itens relevantes do Drive (não imagem/PDF ou não baixados)\n')
out.append('- Miniaturas de capas de e-books (`*.pdf_thumb.jpg`) nas pastas 1pN8letQ…, 1lsQNf_…, 1luny2xS…, 1lonbhaHg… — capas de livros, sem valor para desenhar biômetros; não baixadas.')
out.append('- Documentos próprios do usuário (Word/PowerPoint) com gráficos: Etiquetas Chakras.docx, Mãos.docx, Guias.docx, GEOBIOLOGIA.docx, CHAKRA.docx, CHAKRA 2.docx, Doc2.docx, Mesas.pptx, Graficos para Impressão.pptx, GRÁFICOS RADIESTESIA PARA IMPRIMIR DANI_4.pptx, BONUS_RADIESTESIA IMP.pptx (pasta Graficos). Os PDFs CHAKRA.pdf e CHAKRA 2.pdf baixados correspondem aos .docx.')
out.append('- A busca por "mesa" também retornou ~60 arquivos CAD de móveis (.dwg/.cdr, pasta de arquivos.hadron) — excluídos.')
out.append('\n## 6. Mais úteis para o manual (20 arquivos de referência para desenhar biômetros)\n')
top=[
('1RFpeokeYs0Dzne-o-u1_0eNW5HDsPJbi','Biômetro Completo (PDF vetorial) — réguas Bovis em 4 escalas + barras de chakras/corpos/planos + leque Sub/Super Ativo; a referência de régua'),
('19FQGpLDFOV6nDQqBdP51BWhJ32Kh5yWp','BiometroCompleto.jpg — mesma peça em imagem (1280x913), útil para conferir cores das barras de chakras'),
('1yCStwbTCpYhQkXD2HsgmGLyNG885jamn','Biómetro de Bovis/Simoneton — régua horizontal 0–10.000 com faixas Letal→Bioenergía e divisa 6.500; a régua Bovis mais limpa'),
('1dbQbjCchqt1T7CnJeCU6Q1vLSY2zp3sW','Biômetro dos Chakras — leque multianel: Bovis + 7 corpos sutis + 7 chakras + horas/dias/meses + Sub/Super Ativo + decágono'),
('1l_85ie0W8aC6cfj17RsKkeaPIbHXkrnh','Relógio Radiestésico A3 — versão A3 do anterior, pronta para impressão'),
('1OhFmQBqt96e8RVggkmq7J_goJ7Gc9A1B','Chakras hipo/normal/hiper (subtil.net) — leque colorido de 7 chakras × 4 estados; modelo de leque de harmonização'),
('1jOdCpxDo4TdhC8OmT6RwhCkAwv6-Jj91','CHAKRA 2.pdf (próprio) — leque de chakras com afirmação, glândula, −100%…+100% e anel de tempo 1–60'),
('1xFc2fIYx5IPzhM2vKlcH-IQ6yZe80t-O','CHAKRA.pdf (próprio) — leques de causas/desequilíbrios por chakra (listas completas na tabela 2)'),
('1mBFAQzWJLuzHdZCkIIvR6o-oXEksDzVV','Mesa Formação Autodiagnóstico (Mannah) — 6 leques: Origem do Problema, Estado Emocional/Hz, Influência de Energia, Seres Negativos, Causas Sistêmicas, Tratamento (setores na seção 1a)'),
('14vS8_7aTE0xYyjCcduNMh4UY9g04HE2X','Avaliação Radiestesia A3 (próprio, não baixado) — listas prontas de causas, agentes nocivos, órgãos, sistemas, fases da vida (seção 3)'),
('1JQ8hnLtfkPvIn9igcjAWb7sUSLe8MlLR','AURA-PETs (subtil.net) — leque de 4 anéis coloridos (%, cores da aura, proteção, tamanho, Sim/Não); modelo de multianel'),
('1IwCizJvS9CnZdtuCqvxHUyHXHayxHr-n','Biômetro Completo II / Aura — leque de 6+ anéis (cores, chakras transpessoais, camadas, situação áurica, Hz, tempo, elementos)'),
('10_YQF6Ek3jOxGx1kKM2F1xBSGRoNOzXu','Medição Mesa Pets (subtil.net) — leque de 3 anéis: 5–100, −100.000…+100.000 e zonas perigosa/perturbada/neutra/saudável/espiritual'),
('1WUeHnY42s9i7YeHEcTxOy9QkLnlNL2i7','Biômetro 5G — anel Bovis 0–20.000/∞ + energias + impacto % + sintomas; modelo de leque de interferências'),
('1LzrgsdBhlAD_xQtdzbBQOtm8OtM7nmOB','Prosperidade — bloqueios (subtil.net) — leque de 22 causas; modelo de leque de causas'),
('1n026lIITkWXVieX9BVFLeCPHYCfun_WX','Doenças causadas pelas emoções — leque de 29 doenças'),
('1eHjPiZEHr-DUsrGk5eG4cs7kOLTkPjhg','Equilíbrio dos Chakras — silhueta com 7 chakras + decágono + leque −100%/+100% (hipo/equilíbrio/hiper)'),
('1Te6HjdAqleHqh6XyszbV_aN-Ggxd1GaY','Corpo Humano / Auras — silhueta com 7 corpos sutis em camadas coloridas'),
('1B1Irak2YcQ_RIuuym1d2H-T2dLFd7wHi','Florais Saint Germain — Fórmulas (subtil.net) — leque limpo de 16 setores; template de rotulagem radial'),
('1mLOq0t0ehR_8zNtYQdCvy4K1r7aPLk31','Mesa de Investigação (Mesas Universais) — leque numérico multianel (0–100 / 0–60 / 0–24 / 0–12 / tempo) + leque de 9 mesas'),
]
for n,(i,t) in enumerate(top,1):
    f=disk.get(i,'(não baixado)')
    out.append(f'{n}. **{esc(t)}** — `{f}` — [link]({link(i)})')
out.append('\nMenções honrosas: Mesa Seletora 2 (catálogo de ~45 gráficos por função), Graficos.pdf carlopes (relógio Sim/Não minutos/horas), Biômetro Capacidade de Auto Cura (órgãos), Biômetro Animais Perdidos (direção/distância), Florais de Bach roda de 38 setores, Ondas Eletromagnéticas e Cerebrais (escala Hz + faixas), biometros.pdf (21 MB, coletânea subtil.net — listas de setores na seção 3), 92 Gráficos Seleção (índice de 92 temas).')
open('drive_imagens/INDICE.md','w',encoding='utf-8').write('\n'.join(out)+'\n')
print('rows img',len(imgs),'pdf',len(pdfs),'missing',len(missing),'lines',len(out))
