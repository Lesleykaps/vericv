# VeriCV

An evidence-grounded Codex/ChatGPT skill for comparing a CV with a job description and, when requested, tailoring the CV without inventing facts.

Invoke it as `$vericv analyze`, `$vericv tailor`, or `$vericv batch`.

## What it does

- Parses CVs and job descriptions supplied as pasted text or local PDF, DOCX, TXT, or Markdown files.
- Maps each material job requirement to supporting CV/profile evidence.
- Labels requirements **Strong Match**, **Partial Match**, or **Not Evidenced**; it also identifies presentation, evidence, and qualification gaps.
- Produces a transparent report rather than a fake ATS score.
- Tailors structure and wording only where the source material supports it, then performs a claim-level hallucination validation.
- Keeps work local/file-based by default. It does not upload CVs or retrieve job-posting URLs unless the user explicitly asks.

## Install

Copy the `vericv` folder into your local Codex skills folder (normally `%USERPROFILE%\.codex\skills\vericv`), then start a new Codex turn. On PowerShell:

```powershell
Copy-Item -Recurse -Force .\vericv "$env:USERPROFILE\.codex\skills\vericv"
```

Validate the package before or after copying:

```powershell
python .\scripts\validate_package.py
python -m unittest discover -s tests -v
```

The optional PDF page-density helper requires `pdfplumber` only when inspecting a generated PDF. Install it with `pip install pdfplumber` if your environment does not already provide it.

## Usage

```text
$vericv analyze
CV: C:\path\candidate-cv.docx
Job description: C:\path\job.md
Focus on mandatory requirements and explain every classification.
```

```text
$vericv tailor
CV: [attached]
Job description: [attached]
Candidate profile: I am eligible to work in Zimbabwe; do not add any other facts.
Create a two-page, ATS-friendly CV and a match report.
```

```text
$vericv batch
Master CV: C:\path\master-cv.pdf
Vacancies:
1. C:\path\backend-engineer.md
2. C:\path\data-analyst.md
Rank these by evidence-grounded fit. Do not create tailored CVs unless I ask.
```

See `examples/` for a complete input/output pair. The prompt-facing workflow is in `SKILL.md`; format and policy details are in `references/`.

## Development

`scripts/claim_validator.py` is a small, deterministic guard used by the tests. It detects unsupported skills, metrics, employers, dates, years, qualifications, technologies, responsibilities, and achievements proposed for a tailored CV. It is intentionally conservative: a clean result does not replace the required human evidence review described in the skill.

This project is MIT licensed.
