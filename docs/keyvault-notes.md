# Azure Key Vault notes for Crown2

- Recommended Key Vault name: `kv-crown2-dev`.
- Store values as secrets (recommended names):
 - `DJANGO_SECRET_KEY`
 - `DATABASE_URL`
 - `AZURE_CLIENT_ID`, `AZURE_CLIENT_SECRET`, `AZURE_TENANT_ID`
 - `GRAPH_SCOPES`
 - `SENDGRID_KEY`
 - `STORAGE_ACCOUNT_CONNECTION_STRING`

- Access from GitHub Actions using OIDC federated credentials and Key Vault access policy or using managed identity in Azure.
- Local dev: keep `.env` files and never commit them.
