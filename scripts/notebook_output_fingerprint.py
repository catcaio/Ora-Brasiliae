"""Notebook output fingerprinting for reproducibility auditing.

Generates deterministic SHA-256 fingerprints for notebook outputs and can
verify drift against a committed baseline file.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

DEFAULT_NOTEBOOK_GLOB = "notebooks/*.ipynb"
DEFAULT_BASELINE_PATH = Path("fingerprints/notebook_outputs_fingerprints.json")


@dataclass(frozen=True)
class FingerprintEntry:
    notebook: str
    output_sha256: str
    code_cell_count: int


def _json_log(event: str, **fields: Any) -> None:
    payload = {"event": event, **fields}
    print(json.dumps(payload, ensure_ascii=False, sort_keys=True))


def _normalize_output(output: dict[str, Any]) -> dict[str, Any]:
    """Normalize a Jupyter output object to avoid unstable fields."""
    normalized = dict(output)

    # Transient metadata should not contribute to deterministic fingerprinting.
    transient = normalized.get("transient")
    if isinstance(transient, dict):
        normalized["transient"] = {}

    # Keep metadata, but remove known runtime-only fields when present.
    metadata = normalized.get("metadata")
    if isinstance(metadata, dict):
        metadata = dict(metadata)
        metadata.pop("execution", None)
        metadata.pop("collapsed", None)
        normalized["metadata"] = metadata

    return normalized


def _fingerprint_notebook(path: Path, repo_root: Path) -> FingerprintEntry:
    notebook = json.loads(path.read_text(encoding="utf-8"))
    outputs_payload: list[dict[str, Any]] = []
    code_cell_count = 0

    for cell in notebook.get("cells", []):
        if cell.get("cell_type") != "code":
            continue
        code_cell_count += 1
        for output in cell.get("outputs", []):
            outputs_payload.append(_normalize_output(output))

    canonical_payload = json.dumps(
        outputs_payload,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    )
    digest = hashlib.sha256(canonical_payload.encode("utf-8")).hexdigest()

    return FingerprintEntry(
        notebook=str(path.relative_to(repo_root).as_posix()),
        output_sha256=digest,
        code_cell_count=code_cell_count,
    )


def _resolve_notebooks(repo_root: Path, pattern: str) -> list[Path]:
    notebooks = sorted(repo_root.glob(pattern))
    if not notebooks:
        raise FileNotFoundError(f"No notebooks found for pattern: {pattern}")
    return notebooks


def _build_manifest(repo_root: Path, pattern: str) -> dict[str, Any]:
    notebooks = _resolve_notebooks(repo_root, pattern)

    entries = [_fingerprint_notebook(nb, repo_root) for nb in notebooks]
    return {
        "version": 1,
        "fingerprint_scope": "code_cell_outputs",
        "notebook_glob": pattern,
        "entries": [entry.__dict__ for entry in entries],
    }


def _write_manifest(path: Path, manifest: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def command_generate(repo_root: Path, pattern: str, output: Path) -> int:
    manifest = _build_manifest(repo_root, pattern)
    _write_manifest(output, manifest)
    _json_log(
        "fingerprint.generated",
        output_file=str(output.as_posix()),
        notebook_count=len(manifest["entries"]),
    )
    return 0


def command_verify(repo_root: Path, pattern: str, baseline: Path) -> int:
    if not baseline.exists():
        _json_log("fingerprint.error", reason="baseline_missing", baseline=str(baseline.as_posix()))
        return 2

    current = _build_manifest(repo_root, pattern)
    baseline_manifest = json.loads(baseline.read_text(encoding="utf-8"))

    current_map = {e["notebook"]: e["output_sha256"] for e in current["entries"]}
    baseline_map = {e["notebook"]: e["output_sha256"] for e in baseline_manifest.get("entries", [])}

    missing = sorted(set(baseline_map) - set(current_map))
    added = sorted(set(current_map) - set(baseline_map))
    changed = sorted(
        nb for nb in set(current_map).intersection(baseline_map) if current_map[nb] != baseline_map[nb]
    )

    if not (missing or added or changed):
        _json_log("fingerprint.verify", status="pass", notebook_count=len(current_map))
        return 0

    _json_log(
        "fingerprint.verify",
        status="drift_detected",
        missing=missing,
        added=added,
        changed=changed,
    )
    return 1


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Notebook output fingerprinting")
    parser.add_argument("command", choices=["generate", "verify"])
    parser.add_argument("--notebook-glob", default=DEFAULT_NOTEBOOK_GLOB)
    parser.add_argument("--baseline", type=Path, default=DEFAULT_BASELINE_PATH)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    repo_root = Path(__file__).resolve().parent.parent

    if args.command == "generate":
        return command_generate(repo_root, args.notebook_glob, args.baseline)
    return command_verify(repo_root, args.notebook_glob, args.baseline)


if __name__ == "__main__":
    raise SystemExit(main())
