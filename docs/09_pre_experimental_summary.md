# Síntese Pré-Experimental

## Objetivo

Consolidar os resultados da trilha de previsão (notebooks 10–17) em uma visão única, operacional e auditável, sem promover a previsão ao status de validação experimental.

---

## Resultados Consolidados

### Escalonamento de visibilidade
- **Contraste:** Diferenciação clara entre regimes linear ($N$) e quadrático ($N^2$) para tempos de observação $\tau \approx 1.0$ s.
- **Valores de N*:** Cruzamento de visibilidade ($N^*$) identificado na faixa de 35–40 unidades para os parâmetros calibrados.
- **Faixa de Separação:** A distinção é mais pronunciada na janela de $N \in [20, 100]$, com pico de distinguibilidade em $N \approx 50$.

### Calibração paramétrica
- **Valores Plausíveis:** $a \approx 0.014$ (regime A) e $b \approx 0.00014$ (regime B).
- **Interpretação:** Estes valores são tratados estritamente como uma estimativa de plausibilidade paramétrica baseada em referências físicas de decoerência, sem constituir medição real.

### Robustez
- **Ruído e Jitter:** Em cenário de estresse, o contraste sobrevive a ruídos de decoerência basal de 30% ($\gamma_{th}$) e jitter temporal de 5% ($\tau$).
- **Sobrevivência:** O sinal de distinguibilidade permanece acima do piso estatístico de 10% para $N$ entre 20 e 67.

### Janela de detectabilidade
- **Sistema físico mais promissor:** Interferometria molecular (massiva).
- **N recomendado:** Janela mesoscópica de $30 < N < 70$.
- **Tempo de observação alvo:** $\tau \approx 1.0$ s.
- **Precisão mínima desejável:** Erro de medição de contraste interferométrico $< 5\%$.

---

## Sistema-alvo prioritário

O sistema de **interferometria molecular** (ex: macromoléculas massivas) parece o mais plausível no estado atual do modelo, por operar naturalmente na faixa de $N$ onde o escalonamento quadrático diverge do linear sem que a decoerência total ocorra instantaneamente (como em gases frios de alto $N$).


## Encadeamento com MPV-59

A comparação de faixa operacional com literatura primária foi consolidada em `docs/13_feasibility_ranges.md` para manter separação entre síntese de simulação e decisão de viabilidade experimental.

---

## Restrições

- Este documento **não constitui validação experimental**.
- Não altera o **core** do repositório.
- Não transforma o escalonamento $N^2$ em uma lei física derivada.
- Não transforma $N^*$ em um valor confirmado fisicamente; permanece uma hipótese operacional.

---

## Status Epistemológico

- Categoria: PREVISÃO
- Pertence ao Core: NÃO
- Função: consolidar a ponte entre simulação e teste possível
