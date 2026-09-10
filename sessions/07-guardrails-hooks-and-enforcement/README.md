# 0.7 — Exercise one executable rule

**Starting state:** Begin in `playground`. The policy check and protected fixture live under `exercises/07`. The demonstration changes only a temporary copy.

**Exact prompt:**

> Run `python3 exercises/07/run_demo.py`. Explain which decision came from the model and which decision came from code. Do not edit the protected fixture. End with the number of policy checks and the number of violations.

**Atoms card:** rule: ___; clean result: ___; changed result: ___; policy checks: ___; deliberate violations: ___; enforcement scope: ___.

**Worked expected example:** The shell run prints `PASS: protected/reference.txt matches policy`, then `FAIL: protected/reference.txt changed`, followed by `policy checks: 2` and `violations: 1`. The source fixture stays unchanged because `run_demo.py` uses a temporary directory. This evidence shows the local policy decision; it does not show a universal agent or Codex hook.

**Common snag / recovery:** Calling the check a hook. It is portable validation code. A supported harness can optionally invoke it at a lifecycle event, but verify that harness's current official docs and review its configuration before enabling it.
