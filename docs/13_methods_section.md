# Methods (gerado automaticamente)

## Objetivo

Gerar uma seção de metodologia rastreável a partir das fontes canônicas do repositório, sem introduzir hipóteses novas.

## Pipeline metodológico

| Etapa | Fonte canônica | Função metodológica |
| --- | --- | --- |
| Domínio geométrico local | `core/00_domain.md` | Define o diamante causal local, o corte e a superfície de bifurcação usados em toda a derivação. |
| Entropia generalizada | `core/01_sgen.md` | Estabelece S_gen e as convenções de primeira ordem adotadas no formalismo. |
| Operador variacional projetado | `core/02_variational_operator.md` | Constrói o operador variacional no cone nulo e fixa a normalização local. |
| Ponte modular em primeira ordem | `core/03_modular_bridge.md` | Conecta a variação de entropia à primeira lei do entrelaçamento no regime linear. |
| Raychaudhuri linearizada | `core/04_raychaudhuri.md` | Relaciona expansão nula e curvatura local na aproximação linear pertinente ao claim mínimo. |
| Recuperação nulo-local de Einstein | `core/05_minimal_einstein_recovery.md` | Fecha a cadeia lógica e explicita a projeção local de Einstein no cone nulo. |

## Procedimento reproduzível

1. Executar a validação de notebooks: `python scripts/run_notebooks_smoke.py`.
2. Gerar esta seção: `python scripts/generate_methods_section.py`.
3. Confirmar ausência de drift com `git diff -- docs/13_methods_section.md`.

## Ordem mínima de auditoria computacional

1. `notebooks/00_index.ipynb`
2. `notebooks/01_domain_and_definitions.ipynb`
3. `notebooks/02_variational_operator.ipynb`
4. `notebooks/03_modular_first_law.ipynb`
5. `notebooks/04_gap10_symbolic.ipynb`
6. `notebooks/05_bianchi_and_phi.ipynb`
7. `notebooks/06_newtonian_limit.ipynb`
8. `notebooks/07_claim_minimo.ipynb`

## Assinaturas de integridade das fontes

| Arquivo | SHA-256 |
| --- | --- |
| `core/00_domain.md` | `9b95a622517670bd583733853be57cab7377cc36545f3cc2283b4e9ec47a2382` |
| `core/01_sgen.md` | `d43c6d5a72526ff0f1d4c6c150e6130cd319ac073f426963cf6ea8fef84e1f7e` |
| `core/02_variational_operator.md` | `02556d6fcce21b6fdac51b7c37bde2ddf6a3c9dc6878c201b51e06f61d15b4e8` |
| `core/03_modular_bridge.md` | `aa2f5d7b6ef7c3904a03d79a573aa3e520543d9eab2a95ec4063f36805035bb3` |
| `core/04_raychaudhuri.md` | `b3ba263ffc3475c08822f3a10adee7419c34aca7a0f5b8366211431edba559b1` |
| `core/05_minimal_einstein_recovery.md` | `23aba3162bef4e8551b6274ec8c37b50e64cd2e950136c247c72ed4b8012fefb` |

## Restrições

- Não promove resultados de `/gaps` ao status de core.
- Não transforma previsões em validação empírica.
- Mantém o status epistemológico declarado no repositório.

## Status Epistemológico

- Categoria: SUPORTE
- Pertence ao Core: NÃO
- Função: materializar a seção Methods com rastreabilidade e reprodução

_Arquivo gerado automaticamente por `scripts/generate_methods_section.py`. Edite as fontes canônicas e regenere este documento._
