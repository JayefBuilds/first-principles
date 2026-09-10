#!/usr/bin/env python3
"""Measure verification time with only the Python standard library."""

import json
import sys
import time
from pathlib import Path


RECEIPT = Path(__file__).with_name("verification-receipt.json")


def main():
    if len(sys.argv) != 2 or sys.argv[1] not in {"start", "stop"}:
        raise SystemExit("usage: verification_timer.py start|stop")
    if sys.argv[1] == "start":
        RECEIPT.write_text(json.dumps({"started_at": time.time()}) + "\n", encoding="utf-8")
        print("Verification timer started.")
        return
    if not RECEIPT.exists():
        raise SystemExit("Start the timer before stopping it.")
    receipt = json.loads(RECEIPT.read_text(encoding="utf-8"))
    elapsed_seconds = round(time.time() - receipt["started_at"], 1)
    receipt["elapsed_seconds"] = elapsed_seconds
    receipt["elapsed_minutes"] = round(elapsed_seconds / 60, 2)
    RECEIPT.write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
    print(f"Verification time: {elapsed_seconds} seconds ({receipt['elapsed_minutes']} minutes)")


if __name__ == "__main__":
    main()
