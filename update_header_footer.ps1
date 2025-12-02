$rootPath = "c:\xampp\htdocs\pakgusu-new\intoriza"
$files = Get-ChildItem -Path $rootPath -Recurse -Filter "*.html"

foreach ($file in $files) {
    $content = Get-Content -Path $file.FullName -Raw
    $originalContent = $content

    # 1. Remove Search Button Extra Nav
    # Pattern matches the comment and the div block
    $searchBtnPattern = '(?s)\s*<!-- ETRA Nav -->\s*<div class="extra-nav">\s*<div class="extra-cell">\s*<a class="site-search-btn".*?</div>\s*</div>'
    $content = $content -replace $searchBtnPattern, ""

    # 2. Remove Search Popup
    $searchPopupPattern = '(?s)\s*<!-- Search popup -->\s*<div id="search">.*?</div>'
    $content = $content -replace $searchPopupPattern, ""

    # 3. Ensure UI/UX CSS is linked
    # Calculate relative path
    $relativePath = $file.FullName.Substring($rootPath.Length + 1)
    $depth = ($relativePath.Split('\').Count) - 1
    $prefix = "../" * $depth
    if ($depth -eq 0) { $prefix = "" } # Root files use css/ directly? No, root files usually use ./css or just css/
    
    # Check existing links to determine style
    # Root files in this project seem to use css/style.css
    # Subfolders use ../css/style.css
    
    # Let's just check if it's already there
    if ($content -notmatch "ui-ux-enhancements.css") {
        $cssLink = "<link href=""$($prefix)css/ui-ux-enhancements.css"" rel=""stylesheet"" />"
        $content = $content -replace "</head>", "    $cssLink`n</head>"
    }

    # 4. Ensure UI/UX JS is linked
    if ($content -notmatch "ui-ux-enhancements.js") {
        $jsLink = "<script src=""$($prefix)js/ui-ux-enhancements.js""></script><!-- UI/UX ENHANCEMENTS -->"
        $content = $content -replace "</body>", "    $jsLink`n</body>"
    }

    if ($content -ne $originalContent) {
        Set-Content -Path $file.FullName -Value $content -Encoding UTF8
        Write-Host "Updated: $($file.Name)"
    }
}
