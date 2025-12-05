# Level 2 Pages: services, about, contact, careers, case-studies, resources pages
$files = @(
    "intoriza/services/index.html",
    "intoriza/about/index.html",
    "intoriza/contact/index.html",
    "intoriza/careers/index.html",
    "intoriza/case-studies/index.html",
    "intoriza/resources/index.html",
    "intoriza/resources/blog/index.html"
)

foreach ($file in $files) {
    if (Test-Path $file) {
        $content = Get-Content -Path $file -Raw
        
        # Update Contact Info
        $content = $content -replace '\(456\) 789 10 12', '92 321 8073738'
        $content = $content -replace 'demo@gmail\.com', 'info@pakgusu.com'
        $content = $content -replace '55/11 Land Street, Modern New Yourk City, USA', '8-Km, Sundar-Raiwand Road, Lahore, Pakistan'
        $content = $content -replace 'intoriza@gmail\.com', 'info@pakgusu.com'
        $content = $content -replace '\(\+291\) 912-3456-073', '92 321 8073738'
        $content = $content -replace '92 Princess Road, parkvenue,Greater London, NW18JR, United Kingdom', '8-Km, Sundar-Raiwand Road, Lahore, Pakistan'
        
        # Update Meta Author
        $content = $content -replace '(<meta content=")[^"]*(" name="author" />)', '${1}PakGusu Technology${2}'
        
        # Update Meta Robots
        $content = $content -replace '(<meta content=")[^"]*(" name="robots" />)', '${1}index, follow${2}'
        
        # Page-specific updates
        $filename = Split-Path $file -Leaf
        $directory = Split-Path (Split-Path $file -Parent) -Leaf
        
        if ($file -match "services") {
            $content = $content -replace '<title>.*?</title>', '<title>Turnkey Cleanroom Services | PakGusu Technology</title>'
            $content = $content -replace '(<meta content=")[^"]*(" name="description" />)', '${1}PakGusu provides end-to-end cleanroom services from design and construction to installation, commissioning, and after-sales support.${2}'
            $content = $content -replace '(<meta content=")[^"]*(" name="keywords" />)', '${1}cleanroom services, cleanroom design, cleanroom construction, cleanroom commissioning, GMP validation${2}'
        }
        elseif ($file -match "about") {
            $content = $content -replace '<title>.*?</title>', '<title>About PakGusu - Cleanroom Manufacturer in Pakistan</title>'
            $content = $content -replace '(<meta content=")[^"]*(" name="description" />)', '${1}PakGusu Technology is a specialized cleanroom solution provider in Pakistan, delivering modular cleanroom systems that meet international standards for cleanliness and safety.${2}'
            $content = $content -replace '(<meta content=")[^"]*(" name="keywords" />)', '${1}about pakgusu, cleanroom manufacturer pakistan, GUSU partnership, modular cleanroom systems${2}'
        }
        elseif ($file -match "contact") {
            $content = $content -replace '<title>.*?</title>', '<title>Contact PakGusu - Cleanroom Solutions in Pakistan</title>'
            $content = $content -replace '(<meta content=")[^"]*(" name="description" />)', '${1}Contact PakGusu Technology for turnkey cleanroom design, construction, and maintenance services in Pakistan.${2}'
            $content = $content -replace '(<meta content=")[^"]*(" name="keywords" />)', '${1}contact pakgusu, cleanroom inquiry, cleanroom quote pakistan${2}'
        }
        elseif ($file -match "careers") {
            $content = $content -replace '<title>.*?</title>', '<title>Careers at PakGusu - Join Our Cleanroom Team</title>'
            $content = $content -replace '(<meta content=")[^"]*(" name="description" />)', '${1}Join PakGusu and help build the next generation of cleanroom facilities in Pakistan. We are looking for engineers, technicians, and professionals passionate about quality and innovation.${2}'
            $content = $content -replace '(<meta content=")[^"]*(" name="keywords" />)', '${1}cleanroom jobs pakistan, cleanroom engineer jobs, pakgusu careers${2}'
        }
        elseif ($file -match "case-studies") {
            $content = $content -replace '<title>.*?</title>', '<title>Cleanroom Case Studies | PakGusu Projects in Pakistan</title>'
            $content = $content -replace '(<meta content=")[^"]*(" name="description" />)', '${1}Explore PakGusu cleanroom projects across pharmaceutical, healthcare, electronics, and food industries in Pakistan.${2}'
            $content = $content -replace '(<meta content=")[^"]*(" name="keywords" />)', '${1}cleanroom projects pakistan, pharmaceutical cleanroom case study, cleanroom success stories${2}'
        }
        elseif ($file -match "resources/blog") {
            $content = $content -replace '<title>.*?</title>', '<title>Cleanroom Blog | PakGusu Insights and Tips</title>'
            $content = $content -replace '(<meta content=")[^"]*(" name="description" />)', '${1}The PakGusu blog shares cleanroom insights, design tips, regulatory updates, and project stories to help engineers and facility managers make informed decisions.${2}'
            $content = $content -replace '(<meta content=")[^"]*(" name="keywords" />)', '${1}cleanroom blog, cleanroom design tips, GMP guidelines, ISO 14644${2}'
        }
        elseif ($file -match "resources/index") {
            $content = $content -replace '<title>.*?</title>', '<title>Cleanroom Resources | PakGusu Knowledge Hub</title>'
            $content = $content -replace '(<meta content=")[^"]*(" name="description" />)', '${1}PakGusu Resources section provides practical cleanroom information, standards, design best practices, and industry trends.${2}'
            $content = $content -replace '(<meta content=")[^"]*(" name="keywords" />)', '${1}cleanroom resources, cleanroom standards, ISO 14644, GMP guidelines${2}'
        }
        
        Set-Content -Path $file -Value $content -NoNewline
        Write-Host "Updated: $file"
    }
    else {
        Write-Host "Skipped (not found): $file"
    }
}

Write-Host "Level 2 pages updated successfully"
