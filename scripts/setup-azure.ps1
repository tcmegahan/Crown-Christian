<#
PowerShell script to provision Azure resources for Crown / Arete360.
Requires: Azure CLI installed and user logged in: az login
#>
param(
 [string]$rgName = "rg-crown2-dev",
 [string]$location = "eastus",
 [string]$acrName = "crown2acr$(Get-Random -Maximum9999)",
 [string]$appServiceName = "crown2-api",
 [string]$postgresName = "crown2pg$(Get-Random -Maximum9999)",
 [string]$kvName = "kv-crown2-dev$(Get-Random -Maximum9999)"
)

Write-Output "Creating resource group $rgName in $location"
az group create --name $rgName --location $location | ConvertFrom-Json | Write-Output

Write-Output "Creating Azure Container Registry $acrName"
az acr create --resource-group $rgName --name $acrName --sku Standard --admin-enabled false

Write-Output "Creating Azure Database for PostgreSQL Flexible Server $postgresName"
az postgres flexible-server create --resource-group $rgName --name $postgresName --location $location --admin-user crown2 --admin-password 'ReplaceWithSecurePassword!' --sku-name Standard_B1ms --version13 --storage-size32

Write-Output "Creating Key Vault $kvName"
az keyvault create --name $kvName --resource-group $rgName --location $location

Write-Output "Creating App Service plan and Web App (Linux)
"
az appservice plan create --name crown2-plan --resource-group $rgName --sku B1 --is-linux
az webapp create --resource-group $rgName --plan crown2-plan --name $appServiceName --deployment-container-image-name "ghcr.io/yourorg/crown360:latest"

Write-Output "Note: replace placeholders for passwords, secure secrets and configure managed identity / OIDC for GitHub Actions."
Write-Output "Script completed (partial)."