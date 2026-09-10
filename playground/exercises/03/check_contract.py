"""Validate the reduced Session 03 project instruction contract."""

from pathlib import Path
import sys


ALLOWED_NAMES = {"AGENTS.md", "CLAUDE.md"}
MAX_NONBLANK_LINES = 10
REQUIRED_PHRASES = ("training project", "python3 -m unittest discover -s tests -v")


def validate(path: Path) -> list[str]:
    errors: list[str] = []
    if path.name not in ALLOWED_NAMES:
        errors.append("Choose AGENTS.md or CLAUDE.md for the harness you are using.")
        return errors
    if not path.is_file():
        errors.append(f"{path.name} does not exist.")
        return errors

    text = path.read_text(encoding="utf-8")
    nonblank = [line for line in text.splitlines() if line.strip()]
    if len(nonblank) > MAX_NONBLANK_LINES:
        errors.append(
            f"{path.name} has {len(nonblank)} nonblank lines. "
            f"Reduce it to {MAX_NONBLANK_LINES} or fewer."
        )
    if "Always start every reply with ACK" in text:
        errors.append("Remove the planted ACK rule before validating the final contract.")
    for phrase in REQUIRED_PHRASES:
        if phrase.lower() not in text.lower():
            errors.append(f"The contract must retain a line containing: {phrase}")
    return errors


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: python3 exercises/03/check_contract.py AGENTS.md")
        print("   or: python3 exercises/03/check_contract.py CLAUDE.md")
        return 2

    path = Path(sys.argv[1])
    errors = validate(path)
    if errors:
        print("Contract needs another pass:")
        for error in errors:
            print(f"  {error}")
        return 1

    line_count = sum(1 for line in path.read_text(encoding="utf-8").splitlines() if line.strip())
    print(f"PASS: {path.name} has {line_count} nonblank lines and no planted rule.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
