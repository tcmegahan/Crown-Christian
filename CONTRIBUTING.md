# Contributing

Please do not commit secrets (tokens, passwords, private keys) into the repository.

Recommended workflow:

- Store secrets in environment variables or use GitHub Secrets / Azure Key Vault.
- Add secrets to your local `.env` file and ensure `.env` is in `.gitignore`.
- Use the pre-commit hook that scans for secrets (installed with `pre-commit install`).

If a secret is accidentally committed:
- Revoke the exposed credential immediately.
- Remove the secret from history using `git filter-repo` or BFG and force-push after coordinating with your team.
- Rotate the credential.
