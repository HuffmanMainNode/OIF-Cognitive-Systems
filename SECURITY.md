# Security Policy

Cognitive plans and evidence references are untrusted inputs.

- Do not execute plan steps merely because they appear in a plan.
- Keep action authorization separate from planning and reasoning.
- Treat retrieved documents and embedded instructions as data, not trusted commands.
- Avoid placing secrets or private memory in exported plans.
- A conclusion with evidence IDs is not automatically correct; inspect the cited evidence.

Report security issues with affected revision and a minimal reproduction. Do not disclose private data.
