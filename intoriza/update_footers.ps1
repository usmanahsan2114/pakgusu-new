$rootPath = "c:\xampp\htdocs\pakgusu-new\intoriza"
$files = Get-ChildItem -Path $rootPath -Filter *.html -Recurse

foreach ($file in $files) {
    Write-Host "Processing $($file.FullName)..."
    $content = Get-Content $file.FullName -Raw

    # 1. Clean up literal `r`n artifacts from previous edits
    $content = $content -replace '`r`n', ''

    # 2. Add Footer Main Section ID
    if ($content -match '<div class="footer-top overlay-wraper">') {
        $content = $content -replace '<div class="footer-top overlay-wraper">', '<div id="footer-main-section" class="footer-top overlay-wraper">'
        Write-Host "  - Added footer-main-section ID"
    }

    # 3. Add Footer Bottom Section ID
    if ($content -match '<div class="footer-bottom overlay-wraper">') {
        $content = $content -replace '<div class="footer-bottom overlay-wraper">', '<div id="footer-bottom-section" class="footer-bottom overlay-wraper">'
        Write-Host "  - Added footer-bottom-section ID"
    }

    # 4. Inject CSS Links
    # Check if footer-master.css (bottom) is linked
    if (-not ($content -match 'footer-master.css')) {
        $cssLink = '    <!-- Footer Master UI -->' + [Environment]::NewLine + '    <link href="./css/footer-master.css" rel="stylesheet" />' + [Environment]::NewLine
        $content = $content -replace '</head>', ($cssLink + '</head>')
        Write-Host "  - Linked footer-master.css"
    }

    # Check if footer-main-master.css (main) is linked
    if (-not ($content -match 'footer-main-master.css')) {
        $cssLink = '    <!-- Footer Main Master UI -->' + [Environment]::NewLine + '    <link href="./css/footer-main-master.css" rel="stylesheet" />' + [Environment]::NewLine
        $content = $content -replace '</head>', ($cssLink + '</head>')
        Write-Host "  - Linked footer-main-master.css"
    }
    
    # Fix relative paths for files in subdirectories
    # If file is in a subdirectory (e.g. products/index.html), the link needs to be ../css/...
    # This is a simple heuristic: count depth from root
    $relativePath = $file.FullName.Substring($rootPath.Length + 1)
    $depth = ($relativePath.Split('\').Count) - 1
    
    if ($depth -gt 0) {
        $prefix = "../" * $depth
        $content = $content -replace 'href="./css/footer-master.css"', "href=`"${prefix}css/footer-master.css`""
        $content = $content -replace 'href="./css/footer-main-master.css"', "href=`"${prefix}css/footer-main-master.css`""
        Write-Host "  - Adjusted CSS paths for depth $depth"
    }

    $content | Set-Content $file.FullName -NoNewline
}

Write-Host "All files processed."
