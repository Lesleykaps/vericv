# VeriCV

VeriCV is a Codex plugin for evidence-grounded CV matching and tailoring. It compares a candidate's documented background with a job description, classifies requirements as Strong Match, Partial Match, or Not Evidenced, and creates ATS-friendly CVs without inventing facts.

## Included skill

`$vericv` supports `analyze`, `tailor`, and `batch` modes. It works from local files or pasted content by default and uses a final claim-validation and visual-layout review before delivery.

## Local development

The plugin manifest is in `.codex-plugin/plugin.json`; the skill lives in `skills/vericv/`.

```powershell
python .\skills\vericv\scripts\validate_package.py
python -m unittest discover -s .\skills\vericv\tests -v
```

See [GITHUB-PUBLISHING.md](GITHUB-PUBLISHING.md) to publish this package from a GitHub repository.
