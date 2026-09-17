# VeriCV

VeriCV is a portable plugin for evidence-grounded CV matching and truthful ATS-friendly tailoring. It uses the candidate's supplied CV and profile as its factual source, and never invents qualifications, experience, metrics, or achievements.

## Install

```text
npx @ciphertechnologies/vericv codex
npx @ciphertechnologies/vericv claude
```

The installer adds the VeriCV marketplace, refreshes it, and installs the plugin after confirmation.

## Use

In Codex, use `$vericv:vericv`. In Claude Code, use `/vericv:vericv`.

See [`plugins/vericv/README.md`](plugins/vericv/README.md) for validation and usage details.
