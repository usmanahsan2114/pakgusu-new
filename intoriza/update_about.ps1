$file = "c:\xampp\htdocs\pakgusu-1\intoriza\pakgusu-new\intoriza\about\index.html"
$content = Get-Content $file -Raw

# 1. Add CSS Link
$searchHead = '    <link href="../css/industries-redesign.css" rel="stylesheet" /> <!-- INDUSTRIES REDESIGN -->'
$replaceHead = '    <link href="../css/industries-redesign.css" rel="stylesheet" /> <!-- INDUSTRIES REDESIGN -->
    <link href="../css/about-who-we-are.css" rel="stylesheet" /> <!-- ABOUT PAGE REDESIGN -->'

if ($content -match [regex]::Escape($searchHead.Trim())) {
    $content = $content.Replace($searchHead, $replaceHead)
    Write-Host "CSS Link updated."
} else {
    Write-Host "CSS Link pattern not found or already updated."
}

# 2. Replace Section using Regex
# Pattern matches from the unique start div to the unique end comment
$pattern = '(?s)\s+<div class="section-full p-t80 p-b50 bg-white">.*?</div><!-- /Section: Company Snapshot -->'

$newSection = '
            <!-- Section: Who We Are (Redesign) -->
            <section class="section-full p-t80 p-b50 about-hero-section" id="about-pakgusu">
                <div class="about-hero-bg-anim" aria-hidden="true"></div>
                <div class="container">
                    <div class="row align-items-center">
                        <!-- Left Column: Image Stack Slider -->
                        <div class="col-lg-6 col-md-12 m-b30">
                            <div class="about-hero-left">
                                <div class="owl-carousel home-carousel-1 owl-btn-bottom-left">
                                    <div class="item">
                                        <div class="ow-img">
                                            <a href="../products/cleanroom-panels/"><img alt="" src="../images/welcome-slider/1.jpg" /></a>
                                        </div>
                                    </div>
                                    <div class="item">
                                        <div class="ow-img">
                                            <a href="../products/cleanroom-panels/"><img alt="" src="../images/welcome-slider/2.jpg" /></a>
                                        </div>
                                    </div>
                                    <div class="item">
                                        <div class="owl-img">
                                            <a href="../products/cleanroom-panels/"><img alt="" src="../images/welcome-slider/3.jpg" /></a>
                                        </div>
                                    </div>
                                    <div class="item">
                                        <div class="ow-img">
                                            <a href="../products/cleanroom-panels/"><img alt="" src="../images/welcome-slider/4.jpg" /></a>
                                        </div>
                                    </div>
                                    <div class="item">
                                        <div class="ow-img">
                                            <a href="../products/cleanroom-panels/"><img alt="" src="../images/welcome-slider/5.jpg" /></a>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                        
                        <!-- Right Column: Text Content -->
                        <div class="col-lg-6 col-md-12 m-b30">
                            <div class="about-hero-right">
                                <div class="wt-separator-outer separator-left">
                                    <div class="wt-separator">
                                        <span class="site-text-primary text-uppercase sep-line-one">Who We Are</span>
                                    </div>
                                </div>
                                <h2 style="font-size: 32px; font-weight: 700;">About PakGusu – Cleanroom Manufacturer in Pakistan</h2>
                                <div class="about-hero-text">
                                    <p class="m-b15"><strong>PakGusu Technology (Pvt) Ltd</strong> is a specialized <strong>cleanroom solution provider</strong> based in Lahore, Pakistan. We design, manufacture, and install <strong>modular cleanroom systems</strong> that meet international standards for cleanliness, safety, and regulatory compliance.</p>
                                </div>
                                <div class="about-hero-cta">
                                    <a class="site-button m-t15 m-b15" href="../products/cleanroom-panels/">Read More</a>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </section>
            <!-- /Section: Who We Are -->'

if ($content -match $pattern) {
    # Use Regex Replace
    $content = [regex]::Replace($content, $pattern, $newSection)
    Write-Host "Section updated."
    $content | Set-Content -Path $file -Encoding UTF8
    Write-Host "File saved."
} else {
    Write-Host "Section pattern not found."
    # Debug: Output a small chunk where we expect it
    $start = $content.IndexOf("Company Snapshot")
    if ($start -ge 0) {
        Write-Host "Found 'Company Snapshot' at $start"
    }
}
