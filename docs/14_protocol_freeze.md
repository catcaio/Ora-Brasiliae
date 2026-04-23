# Protocol Freeze — Congelamento do Protocolo de Validação

## 1. Objetivo
Este documento estabelece o congelamento formal dos critérios, parâmetros e procedimentos para a validação pré-experimental do programa Ora Brasiliae. O congelamento visa garantir a integridade da análise e evitar o ajuste "post-hoc" de critérios de sucesso.

## 2. Parâmetros Físicos e Operacionais
- **Observável Oficial:** Visibilidade Interferométrica ($V$), definida como o contraste das franjas de interferência normalizado ($V=1$ em $N=1$).
- **Modelos Comparados:**
  - Modelo Linear (Padrão): $V(N) = \exp(-a N \tau / 2)$
  - Modelo Quadrático (Ora): $V(N) = \exp(-b N^2 \tau / 2)$
- **Janela de Observação ($N$):** $N \in [30, 70]$.
- **Tempo de Integração ($\tau$):** $1.0$ segundo por corrida.

## 3. Requisitos de Precisão
- **Erro Relativo Máximo:** $< 5\%$ na medida de visibilidade.
- **Poder Estatístico:** Repetição de pelo menos 10 corridas por ponto de $N$. O desvio padrão deve ser inferior à separação teórica entre as curvas dos modelos concorrentes na janela mesoscópica.

## 4. Critérios Estatísticos e Decisão
- **Métrica Primária:** Critério de Informação de Akaike (AIC).
- **Métrica Secundária:** p-value $< 0.05$ para a separação das curvas de ajuste.
- **Regra de Decisão:** O modelo com o **menor AIC** será selecionado como o melhor descritor dos dados. O `delta_aic` deve ser reportado para qualificar a força da distinção.

## 5. Condições de Sucesso e Fracasso
- **Sucesso:** Identificação estatisticamente consistente do regime quadrático ($N^2$) como o melhor ajuste (menor AIC) dentro da janela mesoscópica, após controle de ruídos.
- **Fracasso:** 
  - Melhor ajuste para o modelo linear ($N$).
  - Indistinguibilidade estatística entre os modelos ($delta\_aic$ insignificante).
  - Persistência de ruídos basais acima da sensibilidade do observável.

## 6. Regras de Blind Test
1. O mapeamento entre a identificação dos modelos (ex: "Modelo A" vs "Modelo B") e a natureza física (Linear vs Quadrático) deve ser mantido em registro selado sob custódia externa.
2. Todo o tratamento de dados e cálculo de métricas deve ser realizado antes da abertura do registro.
3. O relatório final com a decisão estatística deve ser congelado antes da revelação da identidade física dos modelos.

## 7. Validação Adversarial (MPV-65)
- O protocolo exige a aprovação no teste adversarial documentado em `docs/13_adversarial_test.md`.
- Procedimento: `python scripts/simulate_false_positive.py --seed 65`.
- **Exigência:** O sistema deve ser capaz de detectar e sinalizar a presença de falsos positivos induzidos por drift instrumental correlacionado com $N$.

---
## Status Epistemológico
- **Categoria:** PROTOCOLO CONGELADO
- **Pertence ao Core:** NÃO
- **Função:** Fixar as regras do jogo antes da fase de bancada real.
