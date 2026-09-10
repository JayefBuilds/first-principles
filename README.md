# First Principles

First Principles is a practical series for moving from a browser chat to working with an agent in a real project. Each session explains one small idea, shows it in a shared playground, and gives you a way to check the result yourself.

## Start here

1. Clone or download this repository.
2. Open `playground/` in Claude Code, Codex, or another coding agent.
3. Read the session README you want to try under `sessions/`.
4. Open that session's `slides.html` in a browser when you want the presentation.

## Prerequisites

- Python 3.10 or newer.
- A coding agent that can work from a local folder. Claude Code and Codex both work.
- No API keys, package installs, servers, or production projects are required.

Verify the sample project from the repository root:

```sh
cd playground
python3 -m unittest discover -s tests -v
```

## What's here

- [Curriculum](CURRICULUM.md) describes the seven sessions.
- [playground](playground/README.md) is the shared Python project used by every exercise.
- `sessions/` contains one folder per session. Each folder has the slides and one learner-facing README.

Speaker notes and recording planning deliberately stay out of this public repository.

## License

First Principles is available for personal, educational, research, and other noncommercial use under the [PolyForm Noncommercial License 1.0.0](LICENSE). Commercial use is not permitted.
