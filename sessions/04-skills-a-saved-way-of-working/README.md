# 0.4 — Save a repeatable triage procedure

**Starting state:** Begin in `playground`. A sample skill already lives at `skills/bug-report-triage/SKILL.md`; two inputs are under `exercises/04/bug-reports/`.

**Exact prompt:**

> Read `skills/bug-report-triage/SKILL.md` and follow its procedure on `exercises/04/bug-reports/bug-01-checkout-retry.md`, then on `exercises/04/bug-reports/bug-02-search-filter.md`. For each, return Impact, Evidence, and Missing facts. Do not invent a cause or fix.

**Atoms card:** skill name: ___; input A output has all three fields: yes/no; input B output has all three fields: yes/no; harness value before/after invocation if available: ___ / ___.

**Worked expected example:** For report A, impact is checkout remaining pending after an approved retry; evidence includes the disabled Retry button and the still-pending page ten minutes later; missing facts include request identifiers and logs. For report B, impact is EU products remaining hidden after the filter is visibly cleared; evidence includes `region=na` remaining in the request and the 51-versus-84 result difference; missing facts include browser and account details. The same three-field shape is the saved procedure.

**Common snag / recovery:** The result adds a diagnosis. Re-read the last line of `SKILL.md` and return only evidence-backed fields. Reference: `skills/bug-report-triage/SKILL.md`.

## Loading the procedure

The explicit file read makes this exercise work without installing a skill. The `skills/` folder here is an example location, not a promise that a product will discover it. You are trying the procedure first. To register it later, use your product's supported skill directory and invocation method. [Codex skills](https://developers.openai.com/codex/skills) and [Claude Code skills](https://code.claude.com/docs/en/skills) describe those separately.
