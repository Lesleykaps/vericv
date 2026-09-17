"""Lightweight structural validation for a distributable VeriCV skill."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    "README.md", "LICENSE", "SKILL.md", "references/matching-rules.md",
    "references/evidence-policy.md", "references/ats-guidelines.md", "references/layout-quality.md",
    "references/cv-writing-guidelines.md", "references/output-schema.md",
    "templates/match-report.md", "templates/tailored-cv.md",
    "examples/sample-cv.md", "examples/sample-job-description.md",
    "examples/sample-output.md", "scripts/claim_validator.py", "scripts/check_pdf_page_density.py",
]

def main() -> int:
    missing = [item for item in REQUIRED if not (ROOT / item).is_file()]
    body = (ROOT / "SKILL.md").read_text(encoding="utf-8")
    if not body.startswith("---\nname: vericv\n"):
        missing.append("valid SKILL.md frontmatter")
    if missing:
        print("Missing or invalid: " + ", ".join(missing))
        return 1
    print("vericv package validation passed")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
