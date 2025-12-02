$rootPath = "c:\xampp\htdocs\pakgusu-new\intoriza"
$files = Get-ChildItem -Path $rootPath -Recurse -Filter "*.html"

foreach ($file in $files) {
    # Read content
    $content = Get-Content -Path $file.FullName -Raw -Encoding UTF8
    $originalContent = $content

    # Perform replacements using .Replace() method which is often safer for special chars than -replace operator regex
    $content = $content.Replace('â€“', '–')
    $content = $content.Replace('Ã—', '×')
    $content = $content.Replace('Â©', '©')
    $content = $content.Replace('Â ', ' ')

    if ($content -ne $originalContent) {
        Set-Content -Path $file.FullName -Value $content -Encoding UTF8
        Write-Host "Fixed encoding in: $($file.Name)"
    }
}
