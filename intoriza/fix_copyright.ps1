$rootPath = "c:\xampp\htdocs\pakgusu-new\intoriza"
$files = Get-ChildItem -Path $rootPath -Filter *.html -Recurse

$count = 0

foreach ($file in $files) {
    Write-Host "Processing $($file.FullName)..."
    $content = Get-Content $file.FullName -Raw -Encoding UTF8
    
    $modified = $false
    
    # Fix copyright symbol (? to ©)
    if ($content -match '\? 2025 by') {
        $content = $content -replace '\? 2025 by', '© 2025 by'
        Write-Host "  - Fixed copyright symbol"
        $modified = $true
    }
    
    # Ensure proper capitalization for company names
    if ($content -match 'Apex IT Solutions' -or $content -match 'Apex Marketings') {
        # Already correct
    }
    
    if ($modified) {
        $content | Set-Content $file.FullName -NoNewline -Encoding UTF8
        $count++
    }
}

Write-Host "`nTotal files updated: $count"
