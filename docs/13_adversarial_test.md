# Teste Adversarial (MPV-65)

## Objetivo

Simular um **falso positivo** onde o sistema gerador real segue dinâmica linear, mas um artefato instrumental (drift correlacionado com `N`) induz ajuste aparentemente melhor para o modelo quadrático.

---

## Procedimento reprodutível

Executar:

```bash
python scripts/simulate_false_positive.py --seed 65
```

Saídas esperadas:

1. Logs estruturados JSON no stdout com:
   - `simulation_config`
   - `fit_results`
   - `adversarial_assessment`
2. Artefato auditável em:
   - `outputs/adversarial_false_positive_dataset.csv`

---

## Critério de validação auditável

A simulação é considerada válida quando:

- o dataset CSV é gerado com a mesma contagem de pontos para a janela `N`;
- o evento `adversarial_assessment` é emitido;
- o campo `false_positive_detected` é `true`, indicando que a seleção por AIC favoreceu indevidamente o regime quadrático.

---

## Interpretação

Este teste **não valida** o regime quadrático como efeito físico. Ele valida apenas que uma combinação de drift + ruído pode induzir classificação incorreta se os controles não forem suficientemente rígidos.

---

## Relação com riscos previamente mapeados

O cenário exercita explicitamente os riscos já listados em `docs/10_false_positive_risks.md`, sobretudo:

- drift instrumental;
- seleção enviesada por métrica;
- ruído estatístico confundido com assinatura física.

---

## Status Epistemológico

- Categoria: SUPORTE À PREVISÃO
- Pertence ao Core: NÃO
- Função: teste adversarial de robustez interpretativa
