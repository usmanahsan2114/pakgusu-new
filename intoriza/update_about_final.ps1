$file = "c:\xampp\htdocs\pakgusu-1\intoriza\pakgusu-new\intoriza\about\index.html"
$content = Get-Content $file -Raw

# 1. Add CSS Link (Rigorous check)
# We look for industries-redesign.css and make sure about-who-we-are.css is not already there.
if ($content -notmatch 'about-who-we-are.css') {
    $content = $content -replace '(<link href="\.\./css/industries-redesign\.css" rel="stylesheet" /> <!-- INDUSTRIES REDESIGN -->)', '$1
    <link href="../css/about-who-we-are.css" rel="stylesheet" /> <!-- ABOUT PAGE REDESIGN -->'
    Write-Host "CSS Link added."
}
else {
    Write-Host "CSS Link already present."
}

# 2. Fix Typo / Encoding
# â€“ to -
if ($content -match 'â€“') {
    $content = $content -replace 'â€“', '–'
    Write-Host "Fixed encoding artifact."
}

$content | Set-Content -Path $file -Encoding UTF8
Write-Host "Final update complete."
