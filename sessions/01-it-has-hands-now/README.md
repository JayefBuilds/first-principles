# 0.1 — See what the agent inspected

**Starting state:** Open a new agent session in this repository's `playground/` folder. Do not edit files.

**Exact prompt:**

> Inspect this playground. Read its README, find the automated tests, run them, and tell me which behavior has the strongest boundary-case coverage. Do not edit files. End with the tools you used in order and the number of tool calls.

**Atoms card:** tools in order: ___; largest result: ___; calls before answer: ___; one observation: ___.

**Worked expected example:** A human shell receipt is `python3 -m unittest discover -s tests -v`: it reports six tests and `OK`. `join_with_code` has the broadest exercised set, including a valid join, wrong code, the exact expiration boundary, and a full lobby. This is shell output, not an agent transcript; an agent's actual tool order and call count will vary, so record its real run rather than copying this receipt.

**Common snag / recovery:** An answer names coverage without opening `tests/test_lobby.py`. Ask it to cite the test names and inspect that file before you accept the claim.
