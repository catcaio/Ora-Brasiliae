# Protocolo de Validação Externa (EPIC MPV-62)

## Data de emissão
2026-04-23

## Objetivo

Definir um padrão único para concluir a etapa de **validação externa** com:

1. **outputs reproduzíveis** (reexecução independente sem mudanças manuais);
2. **validação auditável** (trilha de evidências + parecer verificável).

Este documento é operacional e não altera o claim do core.

---

## Dependência de sequência

- Esta etapa depende da conclusão de **MPV-57 (Lab Readiness)**.
- Nenhum novo bloco deve iniciar antes do aceite formal dos critérios abaixo.

---

## Escopo da validação externa

### Inclui
- Reexecução independente dos notebooks canônicos e de suporte necessário.
- Verificação de consistência entre documentos de previsão e protocolo experimental.
- Revisão de rastreabilidade entre claims, hipóteses e limitações.

### Não inclui
- Promoção de previsão para validação experimental real.
- Inclusão de novos completamentos no core.
- Reinterpretação de hipótese externa como resultado derivado.

---

## Pacote mínimo de evidências (outputs reproduzíveis)

Para considerar a etapa “reproduzível”, o pacote de evidências deve conter:

1. **Registro de ambiente**
   - versão de Python;
   - hash de `requirements.txt`;
   - data/hora UTC da execução.
2. **Log de execução**
   - comando usado para execução/smoke;
   - status final (pass/fail);
   - notebook(s) executados.
3. **Artefatos de execução**
   - outputs persistidos no próprio notebook;
   - eventuais tabelas/gráficos citados no sumário pré-experimental.
4. **Resumo de integridade**
   - lista do que foi executado;
   - lista do que foi explicitamente não executado (com justificativa).

---

## Checklist de validação auditável

- [ ] Dependência MPV-57 formalmente encerrada.
- [ ] Ambiente de execução identificado e documentado.
- [ ] Procedimento de reexecução documentado em linguagem operacional.
- [ ] Evidências de execução anexadas (logs e status).
- [ ] Coerência entre `docs/09_pre_experimental_summary.md` e `docs/11_minimal_experimental_protocol.md` verificada.
- [ ] Nenhum overclaim detectado (previsão ≠ validação experimental).
- [ ] Limitações e riscos de falso positivo explicitamente rechecados.
- [ ] Parecer final assinado com decisão: **Aprovado / Aprovado com ressalvas / Reprovado**.

---

## Critérios de aceite da EPIC (gate de passagem)

A EPIC MPV-62 só pode ser encerrada quando:

1. Checklist acima estiver 100% preenchido;
2. houver evidência mínima reproduzível anexada ao repositório;
3. o parecer final registrar claramente:
   - escopo auditado;
   - não conformidades (se houver);
   - decisão final.

Se qualquer item falhar, o status deve permanecer “em validação” e o próximo bloco continua bloqueado.

---

## Template de parecer final (usar no encerramento)

### Identificação
- Data (UTC):
- Revisor externo:
- Escopo auditado:

### Resultado da reprodutibilidade
- Execução independente: [PASS/FAIL]
- Evidências anexadas: [SIM/NÃO]
- Observações:

### Resultado da auditabilidade
- Checklist completo: [SIM/NÃO]
- Não conformidades:
- Risco residual:

### Decisão
- [ ] Aprovado
- [ ] Aprovado com ressalvas
- [ ] Reprovado

### Próxima ação
- Condição para desbloqueio do próximo bloco:

---

## Status Epistemológico

- Categoria: GOVERNANÇA / VALIDAÇÃO
- Pertence ao Core: NÃO
- Função: formalizar aceite auditável da transição para validação externa
