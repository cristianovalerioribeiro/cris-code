# Pendências do site · decisões do Cristiano

Espelha o *Caderno de Definições do Site (02/10/2026, v01)*. Nada aqui foi decidido
por quem construiu: onde foi preciso escolher algo para o site existir, ficou o que
já estava no ar ou o que as Regras mandam, e está marcado abaixo.

## Travam a publicação

| Item | Como está no site novo | Onde muda |
|---|---|---|
| **1.1 Canal de contato** | Formulário pronto, mas **não envia**: avisa que é prévia. | `FORMULARIO_ATIVO` no `build.py` liga o Netlify Forms; falta definir e-mail, WhatsApp, telefone e LinkedIn. |
| **1.2 Sair da prévia** | `noindex` em todas as páginas, `robots.txt` bloqueando e aviso no rodapé. | `PREVIA = False` no `build.py` e apagar a linha `X-Robots-Tag` em `_headers`. |
| **1.3 Quem você é, de forma verificável** | "Quem conduz" com formação e trajetória, **sem foto, sem LinkedIn, sem CNPJ**. No lugar da foto, o símbolo da marca. Schema `Person` sem `sameAs`. | Foto e URL do LinkedIn entram em `paginas/00-inicio.html` e `paginas/70-sobre.html`; `sameAs` em `json_ld()` do `build.py`. |
| **1.4 A prova** | **Nenhum número de experiência**. Os R$ 324 mi não aparecem (atribuição com a TRAL3 pendente). | Faixa de credenciais logo abaixo do hero, em `paginas/00-inicio.html`. |

## Divergências entre documentos

| Item | O que foi usado | Observação |
|---|---|---|
| **2.1 Tipografia** | Manrope + Inter, como está no ar. | Manual v2.0 pede Cambria + Arial. Trocar é mudar duas linhas em `assets/site.css`. |
| **2.2 Nome do trabalho inicial** | "Diagnóstico de estruturação", como está no ar e como você pediu. | O Manual v2.0 ainda diz "Setup de Estruturação" e precisa ser corrigido. |
| **2.3 Ordem das vertentes** | **Empresas · Empreendimentos · Capital** em todo o site (menu, home, rodapé), como nas Regras e no Manual p8. | A inconsistência do v12 (menu numa ordem, cards em outra) acabou. Se a ordem for outra, muda em `VERTENTES` no `build.py` e nos blocos da home. |

## Visual

| Item | Como está |
|---|---|
| **3.1 Intensidade do cenário** | Redesenhado: implantação isométrica com quadras, massas e, à frente, o lote tracejado com **três volumetrias alternativas** sobre ele (o MODELAR desenhado). CSS puro no scroll, sem biblioteca. No celular fica bem mais discreto. |
| **3.2 Marinho no hero** | Mantido (o marinho "abre capítulos", Manual p37). Páginas internas claras. |
| **3.3 Movimento nas internas** | Só a home tem cenário. |

## Conteúdo que falta

| Item | Como está |
|---|---|
| **4.1 Cases** | Sem bloco de cases. |
| **4.2 Seção "Inteligência"** | Não criada. Simulador e comparador ganharam destaque **dentro de Empreendimentos**, na home (quadro de alternativas) e no rodapé ("Para decidir"). |
| **4.3 GERIC, plano empresário, apoio à produção, SBPE** | Fora do site. Só "financiamento à produção na Caixa" numa FAQ de Capital, como no v12. |
| **4.4 Página de estudo de viabilidade** | Não criada. |
| **4.5 Frase de proteção regulatória** | **Não publicada** (aguarda revisão jurídica). |
| **4.6 Nomes fixos dos entregáveis** | Não usados: os entregáveis estão descritos, sem nome próprio. |

## Textos em teste

| Onde | No ar | Alternativa do Caderno |
|---|---|---|
| H1 da home | Para realizar mais, é preciso estruturar melhor. | Entre uma oportunidade e sua realização existe muito a estruturar. |
| CTA do hero | Conversar sobre uma oportunidade | Analisar meu caso (é o CTA do cabeçalho) |
| "Advisor estratégico" | Não usado | Uso público ainda em aberto |

## Outros pontos que surgiram na reconstrução

- **Endereços novos**: `/setup/` virou `/como-comeca/` (o nome "setup" foi abandonado) e
  terreno, simulador e obra parada passaram para dentro de `/empreendimentos/`. Os
  antigos redirecionam (`_redirects`).
- **"Crédito imobiliário dos dois lados"** aparece na faixa de credenciais e em /sobre/,
  como no site atual. No Caderno §09 esse item ainda está como "[confirmar]".
- **Imagem de compartilhamento (`og.png`)** é a do v12. Vale refazer quando o H1 fechar.
