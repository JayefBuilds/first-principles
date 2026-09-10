# Lobby playground

This tiny Python project models join-code and player-blocking rules for a multiplayer
lobby. It has no third-party dependencies and does not connect to a network or service.

Run its tests from this directory:

```bash
python3 -m unittest discover -s tests -v
```

The application core used in Episode 0.1 is:

- `src/lobby.py` — the behavior under test
- `tests/test_lobby.py` — the executable examples
- `docs/` — the intended product and API behavior
- `tickets/` — deliberately incomplete practice requests for later exercises

Episodes 0.2–0.7 keep their supporting material in this same workspace:

- `exercises/02/` — a synthetic lobby soak-test log
- `exercises/03/` — the project-instruction contract checker
- `exercises/04/` — bug reports and context-measurement helper
- `exercises/05/` — a synthetic incident packet and verification timer
- `exercises/06/` — tool schemas and their measurement script
- `exercises/07/` — a protected fixture, policy check, and safe demonstration
- `skills/bug-report-triage/SKILL.md` — the reusable procedure for Episode 0.4

Every artifact is generated training material. The playground uses only the Python
standard library and makes no network or service connections.
