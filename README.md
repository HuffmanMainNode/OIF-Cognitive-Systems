# OIF Cognitive Systems

**Inspectable task decomposition and evidence-aware reasoning primitives.**

This repository focuses on cognitive workflow structures rather than model training. It provides a small planner that turns a goal into ordered, dependency-aware steps and an evidence ledger that flags unsupported conclusions. It does not claim to reproduce human cognition or guarantee correct reasoning.

## Implemented

- Structured plans with stable step IDs, dependencies, and explicit completion state.
- Dependency validation and cycle detection.
- Evidence references attached to conclusions.
- A guard that prevents a conclusion from being marked supported without evidence.
- Standard-library-only Python package, CLI, examples, and tests.

## Quick start

```bash
python -m pip install -e .
python -m unittest discover -s tests -v
oif-cognitive-check examples/plan.json
```

## Design principles

- Separate observations, hypotheses, and conclusions.
- Make dependencies explicit rather than hiding them in prose.
- Preserve uncertainty and missing evidence.
- Do not equate fluent output with verified reasoning.
- Keep memory writes and external actions behind explicit policy boundaries.

## Scope

This project owns plan structure, dependency checks, and evidence-linked reasoning records. Distributed expert selection is handled by [OI-Swarm-Intelligence](https://github.com/HuffmanMainNode/OI-Swarm-Intelligence); cross-agent aggregation belongs in [OIF-Collective-Intelligence](https://github.com/HuffmanMainNode/OIF-Collective-Intelligence).
