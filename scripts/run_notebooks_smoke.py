"""
Smoke test runner for Ora Brasiliae notebooks.
Executes all notebooks in order and reports pass/fail status.
"""

import subprocess
import sys
import os

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
]


def run_notebook(path):
    """Execute a notebook via nbconvert. Returns True on success."""
    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "nbconvert",
            "--to",
            "notebook",
            "--execute",
            "--inplace",
            path,
        ],
        capture_output=True,
        text=True,
    )
    return result.returncode == 0


def main():
    # Resolve paths relative to repository root
    repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    os.chdir(repo_root)

    results = {}
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
    else:
        print("\nSome notebooks failed.")
        sys.exit(1)


if __name__ == "__main__":
    main()
