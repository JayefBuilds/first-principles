#!/usr/bin/env python3
"""Measure the serialized size of a tool definition file."""

import argparse
import json
import math
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("schema_file", type=Path)
    args = parser.parse_args()

    data = json.loads(args.schema_file.read_text(encoding="utf-8"))
    tools = data.get("tools")
    if not isinstance(tools, list):
        raise SystemExit("schema file must contain a tools array")

    serialized = json.dumps(tools, separators=(",", ":"), ensure_ascii=False)
    print(f"file: {args.schema_file}")
    print(f"tools: {len(tools)}")
    print(f"definition characters: {len(serialized)}")
    print(f"estimated tokens: {math.ceil(len(serialized) / 4)}")
    print("estimate rule: 4 characters per token")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
