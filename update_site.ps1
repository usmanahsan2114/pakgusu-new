$files = Get-ChildItem -Path "intoriza" -Recurse -Filter "*.html"

foreach ($file in $files) {
    $content = Get-Content -Path $file.FullName -Raw
    $originalContent = $content

    # 1. Remove Careers and Case Studies from Header (Regex on full string)
    $headerPattern = '(?s)\s*<li>\s*<a href="[^"]*case-studies/">Case Studies</a>\s*</li>\s*<li>\s*<a href="[^"]*careers/">Careers</a>\s*</li>'
    $content = $content -replace $headerPattern, ''

    # 2. Add Careers to Footer (Line-by-line)
    # Check if Careers is already in footer
    if ($content -notmatch '<li><a data-hover="Careers" href="[^"]*careers/">Careers</a></li>') {
        $lines = $content -split "`r`n"
        $newLines = @()
        $updatedFooter = $false

        foreach ($line in $lines) {
            $newLines += $line
            # Check for Case Studies link in footer
            if ($line -match '<li><a data-hover="Case Studies" href="([^"]*)case-studies/">Case Studies</a></li>') {
                $relativePath = $matches[1]
                # Preserve indentation (capture leading whitespace)
                if ($line -match '^(\s*)') {
                    $indent = $matches[1]
                }
                else {
                    $indent = ""
                }
                
                $careersLine = "${indent}<li><a data-hover=`"Careers`" href=`"${relativePath}careers/`">Careers</a></li>"
                $newLines += $careersLine
                $updatedFooter = $true
                Write-Host "  Added Careers link to $($file.Name)"
            }
        }
        
        if ($updatedFooter) {
            $content = $newLines -join "`r`n"
        }
    }

    if ($content -ne $originalContent) {
        Set-Content -Path $file.FullName -Value $content -NoNewline
        Write-Host "Updated: $($file.Name)"
    }
    else {
        Write-Host "Skipped: $($file.Name)"
    }
}
