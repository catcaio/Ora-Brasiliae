# Mapeamento Notion → Repositório

## Objetivo

Este documento mapeia o material prévio produzido fora do repositório para seus destinos corretos dentro da arquitetura canônica da Teoria de Ora Brasiliae.

Seu papel é editorial e organizacional: evitar duplicação, evitar mistura entre core e support, e registrar onde cada bloco deve ser absorvido.

---

## Regras de Mapeamento

- Material do núcleo mínimo vai para `/core/`
- Fechamentos condicionais e completamentos consistentes vão para `/gaps/`
- Histórico, formulações superadas e exploração ampla vão para `/appendices/`
- Governança, ledger e rastreamento epistemológico vão para `/docs/`
- Demonstrações simbólicas e auditoria reprodutível vão para `/notebooks/`

---

## Tabela de Mapeamento

| Documento / Bloco original | Tipo | Destino no repositório | Status editorial | Observação |
| :--- | :--- | :--- | :--- | :--- |
| Blocos sobre domínio causal local e claim mínimo | técnico/estrutural | core/00_domain.md, docs/01_claim_minimo_irredutivel.md | Canônico | Manter apenas formulação mínima |
| Definição de S_gen e operador variacional | técnico | core/01_sgen.md, core/02_variational_operator.md, notebooks/01-02 | Canônico | Separar definição de implementação simbólica |
| Primeira lei do entrelaçamento | técnico | core/03_modular_bridge.md, notebooks/03_modular_first_law.ipynb | Canônico condicional | Manter hipóteses explícitas |
| Raychaudhuri e recuperação nulo-local | técnico | core/04_raychaudhuri.md, core/05_minimal_einstein_recovery.md, notebooks/07_claim_minimo.ipynb | Canônico | Não extrapolar para equivalência global |
| GAP-10 e coeficientes logarítmicos | derivação condicional | gaps/gap10.md, notebooks/04_gap10_symbolic.ipynb | Suporte | Explicitar dependência de regularização |
| Jacobiano de Bogoliubov → S_edge | completamento consistente | gaps/jacobian_edge_entropy.md | Suporte | Não promover ao core |
| Promoção c_eff → φ(x) | completamento consistente | gaps/bianchi_phi.md, notebooks/05_bianchi_and_phi.ipynb | Suporte | Tratar apenas como ansatz consistente |
| Limite Newtoniano | fechamento condicional | gaps/newtonian_limit.md, notebooks/06_newtonian_limit.ipynb | Suporte | Não pertence ao claim mínimo |
| Equação de Ouro antiga | histórico | appendices/historical_equation_of_ouro.md | Histórico | Não usar no core |
| Explorações amplas / manifesto / comparações extensas | exploração | appendices/noncanonical_explorations.md, appendices/literature_comparison.md | Não canônico | Fora do fluxo principal |

---

## Critérios Editoriais

- Todo material deve ser desidratado antes de entrar no core
- Nenhum texto histórico deve ser promovido ao status de claim vigente
- Nenhum completamento consistente deve ser tratado como derivação inevitável
- O repositório é a fonte canônica; material externo é apenas insumo bruto

---

## Status Epistemológico

- Categoria: SUPORTE
- Pertence ao Core: NÃO
- Função: organizar a migração editorial e blindar a arquitetura do repositório
