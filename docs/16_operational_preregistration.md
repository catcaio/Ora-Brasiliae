# Pré-Registro Operacional — Fase de Pré-Bancada

## 1. Identificação do Experimento
- **Projeto:** Ora Brasiliae (Fase Experimental I)
- **Status:** Pré-Bancada (Pre-Bench)
- **Protocolo de Referência:** `docs/14_protocol_freeze.md`

## 2. Observáveis e Metodologia
O objetivo central é a medição da visibilidade interferométrica $V$ em função do número de componentes $N$ para distinguir entre decaimento linear e quadrático.

- **Observável Primário:** Visibilidade $V(N)$.
- **Janela Operacional:** $N \in [30, 70]$.
- **Pontos de Coleta:** Mínimo de 5 valores de $N$ distribuídos na janela.
- **Integração:** $\tau = 1.0$s por amostra.

## 3. Hipóteses e Modelos
Serão testados dois modelos concorrentes:
1. **Modelo H0 (Linear):** Decoerência proporcional a $N$.
2. **Modelo H1 (Quadrático):** Decoerência proporcional a $N^2$.

A análise será realizada via **Akaike Information Criterion (AIC)** para determinar qual modelo melhor descreve os dados com menor penalidade por complexidade.

## 4. Critérios de Sucesso (Stop/Go)
- **GO (Sucesso):** $AIC_{H1} < AIC_{H0}$ com evidência estatística ($p < 0.05$ na separação das curvas).
- **STOP (Inconclusivo/Falha):** $AIC_{H0} \leq AIC_{H1}$, ruído instrumental $> 5\%$ da visibilidade, ou incapacidade de manter o baseline UHV.

## 5. Regras de Integridade
- **Blind Analysis:** O mapeamento entre os modelos A/B e as teorias H0/H1 será mantido em registro selado até o fim do ajuste.
- **Auditabilidade:** Toda corrida deve gerar um hash de integridade vinculado ao `timestamp` e aos metadados do aparato.

---
## Status Epistemológico
- **Categoria:** GOVERNANÇA OPERACIONAL
- **Pertence ao Core:** NÃO
- **Função:** Garantir que os critérios de sucesso sejam fixados antes da coleta de dados.
