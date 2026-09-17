# Output schema

## Match report

```text
job_title: string or "Not stated"
mode: analyze | tailor | batch
source_note: local files/pasted text; profile used yes/no
requirements:
  - id: R1
    priority: required | preferred | unstated
    requirement: string
    classification: Strong Match | Partial Match | Not Evidenced
    evidence:
      - source: CV section / profile statement
        excerpt: minimal supporting text
    reasoning: string
    gap_type: presentation | evidence | qualification | none
supported_keywords: [string]
recommendations: [string]
validation_ledger: # tailor only
  - output_claim: string
    source: string
    status: Supported | Supported with wording adjustment | Removed / ask candidate
```

## Batch comparison

```text
vacancy | qualitative alignment | strongest evidence | key gap | caveat
```

Qualitative alignment must describe the evidence pattern, not an ATS score or hiring likelihood.
