# PowerShell helper to run Django migrations using venv if available, otherwise via docker-compose
param()
$repoRoot = Split-Path -Parent $PSScriptRoot
$venvPy = Join-Path $repoRoot ".venv\Scripts\python.exe"
if (Test-Path $venvPy) {
 Write-Output "Using local venv at $venvPy"
 & $venvPy manage.py makemigrations
 & $venvPy manage.py migrate
} elseif (Test-Path "venv\Scripts\python.exe") {
 $py = Join-Path $repoRoot "venv\Scripts\python.exe"
 Write-Output "Using venv at venv: $py"
 & $py manage.py makemigrations
 & $py manage.py migrate
} else {
 Write-Output "No venv found — attempting to run migrations inside Docker Compose (requires docker)."
 docker-compose run --rm api python manage.py makemigrations
 docker-compose run --rm api python manage.py migrate
}
