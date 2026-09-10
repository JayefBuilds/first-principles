# 0.6 — Measure a tool contract, locally

**Starting state:** Begin in `playground`. No MCP server is installed or needed.

**Exact prompt:**

> Read `exercises/06/schemas/lean.json` and `exercises/06/schemas/crowded.json`. Run `python3 exercises/06/measure_tools.py` on each. Tell me which set has fewer serialized characters, the character difference, and which one focused tool you would keep for reading an issue. Do not connect to any service.

**Atoms card:** lean tools / characters: ___ / ___; crowded tools / characters: ___ / ___; difference: ___; tool I would keep: ___; reason: ___.

**Worked expected example:** The included shell run reports lean: `tools: 1`, `definition characters: 194`; crowded: `tools: 4`, `definition characters: 1552`. The difference is 1358 characters. These are character counts of compact serialized tool arrays. They are not model token counts, usage, or cost. The named tools are definitions for inspection; this kit does not implement an MCP server or callable `read_issue` integration.

**Common snag / recovery:** Someone starts installing a server. Stop: the exercise is about reading a local contract and comparing its defined surface area. `read_issue` is sufficient for the stated issue-reading job.
