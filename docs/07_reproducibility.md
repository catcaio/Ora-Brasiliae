# Reprodutibilidade

## Objetivo

Este documento define o procedimento mínimo para reproduzir a execução dos notebooks do repositório.

---

## Ambiente mínimo

- Python 3.x
- requirements.txt
- kernel local configurado

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

---

## Critério de sucesso

- todos os notebooks executam sem erro
- outputs persistem
- nenhuma previsão é promovida ao core durante a execução

---

## Status Epistemológico

- Categoria: SUPORTE
- Pertence ao Core: NÃO
- Função: garantir auditabilidade técnica do repositório
