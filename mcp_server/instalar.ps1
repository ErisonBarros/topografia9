# Instala o servidor MCP "openbot" no Claude Desktop (Windows).
# Uso (PowerShell, na pasta do repositório):
#   powershell -ExecutionPolicy Bypass -File .\mcp_server\instalar.ps1
# Parâmetro opcional: -Repo "D:\outro\caminho"

param(
    [string]$Repo = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path
)
$ErrorActionPreference = "Stop"

# 1) Localiza o uv
$uv = Join-Path $env:USERPROFILE ".local\bin\uv.exe"
if (-not (Test-Path $uv)) {
    $cmd = Get-Command uv -ErrorAction SilentlyContinue
    if (-not $cmd) { throw "uv não encontrado. Instale com: winget install astral-sh.uv" }
    $uv = $cmd.Source
}
$script = Join-Path $Repo "mcp_server\openbot_mcp.py"
if (-not (Test-Path $script)) { throw "Script não encontrado: $script" }
Write-Host "uv:     $uv"
Write-Host "Script: $script"
Write-Host "Repo:   $Repo"

# 2) Pré-instala as dependências no cache do uv (fora do Google Drive)
& $uv sync --script $script
if ($LASTEXITCODE -ne 0) { throw "Falha ao instalar dependências (uv sync --script)." }

# 3) Grava/mescla o claude_desktop_config.json. A versão MSIX atual usa
#    %LOCALAPPDATA%\Claude-Data\claude_<id>\ como pasta de dados; as demais
#    entradas cobrem instalações clássicas/antigas.
$destinos = @(Join-Path $env:APPDATA "Claude\claude_desktop_config.json")
Get-ChildItem (Join-Path $env:LOCALAPPDATA "Claude-Data") -Directory -Filter "claude_*" -ErrorAction SilentlyContinue |
    ForEach-Object { $destinos += Join-Path $_.FullName "claude_desktop_config.json" }
Get-ChildItem (Join-Path $env:LOCALAPPDATA "Packages") -Directory -Filter "Claude_*" -ErrorAction SilentlyContinue |
    ForEach-Object { $destinos += Join-Path $_.FullName "LocalCache\Roaming\Claude\claude_desktop_config.json" }

$servidor = [ordered]@{
    command = $uv
    args    = @("run", "--script", $script)
    env     = [ordered]@{ OPENBOT_REPO = $Repo; PYTHONIOENCODING = "utf-8" }
}

foreach ($cfg in $destinos) {
    $dir = Split-Path $cfg
    if (-not (Test-Path $dir)) { New-Item -ItemType Directory -Path $dir -Force | Out-Null }
    if (Test-Path $cfg) {
        $doc = Get-Content $cfg -Raw -Encoding UTF8
        if ($doc -match '"openbot"') { Write-Host "Já configurado: $cfg"; continue }
        Copy-Item $cfg "$cfg.bak" -Force
        $json = $doc | ConvertFrom-Json
    } else {
        $json = [pscustomobject]@{}
    }
    if (-not ($json.PSObject.Properties.Name -contains "mcpServers")) {
        $json | Add-Member -NotePropertyName mcpServers -NotePropertyValue ([pscustomobject]@{})
    }
    $json.mcpServers | Add-Member -NotePropertyName openbot -NotePropertyValue $servidor -Force
    $texto = $json | ConvertTo-Json -Depth 20
    [IO.File]::WriteAllText($cfg, $texto, (New-Object System.Text.UTF8Encoding($false)))  # UTF-8 sem BOM
    Write-Host "Configurado: $cfg"
}

Write-Host ""
Write-Host "Pronto. Feche o Claude Desktop pela bandeja do sistema (Sair) e abra de novo."
Write-Host "Depois, em Configurações > Desenvolvedor, o servidor 'openbot' deve aparecer como 'running'."
