# Gate da EPIC MPV-57 — Lab Readiness

## Data
2026-04-23

## Objetivo
Formalizar o critério de conclusão da EPIC de prontidão de laboratório com dois requisitos mandatórios do projeto:

1. **outputs reproduzíveis**;
2. **validação auditável**.

Este gate também registra a dependência operacional da MPV-57 em relação à MPV-52.

---

## Dependência e Sequenciamento

- **EPIC atual:** MPV-57 — Lab Readiness.
- **Bloqueador declarado:** MPV-52 — Experimental Translation.
- **Regra operacional:** o próximo bloco só inicia após validação completa do bloco anterior.

### Estado do gate (nesta data)

- **Sequenciamento:** ⛔ BLOQUEADO por dependência de MPV-52.
- **Outputs reproduzíveis:** ✅ Definidos no repositório (estrutura + ordem de execução + script de smoke).
- **Validação auditável:** ✅ Definida no repositório (ledger + relatórios + checklist de conformidade).
- **Encerramento formal da MPV-57:** ⚠️ PENDENTE até liberação do bloqueio e revalidação final.

---

## Evidências de Outputs Reproduzíveis

### Estrutura e trilha canônica
- Ordem de notebooks explicitada em `notebooks/00_index.ipynb`.
- Organização por escopo (`core/`, `gaps/`, `docs/`, `notebooks/`) descrita no `README.md`.

### Execução mínima verificável
- Script de smoke: `scripts/run_notebooks_smoke.py`.
- Dependências declaradas: `requirements.txt`.

### Critério mínimo de reprodutibilidade
Para considerar o output reproduzível, deve existir:
- execução sem erro do smoke das trilhas mínimas;
- consistência entre claim mínimo, ledger e checklist experimental;
- ausência de promoção indevida de conteúdo não-core para core.

---

## Evidências de Validação Auditável

### Trilha de governança epistemológica
- Claim mínimo: `docs/01_claim_minimo_irredutivel.md`.
- Ledger epistemológico: `docs/02_epistemic_ledger.md`.
- Fronteiras de claim: `docs/06_claim_boundaries.md`.

### Auditoria registrada
- Relatório de conformidade: `docs/06_audit_conformity_report.md`.
- Checklist de prontidão experimental: `docs/12_experimental_readiness_checklist.md`.
- Síntese pré-experimental: `docs/09_pre_experimental_summary.md`.

### Critério mínimo de auditabilidade
Para considerar a validação auditável, deve existir:
- classificação epistemológica explícita para cada artefato relevante;
- histórico datado de auditoria com escopo e resultado;
- checklist rastreável para saída controlada do repositório para bancada.

---

## Decisão Operacional

**Decisão atual:** manter MPV-57 em estado **READY-BUT-BLOCKED**.

A EPIC está metodologicamente preparada (reprodutibilidade + auditabilidade especificadas), porém não pode ser encerrada enquanto a MPV-52 não for concluída e validada no mesmo padrão.
