"""Deterministic notebook runner for Ora Brasiliae.

Executes notebooks 00-17 in canonical order and emits an audit report with
per-notebook status, duration, and stderr snippets for failures.
"""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import time
from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable

NOTEBOOKS = [
    "notebooks/00_index.ipynb",
    "notebooks/01_domain_and_definitions.ipynb",
    "notebooks/02_variational_operator.ipynb",
    "notebooks/03_modular_first_law.ipynb",
    "notebooks/04_gap10_symbolic.ipynb",
    "notebooks/05_bianchi_and_phi.ipynb",
    "notebooks/06_newtonian_limit.ipynb",
    "notebooks/07_claim_minimo.ipynb",
    "notebooks/08_gap10_numeric_scan.ipynb",
    "notebooks/09_newtonian_parameter_scan.ipynb",
    "notebooks/10_visibility_prediction_scan.ipynb",
    "notebooks/11_nstar_threshold_exploration.ipynb",
    "notebooks/12_physical_parameter_calibration.ipynb",
    "notebooks/13_scaling_stability_test.ipynb",
    "notebooks/14_model_discrimination_metric.ipynb",
    "notebooks/15_physical_system_mapping.ipynb",
    "notebooks/16_signal_vs_noise_analysis.ipynb",
    "notebooks/17_experimental_window_estimation.ipynb",
]


@dataclass
class NotebookResult:
    path: str
    status: str
    duration_seconds: float
    returncode: int
    stderr_tail: str


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Execute Ora Brasiliae notebooks with audit output")
    parser.add_argument(
        "--timeout-seconds",
        type=int,
        default=600,
        help="Per-notebook timeout in seconds (default: 600)",
    )
    parser.add_argument(
        "--report",
        default="docs/reports/notebook_reproducibility_report.json",
        help="Path for JSON audit report",
    )
    return parser.parse_args()


def run_notebook(path: str, timeout_seconds: int) -> NotebookResult:
    start = time.monotonic()
    cmd = [
        sys.executable,
        "-m",
        "nbconvert",
        "--to",
        "notebook",
        "--execute",
        "--inplace",
        "--ExecutePreprocessor.timeout",
        str(timeout_seconds),
        path,
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    duration = time.monotonic() - start
    stderr_tail = "\n".join(result.stderr.strip().splitlines()[-20:])
    status = "PASS" if result.returncode == 0 else "FAIL"
    return NotebookResult(
        path=path,
        status=status,
        duration_seconds=round(duration, 3),
        returncode=result.returncode,
        stderr_tail=stderr_tail,
    )


def ensure_paths_exist(paths: Iterable[str]) -> None:
    missing = [path for path in paths if not Path(path).exists()]
    if missing:
        print("Missing notebooks detected:")
        for notebook in missing:
            print(f"  - {notebook}")
        raise FileNotFoundError("Notebook list contains paths that do not exist")


def write_report(report_path: Path, timeout_seconds: int, results: list[NotebookResult]) -> None:
    report_path.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "generated_at_utc": datetime.now(tz=timezone.utc).isoformat(),
        "python": sys.version,
        "timeout_seconds": timeout_seconds,
        "notebook_count": len(results),
        "passed": sum(1 for result in results if result.status == "PASS"),
        "failed": sum(1 for result in results if result.status == "FAIL"),
        "results": [asdict(result) for result in results],
    }
    report_path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def main() -> int:
    args = parse_args()

    repo_root = Path(__file__).resolve().parent.parent
    os.chdir(repo_root)

    ensure_paths_exist(NOTEBOOKS)

    results: list[NotebookResult] = []
    print(f"Running {len(NOTEBOOKS)} notebooks with timeout={args.timeout_seconds}s")

    for notebook in NOTEBOOKS:
        print(f"Running: {notebook} ... ", end="", flush=True)
        notebook_result = run_notebook(notebook, timeout_seconds=args.timeout_seconds)
        results.append(notebook_result)
        print(notebook_result.status)

    write_report(Path(args.report), timeout_seconds=args.timeout_seconds, results=results)

    print("\n=== SUMMARY ===")
    for result in results:
        print(f"  {result.status}  {result.path} ({result.duration_seconds}s)")

    failed = [result for result in results if result.status == "FAIL"]
    if failed:
        print("\nSome notebooks failed. Failure diagnostics:")
        for result in failed:
            print(f"\n--- {result.path} ---")
            print(result.stderr_tail or "(no stderr)")
        return 1

    print("\nAll notebooks passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
