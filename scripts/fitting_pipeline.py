"""Pipeline reprodutível para comparar ajuste linear vs quadrático de visibilidade.

Modelos avaliados:
  A) V(N) = exp(-a * N * tau / 2)
  B) V(N) = exp(-b * N^2 * tau / 2)

Entrada esperada (CSV):
  N,V
  30,0.84
  40,0.79
  ...

Saída:
  JSON com parâmetros ajustados, métricas e decisão de melhor modelo.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


@dataclass(frozen=True)
class Observation:
    n: float
    v: float


@dataclass(frozen=True)
class FitResult:
    model_name: str
    parameter_name: str
    parameter_value: float
    rmse: float
    mae: float
    r2: float
    rss: float
    aic: float
    bic: float


def _safe_log_visibility(v: float) -> float:
    # Evita log(0) e mantém robustez numérica em medidas extremas.
    return math.log(max(v, 1e-12))


def _estimate_parameter(observations: Iterable[Observation], tau: float, power: int) -> float:
    xs = [obs.n**power for obs in observations]
    ys = [_safe_log_visibility(obs.v) for obs in observations]

    denominator = sum(x * x for x in xs)
    if denominator <= 0:
        raise ValueError("Denominador inválido no ajuste; verifique valores de N.")

    # ln(V) = -(p * x * tau / 2) => p = -2 * sum(x*ln(V)) / (tau * sum(x^2))
    parameter = -2.0 * sum(x * y for x, y in zip(xs, ys)) / (tau * denominator)
    return max(parameter, 0.0)


def _predict_visibility(n: float, tau: float, parameter: float, power: int) -> float:
    return math.exp(-(parameter * (n**power) * tau) / 2.0)


def _evaluate_model(
    observations: list[Observation],
    tau: float,
    model_name: str,
    parameter_name: str,
    power: int,
) -> FitResult:
    parameter = _estimate_parameter(observations, tau=tau, power=power)
    predictions = [_predict_visibility(obs.n, tau=tau, parameter=parameter, power=power) for obs in observations]
    actuals = [obs.v for obs in observations]

    errors = [pred - real for pred, real in zip(predictions, actuals)]
    rss = sum(err * err for err in errors)
    n_points = len(observations)

    rmse = math.sqrt(rss / n_points)
    mae = sum(abs(err) for err in errors) / n_points

    mean_actual = sum(actuals) / n_points
    tss = sum((real - mean_actual) ** 2 for real in actuals)
    r2 = 1.0 - (rss / tss) if tss > 0 else float("nan")

    # AIC/BIC sob hipótese gaussiana para comparação relativa entre modelos.
    # k = 1 parâmetro efetivo (a ou b).
    k = 1
    sigma2 = max(rss / n_points, 1e-12)
    log_likelihood = -0.5 * n_points * (math.log(2.0 * math.pi * sigma2) + 1.0)
    aic = 2 * k - 2 * log_likelihood
    bic = math.log(n_points) * k - 2 * log_likelihood

    return FitResult(
        model_name=model_name,
        parameter_name=parameter_name,
        parameter_value=parameter,
        rmse=rmse,
        mae=mae,
        r2=r2,
        rss=rss,
        aic=aic,
        bic=bic,
    )


def _read_observations(csv_path: Path) -> list[Observation]:
    observations: list[Observation] = []
    with csv_path.open("r", encoding="utf-8", newline="") as fp:
        reader = csv.DictReader(fp)
        required = {"N", "V"}
        if not required.issubset(reader.fieldnames or []):
            raise ValueError("CSV deve conter cabeçalhos N,V.")

        for row in reader:
            n = float(row["N"])
            v = float(row["V"])
            if n <= 0:
                raise ValueError("N deve ser positivo.")
            if not (0 < v <= 1.0):
                raise ValueError("V deve estar no intervalo (0, 1].")
            observations.append(Observation(n=n, v=v))

    if len(observations) < 5:
        raise ValueError("São necessários pelo menos 5 pontos para comparação robusta.")

    return observations


def _sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as fp:
        while chunk := fp.read(8192):
            digest.update(chunk)
    return digest.hexdigest()


def run_pipeline(input_csv: Path, output_json: Path, tau: float) -> None:
    observations = _read_observations(input_csv)

    linear = _evaluate_model(
        observations,
        tau=tau,
        model_name="linear",
        parameter_name="a",
        power=1,
    )
    quadratic = _evaluate_model(
        observations,
        tau=tau,
        model_name="quadratic",
        parameter_name="b",
        power=2,
    )

    by_aic = sorted([linear, quadratic], key=lambda item: item.aic)
    winner = by_aic[0]

    result = {
        "meta": {
            "input_csv": str(input_csv),
            "input_sha256": _sha256_file(input_csv),
            "tau": tau,
            "n_points": len(observations),
        },
        "models": [
            {
                "name": linear.model_name,
                linear.parameter_name: linear.parameter_value,
                "rmse": linear.rmse,
                "mae": linear.mae,
                "r2": linear.r2,
                "rss": linear.rss,
                "aic": linear.aic,
                "bic": linear.bic,
            },
            {
                "name": quadratic.model_name,
                quadratic.parameter_name: quadratic.parameter_value,
                "rmse": quadratic.rmse,
                "mae": quadratic.mae,
                "r2": quadratic.r2,
                "rss": quadratic.rss,
                "aic": quadratic.aic,
                "bic": quadratic.bic,
            },
        ],
        "decision": {
            "best_model": winner.model_name,
            "delta_aic": by_aic[1].aic - by_aic[0].aic,
            "rule": "menor AIC",
        },
    }

    output_json.parent.mkdir(parents=True, exist_ok=True)
    with output_json.open("w", encoding="utf-8") as fp:
        json.dump(result, fp, indent=2, ensure_ascii=False)
        fp.write("\n")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Compara ajuste linear vs quadrático para V(N).")
    parser.add_argument("--input", required=True, type=Path, help="CSV com colunas N,V")
    parser.add_argument("--output", required=True, type=Path, help="Arquivo JSON de saída")
    parser.add_argument("--tau", required=False, type=float, default=1.0, help="Tempo tau (s)")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    run_pipeline(input_csv=args.input, output_json=args.output, tau=args.tau)


if __name__ == "__main__":
    main()
