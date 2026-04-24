# Pacote de Execução Pré-Bancada (Pre-Bench Package)

## 1. Objetivo
Consolidar os requisitos operacionais e técnicos para a execução da fase pré-experimental, baseando-se no protocolo congelado em `docs/14_protocol_freeze.md`. Este documento serve como o guia prático de execução para a coleta de dados e auditoria de prontidão.

## 2. Definições Operacionais
- **Sistema-Alvo Prioritário:** Interferometria molecular mesoscópica (macromoléculas/fulerenos).
- **Observável Oficial:** Visibilidade Interferométrica ($V$), normalizada para $V=1$ em $N=1$.
- **Janela Operacional:** 
  - $N \in [30, 70]$.
  - Pontos mínimos: 5 valores distintos de $N$.
  - Tempo de integração ($\tau$): $1.0$ segundo por corrida.
- **Precisão Requerida:** Erro relativo de visibilidade $< 5\%$.

## 3. Especificação do Aparato (Resumo)
- **Câmara de Vácuo:** Regime UHV ($10^{-8} - 10^{-9}$ mbar).
- **Interferômetro:** Geometria de três grades (Talbot-Lau ou KDTLI).
- **Estabilidade:** Isolamento vibracional ativo/passivo da bancada e monitoramento térmico dos componentes críticos.

## 4. Controles e Baseline
- **Baseline Ambiental:** Caracterização obrigatória da decoerência térmica e de fundo com amostra de controle ($N=1$).
- **Controle de Jitter:** Monitoramento síncrono da estabilidade temporal do interferômetro durante $\tau$. Corridas fora da banda de tolerância devem ser marcadas como inválidas automaticamente.

## 5. Critérios de Avaliação (Congelados)
- **Métrica Primária:** Comparação de modelos Linear ($N$) vs Quadrático ($N^2$) via **AIC**.
- **Métrica Secundária:** p-value $< 0.05$ para a separação das curvas de ajuste.
- **Sucesso:** Melhor ajuste persistente e estatisticamente superior (menor AIC) para o regime quadrático.
- **Fracasso:** Melhor ajuste para o regime linear, indistinguibilidade estatística ou domínio de ruído instrumental.

## 6. Formato dos Dados e Artefatos
Os dados experimentais devem ser registrados no formato CSV com as seguintes colunas obrigatórias:
- `timestamp`: UTC ISO 8601.
- `N`: contagem de componentes.
- `V`: visibilidade medida.
- `P_chamber`: pressão na câmara (mbar).
- `T_block`: temperatura do bloco interferométrico (K).
- `jitter_metric`: indicador de estabilidade temporal.

**Artefatos de Saída por Campanha:**
- `raw_runs.csv`: dados brutos de todas as corridas.
- `run_metadata.json`: ambiente, versões de software e hashes de integridade.
- `fit_report.md`: relatório de ajuste e decisão estatística.
- `readiness_report.md`: checklist final de conformidade com o aparato.

---
## Status Epistemológico
- **Categoria:** SUPORTE À PREVISÃO (PACOTE OPERACIONAL)
- **Pertence ao Core:** NÃO
- **Função:** Guiar a execução prática e a coleta de dados auditáveis.
