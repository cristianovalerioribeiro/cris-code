# FRE — Ficha Resumo do Empreendimento (CAIXA) — Faixa 1 / FAR

Análise completa do arquivo `FRE_FAR_2025_v005_SG_rev3_editável.xlsb`.

| | |
|---|---|
| Autor do arquivo | Caixa (última edição: "Ildeu") |
| Criado / modificado | 20/04/2022 → 11/09/2026 |
| Formato | `.xlsb` (BIFF12 binário) com macros VBA (`vbaProject.bin`) |
| Tamanho | 2,4 MB · 45 abas · 777 nomes definidos · ~60 mil fórmulas |
| Programa | MCMV — **4. Minha Casa Minha Vida (FAR/FDS)** |
| Fonte de recursos do exemplo | **FAR** (Fundo de Arrendamento Residencial) = **Faixa 1** |

> O LibreOffice **não** abre este `.xlsb`. Toda a extração (valores + fórmulas +
> nomes definidos + comentários + VBA) foi feita com um parser BIFF12 próprio,
> em `ferramentas/`. Ver §10.

---

## 1. O que é o FRE

O FRE é o **formulário único de engenharia** que o proponente entrega à CAIXA
para análise técnica e contratação de um empreendimento habitacional. Ele
concentra, num só arquivo:

1. identificação e checklist documental,
2. caracterização do terreno e interferências,
3. memorial descritivo e tipologias,
4. **orçamento sintético** (habitação, equipamentos comunitários, infraestrutura
   interna/externa),
5. **quadro de origem e aplicação de recursos** (Resumo de Valores para FAR, QCI
   para FDS),
6. cronograma físico-financeiro.

O título da aba muda sozinho conforme o programa:
`="Ficha Resumo do Empreendimento" & " - Habitação de Interesse Social"` quando
`ProgramaProp = "4. Minha Casa Minha Vida (FAR/FDS)"`.

**Duas chaves comandam o formulário inteiro:**

| Nome definido | Célula | Efeito |
|---|---|---|
| `ProgramaProp` | `1-IDENTIFICAÇÃO!N7` | HIS × Mercado; liga/desliga abas |
| `RecursosProp` | `1-IDENTIFICAÇÃO!S7` | **FAR** → aba `5-RESUMO DE VALORES`; **FDS/OGU** → aba `5-QCI` |

Na aba `0-BEM-VINDO` isso aparece explicitamente:

```
K23: =IF(RecursosProp<>"FAR",1,0)   → mostra "5-QCI"
K24: =IF(RecursosProp="FAR",1,0)    → mostra "5-RESUMO DE VALORES"
K22: =IF(CalamidadeRS=TRUE,1,0)     → mostra "4.4-INFRA CALAMIDADE"
K13: =IF(ProgramaProp<>A10,1,0)     → mostra "2.2-TERRENO FOTOS"
```

---

## 2. Arquitetura das 45 abas

### 2.1 Abas de trabalho (o formulário propriamente dito) — 20

| Aba | Papel |
|---|---|
| `0-BEM-VINDO` | Menu de navegação; acende/apaga os botões por fórmula |
| `1-IDENTIFICAÇÃO` | Programa, fonte de recursos, partícipes, RT, regime de construção |
| `1.1-CHECKLIST` | Documentos por fase (Pré-análise / Análise definitiva / Contratação) |
| `2-TERRENO INFRA E INTERF.` | Áreas, GPS, infraestrutura existente, interferências |
| `2.1-TERRENO POTENCIAL CONTAMIN.` | Passivo ambiental (NBR 15515) |
| `2.2-TERRENO FOTOS` | Relatório fotográfico (mín. 6 fotos) |
| `3-CARACTERIZAÇÃO` | Tipologia, nº UH, blocos, pavimentos, elevadores, equipamentos, vagas |
| `3.1-MEMORIAL DESCRITIVO` | Memorial completo (892 linhas × 101 colunas) |
| `3.1.1` / `3.1.2` | Selo Casa Azul + CAIXA (carta-proposta e memorial) |
| `3.2-TIPOLOGIAS` | Uma linha por tipologia de UH; áreas e cômodos |
| `4.1-CUSTOS HABITAÇÃO` | Orçamento sintético da edificação (9 grupos) + BDI + ISS |
| `4.1.1-TABELA ÁREA EQUIVALENTE` | Área equivalente NBR 12721 |
| `4.2-CUSTOS EQUIP. COMUNITÁRIOS` | Orçamento dos equipamentos de uso comum |
| `4.3-CUSTOS INFRA INTERNA` | Orçamento analítico de infra **incidente** (12 grupos, 472 linhas) |
| `4.3.1-CUSTOS INFRA EXTERNA` | Infra **não incidente** |
| `4.4-CUSTOS INFRA CALAMIDADE` | Variante para calamidade RS |
| `5-RESUMO DE VALORES` | **Quadro FAR** — VO, VI, contrapartidas |
| `5-QCI` | **Quadro FDS** — Quadro de Composição de Investimento |
| `6-CRONOGRAMA` | Cronograma físico-financeiro, até 120 etapas |
| `Instruções de Preenchimento` | Texto de orientação |

### 2.2 Memórias de cálculo auxiliares (`PlanCalc_*`) — 12

`Cubacao`, `Agua`, `Esgoto`, `Drenagem`, `Gas`, `Incendio`, `Pavimentacao` —
e cinco duplicatas sufixadas `INI` para a **infra não incidente**
(`CubacaoINI`, `AguaINI`, `EsgotoINI`, `DrenagemINI`, `PavimentacaoINI`).

> **Achado importante:** as abas `PlanCalc_*` **não estão ligadas por fórmula**
> às planilhas de orçamento. Confirmado por varredura: nenhuma célula de
> `4.3`, `4.3.1` ou `4.4` referencia `PlanCalc_*`. Elas são calculadoras
> abertas por botão (macro `PLAN_CALC`, que apenas torna a aba visível) e o
> projetista **transcreve** o resultado para a coluna *Quantidade*. Só há duas
> referências cruzadas residuais (`PlanCalc_EsgotoINI!M…`, `PlanCalc_PavimentacaoINI!M…`).

### 2.3 Bases de dados e apoio — 13

| Aba | Conteúdo |
|---|---|
| `Valores_municipío_MCID_05.2025` | **5.571 municípios** → recorte → valor máximo por UH (base 05/2025) |
| `Municipios` | UF × cidade (listas em cascata) |
| `BDI` | Tabela e fórmula do BDI |
| `Materiais` | Catálogo de tubos/materiais com código SINAPI/ORSE por diâmetro |
| `NumItemOrcInf` | Dicionário de numeração hierárquica dos itens de infraestrutura |
| `Memorial_Parametros` | Padrões de acabamento Alto/Normal/Baixo (NBR 12721) |
| `ListaNomes`, `IntervalosNomeados`, `ListaTudo`, `Planilha1` | Autodocumentação dos 777 nomes e das abas |
| `GERA_CARGA` | Define quais abas vão para o SIOPI em cada fase |
| `-INSTRUÇÕES` | Instruções de preenchimento (texto) |

Há 4 tabelas do Excel (*ListObjects*), usadas por referência estruturada:

| Tabela | Onde | Para quê |
|---|---|---|
| `TabelaAnexoVport725` | `Valores_municipío!L2:P14` | recorte → valor máximo da UH |
| `TabelaMunicipios` | `Valores_municipío!A2:J5573` | município/UF → recorte e valores |
| `TabelaRegiaoNorte` | `Valores_municipío!R2:R9` | UFs com incremento do Norte |
| `Tabela1` | `Municipios` | listas em cascata |

---

## 3. Metodologia de cálculo

### 3.1 Valor máximo de provisão por UH — o teto da operação

É o número que define se o empreendimento cabe no programa. Calculado por
**dois caminhos redundantes** (`5-RESUMO DE VALORES!Y5` e `Y6`), que devem bater:

**Caminho A — "Tabela" (recorte):**

```
recorte = VLOOKUP(Município&"/"&UF ; TabelaMunicipios ; 5 ; 0)
valor   = VLOOKUP(recorte ; TabelaAnexoVport725 ; col ; 0)

col = 2 → APTO           (Condomínio, enquadramento "mínimo")
      3 → APTO SUPERIOR  (Condomínio, enquadramento "Superior")
      4 → CASA           (Loteamento, "mínimo")
      5 → CASA SUPERIOR  (Loteamento, "Superior")
```

**Caminho B — "Calculado" (direto no município), com os dois abatimentos:**

```
valor = VLOOKUP(Município&"/"&UF ; TabelaMunicipios ; col ; 0)
        − SE (terreno doado E opção = "desconto no valor máximo de provisão das UH")
             ENTÃO ValorTerreno / qtdUH
             SENÃO 0

col = 6 APTO · 7 APTO SUPERIOR · 8 APTO RETROFIT · 9 CASA · 10 CASA SUPERIOR
```

**Tabela do Anexo V da Portaria MCid nº 725/2023 (base 05/2025), em R$/UH:**

| Recorte | APTO | APTO SUPERIOR | CASA | CASA SUPERIOR |
|---|---:|---:|---:|---:|
| A1 | 164.000 | 180.500 | 154.500 | 170.000 |
| A2 | 162.000 | 178.500 | 154.500 | 170.000 |
| A3 | 155.000 | 170.500 | 148.000 | 163.000 |
| A4 | 149.500 | 164.500 | 146.500 | 161.500 |
| B1 | 160.000 | 176.000 | 147.000 | 162.000 |
| B2 | 154.000 | 169.500 | 147.000 | 162.000 |
| B3 | 153.000 | 168.500 | 143.500 | 158.000 |
| B4 | 147.500 | 162.500 | 142.500 | 157.000 |
| C1 | 155.000 | 170.500 | 146.000 | 161.000 |
| C2 | 152.500 | 168.000 | 146.000 | 161.000 |
| C3 | 150.000 | 165.000 | 142.500 | 157.000 |
| C4 | 143.500 | 158.000 | 140.000 | 154.000 |

**Dois multiplicadores embutidos na coluna do município:**

```
Região Norte (AC, AM, AP, PA, RO, RR, TO):   valor × (1 + 10%)      incRegNorte      = 0,10
Requalificação / Retrofit:                   APTO SUPERIOR × (1+40%) incRequaliRetrofit = 0,40
```

> Exemplo do arquivo: Belo Horizonte/MG → recorte **B1**; Condomínio +
> enquadramento **Superior** → **R$ 176.000/UH**. Com 184 UH, o teto de
> provisão é **R$ 32.384.000**.

### 3.2 BDI — aba `BDI`

Fórmula do Acórdão TCU (truncada em 2 casas):

```
BDI = [ ((1 + AC + S+G + R) × (1 + DF) × (1 + L)) / (1 − (I1 + I2 + I3)) − 1 ] × 100
```

| Parcela | Não desonerado | Desonerado | Adm. Direta | Beneficiários |
|---|---:|---:|---:|---:|
| AC — Administração Central | 4,00 % | 4,00 % | 3,50 % | 3,50 % |
| S+G — Seguro e Garantia | 0 | 0 | 0 | 0 |
| R — Risco | 1,27 % | 1,27 % | 1,27 % | 1,27 % |
| DF — Despesas Financeiras | 1,23 % | 1,23 % | 0 | 0 |
| L — Lucro | 7,40 % | 7,40 % | 0 | 0 |
| I1 — RET (Lei 14.620) | 0,53 % | 0,53 % | 1,825 % | 0 |
| I2 — ISS | alíquota municipal | alíquota municipal | alíquota × 50 % | 0 |
| I3 — Contrib. Previdenciária (CPRB) | 0 | **ver transição** | 0 | 0 |

O regime é escolhido automaticamente:

```
=IF(RegConsAdmDireta;"AdmDireta";
   IF(OR(RegConsMutiraoAjMutua;RegConsAutoCons);"Beneficiários";
      IF('4.1-CUSTOS HABITAÇÃO'!B6;"Desonerado";"Não Desonerado")))
```

**Transição da desoneração (Lei 14.973/2024)** — `BDI!M15:O19`, lida por
`VLOOKUP(YEAR(TODAY());…;2;1)`:

| Ano | CPRB | Alíquota sobre a folha |
|---|---:|---:|
| 2024 | 4,5 % | 0 % |
| 2025 | 3,6 % | 5 % |
| 2026 | 2,7 % | 10 % |
| 2027 | 1,8 % | 15 % |
| 2028 | 0 % | 20 % |

**Valores resultantes com ISS = 0:** Não desonerado **15,06 %** · Desonerado
**18,27 %** (2026) · Adm. Direta **6,71 %** · Beneficiários **4,77 %**.
Há uma matriz completa por alíquota de ISS (0 / 1 / 1,5 / 2 / 2,5 / 3 / 4 / 5 %) —
ex.: não desonerado com ISS 5 % → 21,15 %.

O usuário escolhe entre **BDI cartilha** (calculado, `BDI_calc`) e **BDI proposto**
(`BDI_cart`); `BDI_HIS` é o efetivamente aplicado. Para **FAR ou Cogestão** o
formulário força o BDI cartilha:
`=IF(AND(OR(RecursosProp="FAR";RegCons="Cogestão");BDI_adotcalc);TRUE;FALSE)`.

### 3.3 Área equivalente — `4.1.1` (NBR 12721)

```
Área real total      S = (Área × Repetições) − (Vazios/Shafts × Repetições)
Coeficiente          U = (Custo_item / Área_item) ÷ (Custo_padrão / Área_padrão)
Área equivalente     V = S × U
```

A **área coberta padrão** (item 1.1) tem coeficiente fixo **1,0**, e o seu custo é
obtido por diferença:

```
T14 = CusTotSemBdi − CUSTHAB1SPG − T31
      (custo total sem BDI − serviços preliminares e gerais − demais áreas)
```

Cada área de padrão diferente (marquise, calçada perimetral, abrigo de gás…)
recebe o coeficiente pela razão entre seu custo unitário e o da área padrão.
Blocos do tipo Condomínio usam `V32`; Casas/Loteamento usam `V93`.
Suporta até 3 projetos-tipo de bloco e 7 de casa, com os totais somados por
`SUM(...INDIRECT(ADDRESS(...)+QtdProjTipo*n))` — intervalo elástico.

O indicador final é o **custo por m² equivalente**:

```
P8 = IF(TipologiaEmpreend="Condomínio"; AreEqvAp; AreEqvCs)
P9 = CusTotSemBdi / AreEqvAp            → R$/m² a comparar com o CUB do SINDUSCON
```

A orientação da aba `-INSTRUÇÕES` é explícita: *"Não serão acatadas na análise
propostas de valor de orçamento abaixo da referência de preço CUB."*

### 3.4 Custos de habitação — `4.1`

Estrutura em 9 grupos / 2 níveis (`L = IF(LEN(N)<=2;1;2)`):

```
1 SERVIÇOS PRELIMINARES E GERAIS   1.1 serviços técnicos · 1.2 mobilização ·
                                   1.3 máquinas e equip. · 1.4 administração local
2 FUNDAÇÕES (só superficiais)
3 SUPRAESTRUTURA
4 PAREDES E PAINÉIS                4.1 alvenarias · 4.2 esquadrias metálicas · 4.3 madeira
5 COBERTURA E PROTEÇÕES            5.1 telhados · 5.2 impermeabilizações
6 REVESTIMENTOS                    6.1 internos · 6.2 cerâmicos · 6.3 externos ·
                                   6.4 forros · 6.5 pinturas
7 PAVIMENTAÇÃO                     7.1 cimentados · 7.2 cerâmicos · 7.3 rodapés · 7.4 especiais
8 INSTALAÇÕES E APARELHOS          8.1 elétricas · 8.2 hidráulicas/gás/incêndio ·
                                   8.3 sanitárias/pluviais · 8.4 aparelhos/metais
9 COMPLEMENTAÇÕES                  9.1 calafete/limpeza
```

Preenche-se o **custo**; a incidência é derivada
(`R = S / CusTotSemBdi`) e há um validador permanente:

```
=IF(SUMIF(nivel;"=1";incid)=100%;"ok";
    IF(<100%;"Falta "&TEXT(…);"Passou "&TEXT(…)))
```

Suporta **dois sistemas construtivos** simultâneos (colunas U/V e W/X), quando
`SistConstrutivoMisto = "Sim"`.

Regras de fronteira relevantes (coluna *Observações*):
- fundações **profundas** vão para a infraestrutura, não aqui;
- **elevadores** vão para a infraestrutura;
- **demolição** não pode entrar na proposta (terreno deve estar livre);
- abrigos de gás adjacentes ao bloco entram em 8.2;
- contrapisos entram em 7.2; chapisco+emboço do cerâmico entram em 6.2.

### 3.5 Infraestrutura — `4.3`, `4.3.1`, `4.4`

Orçamento **analítico** com 12 grupos e ~470 linhas, cada item já pré-associado
a um código **SINAPI** ou **ORSE**:

```
1 Serviços preliminares e gerais      7 Energia e iluminação
2 Movimento de terra / fundações prof. 8 Telecomunicações
3 Água potável                         9 Gás
4 Esgoto sanitário                    10 Rede de incêndio
5 Drenagem pluvial                    11 Fechamento perimetral
6 Pavimentação                        12 Paisagismo e equipamentos
```

**Numeração automática e auto-compactante.** O número do item só avança se o
item tiver custo:

```
G7  = IF(AA7>0;1;0)            ' item "existe"?
J8  = J7 + G8                   ' contador acumulado
N8  = $N$6 & "." & IF(G8=0;"";J8)
```

e os títulos de grupo vêm de um dicionário:
`N = INDEX(NumItemOrcInf!D:G; MATCH(Grupo&"_"&Descrição; NumItemOrcInf!G:G;0);2)`.

**Rateio dos serviços preliminares (1.1 a 1.4).** Não se digita o valor: ele é
obtido por *gross-up* a partir das incidências definidas em `4.1`:

```
Z7 = ( ΣCustosDiretos / (1 − Σincidências₁.₁₋₁.₄) − ΣCustosDiretos )
     × ( AB7 / Σincidências₁.₁₋₁.₄ )
```

com `AB7:AB10 = '4.1-CUSTOS HABITAÇÃO'!R14:R17` — isto é, **os percentuais de
serviços preliminares são os mesmos em Habitação, Infraestrutura e
Equipamentos Comunitários**, como o próprio título do item 1 exige.

**Fechamento:**

```
AA470 = SUM(AA7:AA469)/2          ' ÷2 porque as linhas "CUSTO TOTAL DO ITEM" entram na soma
AA471 = BDI_HIS
AA472 = AA470 × (1 + BDI_HIS)     ' CUSTO TOTAL DE CONSTRUÇÃO
```

A aba `4.3.1` (não incidente / externa) e a `4.4` (calamidade RS) repetem a
mesma mecânica.

### 3.6 Memórias de cálculo `PlanCalc_*`

**Terraplenagem (`PlanCalc_Cubacao`) — método das seções médias:**

```
Volume corte   F = (D_i + D_{i−1}) / 2 × Extensão
Volume aterro  G = (E_i + E_{i−1}) / 2 × Extensão
Volume solto   H = F × 1,30                  ' empolamento 30 %
Peso           J = F × 1,9949 / 1000         ' t  (PE = 1,9949 kg/m³ na planilha)
Momento        L = J × DMT(km)               ' t × km
DMT médio      = ΣMomento / ΣPeso
Saldo          = Σcorte − Σaterro  →  >0 "Bota-fora" · <0 "Empréstimo"
```

**Redes (`PlanCalc_Agua/Esgoto/Drenagem/Gas/Incendio`)** — por trecho:

```
L  largura externa do tubo  = DN/1000 + 2 × espessura do berço
M  profundidade da vala     = MÉDIA(prof. inicial; prof. final) + espessura do berço
N  largura da vala          = INDEX(tabela DN × profundidade)      ' tabela AJ3:BC11
O..R escavação por faixa    = M × N × Extensão, separada em 0–1,5 / 1,5–3 / 3–4,5 / >4,5 m
T  preparo de fundo         = N × Extensão
U  lastro de areia          = (N × L − π(DN/2000)²) × Extensão
V  reaterro                 = Escavação − Lastro − Volume do tubo
W  bota-fora                = (Escavação − Reaterro) × 1,30
X..AA escoramento           = M × Extensão × 2, por faixa de profundidade
AB cadastro/limpeza         = (N + 0,40) × Extensão
```

A largura da vala vem de uma matriz **DN × profundidade** embutida (0,65 m para
DN pequeno e vala rasa, até 2,50 m para DN grande e vala profunda). Em esgoto e
drenagem, **descontam-se os volumes dos poços de visita** (comentário nas
células V13/W13, com regra distinta para DN ≤ 400 e DN > 400).

Aviso na própria aba: *"o Diâmetro Nominal (DN) a ser indicado é o diâmetro
interno, não o comercial. Ex.: a tubulação PBA 160 tem DN = 150 mm."*

### 3.7 Resumo de Valores — FAR (aba `5-RESUMO DE VALORES`)

É o quadro que fecha a operação **Faixa 1**. Colunas: `S` recursos FAR ·
`U:X` até quatro responsáveis por contrapartida · `Y` total (VI).

```
CUSTOS DIRETOS
  TERRENO                        Y12 = VlrTerProp   (0 e "(doado)" se TerrDoado="Sim")
  Habitação (Edificações)        Y13 = CTH
  Infraestrutura                 Y14 = Interna + (Calamidade RS, se houver)
  Equipamentos Comunitários      Y17 = CTEQUIPCOMUM
  CUSTO TOTAL DAS CONSTRUÇÕES    Y18 = Σ(nível 2)                          ← "CTC"
TRABALHO SOCIAL                  Y19 (ver abaixo)
MANUTENÇÃO DOS ELEVADORES        Y20
OUTRAS DESPESAS                  Y21 = Legalização + Seguros + Vigilância
INFRAESTRUTURA EXTERNA           Y25 = CTINFRAEXT
TOTAL FAR (VO)                   Y26 = SUMIF(nível="1"; coluna S)
TOTAL VALOR DO INVESTIMENTO (VI) Y30 = SUMIF(nível="1"; coluna Y)
```

**Recursos FAR por linha** = total menos contrapartidas:
`S = Y − SUM(U:X)`.

**Trabalho Social — cálculo por *gross-up*:**

```
S19 = ROUND( Σ(linhas marcadas K=1 da coluna S) / (1 − i) × i ; 2 )
i   = 2,0 % para Condomínio · 1,5 % para Loteamento    (HLOOKUP em B4:C5)
```

O *gross-up* garante que o TS represente exatamente `i` **do VO final**, e não
`i` da base. O terreno só entra na base se **não** for doado (`K12`); o próprio
TS é excluído da base (`K19 = 0`).

> **Referência circular intencional.** `T19 = S19 / TotalVOFAR` e
> `TotalVOFAR` já inclui `S19`. O arquivo traz um nome definido
> `CircularReference` nessa aba e uma macro dedicada:
> ```vba
> Public Sub CalcIterativoLIGA()
>     Set rng = Sheets("5-RESUMO DE VALORES").CircularReference
>     If Not rng Is Nothing Then
>         Application.Iteration = True
>         Application.MaxIterations = 1
>         Application.MaxChange = 0.000001
>     End If
> End Sub
> ```
> **Sem cálculo iterativo ligado, o quadro não converge.**

**Contrapartidas.** Dois regimes:

- **Globais** (`N34:U36`) — só para obras internas; rateadas por incidência:
  `U13 = SUMIF(RespFinGlob;U$11;ValorGlob) × ResValCTCIncidHab`, e análogas para
  infraestrutura e equipamentos. As incidências são
  `AA13 = CTH / CTCFARVIliq`, `AA15`, `AA17`, onde
  `CTCFARVIliq = Y18 − (contrapartidas vinculadas à infra interna)`.
- **Vinculadas** (`N40:W44`) — casadas por objeto e tipo
  (`Financeira Vinculada`, `Bens`, `Serviços`) via `SUMIFS` de três critérios.

Validador embutido para a infra externa:
`"Falta indicar o(s) responsável(is) por R$ X, a título de contrapartida"`.

A lista de responsáveis no cabeçalho é montada por fórmula dinâmica:
`=IFERROR(TRANSPOSE(UNIQUE(FILTER(VSTACK(…)))) ; "Nome do Ente")` — exige
Excel 365.

### 3.8 QCI — FDS (aba `5-QCI`)

Mesma lógica, formato do **Quadro de Composição de Investimento**, com as
particularidades do FDS:

- **Fase I** opcional (elaboração de projetos, com ou sem aquisição de terreno)
  e **Fase Única**;
- linhas próprias de **ATEC** (Assistência Técnica) e **Administração da Sede da
  Entidade Organizadora**, com limite `1 %` (`C9`);
- percentuais por regime: **Cogestão 3,5 %** · **Autogestão 4,0 %** (`B11/C11`);
- modalidade: **III — Produção de unidades novas** ou **VI — Requalificação
  (retrofit)**, escolhida por `RequaliRetrofit`;
- TS com a mesma fórmula de *gross-up*, descontando `ModProjTSPreObra`.

### 3.9 Cronograma — `6-CRONOGRAMA`

Até 120 etapas, três curvas independentes (Habitação, Infraestrutura,
Equipamentos Comunitários) e duas derivadas:

**Evolução física = média ponderada pelas incidências do CTC**

```
U = O15×O_etapa + Q15×Q_etapa + S15×S_etapa
O15 = IF(RecursosProp="FAR"; ResValCTCIncidHab ; FDSQCICTCIncidHab)     ' idem infra e equip.
V = acumulado
```

**Liberação financeira — trava dos 5 %**

```
Z (acumulado) = IF( X ≥ 100% ; V ;                 ' X = habite-se E CND indicados
                    IF( V > 95% ; 95% ; V ) )

Y (da etapa)  = IF( Z_anterior = 100% ; 0 ;
                    IF( X = 100% ; 5% ;
                        IF( Z_anterior ≥ 95% ; 0 ;
                            IF( V ≤ 95% ; U ; U − (V − 95%) ))))

X = COUNTA($W$18:W_atual) / COUNTA($W$18:$W$138)   ' 2 marcações "X" → 100%
```

Ou seja: a liberação acompanha a evolução física até **95 %**; os **5 % finais**
só são liberados na etapa em que **habite-se e CND** estiverem marcados. A aba
`-INSTRUÇÕES` descreve exatamente isso.

---

## 4. Nomes definidos — o vocabulário do arquivo

São **777** nomes (595 no manifesto original + internos). Distribuição:

| Aba de destino | Nomes |
|---|---:|
| `3-CARACTERIZAÇÃO` | 101 |
| `3.1-MEMORIAL DESCRITIVO` | 73 |
| `1-IDENTIFICAÇÃO` | 68 |
| `5-QCI` | 55 |
| `4.3-CUSTOS INFRA INTERNA` | 41 |
| `4.1-CUSTOS HABITAÇÃO` | 40 |
| `2-TERRENO` / `5-RESUMO DE VALORES` | 37 cada |
| demais | resto |
| fórmulas dinâmicas (`OFFSET`, `UNIQUE`) | ~25 |

As abas `ListaNomes` e `IntervalosNomeados` mantêm o **catálogo autodocumentado**
(nome → referência), em duas colunas de versão — usado pela rotina
`AtualizaVersao` para migrar dados entre versões do formulário.

**Nomes-chave para leitura de fórmulas:**

| Nome | Referência | Significado |
|---|---|---|
| `ProgramaProp` / `RecursosProp` | `1-IDENT!N7` / `S7` | programa e fonte |
| `TipologiaEmpreend` | `3-CARACT!N7` | Condomínio × Loteamento |
| `Enquadramento` | `3-CARACT!W7` | "mínimo" × "Superior" |
| `RequaliRetrofit` | — | retrofit sim/não |
| `qtdApart` / `qtdCasa` | `3-CARACT!P21` / `Q14` | nº de UH |
| `CusTotSemBdi` | `4.1!P7` | custo direto de habitação |
| `CTH` / `CTHSBDI` | `4.1!K3` / `K2` | habitação com / sem BDI |
| `CTINFRA` / `CTINFRASBDI` | `4.1!K5` / `K4` | infra interna |
| `CTINFRAEXT` / `CTINFRACALAMRS` | `4.1!K9` / `K11` | infra externa / calamidade |
| `CTEQUIPCOMUM` | `4.1!K7` | equipamentos comunitários |
| `AreEqvAp` / `AreEqvCs` | `4.1.1!V32` / `V93` | área equivalente |
| `BDI_calc` / `BDI_cart` / `BDI_HIS` | `BDI!N10`, `4.1!R6`, `4.1!R7` | BDI cartilha / proposto / aplicado |
| `ISS_aliquota` / `DtBsCt` | `4.1!V8` / `V9` | ISS e data-base dos custos |
| `TotalVOFAR` | `5-RESUMO!Y26` | valor da operação |
| `CTCFARVIliq` | fórmula | CTC líquido de contrapartidas de infra |
| `ResValCTCIncidHab/Inf/EquCom` | `5-RESUMO!AA13/15/17` | incidências que pesam o cronograma |
| `TerrDoado` / `TerrDoaçãoOpç` / `VlrTerProp` | `2-TERRENO!P13` / `X13` / `Z11` | terreno |
| `incRegNorte` / `incRequaliRetrofit` | `Valores_municipío!S3` / `U3` | +10 % / +40 % |

---

## 5. Bases de dados embutidas

### 5.1 `Valores_municipío_MCID_05.2025`
5.571 municípios × (Município/UF, código, UF, recorte, 5 colunas de valor).
As colunas de valor são **fórmulas**, não constantes — recalculam a partir do
recorte e dos incrementos. Trocar a data-base significa trocar
`TabelaAnexoVport725` (12 linhas) e os recortes, não os 5.571 valores.

### 5.2 `Materiais`
Catálogo de tubos por sistema (água potável, esgoto, drenagem, gás, incêndio),
com descrição SINAPI completa, descrição resumida, diâmetro e código
(SINAPI ou insumo `IN …`; ORSE onde não há SINAPI). Alimenta as listas suspensas
dos itens de tubulação das abas de infraestrutura — daí os nomes definidos do
tipo `OFFSET(Materiais…)`.

### 5.3 `NumItemOrcInf`
94 linhas: `Nível | Vínculo N1 | Nuitem | Descrição | DescriçãoChave`. É o
dicionário que dá o número hierárquico correto a cada grupo de infraestrutura
(`2.2.1`, `3.3.5`, …) via `INDEX/MATCH` sobre `Grupo_Descrição`.

### 5.4 `Memorial_Parametros`
Especificações de acabamento nos três padrões da **NBR 12721**
(**Alto / Normal / Baixo**) para portas, janelas, peitoris, impermeabilização,
acessórios sanitários, cozinha, área de serviço etc. É a base das listas
suspensas do memorial descritivo e da aderência ao projeto-padrão do CUB.

### 5.5 `GERA_CARGA`
Define, por fase, quais abas compõem o arquivo enviado ao **SIOPI**:

```
P8  = IF(optSeloAzul="sim";"S";"N")        ' abas do Selo Casa Azul
P22 = IF(CTINFRAEXT>0;"S";"N")             ' aba de infra externa e suas PlanCalc
```

A lista final é montada por `OFFSET/MATCH/COUNTIF` sobre a coluna da fase.
**Pré-análise** exige só as abas 1, 1.1, 2, 2.1 e 3; **Análise definitiva**
exige praticamente tudo.

---

## 6. Macros VBA

78 módulos, ~167 mil caracteres. Não há cálculo de engenharia em VBA — as
macros cuidam de **navegação, exibição, inserção/exclusão de linhas e versão**.

| Módulo | Função |
|---|---|
| `CalcIterativo` | Liga/desliga o cálculo iterativo (§3.7) — **crítico** |
| `MódNavegação` | Botões entre abas (`PLAN_CALC`, `VOLTAR`), filtros de impressão |
| `MódFiltrosExibição` (22 KB) | Mostra/oculta linhas por critério (`FILTIDENT`, `FILTCARACT`, `FILTQCI`, `FiltroMemorialCompleto`…) |
| `MódInsExcCampos` (20 KB) | Insere/exclui linhas preservando fórmulas (`InsLinOrcInfra`, `ExcLinOrcInfra`, `InsLinOrcInfAguPotDre`) |
| `MódAtualizaVersão` | Migra dados de uma versão do FRE para outra usando o catálogo de nomes |
| `MódSalvaSIOPI` | `SalvaParaSIOPI` — salva cópia `.xlsx` na mesma pasta (o SIOPI não aceita `.xlsb`) |
| `MódAtualizaGrafCron` | Atualiza o gráfico do cronograma |
| `FunxAux` | Utilitários (`Crypt`, `Acento`, `IsSheetPro`, `FormatarBR`, `validationtype`) |

Eventos `Worksheet_Change` / `Worksheet_Activate` / `Workbook_Open` reaplicam
filtros e proteção ao abrir e ao editar.

> **Consequência prática:** abrir o FRE sem habilitar macros deixa o arquivo
> funcional para leitura, mas quebra navegação, inserção de linhas e,
> principalmente, a convergência do Resumo de Valores.

---

## 7. Regras e travas que a planilha impõe

1. **Cálculo iterativo obrigatório** (Trabalho Social ↔ VO).
2. **Soma das incidências de habitação = 100 %** — validador permanente em `4.1!R11`.
3. **Serviços preliminares 1.1–1.4 idênticos** nas três planilhas de custo.
4. **Trava de 95 %** na liberação financeira até habite-se + CND.
5. **Áreas ociosas < 30 %** da área da matrícula (aviso em `2-TERRENO!K18`).
6. **Orçamento não pode ficar abaixo do CUB** de referência.
7. **BDI cartilha forçado** em FAR e Cogestão.
8. Fundações profundas, elevadores e equipamentos condominiais → **infraestrutura**,
   nunca habitação.
9. **Demolição não é custo elegível** — o terreno deve estar livre de ocupação
   para a contratação.
10. **Mínimo 1 árvore por bloco/casa térrea** (item 12.1 da infra).
11. Fotos do terreno: **mínimo 6**, sendo 2 da via de acesso e 1 da testada.

---

## 8. O empreendimento preenchido no arquivo

| Campo | Valor |
|---|---|
| Empreendimento | **Residencial São Gabriel** |
| Local | Rua Ana Pereira Menezes, 197 — São Gabriel — Belo Horizonte/MG — CEP 31.980-065 |
| GPS | −19.859938, −43.921143 |
| Programa / Recursos | MCMV (FAR/FDS) / **FAR** → **Faixa 1** |
| Proponente e Ente Público | **Município de Belo Horizonte** (CNPJ 18.715.383/0001-40) — URBEL |
| Construtora | **KTM Administração e Engenharia Ltda** (CNPJ 26.279.935/0001-42) |
| Responsável técnico | Renato Rodriges Rocha — CREA/MG 22335/D |
| Tipologia | **Condomínio**, 1 condomínio |
| UH | **184 apartamentos** · 2 blocos · 14 pavimentos · 8 UH/pavimento-tipo |
| Elevadores | 2 por bloco → **4 no total** |
| Enquadramento | **Superior** → **R$ 176.000/UH** (recorte B1) → teto ≈ **R$ 32,38 mi** |
| Sistema construtivo | Alvenaria Estrutural (não misto) |
| Terreno | 3.285,48 m² — **doado pelo Ente Público**; laudo revertido em aumento de área das UH |
| Uso do terreno | viário 868 m² (26,4 %) · praças/áreas verdes 856,84 m² (26,1 %) · outros equip. 1.257,57 m² (38,3 %) |
| Áreas verdes | 766,43 m² (23,3 %) · 100 mudas a plantar |
| Vagas | 37 carro · 18 moto · 56 bicicletário |
| Equipamentos | 7 — depósito de lixo, espaço de convivência, playground, portaria/guarita, sala do síndico, biblioteca, bicicletário |
| Instalações | rede de gás/central GLP **sim**; aquecimento solar **não**; fotovoltaico **não** |
| Selo Casa Azul | não optante |
| Interferência | **rede de drenagem pluvial atravessa o terreno e deverá ser remanejada** |
| Regime de construção | não preenchido (`(escolha)`) — reportado como "Cogestão sem desoneração" por *default* |

> **Estado de preenchimento:** identificação, terreno e caracterização estão
> preenchidos; **as abas de custo (4.x), o Resumo de Valores e o cronograma estão
> zeradas.** ISS não informado (alerta ativo: *"Preencher Alíquota do ISS"*),
> BDI não calculado, incidências de habitação em *"Falta 100,00 %"*, tipologias
> (3.2) vazias.

---

## 9. Pontos de atenção encontrados

1. **Dependência de Excel 365.** `5-RESUMO!U11` usa `UNIQUE`/`FILTER`/`VSTACK`.
   Em versões antigas a linha de responsáveis pelas contrapartidas quebra.
2. **O `.xlsb` não abre no LibreOffice** (falha de carregamento). Para
   conferência fora do Excel é preciso a macro `SalvaParaSIOPI` (gera `.xlsx`)
   ou um extrator próprio.
3. **`PlanCalc_*` desacoplado do orçamento** — a transcrição das quantidades é
   manual e, portanto, ponto de erro não detectado por fórmula.
4. **Duplicação `PlanCalc_*` × `PlanCalc_*INI`** — memórias de cálculo idênticas
   para infra incidente e não incidente, mantidas em paralelo.
5. **`AA470 = SUM(...)/2`** funciona porque as linhas de subtotal estão dentro do
   intervalo. Inserir uma linha de subtotal sem a contrapartida quebra o total
   silenciosamente.
6. **`NOW()` em `1-IDENT!Z7` e `TODAY()` no BDI** tornam o arquivo volátil: o BDI
   desonerado muda de ano para ano (2,7 % em 2026 → 1,8 % em 2027) mesmo sem
   ninguém editar a planilha.
7. Erro de digitação preservado na base: `1.1-CHECKLIST` tem numeração repetida
   (vários "15.0", "11.0", "12.0") na coluna de itens.

---

## 10. Como a extração foi feita (reprodutível)

`ferramentas/xlsb.py` é um parser **BIFF12** independente (sem dependências além
da biblioteca padrão) que lê:

- registros do `workbook.bin` (abas, `BrtName`, `BrtExternSheet`);
- células de todos os tipos (`BrtCellRk`, `BrtCellReal`, `BrtCellIsst`, …);
- **fórmulas**, decompilando o `rgce` token a token (`PtgRef`, `PtgArea`,
  `PtgRef3d`, `PtgName`, `PtgFunc`, `PtgFuncVar`, `PtgAttr`, `PtgList`…);
- **fórmulas compartilhadas e matriciais** (`BrtShrFmla` 427, `BrtArrFmla` 426),
  resolvendo o `PtgExp` de cada célula contra a faixa dona;
- tabela de funções completa, inclusive as `_xlfn.*` (`IFERROR`, `SUMIFS`,
  `UNIQUE`, `FILTER`, `VSTACK`).

```bash
pip install oletools          # só para o VBA
python3 ferramentas/dump.py   # gera out/<aba>.txt com valor + fórmula por célula
python3 ferramentas/tab.py '4.3-CUSTOS INFRA INTERNA' N,O,V,W,X,Y,Z,AA 6 472
```

Detalhes do formato que custaram a descobrir e ficaram registrados no código:

| Ponto | Regra correta no BIFF12 |
|---|---|
| Classe do token | `p ≥ 0x60 → base = p−0x40`; `p ≥ 0x40 → base = p−0x20` |
| `PtgStr` | contador de caracteres em **2 bytes** (não 4, ao contrário de `XLWideString`) |
| `PtgRef` / `PtgArea` | linha/coluna **absolutas**, mesmo com o bit "relativo" ligado |
| `PtgRefN` / `PtgAreaN` | deslocamentos relativos à célula — só em fórmula compartilhada |
| `PtgExp` | payload de **4 bytes** (só a linha); a coluna vem da célula |
| `PtgAttr` com `grbit & 0x10` | `SUM` otimizado de operando único — sem ele, `=SUM(A1:A9)` vira `=A1:A9` |
| `PtgList` | `0x18` + eptg `0x19` + 12 bytes (referência estruturada de tabela) |
| Funções de aridade fixa | `IFERROR` = 2 argumentos (23.497 ocorrências no arquivo) |

---

## 11. Mapa de dependências (resumo)

```
1-IDENTIFICAÇÃO ─ ProgramaProp, RecursosProp, RegCons
      │
      ├─► 0-BEM-VINDO (quais abas existem)
      ├─► BDI (regime: desonerado / adm. direta / beneficiários)
      └─► 5-RESUMO (FAR)  ou  5-QCI (FDS)

2-TERRENO ─ VlrTerProp, TerrDoado, área ──────────┐
3-CARACTERIZAÇÃO ─ Tipologia, Enquadramento, qtdUH┤
                                                  ▼
          Valores_municipío ── recorte ── VALOR MÁXIMO POR UH

4.1 CUSTOS HABITAÇÃO ──► CusTotSemBdi ──► 4.1.1 ÁREA EQUIVALENTE ──► R$/m² vs CUB
   │  incidências 1.1–1.4 ────────────┐
   │  ISS ──► BDI ──► BDI_HIS ────────┤
   ▼                                  ▼
  CTH                       4.2 / 4.3 / 4.3.1 / 4.4  ──► CTEQUIPCOMUM, CTINFRA, CTINFRAEXT
   └──────────────┬───────────────────┘
                  ▼
        5-RESUMO DE VALORES (FAR)
        CTC ─► TS (gross-up, iterativo) ─► VO ─► VI
                  │
                  └─ incidências CTC ──► 6-CRONOGRAMA ──► evolução física ──► liberação (trava 95 %)
```
