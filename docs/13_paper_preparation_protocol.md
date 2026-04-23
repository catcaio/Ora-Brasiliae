# Protocolo de Preparação do Paper (EPIC MPV-47)

## Objetivo

Definir um fluxo auditável para converter o estado atual do repositório em submissão de paper, sem promover conteúdo condicional ao status de core e sem pular etapas de validação.

Este protocolo segue a regra operacional do projeto:

- cada bloco deve gerar **outputs reproduzíveis**;
- cada bloco deve ter **validação auditável**;
- o próximo bloco só inicia após fechamento completo do anterior.

---

## Dependência de entrada

- Dependência explícita: **MPV-42 — Reproducibility Hardening**.
- Condição para iniciar MPV-47: todos os artefatos de reprodução de MPV-42 devem estar estáveis e reexecutáveis no ambiente documentado.

---

## Blocos sequenciais e critérios de saída

## Bloco 1 — Congelamento de escopo científico

**Entradas**
- `docs/00_scope_and_status.md`
- `docs/01_claim_minimo_irredutivel.md`
- `docs/02_epistemic_ledger.md`
- `docs/06_claim_boundaries.md`

**Saídas reproduzíveis**
- snapshot textual do claim mínimo e das fronteiras de validade;
- lista de exclusões explícitas (o que não será reivindicado no paper).

**Validação auditável**
- revisão cruzada: nenhum item marcado como `HIPÓTESE EXTERNA` aparece como conclusão derivada;
- checklist assinado no próprio commit (mensagem + diff documental).

## Bloco 2 — Rastreabilidade claim ↔ evidência

**Entradas**
- `core/`
- `docs/02_epistemic_ledger.md`
- `notebooks/00_index.ipynb`

**Saídas reproduzíveis**
- tabela de rastreabilidade contendo, para cada afirmação do paper:
  - status epistemológico (`DERIVADO`, `FECHADO CONDICIONALMENTE`, etc.);
  - fonte primária no repositório (arquivo + seção);
  - evidência computacional associada (notebook/célula).

**Validação auditável**
- amostragem de pelo menos 100% das claims centrais e 100% das claims condicionais;
- ausência de claims sem referência de evidência.

## Bloco 3 — Pacote de figuras e tabelas reproduzíveis

**Entradas**
- notebooks numéricos e simbólicos referenciados no outline.

**Saídas reproduzíveis**
- lista fechada de figuras/tabelas candidatas;
- parâmetros, seeds e versão de dependências para regeneração;
- artefatos gerados com nomenclatura estável.

**Validação auditável**
- execução limpa via script automatizado (`scripts/run_notebooks_smoke.py` ou sucessor);
- comparação de hash/assinatura dos artefatos esperados.

## Bloco 4 — Montagem de narrativa técnica

**Entradas**
- `docs/paper_outline.md`
- resultados aprovados nos blocos 1–3.

**Saídas reproduzíveis**
- versão inicial da narrativa por seções;
- mapeamento seção ↔ fonte canônica no repo;
- lista explícita de limitações e não-claims no texto principal.

**Validação auditável**
- revisão de consistência terminológica com `docs/05_glossario.md`;
- checagem de aderência entre narrativa e ledger epistemológico.

## Bloco 5 — Pré-submissão e pacote de auditoria

**Entradas**
- narrativa técnica consolidada;
- artefatos reproduzíveis de figuras/tabelas;
- checklist de prontidão experimental.

**Saídas reproduzíveis**
- pacote final de submissão (texto + apêndices + instruções de reprodução);
- relatório de conformidade final para auditoria externa.

**Validação auditável**
- dry-run de reprodução por terceiro (ou ambiente limpo equivalente);
- verificação de que toda afirmação quantitativa possui trilha de reprodução.

---

## Gate de qualidade (DoD de MPV-47)

MPV-47 só pode ser encerrada quando todos os itens abaixo estiverem verdadeiros:

- [ ] paper sem extrapolações além de `docs/06_claim_boundaries.md`;
- [ ] 100% das claims centrais com rastreabilidade para `core/` e/ou notebooks;
- [ ] 100% das figuras/tabelas regeneráveis por procedimento documentado;
- [ ] relatório final de auditoria anexado ao repositório;
- [ ] dependência MPV-42 explicitamente satisfeita no histórico.

---

## Referências externas de processo (não normativas)

Para calibrar o nível de auditabilidade e reprodutibilidade, é útil alinhar o pacote final com checklists de avaliação de artefatos usados em conferências e sociedades científicas (por exemplo, orientações de artifact evaluation da ACM SIGMOBILE e checklists de reprodutibilidade da AAAI). Essas referências são guias de qualidade, não fonte de claim científico.

---

## Status Epistemológico

- Categoria: GOVERNANÇA DE EXECUÇÃO
- Pertence ao Core: NÃO
- Função: garantir que a redação do paper preserve rastreabilidade, reproduzibilidade e auditabilidade
