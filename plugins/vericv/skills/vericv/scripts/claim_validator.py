"""Conservative source-claim validator used as a safety backstop for tailored CV facts."""
from __future__ import annotations

import re
from dataclasses import dataclass

MATERIAL_KINDS = ("employer", "date", "qualification", "technology", "year", "metric", "responsibility", "achievement", "skill")

@dataclass(frozen=True)
class Finding:
    kind: str
    value: str
    message: str

def _norm(value: str) -> str:
    return re.sub(r"\s+", " ", value.strip().lower())

def validate_claims(source_facts: dict[str, set[str]], proposed_facts: dict[str, set[str]]) -> list[Finding]:
    """Return findings for proposed material facts not explicitly supported by source facts.

    Callers should extract facts conservatively. This function deliberately does not infer
    equivalents; semantic review remains required by the skill's evidence policy.
    """
    findings: list[Finding] = []
    for kind in MATERIAL_KINDS:
        allowed = {_norm(v) for v in source_facts.get(kind, set())}
        for value in proposed_facts.get(kind, set()):
            if _norm(value) not in allowed:
                findings.append(Finding(kind, value, f"Unsupported {kind}: {value}"))
    return findings
