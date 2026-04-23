# Fitting Pipeline (Linear vs Quadrático)

## Objetivo

Estabelecer um pipeline reprodutível e auditável para comparar dois modelos concorrentes do decaimento de visibilidade interferométrica em função de \(N\):

- **Modelo linear:** \(V(N) = e^{-a N \tau / 2}\)
- **Modelo quadrático:** \(V(N) = e^{-b N^2 \tau / 2}\)

---

## Entrada

CSV com cabeçalhos `N,V` e pelo menos 5 observações:

```csv
N,V
30,0.9200
40,0.8511
...
```

Restrições:

- \(N > 0\)
- \(0 < V \leq 1\)

---

## Execução

```bash
python scripts/fitting_pipeline.py \
  --input data/mpv55_visibility_synthetic.csv \
  --output results/mpv55_fitting_report.json \
  --tau 1.0
```

---

## Saída auditável

O JSON de saída contém:

- hash SHA-256 do input (rastreabilidade);
- parâmetros ajustados (`a` e `b`);
- métricas de ajuste (`RMSE`, `MAE`, `R²`, `RSS`, `AIC`, `BIC`);
- decisão final por menor AIC.

---

## Regra de decisão

- Selecionar o modelo com **menor AIC**.
- Reportar `delta_aic` para qualificar a separação entre modelos.

---

## Observação epistemológica

Este pipeline é um artefato de comparação de hipóteses operacionais. Não constitui validação experimental do programa e não altera o status do core teórico.
