$IndexPath = "c:\xampp\htdocs\pakgusu-1\intoriza\pakgusu-new\intoriza\index.html"
$NewContentPath = "c:\xampp\htdocs\pakgusu-1\intoriza\pakgusu-new\intoriza\solutions_final.html"

# Read files using UTF8
$IndexContent = Get-Content -Path $IndexPath -Raw -Encoding UTF8
$NewContent = Get-Content -Path $NewContentPath -Raw -Encoding UTF8

# Define Markers (Simplified to avoid special char issues)
$StartMarker = "<!-- Our Solutions Overview"
$EndMarker = "<!-- Section: Latest from Resources (Redesigned: News Hub) -->"

# Find positions
$StartIndex = $IndexContent.IndexOf($StartMarker)
$EndIndex = $IndexContent.IndexOf($EndMarker)

if ($StartIndex -eq -1 -or $EndIndex -eq -1) {
    Write-Host "Error: Markers not found."
    Write-Host "Start ($StartMarker): $StartIndex"
    Write-Host "End ($EndMarker): $EndIndex"
    exit 1
}

# Construct new content
# Keep everything before StartMarker
$PreContent = $IndexContent.Substring(0, $StartIndex)
# Keep everything from EndMarker onwards
$PostContent = $IndexContent.Substring($EndIndex)

# Combine
$FinalContent = $PreContent + $NewContent + "`r`n" + $PostContent

# Write back
$FinalContent | Set-Content -Path $IndexPath -Encoding UTF8
Write-Host "Successfully updated index.html with new Solutions section."
