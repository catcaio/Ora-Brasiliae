"""Generate the paper Methods section from canonical repository sources.

This script creates docs/13_methods_section.md deterministically so the
methodology narrative is reproducible and auditable.
"""

from __future__ import annotations

import hashlib
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class MethodStep:
    title: str
    source: str
    summary: str


METHOD_STEPS: tuple[MethodStep, ...] = (
    MethodStep(
        title="Domínio geométrico local",
        source="core/00_domain.md",
        summary="Define o diamante causal local, o corte e a superfície de bifurcação usados em toda a derivação.",
    ),
    MethodStep(
        title="Entropia generalizada",
        source="core/01_sgen.md",
        summary="Estabelece S_gen e as convenções de primeira ordem adotadas no formalismo.",
    ),
    MethodStep(
        title="Operador variacional projetado",
        source="core/02_variational_operator.md",
        summary="Constrói o operador variacional no cone nulo e fixa a normalização local.",
    ),
    MethodStep(
        title="Ponte modular em primeira ordem",
        source="core/03_modular_bridge.md",
        summary="Conecta a variação de entropia à primeira lei do entrelaçamento no regime linear.",
    ),
    MethodStep(
        title="Raychaudhuri linearizada",
        source="core/04_raychaudhuri.md",
        summary="Relaciona expansão nula e curvatura local na aproximação linear pertinente ao claim mínimo.",
    ),
    MethodStep(
        title="Recuperação nulo-local de Einstein",
        source="core/05_minimal_einstein_recovery.md",
        summary="Fecha a cadeia lógica e explicita a projeção local de Einstein no cone nulo.",
    ),
)

NOTEBOOK_SEQUENCE: tuple[str, ...] = (
    "notebooks/00_index.ipynb",
    "notebooks/01_domain_and_definitions.ipynb",
    "notebooks/02_variational_operator.ipynb",
    "notebooks/03_modular_first_law.ipynb",
    "notebooks/04_gap10_symbolic.ipynb",
    "notebooks/05_bianchi_and_phi.ipynb",
    "notebooks/06_newtonian_limit.ipynb",
    "notebooks/07_claim_minimo.ipynb",
)


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def validate_sources(repo_root: Path) -> None:
    missing = [step.source for step in METHOD_STEPS if not (repo_root / step.source).exists()]
    if missing:
        formatted = ", ".join(missing)
        raise FileNotFoundError(f"Arquivos canônicos ausentes para metodologia: {formatted}")


def build_methods_markdown(repo_root: Path) -> str:
    lines: list[str] = []
    lines.append("# Methods (gerado automaticamente)")
    lines.append("")
    lines.append("## Objetivo")
    lines.append("")
    lines.append(
        "Gerar uma seção de metodologia rastreável a partir das fontes canônicas do repositório, "
        "sem introduzir hipóteses novas."
    )
    lines.append("")
    lines.append("## Pipeline metodológico")
    lines.append("")
    lines.append("| Etapa | Fonte canônica | Função metodológica |")
    lines.append("| --- | --- | --- |")
    for step in METHOD_STEPS:
        lines.append(f"| {step.title} | `{step.source}` | {step.summary} |")

    lines.append("")
    lines.append("## Procedimento reproduzível")
    lines.append("")
    lines.append("1. Executar a validação de notebooks: `python scripts/run_notebooks_smoke.py`.")
    lines.append("2. Gerar esta seção: `python scripts/generate_methods_section.py`.")
    lines.append("3. Confirmar ausência de drift com `git diff -- docs/13_methods_section.md`.")

    lines.append("")
    lines.append("## Ordem mínima de auditoria computacional")
    lines.append("")
    for idx, notebook in enumerate(NOTEBOOK_SEQUENCE, start=1):
        lines.append(f"{idx}. `{notebook}`")

    lines.append("")
    lines.append("## Assinaturas de integridade das fontes")
    lines.append("")
    lines.append("| Arquivo | SHA-256 |")
    lines.append("| --- | --- |")
    for step in METHOD_STEPS:
        source_path = repo_root / step.source
        lines.append(f"| `{step.source}` | `{sha256_file(source_path)}` |")

    lines.append("")
    lines.append("## Restrições")
    lines.append("")
    lines.append("- Não promove resultados de `/gaps` ao status de core.")
    lines.append("- Não transforma previsões em validação empírica.")
    lines.append("- Mantém o status epistemológico declarado no repositório.")

    lines.append("")
    lines.append("## Status Epistemológico")
    lines.append("")
    lines.append("- Categoria: SUPORTE")
    lines.append("- Pertence ao Core: NÃO")
    lines.append("- Função: materializar a seção Methods com rastreabilidade e reprodução")
    lines.append("")
    lines.append(
        "_Arquivo gerado automaticamente por `scripts/generate_methods_section.py`. "
        "Edite as fontes canônicas e regenere este documento._"
    )
    lines.append("")

    return "\n".join(lines)


def main() -> None:
    repo_root = Path(__file__).resolve().parents[1]
    validate_sources(repo_root)

    output_path = repo_root / "docs/13_methods_section.md"
    content = build_methods_markdown(repo_root)
    output_path.write_text(content, encoding="utf-8")
    print(f"Methods section gerada em: {output_path.relative_to(repo_root)}")


if __name__ == "__main__":
    main()
