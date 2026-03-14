# GitHub README Fetcher

param (
    [string]$OutputFolder = "all_readmes"
)

if (-not (Test-Path $OutputFolder)) {
    New-Item -ItemType Directory -Path $OutputFolder
}

Write-Host "Fetching repository list..." -ForegroundColor Cyan
$repos = gh repo list --limit 1000 --json name,nameWithOwner | ConvertFrom-Json

foreach ($repo in $repos) {
    $repoName = $repo.name
    $nameWithOwner = $repo.nameWithOwner
    $outputFile = Join-Path $OutputFolder "$repoName.README.md"
    
    Write-Host "Fetching README for $nameWithOwner..." -ForegroundColor Gray
    
    # Use gh repo view to get the README content
    $readme = gh repo view $nameWithOwner 2>$null
    if ($LASTEXITCODE -eq 0) {
        $readme | Out-File -FilePath $outputFile -Encoding utf8
        Write-Host "  Success: Saved to $repoName.README.md" -ForegroundColor Green
    } else {
        Write-Host "  Skip: No README found in $nameWithOwner" -ForegroundColor Yellow
    }
}

Write-Host "`nFinished! All READMEs are in the '$OutputFolder' folder." -ForegroundColor Magenta
