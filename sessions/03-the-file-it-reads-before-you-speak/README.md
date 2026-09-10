# 0.3 Write an instruction you can test

Use a fresh copy of this repository's `playground/` folder for this experiment. All agent sessions below start from `playground/`.

## Choose the file

For Codex, use `AGENTS.md`. For Claude Code, use `CLAUDE.md`. The examples in this session's `examples/` folder show the same small project facts. Copy the matching example into the playground with its real filename. Read any existing file first and preserve it: if you already added your own instructions, back them up and add only the temporary test line.

From the playground, on macOS/Linux, a fresh sample can use one of these commands:

```sh
cp ../sessions/03-the-file-it-reads-before-you-speak/examples/AGENTS.md AGENTS.md
```

or, for Claude Code:

```sh
cp ../sessions/03-the-file-it-reads-before-you-speak/examples/CLAUDE.md CLAUDE.md
```

Use a text editor for the equivalent copy on any platform. No script installs or overwrites instruction files automatically.

## Run the comparison yourself

1. Add `Start every reply with ACK.` as a separate line in the instruction file.
2. Start a new agent session from the playground. Ask: “What command runs this playground's tests?” Record whether the reply starts with ACK and check the test command it gives.
3. In your editor, remove only the temporary ACK line. Start another new agent session and ask the same question. Record what changed.
4. Keep the useful project facts, then run `python3 exercises/03/check_contract.py AGENTS.md` or the matching `CLAUDE.md` command. The exercise contract must have ten nonblank lines or fewer and no planted ACK rule.
5. If you backed up an existing file, restore it after the experiment.

Starting a new session is your action. A prompt inside an old conversation cannot reset that conversation. Other parent or personal instructions can still influence both runs.

## Expected observation and limits

You may see ACK in the first response and no ACK in the second. Record the actual behavior even if the rule is missed or persists. This tests whether an instruction influences a response in your setup. It does not prove hidden request transport, guarantee future compliance, or measure cached tokens.

The correct test command in this sample is `python3 -m unittest discover -s tests -v`. Check it against the README. The contract checker lives inside the same playground at `exercises/03/check_contract.py`.

## If you get stuck

Check the filename, the agent's working directory, and whether you really started fresh. Use the product's instruction discovery view or documentation if the rule was not loaded. Avoid deleting other project rules to make the experiment pass.

Sources: [Codex project instructions](https://developers.openai.com/codex/guides/agents-md), [Claude Code memory](https://code.claude.com/docs/en/memory).
