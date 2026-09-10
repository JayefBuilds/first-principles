# 0.2 Choose the evidence for the next question

Start each comparison in a fresh agent session opened from this repository's `playground/` folder. The included synthetic lobby log has 59 lines. It contains routine messages and three recurring failure signatures. It is invented training data.

## First run: read the log

Ask: “Read only `exercises/02/lobby-soak-test.log`. Summarize the recurring failure signatures and their counts. Do not read other project files and do not edit anything.” If the tool offers a context display, record its label and value before and after. Inspect the actual read result: a product may truncate it or read it in pieces. Do not assume a request to read a file means every line reached the model.

## Second run: return the summary

Start fresh from the same playground and ask:

> Run `python3 exercises/02/summarize_failures.py exercises/02/lobby-soak-test.log`. Report the signatures and counts it prints. Do not read the full log or edit files.

Open `exercises/02/summarize_failures.py` yourself if you want to understand how the counting works. For this comparison, the command reads the file locally and prints three summary lines. The full log does not need to appear in its output. Check both answers against the same reference:

```text
  4 blocked-invite-delivered
  4 rejected-join-mutated-state
  4 stale-membership-cache
```

These are deterministic fixture counts, not token measurements. The command's output is a useful size comparison, not proof of lower billable usage or better model quality. Startup instructions and other tool actions can affect the whole session.

## Record what changed

Record the outputs you actually saw, whether either was truncated, and any usage display your tool provides. If unavailable, write “not exposed.” Then describe a question that would need the full log instead of just counts, such as checking the order of two events.

## If you get stuck

If the read is truncated, ask for the next portion or use the summary command and note the limitation. If the command cannot find the file, return to the playground directory. If the model gives a different count, compare it against the reference command and inspect the disagreement. That gives you something useful to learn from.
