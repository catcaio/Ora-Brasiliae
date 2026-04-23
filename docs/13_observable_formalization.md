# Formalização do Observável

## Objetivo

Estabelecer uma definição operacional única para o observável de interesse e um procedimento mensurável/auditável para comparação entre os regimes linear ($N$) e quadrático ($N^2$) de perda de visibilidade.

---

## Escopo

Este documento formaliza **o que é medido** e **como é medido** no bloco experimental. Não reivindica validação física do modelo.

---

## Observável primário

### Definição

Para cada corrida experimental $r$, número de componentes $N$ e tempo de integração $\tau$:

$$
V_r(N,\tau)=\frac{I_{\max,r}(N,\tau)-I_{\min,r}(N,\tau)}{I_{\max,r}(N,\tau)+I_{\min,r}(N,\tau)}
$$

onde:
- $I_{\max,r}$ = intensidade máxima da franja no intervalo de aquisição;
- $I_{\min,r}$ = intensidade mínima da franja no intervalo de aquisição.

### Normalização de referência

Definir um fator de normalização por sessão:

$$
V_{\text{ref}} = \text{mediana}\left( V_r(N=1,\tau_{\text{ref}}) \right)
$$

e usar:

$$
\tilde{V}_r(N,\tau)=\frac{V_r(N,\tau)}{V_{\text{ref}}}
$$

com truncamento físico em $[0,1]$ após propagação de incerteza.

---

## Como medir (protocolo mínimo de aquisição)

1. **Calibração de baseline**
   - medir $N=1$ para estimar $V_{\text{ref}}$;
   - registrar temperatura, pressão, jitter temporal e potência de excitação.
2. **Varredura de $N$**
   - adquirir ao menos 5 valores de $N$ na janela recomendada ($30\le N\le 70$);
   - coletar no mínimo 10 corridas independentes por ponto.
3. **Extração de contraste por corrida**
   - estimar $I_{\max,r}$ e $I_{\min,r}$ na mesma janela temporal;
   - calcular $V_r$ e $\tilde{V}_r$.
4. **Agregação por ponto experimental**
   - média robusta: $\bar{V}(N,\tau)=\text{mediana}(\tilde{V}_r)$;
   - dispersão: MAD e desvio-padrão amostral.
5. **Controle de qualidade (QC)**
   - rejeitar corrida com saturação de detector;
   - rejeitar corrida com drift de fase fora do envelope pré-registrado;
   - registrar motivo da rejeição (sem deleção silenciosa).

---

## Métricas de decisão

### 1) Ajuste de modelos concorrentes

- Modelo linear:

$$
\tilde{V}(N,\tau)=\exp\left(-a\,N\,\tau/2\right)
$$

- Modelo quadrático:

$$
\tilde{V}(N,\tau)=\exp\left(-b\,N^2\,\tau/2\right)
$$

com $a,b\ge 0$.

### 2) Métrica primária de distinguibilidade

Usar **diferença de informação** entre modelos (AIC ou BIC), com regra pré-registrada:

- evidência fraca: $\Delta \in [0,2)$
- evidência moderada: $\Delta \in [2,6)$
- evidência forte: $\Delta \ge 6$

### 3) Métrica secundária

- erro residual normalizado (RMSE normalizado);
- consistência do sinal em bootstrap de corridas.

---

## Incerteza e auditabilidade

### Incerteza mínima a reportar

- incerteza de $I_{\max}$ e $I_{\min}$ por corrida;
- incerteza propagada de $V_r$;
- intervalo de confiança para $\bar{V}(N,\tau)$;
- sensibilidade da decisão a exclusões de QC.

### Artefatos obrigatórios

- tabela bruta por corrida (`run_id`, `N`, `tau`, `I_max`, `I_min`, `V`, `V_norm`, `qc_flag`, `qc_reason`);
- script/notebook de ajuste reproduzível;
- relatório com parâmetros ajustados, ICs e métrica de comparação;
- hash/versão dos artefatos usados no ajuste.

---

## Critérios de conclusão do bloco (MPV-53)

O bloco é considerado concluído quando houver:

1. definição formal única do observável (este documento);
2. procedimento explícito de medição e QC;
3. métrica de decisão pré-registrada entre modelos;
4. pacote mínimo de reprodutibilidade/auditoria definido.

---

## Status epistemológico

- Categoria: SUPORTE À PREVISÃO
- Pertence ao Core: NÃO
- Função: formalização operacional do observável e do método de medição
