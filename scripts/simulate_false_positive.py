"""Simulação adversarial de falso positivo para o regime quadrático.

Gera dados sintéticos com dinâmica linear real, adiciona drift instrumental
correlacionado com N e testa se o ajuste quadrático pode parecer melhor.

Saída:
- logs estruturados em JSON (stdout)
- artefato CSV auditável em outputs/adversarial_false_positive_dataset.csv
"""

from __future__ import annotations

import argparse
import csv
import json
import math
import random
from pathlib import Path
from typing import Dict, Iterable, List, Tuple


def model_linear(n: int, tau: float, alpha: float) -> float:
    return math.exp(-alpha * n * tau / 2.0)


def model_quadratic(n: int, tau: float, beta: float) -> float:
    return math.exp(-beta * (n**2) * tau / 2.0)


def add_noise(value: float, sigma: float, rng: random.Random) -> float:
    noisy = value + rng.gauss(0.0, sigma)
    return max(0.0, min(1.0, noisy))


def generate_dataset(
    n_values: Iterable[int],
    tau: float,
    alpha_real: float,
    drift_lambda: float,
    noise_sigma: float,
    seed: int,
) -> List[Dict[str, float]]:
    rng = random.Random(seed)
    rows: List[Dict[str, float]] = []

    for n in n_values:
        baseline = model_linear(n, tau, alpha_real)
        # Drift adversarial: cresce com N e distorce o contraste observado.
        drift = drift_lambda * ((n - min(n_values)) / (max(n_values) - min(n_values))) ** 2
        observed = add_noise(baseline - drift, sigma=noise_sigma, rng=rng)
        rows.append(
            {
                "N": float(n),
                "tau": tau,
                "v_linear_true": baseline,
                "drift": drift,
                "v_observed": observed,
            }
        )

    return rows


def fit_grid(
    rows: List[Dict[str, float]],
    mode: str,
    tau: float,
    grid_min: float,
    grid_max: float,
    grid_steps: int,
) -> Tuple[float, float]:
    best_param = grid_min
    best_sse = float("inf")

    for i in range(grid_steps + 1):
        candidate = grid_min + (grid_max - grid_min) * (i / grid_steps)
        sse = 0.0
        for row in rows:
            n = int(row["N"])
            observed = row["v_observed"]
            predicted = (
                model_linear(n, tau, candidate)
                if mode == "linear"
                else model_quadratic(n, tau, candidate)
            )
            sse += (observed - predicted) ** 2
        if sse < best_sse:
            best_sse = sse
            best_param = candidate

    return best_param, best_sse


def aic_from_sse(sse: float, n_obs: int, k_params: int = 1) -> float:
    eps = 1e-12
    return n_obs * math.log((sse + eps) / n_obs) + 2 * k_params


def write_csv(path: Path, rows: List[Dict[str, float]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = ["N", "tau", "v_linear_true", "drift", "v_observed"]
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def log_event(event: str, **payload: object) -> None:
    print(json.dumps({"event": event, **payload}, ensure_ascii=False))


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Simula falso positivo adversarial")
    parser.add_argument("--seed", type=int, default=65, help="Seed reprodutível")
    parser.add_argument("--tau", type=float, default=1.0)
    parser.add_argument("--alpha-real", type=float, default=0.021)
    parser.add_argument("--drift-lambda", type=float, default=0.15)
    parser.add_argument("--noise-sigma", type=float, default=0.015)
    parser.add_argument("--n-start", type=int, default=30)
    parser.add_argument("--n-end", type=int, default=70)
    parser.add_argument("--n-step", type=int, default=5)
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("outputs/adversarial_false_positive_dataset.csv"),
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()

    n_values = list(range(args.n_start, args.n_end + 1, args.n_step))
    rows = generate_dataset(
        n_values=n_values,
        tau=args.tau,
        alpha_real=args.alpha_real,
        drift_lambda=args.drift_lambda,
        noise_sigma=args.noise_sigma,
        seed=args.seed,
    )
    write_csv(args.output, rows)

    alpha_fit, sse_linear = fit_grid(rows, "linear", args.tau, 0.001, 0.10, 800)
    beta_fit, sse_quad = fit_grid(rows, "quadratic", args.tau, 0.00001, 0.01, 800)

    aic_linear = aic_from_sse(sse_linear, len(rows))
    aic_quad = aic_from_sse(sse_quad, len(rows))

    best_model = "quadratic" if aic_quad < aic_linear else "linear"
    false_positive = best_model == "quadratic"

    log_event(
        "simulation_config",
        seed=args.seed,
        tau=args.tau,
        alpha_real=args.alpha_real,
        drift_lambda=args.drift_lambda,
        noise_sigma=args.noise_sigma,
        n_values=n_values,
        output=str(args.output),
    )
    log_event(
        "fit_results",
        alpha_fit=round(alpha_fit, 6),
        beta_fit=round(beta_fit, 6),
        sse_linear=round(sse_linear, 6),
        sse_quadratic=round(sse_quad, 6),
        aic_linear=round(aic_linear, 6),
        aic_quadratic=round(aic_quad, 6),
    )
    log_event(
        "adversarial_assessment",
        best_model=best_model,
        false_positive_detected=false_positive,
        criterion="AIC mínimo",
    )

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
