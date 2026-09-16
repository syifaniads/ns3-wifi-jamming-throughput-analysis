#!/usr/bin/env python3
"""Validate the retained NS-3 throughput dataset and its interpretation.

The goal is to protect the portfolio from accidental data drift or misleading
percentage calculations, especially the 80 m case where the baseline is zero.
"""
from __future__ import annotations

import csv
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "verified-results.csv"
EXPECTED_DISTANCES = [10, 30, 50, 80]


def approx(a: float, b: float, tol: float = 0.02) -> bool:
    return abs(a - b) <= tol


def main() -> int:
    with DATA.open(newline="", encoding="utf-8") as fh:
        rows = list(csv.DictReader(fh))

    distances = [int(r["distance_m"]) for r in rows]
    if distances != EXPECTED_DISTANCES:
        raise AssertionError(f"unexpected distance sweep: {distances}")

    expected = {
        10: (4.58, 2.52),
        30: (4.58, 2.25),
        50: (4.58, 2.25),
        80: (0.00, 0.00),
    }

    for row in rows:
        distance = int(row["distance_m"])
        normal = float(row["throughput_normal_mbps"])
        interference = float(row["throughput_interference_mbps"])
        exp_normal, exp_interference = expected[distance]

        if not approx(normal, exp_normal) or not approx(interference, exp_interference):
            raise AssertionError(
                f"{distance} m result drifted: got {normal}/{interference}, "
                f"expected {exp_normal}/{exp_interference}"
            )

        if normal > 0:
            reduction = (normal - interference) / normal * 100.0
            if distance == 10 and not approx(reduction, 45.0, 0.2):
                raise AssertionError(f"10 m reduction mismatch: {reduction:.2f}%")
            if distance in (30, 50) and not approx(reduction, 50.87, 0.2):
                raise AssertionError(f"{distance} m reduction mismatch: {reduction:.2f}%")
        else:
            # A zero baseline makes a jamming-specific percentage undefined.
            note = row["reported_reduction"].lower()
            if "baseline also zero" not in note:
                raise AssertionError("80 m row must explicitly note zero baseline")

    print("NS-3 retained-result validation passed")
    print("- distance sweep: 10, 30, 50, 80 m")
    print("- normal/interference throughput values match retained evidence")
    print("- reductions at 10–50 m are numerically consistent")
    print("- 80 m is guarded against misleading percentage interpretation")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except AssertionError as exc:
        print(f"validation failed: {exc}", file=sys.stderr)
        raise SystemExit(1)
