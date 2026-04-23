# Reprodutibilidade

## Objetivo

Este documento define o procedimento de execução determinística e de auditoria dos notebooks `00` até `17`.

---

## Ambiente mínimo

- Python 3.11+
- Dependências instaladas via `requirements.txt`
- Kernel local configurado para execução de notebooks

---

## Ordem canônica de execução

A execução é estritamente sequencial para preservar rastreabilidade:

1. `notebooks/00_index.ipynb`
2. `notebooks/01_domain_and_definitions.ipynb`
3. `notebooks/02_variational_operator.ipynb`
4. `notebooks/03_modular_first_law.ipynb`
5. `notebooks/04_gap10_symbolic.ipynb`
6. `notebooks/05_bianchi_and_phi.ipynb`
7. `notebooks/06_newtonian_limit.ipynb`
8. `notebooks/07_claim_minimo.ipynb`
9. `notebooks/08_gap10_numeric_scan.ipynb`
10. `notebooks/09_newtonian_parameter_scan.ipynb`
11. `notebooks/10_visibility_prediction_scan.ipynb`
12. `notebooks/11_nstar_threshold_exploration.ipynb`
13. `notebooks/12_physical_parameter_calibration.ipynb`
14. `notebooks/13_scaling_stability_test.ipynb`
15. `notebooks/14_model_discrimination_metric.ipynb`
16. `notebooks/15_physical_system_mapping.ipynb`
17. `notebooks/16_signal_vs_noise_analysis.ipynb`
18. `notebooks/17_experimental_window_estimation.ipynb`

---

## Comando oficial

```bash
python scripts/run_notebooks_smoke.py --timeout-seconds 600
```

Saída de auditoria (JSON):

- `docs/reports/notebook_reproducibility_report.json`

O relatório registra:

- timestamp UTC da execução
- versão de Python
- timeout utilizado
- total de notebooks executados
- contagem de sucesso/falha
- duração por notebook e diagnóstico resumido de erro

---

## Critério de sucesso

- todos os notebooks `00–17` executam sem erro
- os outputs permanecem persistidos (`--inplace`)
- o relatório JSON é gerado para auditoria
- nenhuma previsão é promovida ao core durante a execução

---

## Status epistemológico

- Categoria: SUPORTE
- Pertence ao Core: NÃO
- Função: garantir reprodutibilidade técnica e trilha auditável da execução
