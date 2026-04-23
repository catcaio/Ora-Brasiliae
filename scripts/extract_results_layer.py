"""Results extraction layer for prediction notebooks (10-17).

Builds a single auditable artifact from deterministic computations described
in notebooks 10-17.
"""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any

import numpy as np

REPO_ROOT = Path(__file__).resolve().parents[1]
OUTPUT_JSON = REPO_ROOT / "results" / "prediction_notebooks_10_17.json"
OUTPUT_MD = REPO_ROOT / "docs" / "13_results_extraction_layer.md"


def _find_critical_tau(tau: np.ndarray, visibility: np.ndarray, threshold: float) -> float | None:
    indices = np.where(visibility < threshold)[0]
    if len(indices) == 0:
        return None
    return float(tau[indices[0]])


def _find_n_star(n_vals: np.ndarray, v_vals: np.ndarray, threshold: float) -> int | None:
    indices = np.where(v_vals < threshold)[0]
    if len(indices) == 0:
        return None
    return int(n_vals[indices[0]])


def notebook_10() -> dict[str, Any]:
    tau = np.linspace(0, 10, 1000)
    n_values = [10, 20, 40, 60, 80, 100]
    a = 0.05
    b = 0.005
    threshold = 0.1

    summary = []
    for n in n_values:
        v_a = np.exp(-(a * n) * tau / 2)
        v_b = np.exp(-(b * (n**2)) * tau / 2)
        summary.append(
            {
                "N": n,
                "tau_critical_regime_A": _find_critical_tau(tau, v_a, threshold),
                "tau_critical_regime_B": _find_critical_tau(tau, v_b, threshold),
            }
        )

    return {
        "parameters": {"a": a, "b": b, "threshold": threshold},
        "critical_tau_table": summary,
    }


def notebook_11() -> dict[str, Any]:
    tau_ref = 1.0
    threshold = 0.1
    n_range = np.arange(1, 301)
    a = 0.05
    b = 0.005

    v_a = np.exp(-(a * n_range) * tau_ref / 2)
    v_b = np.exp(-(b * (n_range**2)) * tau_ref / 2)

    return {
        "parameters": {"a": a, "b": b, "tau_ref": tau_ref, "threshold": threshold},
        "n_star_regime_A": _find_n_star(n_range, v_a, threshold),
        "n_star_regime_B": _find_n_star(n_range, v_b, threshold),
    }


def notebook_12() -> dict[str, Any]:
    n_target = 100
    v_target = 0.5
    tau = 1.0
    gamma_required = -2 * math.log(v_target) / tau
    a_calib = gamma_required / n_target
    b_calib = gamma_required / (n_target**2)

    return {
        "calibration_target": {"N": n_target, "V": v_target, "tau": tau},
        "gamma_required": gamma_required,
        "a_calibrated": a_calib,
        "b_calibrated": b_calib,
    }


def notebook_13() -> dict[str, Any]:
    rng = np.random.default_rng(seed=42)
    a = 0.05
    b = 0.005
    tau_ref = 1.0
    n_range = np.arange(1, 101)
    n_simulations = 50
    noise_level = 0.1
    jitter_level = 0.05

    results_a = []
    results_b = []
    for _ in range(n_simulations):
        tau_sim = tau_ref * (1 + rng.normal(0, jitter_level, len(n_range)))
        gamma_a = (a * n_range) * (1 + rng.normal(0, noise_level, len(n_range)))
        gamma_b = (b * (n_range**2)) * (1 + rng.normal(0, noise_level, len(n_range)))
        results_a.append(np.exp(-(gamma_a * tau_sim) / 2))
        results_b.append(np.exp(-(gamma_b * tau_sim) / 2))

    avg_a = np.mean(results_a, axis=0)
    avg_b = np.mean(results_b, axis=0)
    std_a = np.std(results_a, axis=0)
    std_b = np.std(results_b, axis=0)

    return {
        "parameters": {
            "a": a,
            "b": b,
            "tau_ref": tau_ref,
            "n_simulations": n_simulations,
            "noise_level": noise_level,
            "jitter_level": jitter_level,
            "seed": 42,
        },
        "avg_visibility_regime_A_at_N50": float(avg_a[49]),
        "avg_visibility_regime_B_at_N50": float(avg_b[49]),
        "std_visibility_regime_A_at_N50": float(std_a[49]),
        "std_visibility_regime_B_at_N50": float(std_b[49]),
    }


def notebook_14() -> dict[str, Any]:
    a = 0.05
    b = 0.005
    tau_ref = 1.0
    n_vals = np.arange(1, 151)
    v_a = np.exp(-(a * n_vals) * tau_ref / 2)
    v_b = np.exp(-(b * (n_vals**2)) * tau_ref / 2)
    d_n = np.abs(v_a - v_b)

    idx = int(np.argmax(d_n))
    return {
        "parameters": {"a": a, "b": b, "tau_ref": tau_ref},
        "n_at_max_discrimination": int(n_vals[idx]),
        "max_discrimination": float(d_n[idx]),
    }


def notebook_15() -> dict[str, Any]:
    a = 0.014
    b = 0.00014
    systems = [
        ("Gases Frios (ex: BEC em armadilha)", 10000, "0.1 - 10"),
        ("Interferometria Molecular (ex: C60, macro-moléculas)", 50, "1 - 100"),
        ("Átomos de Rydberg (fortes interações dipolo-dipolo)", 30, "10^3 - 10^5"),
    ]
    table = []
    for system, n_value, gamma_range in systems:
        table.append(
            {
                "system": system,
                "N_typical": n_value,
                "gamma_experimental_range_s^-1": gamma_range,
                "gamma_pred_linear": a * n_value,
                "gamma_pred_quadratic": b * (n_value**2),
            }
        )

    return {"parameters": {"a": a, "b": b}, "mapping": table}


def notebook_16() -> dict[str, Any]:
    a = 0.014
    b = 0.00014
    tau = 1.0
    gamma_th = 0.05
    noise_floor = 0.10
    n_vals = np.arange(1, 101)

    v_a = np.exp(-(a * n_vals + gamma_th) * tau / 2)
    v_b = np.exp(-(b * (n_vals**2) + gamma_th) * tau / 2)
    diff = np.abs(v_a - v_b)

    detectable = n_vals[diff > noise_floor]
    return {
        "parameters": {"a": a, "b": b, "tau": tau, "gamma_th": gamma_th, "noise_floor": noise_floor},
        "detectable_n_min": int(detectable[0]) if len(detectable) else None,
        "detectable_n_max": int(detectable[-1]) if len(detectable) else None,
    }


def notebook_17() -> dict[str, Any]:
    a = 0.014
    b = 0.00014
    n_vals = np.arange(1, 151)
    precision_required = 0.05
    taus = [0.1, 0.5, 1.0, 2.0, 5.0]

    windows = []
    for tau in taus:
        v_a = np.exp(-(a * n_vals) * tau / 2)
        v_b = np.exp(-(b * (n_vals**2)) * tau / 2)
        diff = np.abs(v_a - v_b)
        valid = n_vals[diff > precision_required]

        windows.append(
            {
                "tau_s": tau,
                "n_min": int(valid[0]) if len(valid) else None,
                "n_max": int(valid[-1]) if len(valid) else None,
                "max_separation": float(np.max(diff)),
            }
        )

    return {
        "parameters": {"a": a, "b": b, "precision_required": precision_required},
        "windows": windows,
    }


def render_markdown(payload: dict[str, Any]) -> str:
    lines = [
        "# Results Extraction Layer (Notebooks 10–17)",
        "",
        "Artefato gerado automaticamente por `scripts/extract_results_layer.py`.",
        "",
        "## Consolidação",
        "",
        f"- N*_A (notebook 11): {payload['notebook_11']['n_star_regime_A']}",
        f"- N*_B (notebook 11): {payload['notebook_11']['n_star_regime_B']}",
        f"- a calibrado (notebook 12): {payload['notebook_12']['a_calibrated']:.6f}",
        f"- b calibrado (notebook 12): {payload['notebook_12']['b_calibrated']:.6f}",
        f"- N pico de distinguibilidade (notebook 14): {payload['notebook_14']['n_at_max_discrimination']}",
        f"- Intervalo detectável com ruído (notebook 16): N={payload['notebook_16']['detectable_n_min']}..{payload['notebook_16']['detectable_n_max']}",
        "",
        "## Janela experimental (notebook 17)",
        "",
        "| Tau (s) | N mínimo | N máximo | Separação máxima |",
        "|---:|---:|---:|---:|",
    ]

    for row in payload["notebook_17"]["windows"]:
        lines.append(
            f"| {row['tau_s']:.1f} | {row['n_min']} | {row['n_max']} | {row['max_separation']:.3f} |"
        )

    lines.extend(
        [
            "",
            "## Rastreabilidade",
            "",
            "- Fonte: notebooks 10–17 (trilha de previsão).",
            "- Método: recomputação determinística das mesmas equações para exportar dados auditáveis em JSON.",
        ]
    )
    return "\n".join(lines) + "\n"


def main() -> None:
    payload = {
        "notebook_10": notebook_10(),
        "notebook_11": notebook_11(),
        "notebook_12": notebook_12(),
        "notebook_13": notebook_13(),
        "notebook_14": notebook_14(),
        "notebook_15": notebook_15(),
        "notebook_16": notebook_16(),
        "notebook_17": notebook_17(),
    }

    OUTPUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_JSON.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    OUTPUT_MD.write_text(render_markdown(payload), encoding="utf-8")

    print(f"Wrote: {OUTPUT_JSON.relative_to(REPO_ROOT)}")
    print(f"Wrote: {OUTPUT_MD.relative_to(REPO_ROOT)}")


if __name__ == "__main__":
    main()
