"""
Smoke test runner for Ora Brasiliae notebooks.
Executes notebooks 00-18 in order and fails on any execution error.
"""

from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path

GLOBAL_SEED = "20260423"

START_NOTEBOOK = 0
END_NOTEBOOK = 18
NOTEBOOKS_DIR = Path("notebooks")


def build_notebook_list() -> list[str]:
    """Return ordered notebooks 00-18, validating file presence."""
    notebooks: list[str] = []
    missing: list[str] = []

    for index in range(START_NOTEBOOK, END_NOTEBOOK + 1):
        pattern = f"{index:02d}_*.ipynb"
        matches = sorted(NOTEBOOKS_DIR.glob(pattern))
        if not matches:
            missing.append(str(NOTEBOOKS_DIR / pattern))
            continue
        notebooks.append(matches[0].as_posix())

    if missing:
        raise FileNotFoundError(
            "Notebooks obrigatórios ausentes para execução CI: "
            + ", ".join(missing)
        )

    return notebooks


def run_notebook(path: str) -> subprocess.CompletedProcess[str]:
    """Execute a notebook via nbconvert and return process result."""
    env = os.environ.copy()
    env["PYTHONHASHSEED"] = GLOBAL_SEED

    return subprocess.run(
        [
            sys.executable,
            "-m",
            "nbconvert",
            "--to",
            "notebook",
            "--execute",
            "--inplace",
            "--ExecutePreprocessor.timeout=1200",
            path,
        ],
        capture_output=True,
        text=True,
        env=env,
    )


def main() -> int:
    repo_root = Path(__file__).resolve().parents[1]
    os.chdir(repo_root)

    notebooks = build_notebook_list()
    print(f"Global deterministic seed: {GLOBAL_SEED}")

    for notebook in notebooks:
        print(f"Running: {notebook}", flush=True)
        result = run_notebook(notebook)
        if result.returncode != 0:
            print(f"FAIL: {notebook}", flush=True)
            if result.stdout:
                print("--- stdout ---")
                print(result.stdout)
            if result.stderr:
                print("--- stderr ---")
                print(result.stderr)
            return 1
        print(f"PASS: {notebook}", flush=True)

    print("All notebooks 00-18 executed successfully.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
