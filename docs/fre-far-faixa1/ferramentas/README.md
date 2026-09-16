# Extrator de .xlsb (BIFF12)

Parser independente usado para analisar o FRE da CAIXA, que o LibreOffice não
consegue abrir. Só usa a biblioteca padrão do Python (o VBA precisa de `oletools`).

| Arquivo | O que faz |
|---|---|
| `xlsb.py` | Parser BIFF12: abas, células, **fórmulas** (decompila o `rgce`), nomes definidos, fórmulas compartilhadas e matriciais |
| `dump.py` | Gera `out/<aba>.txt` com `célula: =fórmula {valor}` para todas as abas |
| `tab.py` | Recorta um intervalo em forma de tabela: `tab.py '<aba>' A,B,C <lin1> <lin2> [f]` |
| `comments.py` | Extrai os comentários de célula (`xl/comments*.bin`) |

```bash
python3 dump.py                                   # tudo
python3 tab.py '4.1-CUSTOS HABITAÇÃO' N,O,R,S 13 44
python3 tab.py 'BDI' M,N,O,P,Q,R 1 10 f           # 'f' mostra a fórmula
```

Os arquivos esperam `FRE.xlsb` no diretório corrente (ajuste o caminho no topo
de cada script para outro arquivo).

As armadilhas do formato binário estão comentadas em `ANALISE.md` §10 —
principalmente a classe dos tokens, o `PtgStr` de 2 bytes, o `PtgAttrSum` e o
`PtgExp` de 4 bytes.
