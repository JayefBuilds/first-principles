# 0.1 — See what the agent inspected

**Starting state:** Open a new agent session in this repository's `playground/` folder. Do not edit files.

**Exact prompt:**

> Inspect this playground and answer one question: Can a player join the lobby with the wrong code? Read the README, find the relevant code and test, and run the tests before answering. Do not edit files. Show what evidence supports your answer. End with the tools you used in order and the number of tool calls.

**Atoms card:** tools in order: ___; largest result: ___; calls before answer: ___; one observation: ___.

**Worked expected example:** A human shell receipt is `python3 -m unittest discover -s tests -v`: it reports six tests and `OK`. `src/lobby.py` returns `INVALID_CODE` when the supplied code does not match, and `test_wrong_code_is_rejected` confirms that behavior. This is shell output and file evidence, not an agent transcript. Record the path your agent actually takes rather than copying this receipt.

**Common snag / recovery:** The agent answers from the README or source without running the tests. Ask what it ran, then open `src/lobby.py` and `tests/test_lobby.py` to check the answer yourself.
