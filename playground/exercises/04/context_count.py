#!/usr/bin/env python3
"""Record and compare context readings without external packages."""

import json
import sys
from pathlib import Path


RECEIPT = Path(__file__).with_name("context-measurements.json")


def load_measurements():
    if not RECEIPT.exists():
        return {}
    return json.loads(RECEIPT.read_text(encoding="utf-8"))


def show(measurements):
    if not measurements:
        print("No measurements recorded yet.")
        return
    print(json.dumps(measurements, indent=2))
    if "before" in measurements and "after" in measurements:
        difference = measurements["after"] - measurements["before"]
        print(f"difference: {difference:+g}")


def main():
    measurements = load_measurements()
    if len(sys.argv) == 2 and sys.argv[1] == "show":
        show(measurements)
        return
    if len(sys.argv) != 3 or sys.argv[1] not in {"before", "after"}:
        raise SystemExit("usage: context_count.py before|after NUMBER\n       context_count.py show")
    try:
        value = float(sys.argv[2])
    except ValueError as error:
        raise SystemExit("NUMBER must be the numeric value shown by your context view") from error
    measurements[sys.argv[1]] = value
    RECEIPT.write_text(json.dumps(measurements, indent=2) + "\n", encoding="utf-8")
    show(measurements)


if __name__ == "__main__":
    main()
