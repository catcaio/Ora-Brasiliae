"""Parameter translation from abstract coefficients (a, b) to physical decoherence rates.

This script reproduces the calibration used in notebook 12 and projects it onto
reference physical systems used in notebook 15.
"""

from __future__ import annotations

import argparse
import json
import math
from dataclasses import asdict, dataclass


@dataclass(frozen=True)
class CalibrationResult:
    n_target: int
    v_target: float
    tau_s: float
    gamma_required_s_inv: float
    a_linear_s_inv_per_component: float
    b_quadratic_s_inv_per_component2: float


@dataclass(frozen=True)
class SystemProjection:
    system: str
    n_typical: int
    gamma_reference_s_inv: str
    gamma_linear_s_inv: float
    gamma_quadratic_s_inv: float


def calibrate_parameters(n_target: int, v_target: float, tau_s: float) -> CalibrationResult:
    if n_target <= 0:
        raise ValueError("n_target must be > 0")
    if tau_s <= 0:
        raise ValueError("tau_s must be > 0")
    if not (0.0 < v_target < 1.0):
        raise ValueError("v_target must be in (0, 1)")

    gamma_required = -2.0 * math.log(v_target) / tau_s
    a_param = gamma_required / n_target
    b_param = gamma_required / (n_target**2)

    return CalibrationResult(
        n_target=n_target,
        v_target=v_target,
        tau_s=tau_s,
        gamma_required_s_inv=gamma_required,
        a_linear_s_inv_per_component=a_param,
        b_quadratic_s_inv_per_component2=b_param,
    )


def project_to_systems(a_param: float, b_param: float) -> list[SystemProjection]:
    systems = [
        ("Gases Frios (BEC em armadilha)", 10_000, "0.1-10"),
        ("Interferometria Molecular", 50, "1-100"),
        ("Átomos de Rydberg", 30, "1e3-1e5"),
    ]
    return [
        SystemProjection(
            system=system,
            n_typical=n_typical,
            gamma_reference_s_inv=gamma_reference,
            gamma_linear_s_inv=a_param * n_typical,
            gamma_quadratic_s_inv=b_param * (n_typical**2),
        )
        for system, n_typical, gamma_reference in systems
    ]


def main() -> None:
    parser = argparse.ArgumentParser(description="Translate abstract parameters (a,b) to physical rates")
    parser.add_argument("--n-target", type=int, default=100)
    parser.add_argument("--v-target", type=float, default=0.5)
    parser.add_argument("--tau", type=float, default=1.0)
    parser.add_argument("--json", action="store_true", help="Emit JSON instead of plain text")
    args = parser.parse_args()

    calibration = calibrate_parameters(args.n_target, args.v_target, args.tau)
    projections = project_to_systems(
        calibration.a_linear_s_inv_per_component,
        calibration.b_quadratic_s_inv_per_component2,
    )

    if args.json:
        print(
            json.dumps(
                {
                    "calibration": asdict(calibration),
                    "systems": [asdict(item) for item in projections],
                },
                ensure_ascii=False,
                indent=2,
            )
        )
        return

    print("=== Parameter calibration ===")
    print(f"N target            : {calibration.n_target}")
    print(f"V target            : {calibration.v_target}")
    print(f"tau (s)             : {calibration.tau_s}")
    print(f"gamma required (s^-1): {calibration.gamma_required_s_inv:.6f}")
    print(f"a linear             : {calibration.a_linear_s_inv_per_component:.6f}")
    print(f"b quadratic          : {calibration.b_quadratic_s_inv_per_component2:.6f}")
    print("\n=== Physical projection ===")
    for projection in projections:
        print(
            "- "
            f"{projection.system}: "
            f"N={projection.n_typical}, "
            f"gamma_ref={projection.gamma_reference_s_inv} s^-1, "
            f"gamma_linear={projection.gamma_linear_s_inv:.3f} s^-1, "
            f"gamma_quadratic={projection.gamma_quadratic_s_inv:.3f} s^-1"
        )


if __name__ == "__main__":
    main()
