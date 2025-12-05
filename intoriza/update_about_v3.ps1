$file = "c:\xampp\htdocs\pakgusu-1\intoriza\pakgusu-new\intoriza\about\index.html"
$content = Get-Content $file -Raw

# 2. Replace Section using IndexOf with looser end marker
$startMarker = '<div class="section-full p-t80 p-b50 bg-white">'
$endMarker = '<!-- /Section: Company Snapshot -->'

$startIndex = $content.IndexOf($startMarker)
$endIndex = $content.IndexOf($endMarker)

if ($startIndex -ge 0 -and $endIndex -gt $startIndex) {
    # We want to replace everything from start marker up to the END of end marker.
    # But wait, the previous code had </div> before the comment.
    # If we just replace up to end of comment, we might leave a stray </div> or remove too much if there's whitespace.
    # The view_file output showed </div><!-- /Section: Company Snapshot --> on one line.
    
    # Let's adjust endIndex to include the marker length
    $replacementLength = ($endIndex + $endMarker.Length) - $startIndex
    
    # However, we need to check if there is a </div> before the comment that we need to consume.
    # If the file content is "...</div><!-- /Section: Company Snapshot -->", then $startIndex points to start of DIV, $endIndex points to start of COMMENT.
    # If I blindly replace from StartDIV to EndComment, I replace the whole block including the closing DIV.
    # This is correct because my new content includes the new closing DIV and new comment.
    
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

    # Check if there is a </div> preceding the comment immediately?
    # Actually, if I replace from StartDIV to EndComment (inclusive), I remove the old text.
    # The old text was: <div ...> ... </div><!-- Comment -->
    # Replacing it with <section ...> ... </section><!-- Comment -->
    # My newSection includes the closing tags.
    # So replacing from $startIndex to ($endIndex + $endMarker.Length) is correct.
    
    $content = $content.Remove($startIndex, $replacementLength).Insert($startIndex, $newSection)
    
    $content | Set-Content -Path $file -Encoding UTF8
    Write-Host "Section updated successfully using v3."
}
else {
    Write-Host "Markers not found."
    Write-Host "Start Index: $startIndex"
    Write-Host "End Index: $endIndex"
}
