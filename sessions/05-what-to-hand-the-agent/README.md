# 0.5 — Hand over one checkable thing

**Starting state:** Begin in `playground`. The synthetic incident packet lives in `exercises/05/source`. Start the included timer before asking the agent, then inspect one cited heading yourself.

**Exact prompt:**

> Read the incident packet in `exercises/05/source`. Return the trigger, user impact, and recovery in three bullets. Cite the file and heading for each claim. Do not edit anything. Stop when the summary is complete.

**Atoms card:** sort these: summarize the incident ___; choose next quarter's product bet ___; draft a release-note outline ___; approve a customer apology ___; list route boundary cases ___ . One reason each: ___; checked claim: ___; minutes to verify: ___.

**Worked expected example:** A reasonable sort is delegate: incident summary and route boundary cases; pair: release-note outline; keep: product bet and customer apology. The recovery claim is checkable: `exercises/05/source/service-notes.md` → `Recovery` says the on-call engineer cleared the EU West route cache at 14:27.

**Common snag / recovery:** A claim is specific but uncited. Open the named source and heading before accepting it; if it is absent, send the task back as incomplete.

Use `python3 exercises/05/verification_timer.py start` before the prompt and the matching `stop` command after checking one claim. The generated receipt stays inside `exercises/05`.
