---
name: vericv
description: Compare a candidate CV with a job description and create evidence-grounded, ATS-friendly tailoring without inventing qualifications, skills, experience, metrics, or achievements. Use for CV-job fit analysis, tailored CVs, and ranking one CV against multiple vacancies.
metadata:
  short-description: Evidence-grounded CV matching and tailoring
---

# VeriCV

Use this skill for three modes: `analyze`, `tailor`, and `batch`. The output must be useful to a candidate while retaining a strict chain from every material claim back to the CV or an explicitly supplied candidate profile.

## Non-negotiable evidence boundary

- Treat the CV and optional candidate profile as the only factual sources. The job description describes requirements, not candidate facts.
- Do not infer or add employers, job titles, dates, qualifications, certifications, technologies, years of experience, metrics, responsibilities, achievements, work authorization, or contact information.
- A synonym or safe abstraction may improve wording only when it preserves the source claim. Do not turn a related technology into an exact technology claim.
- If evidence is unclear, classify it as **Partial Match** or **Not Evidenced** and say why. Ask a focused follow-up only when the missing fact would materially change the result.
- Never provide a numeric ATS score, probability of getting hired, or claim that an employer's ATS will accept the CV.

## Inputs and privacy

Accept local PDF, DOCX, TXT, Markdown, pasted text, and attachments. Parse locally when available. Do not browse, upload, store, email, or share personal data by default. If the user supplies a job URL, ask before retrieving it; if unavailable, request pasted job text. Do not retain raw CV content beyond the active task unless the user asks for a saved output.

## Workflow

1. Identify mode and collect the CV, job description, and any optional profile/tailoring constraints.
2. Extract factual CV evidence by section and preserve the original wording or a concise quotation. Read [matching rules](references/matching-rules.md) and [evidence policy](references/evidence-policy.md).
3. Extract atomic job requirements, marking required versus preferred where stated and separating qualifications, experience, skills, responsibilities, and constraints.
4. Build an evidence map. For every material requirement, give a classification, exact evidence reference(s), reasoning, and gap type. Use the schema in [output schema](references/output-schema.md).
5. Identify genuinely supported keywords absent or weakly expressed in the CV. Distinguish a presentation gap from missing evidence.
6. For `tailor`, create a rewriting and layout plan, then a plain ATS-friendly CV using [ATS guidelines](references/ats-guidelines.md), [CV writing guidelines](references/cv-writing-guidelines.md), and [layout-quality guidance](references/layout-quality.md). Preserve dates and facts; prioritize relevant, supported material. Do not force a requested page count with empty space: use enough supported, relevant content to balance the pages, or explain that a shorter truthful CV is the professional option.
7. Run a hallucination-validation pass before delivery. Compare every material new or modified claim with its evidence source. Remove or flag unsupported claims. Use `scripts/claim_validator.py` as an optional deterministic backstop, not as a substitute for review.

## Mode outputs

### `analyze`

Return the match report only. Do not rewrite the CV. Use `templates/match-report.md` and include strong, partial, and not-evidenced requirements, gap types, evidence, supported keywords, and recommendations.

### `tailor`

Return the complete match report plus a tailored CV based on `templates/tailored-cv.md`. Add a concise validation ledger: material claim, evidence source, outcome. Put requirements with no evidence in a separate truthful gap list, never into the CV.

### `batch`

Analyze one source CV against each vacancy independently. Return a comparison table sorted by qualitative evidence-grounded fit, with the strongest evidence, key missing requirement, and caveat for each. Do not average requirements into an ATS score or blend evidence between jobs. Tailor only the jobs the user selects.

## Delivery checks

Before delivering, verify that every requirement has a classification, every Strong/Partial classification cites evidence, every tailored material claim has an evidence reference, and no unsupported new fact remains. When a CV file is created, render and inspect every page; revise any forced page break or sparse page before delivery. For PDFs, use `scripts/check_pdf_page_density.py` as a diagnostic alongside visual review. See `references/evidence-policy.md` for the full validation checklist.
