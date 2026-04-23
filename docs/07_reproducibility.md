# Reprodutibilidade

## Objetivo

Este documento define o procedimento mínimo para reproduzir a execução dos notebooks e a tradução de parâmetros do repositório.

---

## Ambiente mínimo

- Python 3.x
- requirements.txt
- kernel local configurado

---

## Determinismo

- seed global fixada em `20260423`
- `PYTHONHASHSEED=20260423` durante a execução automatizada
- notebooks com simulação pseudoaleatória usam gerador explícito (`numpy.random.default_rng`)

---

## Ordem de execução

1. notebooks/00_index.ipynb
2. notebooks/01_domain_and_definitions.ipynb
3. notebooks/02_variational_operator.ipynb
4. notebooks/03_modular_first_law.ipynb
5. notebooks/04_gap10_symbolic.ipynb
6. notebooks/05_bianchi_and_phi.ipynb
7. notebooks/06_newtonian_limit.ipynb
8. notebooks/07_claim_minimo.ipynb
9. notebooks/08_gap10_numeric_scan.ipynb
10. notebooks/09_newtonian_parameter_scan.ipynb
11. notebooks/10_visibility_prediction_scan.ipynb
12. notebooks/11_nstar_threshold_exploration.ipynb
13. notebooks/12_physical_parameter_calibration.ipynb
14. notebooks/13_scaling_stability_test.ipynb
15. notebooks/14_model_discrimination_metric.ipynb
16. notebooks/15_physical_system_mapping.ipynb
17. notebooks/16_signal_vs_noise_analysis.ipynb
18. notebooks/17_experimental_window_estimation.ipynb
19. notebooks/18_measurement_simulation.ipynb
20. python scripts/extract_results_layer.py
21. python scripts/parameter_translation.py

---

## Verificação adicional (MPV-58)

Executar a tradução de parâmetros com saída textual e JSON:

```bash
python scripts/parameter_translation.py
python scripts/parameter_translation.py --json
```

---

## Critério de sucesso

- todos os notebooks `00`–`18` executam sem erro
- outputs persistem
- nenhuma previsão é promovida ao core durante a execução
- fingerprints de output não apresentam drift em relação ao baseline versionado
- artefatos `results/prediction_notebooks_10_17.json` e `docs/13_results_extraction_layer.md` são gerados sem erro
- tradução de parâmetros reproduz os valores de ordem de grandeza documentados

---

## Fingerprinting de output

Baseline no repositório:

- `fingerprints/notebook_outputs_fingerprints.json`

Comandos:

- gerar/atualizar baseline:
  - `python scripts/notebook_output_fingerprint.py generate`
- detectar drift:
  - `python scripts/notebook_output_fingerprint.py verify`

Sem drift: saída com `status=pass`.
Com drift: saída com `status=drift_detected` e lista de notebooks alterados.


---

## Status Epistemológico

- Categoria: SUPORTE
- Pertence ao Core: NÃO
- Função: garantir auditabilidade técnica do repositório


## Trilhas complementares (previsão)

Após o núcleo mínimo (00-07), a trilha preditiva pode ser executada em sequência para auditoria de preparação experimental:

9. notebooks/08_gap10_numeric_scan.ipynb
10. notebooks/09_newtonian_parameter_scan.ipynb
11. notebooks/10_visibility_prediction_scan.ipynb
12. notebooks/11_nstar_threshold_exploration.ipynb
13. notebooks/12_physical_parameter_calibration.ipynb
14. notebooks/13_scaling_stability_test.ipynb
15. notebooks/14_model_discrimination_metric.ipynb
16. notebooks/15_physical_system_mapping.ipynb
17. notebooks/16_signal_vs_noise_analysis.ipynb
18. notebooks/17_experimental_window_estimation.ipynb
19. notebooks/18_measurement_simulation.ipynb
