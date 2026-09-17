# VeriCV

VeriCV is a Codex plugin for evidence-grounded CV matching and tailoring. It compares a candidate's documented background with a job description, classifies requirements as Strong Match, Partial Match, or Not Evidenced, and creates ATS-friendly CVs without inventing facts.

## Included skill

`$vericv:vericv` supports `analyze`, `tailor`, and `batch` modes. It works from local files or pasted content by default and uses a final claim-validation and visual-layout review before delivery.

## Local development

The Codex manifest is in `.codex-plugin/plugin.json`; the skill lives in `skills/vericv/`.

```powershell
python .\skills\vericv\scripts\validate_package.py
python -m unittest discover -s .\skills\vericv\tests -v
```

## Install

For Codex:

```text
npx @ciphertechnologies/vericv codex
```

For Claude Code:

```text
npx @ciphertechnologies/vericv claude
```

The installer confirms before changing marketplace settings. VeriCV is local-file-first: it does not require an account, send candidate material, or include credentials.
