$file = "intoriza/index.html"
$content = Get-Content -Path $file -Raw

# Update Title
$content = $content -replace '<title>.*?</title>', '<title>Turnkey Cleanroom Solutions in Pakistan | PakGusu Technology</title>'

# Update Meta Description
$content = $content -replace '(<meta content=")[^"]*(" name="description" />)', '${1}PakGusu Technology is a leading cleanroom manufacturer in Pakistan, delivering turnkey modular cleanroom solutions for pharmaceutical, healthcare, electronics, and food industries.${2}'

# Update Meta Keywords
$content = $content -replace '(<meta content=")[^"]*(" name="keywords" />)', '${1}cleanroom manufacturer Pakistan, modular cleanroom, GMP cleanroom, pharmaceutical cleanroom, ISO cleanroom${2}'

# Update Meta Author
$content = $content -replace '(<meta content=")[^"]*(" name="author" />)', '${1}PakGusu Technology${2}'

# Update Meta Robots
$content = $content -replace '(<meta content=")[^"]*(" name="robots" />)', '${1}index, follow${2}'

# Update Contact Info in Sidebar
$content = $content -replace '\(456\) 789 10 12', '92 321 8073738'
$content = $content -replace 'demo@gmail\.com', 'info@pakgusu.com'
$content = $content -replace '55/11 Land Street, Modern New Yourk City, USA', '8-Km, Sundar-Raiwand Road, Lahore, Pakistan'

# Update footer contact info
$content = $content -replace 'intoriza@gmail\.com', 'info@pakgusu.com'
$content = $content -replace '\(\+291\) 912-3456-073', '92 321 8073738'
$content = $content -replace '92 Princess Road, parkvenue,Greater London, NW18JR, United Kingdom', '8-Km, Sundar-Raiwand Road, Lahore, Pakistan'

Set-Content -Path $file -Value $content -NoNewline
Write-Host "Updated homepage meta tags and contact info"
