$rootPath = "c:\xampp\htdocs\pakgusu-new\intoriza"
$files = Get-ChildItem -Path $rootPath -Recurse -Filter "*.html"

# Define bad strings using char codes to avoid script encoding issues
# Â© -> ©
$badCopyright = [string][char]0x00C2 + [string][char]0x00A9
$goodCopyright = [string][char]0x00A9

# Ã— -> ×
$badTimes = [string][char]0x00C3 + [string][char]0x00D7
$goodTimes = [string][char]0x00D7

# â€“ -> – (En-dash)
# Variant 1: Literal â + – (User reported)
$badDash1 = [string][char]0x00E2 + [string][char]0x2013
# Variant 2: Mojibake â + € + “ (Common CP1252 interpretation of E2 80 93)
$badDash2 = [string][char]0x00E2 + [string][char]0x20AC + [string][char]0x201C
# Variant 3: Mojibake â + € + – (If 93 was interpreted as En-dash)
$badDash3 = [string][char]0x00E2 + [string][char]0x20AC + [string][char]0x2013

$goodDash = [string][char]0x2013

# Â  -> Space (Non-breaking space artifact)
$badSpace = [string][char]0x00C2 + [string][char]0x00A0
$goodSpace = " "

foreach ($file in $files) {
    $path = $file.FullName
    # Read as UTF-8
    $content = [System.IO.File]::ReadAllText($path, [System.Text.Encoding]::UTF8)
    $originalContent = $content

    $content = $content.Replace($badCopyright, $goodCopyright)
    $content = $content.Replace($badTimes, $goodTimes)
    $content = $content.Replace($badDash1, $goodDash)
    $content = $content.Replace($badDash2, $goodDash)
    $content = $content.Replace($badDash3, $goodDash)
    $content = $content.Replace($badSpace, $goodSpace)
    
    # Also fix the literal string "â€“" if it exists as those chars
    $content = $content.Replace("â€“", $goodDash)

    if ($content -ne $originalContent) {
        [System.IO.File]::WriteAllText($path, $content, [System.Text.Encoding]::UTF8)
        Write-Host "Fixed encoding in: $($file.Name)"
    }
}
