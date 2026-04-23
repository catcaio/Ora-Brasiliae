"""
Smoke test runner for Ora Brasiliae notebooks.
Executes all notebooks in order and reports pass/fail status.
"""

import os
import subprocess
import sys
from pathlib import Path

GLOBAL_SEED = "20260423"


def _discover_notebooks() -> list[str]:
    notebooks_dir = Path("notebooks")
    return sorted(str(path) for path in notebooks_dir.glob("[0-1][0-9]_*.ipynb"))


NOTEBOOKS = _discover_notebooks()


def run_notebook(path: str) -> bool:
    """Execute a notebook via nbconvert. Returns True on success."""
    env = os.environ.copy()
    env["PYTHONHASHSEED"] = GLOBAL_SEED

    result = subprocess.run(
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
    return result.returncode == 0


def main() -> None:
    # Resolve paths relative to repository root
    repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    os.chdir(repo_root)

    if not NOTEBOOKS:
        print("No notebooks found in notebooks/.")
        sys.exit(1)

    results: dict[str, str] = {}
    print(f"Global deterministic seed: {GLOBAL_SEED}")
    for nb in NOTEBOOKS:
        print(f"Running: {nb} ... ", end="", flush=True)
        ok = run_notebook(nb)
        status = "PASS" if ok else "FAIL"
        results[nb] = status
        print(status)

    print("\n=== SUMMARY ===")
    all_pass = True
    for nb, status in results.items():
        print(f"  {status}  {nb}")
        if status == "FAIL":
            all_pass = False

    if all_pass:
        print("\nAll notebooks passed.")
        sys.exit(0)

    print("\nSome notebooks failed.")
    sys.exit(1)


if __name__ == "__main__":
    main()
