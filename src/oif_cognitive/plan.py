"""Dependency-aware plan validation and evidence-linked conclusions."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


def validate_plan(plan: Any) -> list[str]:
    if not isinstance(plan, dict) or not isinstance(plan.get("steps"), list):
        return ["plan must be an object containing a steps array"]
    errors: list[str] = []
    by_id: dict[str, dict[str, Any]] = {}
    for index, step in enumerate(plan["steps"]):
        if not isinstance(step, dict) or not isinstance(step.get("id"), str) or not step["id"]:
            errors.append(f"step {index} must have a non-empty id")
            continue
        if step["id"] in by_id:
            errors.append(f"duplicate step id: {step['id']}")
        by_id[step["id"]] = step
    for step_id, step in by_id.items():
        for dependency in step.get("depends_on", []):
            if dependency not in by_id:
                errors.append(f"{step_id} depends on unknown step: {dependency}")

    visiting: set[str] = set()
    visited: set[str] = set()

    def visit(node: str) -> None:
        if node in visiting:
            errors.append(f"dependency cycle detected at: {node}")
            return
        if node in visited:
            return
        visiting.add(node)
        for dependency in by_id.get(node, {}).get("depends_on", []):
            if dependency in by_id:
                visit(dependency)
        visiting.remove(node)
        visited.add(node)

    for step_id in by_id:
        visit(step_id)

    for conclusion in plan.get("conclusions", []):
        if conclusion.get("status") == "supported" and not conclusion.get("evidence_ids"):
            errors.append(f"supported conclusion lacks evidence: {conclusion.get('id', '<unknown>')}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate an OIF cognitive plan.")
    parser.add_argument("plan", type=Path)
    args = parser.parse_args()
    data = json.loads(args.plan.read_text(encoding="utf-8"))
    errors = validate_plan(data)
    if errors:
        print("\n".join(f"ERROR: {error}" for error in errors))
        return 1
    print(f"VALID: {len(data['steps'])} plan steps")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
