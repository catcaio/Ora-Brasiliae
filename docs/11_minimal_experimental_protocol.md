# Protocolo Experimental Mínimo

## Objetivo

Definir um protocolo mínimo de bancada para tentar distinguir operacionalmente os regimes linear e quadrático de perda de visibilidade.

> Nota: A definição formal do observável, métricas de decisão e pacote auditável de artefatos estão consolidados em `docs/13_observable_formalization.md`.

---

## Sistema Prioritário

**Interferometria Molecular Mesoscópica.** Sistemas de macromoléculas (ex: fulerenos ou complexos moleculares massivos) operando com contagens de átomos/componentes na faixa mesoscópica.

---

## Observável

- **Visibilidade Interferométrica ($V$):** Contraste das franjas de interferência medido em função do número de componentes $N$.
- **Definição Operacional:** $V = (I_{max} - I_{min}) / (I_{max} + I_{min})$, normalizado para $V=1$ em $N=1$.

---

## Faixa Operacional Recomendada

- **N alvo:** Janela de $N \in [30, 70]$ (onde a separação $N^2$ vs $N$ é máxima).
- **Tempo de observação ($\tau$):** Estabilização de $\approx 1.0$ segundo por corrida.
- **Precisão necessária:** Erro relativo na medida de visibilidade $< 5\%$.
- **Repetibilidade mínima:** 10 corridas independentes por ponto de $N$.

---

## Estratégia Comparativa

1. Medir o decaimento do contraste interferométrico para pelo menos 5 valores distintos de $N$ dentro da janela mesoscópica.
2. Realizar o ajuste (fitting) dos dados aos dois modelos concorrentes:
   - **Regime A (Linear):** $V(N) = \exp(-a \cdot N \cdot \tau / 2)$
   - **Regime B (Quadrático):** $V(N) = \exp(-b \cdot N^2 \cdot \tau / 2)$
3. Comparar o erro residual e a métrica de distinguibilidade para determinar qual modelo melhor descreve o escalonamento observado.

---

## Controles Necessários

- **Baseline Ambiental:** Caracterização da decoerência térmica de fundo com amostra de $N=1$.
- **Controle de Jitter:** Monitoramento da estabilidade temporal do interferômetro durante o tempo de integração $\tau$.
- **Controle Térmico:** Manutenção de temperatura criogênica ou vácuo ultra-alto para minimizar colisões basais.
- **Repetição Estatística:** Acúmulo de dados suficiente para que o desvio padrão da visibilidade seja menor que a diferença prevista entre regimes.

---

## Critério mínimo de interesse

Um resultado será considerado promissor se:
- Houver uma separação estatisticamente consistente (p-value < 0.05) entre as curvas dos modelos A e B na faixa operacional prevista.
- A assinatura de decaimento anômalo ($N^2$) persistir mesmo após o controle rigoroso de ruídos basais e jitter.

---

## Restrições

- Este é um documento de **protocolo**, não de validação.
- Não implica que o experimento já foi realizado.
- Não altera o status epistemológico do **core** do repositório.

---

## Status Epistemológico

- Categoria: PREVISÃO
- Pertence ao Core: NÃO
- Função: preparar a transição para possível teste real
