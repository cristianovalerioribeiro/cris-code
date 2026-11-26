# -*- coding: utf-8 -*-
from bookkit import *
from chakra_data import CHAKRAS

def build():
    H = []
    H.append(h1("f-atend", "Fichas de registro", "Para imprimir quantas vezes for preciso"))
    H.append(p("Estas fichas acompanham o Manual de Radiestesia Terapêutica. O manual é fixo e não se escreve nele; cada atendimento é registrado aqui ou num caderno com os mesmos campos. Imprima as páginas necessárias antes de cada sessão. Os números de gráfico (G e C) são os do manual."))
    H.append(h2("ficha-atendimento", "Ficha de atendimento"))
    H.append(p("Protocolo nº ______ · Nome completo _______________________________ · Nascimento ____/____/______ · Data ____/____/______ · Início ____:____ · Modo: presencial / distância / auto · Testemunho: ______________ · Queixa: ______________________________________________ · Sinais de alarme: sim / não (encaminhado: ____) · Consentimento: sim · Terceiro incluído e sua autorização: ______________ · Pergunta exata (quando diferente da do manual): ______________________________"))
    H.append(p("<b>Abertura</b> · calibração: ok / falhou · autoauditoria inicial ____% · Posso ____ Devo ____ Pronto ____"))
    H.append(form_table(["Triagem", "Antes", "Meta", "Depois"], 0) .replace("<tbody></tbody>", "<tbody>" + "".join(f"<tr><td>{x}</td><td></td><td></td><td></td></tr>" for x in ["1A vitalidade geral (UB)", "1A físico", "1A etérico", "1A emocional", "1A mental", "1A espiritual", "1A casa / trabalho", "1B mental % (chakras)", "1B emocional % (chakras)", "1B espiritual % (chakras)", "1B físico % (chakras)", "1C proteção / tamanho / rompimento", "1D polaridade / interferência", "1E áreas (eu, rel., fam., fin., prof., missão)", "Decisão da triagem"]) + "</tbody>"))
    H.append(form_table(["Chakra", "%", "Giro", "Amplitude", "Forma", "Posterior", "Estado", "Prioridade"], 0).replace("<tbody></tbody>", "<tbody>" + "".join(f"<tr><td>{k} {CHAKRAS[k]['nome']}</td>" + "<td></td>" * 7 + "</tr>" for k in range(1, 8)) + "</tbody>"))
    H.append(form_table(["Chakra", "Setor e %", "Item", "Origem", "Época", "Contexto", "Técnica e eficácia", "Dose", "Remedida (%, giro, forma)", "Carga residual"], 5))
    H.append(p("<b>Fechamento</b> · triagem depois (acima) · conferência: ok · proteção e selamento: ok · pendências: ______________________ · orientações: ______________________ · remedir em ____ dias · encaminhamento: ____________ · autoauditoria final ____% · término ____:____"))
    H.append(h2("ficha-remedida", "Registro de remedida"))
    H.append(p("Uma linha por data, com as colunas da planilha de acompanhamento."))
    H.append(form_table(["Data", "Chakra", "%", "Giro", "Bovis geral", "Yin-yang", "Aura prot./tam./regen.", "Prática cumprida", "Tratamento (gráfico, pedra, potencializador, tempo)", "Obs."], 10))
    H.append(h2("ficha-laudo", "Laudo para a pessoa"))
    H.append(p("Campos energéticos (mental, emocional, espiritual, físico: % de desequilíbrio e chakras afetados) · Chakras (os sete: desequilíbrio sim/não, %, tipo de atividade, afeta o corpo físico) · Campo áurico (proteção, tamanho, cores em falta e em excesso) · Energia de saúde (referência 6.500) · Áreas da vida (péssimo a excelente) · Hipótese energética e harmonização aplicada · Orientações e remedida · Assinatura. Rodapé fixo: “Leitura energética complementar; não substitui diagnóstico nem tratamento médico ou psicológico.”"))



    H.append(pagebreak())
    H.append(h2("f-limp", "Ficha de limpeza energética de pessoa (Parte VII)"))
    H.append(p("Nome completo ____________________________ · Data ____/____/______ · Modo: presencial / distância / auto · Permissão: P ____ D ____ E ____ · Autoauditoria inicial ____%"))
    H.append(form_table(["Medida", "Antes", "Depois", "Reforço (data)"], 0).replace("<tbody></tbody>", "<tbody>" + "".join(f"<tr><td>{x}</td><td></td><td></td><td></td></tr>" for x in ["Vitalidade (UB)", "Carga total (0 a 100)", "Aura: tamanho", "Aura: proteção (%)", "Aura: integridade (camada)", "Aura: conteúdo", "Chakras abaixo de 70"]) + "</tbody>"))
    H.append(form_table(["Nº", "Item removido (G64)", "Onde (corpo sutil, chakra, lado)", "Sustentação (G58, G59)", "Técnica (G65) e verbo (G68)", "Selamento (G67)", "Concluído?"], 5))
    H.append(p("Pendências: ______________________________ · Orientações: ______________________________ · Autoauditoria final ____% · Retorno em ____ dias"))

    H.append(pagebreak())
    H.append(h2("f-esp", "Ficha de ambiente (Parte VIII)"))
    H.append(p("Endereço ____________________________________ · Moradores ______________________ · Data ____/____/______ · Planta orientada: sim / não · Permissão: P ____ D ____ E ____ · Casa inteira (G2): antes ____ depois ____ · Bovis antes ______ depois ______"))
    H.append(form_table(["Cômodo", "Giro (H/A)", "% antes", "Fonte (G66)", "Posição (planta)", "Técnica (G71) e gráfico", "Tempo", "% depois", "Pendência"], 8))
    H.append(p("Nós e sobreposições marcados na planta: ______ · Cama ou mesa afetada: sim / não · Remediação proposta: ______________________ · Proteção do imóvel: ______________ · Reavaliar em ____ dias"))

    H.append(pagebreak())
    H.append(h2("f-roda", "Roda da Vida (preenchida pela pessoa antes da medição)"))
    H.append(p("Marque de 0 (centro) a 10 (borda) o quanto está satisfeito com cada área hoje e ligue os pontos. O terapeuta mede o G24 depois, sem ver a roda; a conversa é sobre as diferenças."))
    H.append('<img src="figs/roda_da_vida.svg" style="width:100%" alt="Roda da Vida"/>')
    H.append(h2("f-decisoes", "Registro de decisões (diário de acertos)"))
    H.append(form_table(["Data", "Pergunta exata", "Formulação 2 e 3 (convergiram?)", "Resposta (G84) e grau (G2)", "Momento (G85, G87)", "O que a pessoa decidiu", "Revisão: o que aconteceu, em que data"], 8))
    H.append(pagebreak())
    H.append(h2("f-empresa", "Ficha de decisão empresarial (matriz opções × critérios)"))
    H.append(p("Decisão: ______________________________ · Data ____/____/______ · Quem decide: ______________________ · Empresa: ______________________ · Autoauditoria inicial ____% · Opções numeradas (G109 ou G110): 1 ______________ 2 ______________ 3 ______________ 4 ______________"))
    H.append(form_table(["Critério (G106, G107 ou próprio)", "Peso (alto, médio, baixo)", "Opção 1 (%)", "Opção 2 (%)", "Opção 3 (%)", "Opção 4 (%)"], 13))
    H.append(p("Decisão por opção (G84, duas formulações): 1 ________ 2 ________ 3 ________ 4 ________ · Grau (G2): ____ ____ ____ ____ · Momento (G85): ______________ · Pontos fracos a confirmar com profissional: ______________________________ · O que a pessoa decidiu: ______________________ · Revisão em 90 dias: ______________________"))
    H.append(pagebreak())
    H.append(h2("f-planta", "Planta do imóvel"))
    H.append(p("Desenhe a planta na grade abaixo (norte para cima; anote o norte), com o nome de cada cômodo e a posição da cama, da mesa de trabalho e da porta de entrada. Marque as faixas e os nós encontrados, os pontos de fonte e a posição dos gráficos."))
    H.append('<img src="charts/G72.svg" style="width:100%" alt="grade"/>')
    H.append(end())
    return "".join(H)
