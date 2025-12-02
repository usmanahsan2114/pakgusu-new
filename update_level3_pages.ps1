# Level 3 Pages: Industries and Products
$files = @(
    # Industries
    "intoriza/industries/index.html",
    "intoriza/industries/pharmaceutical-nutraceutical/index.html",
    "intoriza/industries/healthcare-hospitals/index.html",
    "intoriza/industries/food-beverage/index.html",
    "intoriza/industries/electronics-manufacturing/index.html",
    "intoriza/industries/laboratories-rnd/index.html",
    "intoriza/industries/medical-surgical-devices/index.html",
    # Products
    "intoriza/products/index.html",
    "intoriza/products/cleanroom-panels/index.html",
    "intoriza/products/cleanroom-windows/index.html",
    "intoriza/products/cleanroom-doors/index.html",
    "intoriza/products/pass-through-chambers/index.html",
    "intoriza/products/aluminum-profiles/index.html",
    "intoriza/products/cleanroom-led-lights/index.html",
    # Resources sub-pages
    "intoriza/resources/cleanroom-standards-classifications/index.html",
    "intoriza/resources/faqs/index.html",
    "intoriza/resources/news-events/index.html"
)

foreach ($file in $files) {
    if (Test-Path $file) {
        $content = Get-Content -Path $file -Raw
        
        # Update Contact Info
        $content = $content -replace '\(456\) 789 10 12', '0092 321 8073738'
        $content = $content -replace 'demo@gmail\.com', 'info@pakgusu.com'
        $content = $content -replace '55/11 Land Street, Modern New Yourk City, USA', '8-Km, Sundar-Raiwand Road, Lahore, Pakistan'
        $content = $content -replace 'intoriza@gmail\.com', 'info@pakgusu.com'
        $content = $content -replace '\(\+291\) 912-3456-073', '0092 321 8073738'
        $content = $content -replace '92 Princess Road, parkvenue,Greater London, NW18JR, United Kingdom', '8-Km, Sundar-Raiwand Road, Lahore, Pakistan'
        
        # Update Meta Author
        $content = $content -replace '(<meta content=")[^"]*(" name="author" />)', '${1}PakGusu Technology${2}'
        
        # Update Meta Robots
        $content = $content -replace '(<meta content=")[^"]*(" name="robots" />)', '${1}index, follow${2}'
        
        # Page-specific meta tags
        if ($file -match "industries/pharmaceutical") {
            $content = $content -replace '<title>.*?</title>', '<title>GMP Pharmaceutical Cleanrooms in Pakistan | PakGusu</title>'
            $content = $content -replace '(<meta content=")[^"]*(" name="description" />)', '${1}PakGusu delivers GMP-compliant pharmaceutical cleanrooms for solid dosage, sterile injectable, and nutraceutical manufacturing in Pakistan.${2}'
            $content = $content -replace '(<meta content=")[^"]*(" name="keywords" />)', '${1}pharmaceutical cleanroom, GMP cleanroom Pakistan, sterile manufacturing, nutraceutical cleanroom${2}'
        }
        elseif ($file -match "industries/healthcare") {
            $content = $content -replace '<title>.*?</title>', '<title>Healthcare Cleanrooms - Operating Theatres & Hospitals | PakGusu</title>'
            $content = $content -replace '(<meta content=")[^"]*(" name="description" />)', '${1}PakGusu designs cleanrooms for healthcare including operating theatres, isolation rooms, and hospital pharmacies in Pakistan.${2}'
            $content = $content -replace '(<meta content=")[^"]*(" name="keywords" />)', '${1}healthcare cleanroom, hospital cleanroom, operating theatre, isolation room${2}'
        }
        elseif ($file -match "industries/food-beverage") {
            $content = $content -replace '<title>.*?</title>', '<title>Food & Beverage Cleanrooms | Hygienic Production Environments</title>'
            $content = $content -replace '(<meta content=")[^"]*(" name="description" />)', '${1}PakGusu provides hygienic production and packaging cleanroom environments for the food and beverage industry.${2}'
            $content = $content -replace '(<meta content=")[^"]*(" name="keywords" />)', '${1}food processing cleanroom, beverage production cleanroom, hygienic packaging${2}'
        }
        elseif ($file -match "industries/electronics") {
            $content = $content -replace '<title>.*?</title>', '<title>Electronics Manufacturing Cleanrooms | ESD-Safe Environments</title>'
            $content = $content -replace '(<meta content=")[^"]*(" name="description" />)', '${1}Ultra-clean, ESD-safe cleanroom spaces for sensitive electronics assembly and semiconductor manufacturing.${2}'
            $content = $content -replace '(<meta content=")[^"]*(" name="keywords" />)', '${1}electronics cleanroom, ESD safe cleanroom, semiconductor cleanroom${2}'
        }
        elseif ($file -match "industries/laboratories") {
            $content = $content -replace '<title>.*?</title>', '<title>Laboratory Cleanrooms | R&D Controlled Environments</title>'
            $content = $content -replace '(<meta content=")[^"]*(" name="description" />)', '${1}Controlled cleanroom environments for quality control laboratories, research, and experimental analysis.${2}'
            $content = $content -replace '(<meta content=")[^"]*(" name="keywords" />)', '${1}laboratory cleanroom, research cleanroom, QC laboratory${2}'
        }
        elseif ($file -match "industries/medical-surgical") {
            $content = $content -replace '<title>.*?</title>', '<title>Medical Device Cleanrooms | Sterile Manufacturing Spaces</title>'
            $content = $content -replace '(<meta content=")[^"]*(" name="description" />)', '${1}Clean assembly and sterile packaging cleanrooms for medical and surgical device manufacturing.${2}'
            $content = $content -replace '(<meta content=")[^"]*(" name="keywords" />)', '${1}medical device cleanroom, surgical device manufacturing, sterile packaging${2}'
        }
        elseif ($file -match "industries/index") {
            $content = $content -replace '<title>.*?</title>', '<title>Industries We Serve | PakGusu Cleanroom Solutions</title>'
            $content = $content -replace '(<meta content=")[^"]*(" name="description" />)', '${1}PakGusu cleanroom solutions serve pharmaceutical, healthcare, food, electronics, laboratory, and medical device industries.${2}'
            $content = $content -replace '(<meta content=")[^"]*(" name="keywords" />)', '${1}cleanroom industries, pharmaceutical healthcare food electronics${2}'
        }
        elseif ($file -match "products/cleanroom-panels") {
            $content = $content -replace '<title>.*?</title>', '<title>Cleanroom Panels | Modular Wall & Ceiling Systems</title>'
            $content = $content -replace '(<meta content=")[^"]*(" name="description" />)', '${1}PakGusu cleanroom panels are engineered for airtight, thermally stable, and easy-to-clean walls and ceilings for ISO 5-8 cleanrooms.${2}'
            $content = $content -replace '(<meta content=")[^"]*(" name="keywords" />)', '${1}cleanroom panels, modular wall panels, cleanroom ceiling panels${2}'
        }
        elseif ($file -match "products/cleanroom-windows") {
            $content = $content -replace '<title>.*?</title>', '<title>Cleanroom Windows | Vision Panels for Controlled Environments</title>'
            $content = $content -replace '(<meta content=")[^"]*(" name="description" />)', '${1}PakGusu cleanroom windows provide flush double-glazed vision panels for safe observation between cleanroom zones.${2}'
            $content = $content -replace '(<meta content=")[^"]*(" name="keywords" />)', '${1}cleanroom windows, vision panels, cleanroom observation windows${2}'
        }
        elseif ($file -match "products/cleanroom-doors") {
            $content = $content -replace '<title>.*?</title>', '<title>Cleanroom Doors | Airtight Swing & Sliding Doors</title>'
            $content = $content -replace '(<meta content=")[^"]*(" name="description" />)', '${1}PakGusu cleanroom doors provide reliable sealing, robustness, and high-frequency usage capability for demanding environments.${2}'
            $content = $content -replace '(<meta content=")[^"]*(" name="keywords" />)', '${1}cleanroom doors, airtight doors, sliding cleanroom doors${2}'
        }
        elseif ($file -match "products/pass-through") {
            $content = $content -replace '<title>.*?</title>', '<title>Pass-Through Chambers | Material Transfer Solutions</title>'
            $content = $content -replace '(<meta content=")[^"]*(" name="description" />)', '${1}PakGusu pass-through chambers help move materials between cleanroom zones while maintaining cleanliness and pressure balance.${2}'
            $content = $content -replace '(<meta content=")[^"]*(" name="keywords" />)', '${1}pass-through chamber, material transfer, cleanroom airlock${2}'
        }
        elseif ($file -match "products/aluminum-profiles") {
            $content = $content -replace '<title>.*?</title>', '<title>Aluminum Profiles | Cleanroom Structural Systems</title>'
            $content = $content -replace '(<meta content=")[^"]*(" name="description" />)', '${1}PakGusu aluminum profile systems are the structural backbone of modular cleanrooms, providing robust junctions.${2}'
            $content = $content -replace '(<meta content=")[^"]*(" name="keywords" />)', '${1}aluminum profiles, cleanroom structure, modular cleanroom frame${2}'
        }
        elseif ($file -match "products/cleanroom-led") {
            $content = $content -replace '<title>.*?</title>', '<title>Cleanroom LED Lights | Energy-Efficient Lighting</title>'
            $content = $content -replace '(<meta content=")[^"]*(" name="description" />)', '${1}PakGusu cleanroom LED lights are sealed, energy-efficient fixtures designed for IP-rated, low-particulate performance.${2}'
            $content = $content -replace '(<meta content=")[^"]*(" name="keywords" />)', '${1}cleanroom LED lights, cleanroom lighting, IP rated lights${2}'
        }
        elseif ($file -match "products/index") {
            $content = $content -replace '<title>.*?</title>', '<title>Cleanroom Products & Components | PakGusu</title>'
            $content = $content -replace '(<meta content=")[^"]*(" name="description" />)', '${1}PakGusu manufactures a complete range of cleanroom components including panels, doors, windows, and lighting systems.${2}'
            $content = $content -replace '(<meta content=")[^"]*(" name="keywords" />)', '${1}cleanroom products, cleanroom components, modular cleanroom systems${2}'
        }
        elseif ($file -match "resources/cleanroom-standards") {
            $content = $content -replace '<title>.*?</title>', '<title>Cleanroom Standards & Classifications | ISO 14644 Guide</title>'
            $content = $content -replace '(<meta content=")[^"]*(" name="description" />)', '${1}Understanding cleanroom classifications, ISO 14644-1 standards, and how to choose the right cleanroom class for your facility.${2}'
            $content = $content -replace '(<meta content=")[^"]*(" name="keywords" />)', '${1}ISO 14644, cleanroom classification, cleanroom standards${2}'
        }
        elseif ($file -match "resources/faqs") {
            $content = $content -replace '<title>.*?</title>', '<title>Cleanroom FAQs | Common Questions Answered</title>'
            $content = $content -replace '(<meta content=")[^"]*(" name="description" />)', '${1}Frequently asked questions about cleanroom design, construction, classification, and maintenance answered by PakGusu experts.${2}'
            $content = $content -replace '(<meta content=")[^"]*(" name="keywords" />)', '${1}cleanroom FAQ, cleanroom questions, cleanroom design help${2}'
        }
        elseif ($file -match "resources/news-events") {
            $content = $content -replace '<title>.*?</title>', '<title>Cleanroom News & Events | PakGusu Updates</title>'
            $content = $content -replace '(<meta content=")[^"]*(" name="description" />)', '${1}Stay updated with PakGusu news, cleanroom project announcements, and industry events in Pakistan.${2}'
            $content = $content -replace '(<meta content=")[^"]*(" name="keywords" />)', '${1}cleanroom news, pakgusu events, cleanroom industry pakistan${2}'
        }
        
        Set-Content -Path $file -Value $content -NoNewline
        Write-Host "Updated: $file"
    }
    else {
        Write-Host "Skipped (not found): $file"
    }
}

Write-Host "Level 3 pages updated successfully"
