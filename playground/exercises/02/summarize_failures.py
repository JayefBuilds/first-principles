#!/usr/bin/env python3
"""Count synthetic failure signatures without loading the full log into a model."""

import argparse
from collections import Counter
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("log_file", type=Path)
    args = parser.parse_args()

    counts: Counter[str] = Counter()
    for line in args.log_file.read_text(encoding="utf-8").splitlines():
        for field in line.split():
            if field.startswith("signature="):
                counts[field.removeprefix("signature=")] += 1

    for signature, count in sorted(counts.items()):
        print(f"{count:3} {signature}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
