# Publish VeriCV from GitHub

1. Push the repository root, including `.agents/plugins/marketplace.json`, `.claude-plugin/marketplace.json`, and `plugins/vericv/`.
2. Keep the repository, privacy-policy, and terms URLs in both manifests in sync with the published files.
3. Run the validation commands in the plugin README and test Codex and Claude Code from a clean installation.
4. Publish the npm installer from `npm/vericv-installer` as `@ciphertechnologies/vericv`.

Do not publish candidate CVs, job descriptions, test fixtures containing personal data, or private API credentials in the repository.
