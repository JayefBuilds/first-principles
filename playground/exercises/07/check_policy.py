#!/usr/bin/env python3
"""Verify that the protected fixture matches the repository policy."""

import argparse
from pathlib import Path


def check(root: Path) -> int:
    expected = (root / "policy" / "expected.txt").read_text(encoding="utf-8")
    actual = (root / "protected" / "reference.txt").read_text(encoding="utf-8")
    if actual != expected:
        print("FAIL: protected/reference.txt changed")
        return 1
    print("PASS: protected/reference.txt matches policy")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", nargs="?", type=Path, default=Path(__file__).parent)
    args = parser.parse_args()
    return check(args.root.resolve())


if __name__ == "__main__":
    raise SystemExit(main())
