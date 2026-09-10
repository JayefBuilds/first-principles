#!/usr/bin/env python3
"""Exercise the policy check in an isolated temporary copy."""

import tempfile
from pathlib import Path
from shutil import copytree

from check_policy import check


def main() -> int:
    source = Path(__file__).parent
    with tempfile.TemporaryDirectory(prefix="guardrail-demo-") as temp_dir:
        demo_root = Path(temp_dir) / "playground"
        copytree(source / "policy", demo_root / "policy")
        copytree(source / "protected", demo_root / "protected")

        print("check 1, clean copy")
        clean = check(demo_root)

        print("check 2, changed temporary copy")
        target = demo_root / "protected" / "reference.txt"
        target.write_text("temporary change\n", encoding="utf-8")
        changed = check(demo_root)

    violations = int(clean != 0) + int(changed != 0)
    print("policy checks: 2")
    print(f"violations: {violations}")
    return 0 if clean == 0 and changed == 1 else 1


if __name__ == "__main__":
    raise SystemExit(main())
