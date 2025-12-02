$content = Get-Content -Path "intoriza/index.html"
$line = $content | Select-String "Case Studies"
Write-Host "Line found: '$($line.Line)'"
Write-Host "Length: $($line.Line.Length)"
$bytes = [System.Text.Encoding]::UTF8.GetBytes($line.Line)
Write-Host "Bytes: $($bytes -join ' ')"
