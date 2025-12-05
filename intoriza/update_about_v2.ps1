$file = "c:\xampp\htdocs\pakgusu-1\intoriza\pakgusu-new\intoriza\about\index.html"
$content = Get-Content $file -Raw

# 2. Replace Section using IndexOf
$startMarker = '<div class="section-full p-t80 p-b50 bg-white">'
$endMarker = '</div><!-- /Section: Company Snapshot -->'

$startIndex = $content.IndexOf($startMarker)
$endIndex = $content.IndexOf($endMarker)

if ($startIndex -ge 0 -and $endIndex -gt $startIndex) {
    # Calculate length to remove
    # End index points to the START of the end marker. 
    # We want to replace everything from start marker to the END of end marker.
    $lengthToRemove = ($endIndex + $endMarker.Length) - $startIndex
    
    $newSection = '<section class="section-full p-t80 p-b50 about-hero-section" id="about-pakgusu">
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

    # Perform replacement
    # We remove the old block and insert the new one
    $content = $content.Remove($startIndex, $lengthToRemove).Insert($startIndex, $newSection)
    
    $content | Set-Content -Path $file -Encoding UTF8
    Write-Host "Section updated successfully using IndexOf."
}
else {
    Write-Host "Section markers not found."
    Write-Host "Start Index: $startIndex"
    Write-Host "End Index: $endIndex"
}
