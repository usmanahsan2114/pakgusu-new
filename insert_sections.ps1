$file = "c:\xampp\htdocs\pakgusu-new\intoriza\index.html"
$content = Get-Content $file -Raw

$statsCounter = @"
            <!-- Section: Statistics Counter -->
            <div class="section-full p-t80 p-b50 overlay-wraper bg-cover bg-no-repeat" style="background-image:url(./images/background/bg-1.jpg);">
                <div class="overlay-main bg-primary opacity-09"></div>
                <div class="container">
                    <div class="section-content">
                        <div class="row">
                            <!-- Counter 1 -->
                            <div class="col-lg-3 col-md-6 col-sm-6 col-xs-6 m-b30">
                                <div class="wt-icon-box-wraper center text-white">
                                    <div class="icon-lg m-b20">
                                        <span class="icon-cell text-white"><i class="flaticon-sketch"></i></span>
                                    </div>
                                    <div class="icon-content">
                                        <div class="wt-separator-outer separator-center">
                                            <div class="wt-separator">
                                                <span class="sep-line-one bg-white"></span>
                                            </div>
                                        </div>
                                        <div class="counter font-50 font-weight-800 m-b5">250</div>
                                        <span class="text-uppercase">Projects Completed</span>
                                    </div>
                                </div>
                            </div>
                            <!-- Counter 2 -->
                            <div class="col-lg-3 col-md-6 col-sm-6 col-xs-6 m-b30">
                                <div class="wt-icon-box-wraper center text-white">
                                    <div class="icon-lg m-b20">
                                        <span class="icon-cell text-white"><i class="flaticon-users"></i></span>
                                    </div>
                                    <div class="icon-content">
                                        <div class="wt-separator-outer separator-center">
                                            <div class="wt-separator">
                                                <span class="sep-line-one bg-white"></span>
                                            </div>
                                        </div>
                                        <div class="counter font-50 font-weight-800 m-b5">150</div>
                                        <span class="text-uppercase">Happy Clients</span>
                                    </div>
                                </div>
                            </div>
                            <!-- Counter 3 -->
                            <div class="col-lg-3 col-md-6 col-sm-6 col-xs-6 m-b30">
                                <div class="wt-icon-box-wraper center text-white">
                                    <div class="icon-lg m-b20">
                                        <span class="icon-cell text-white"><i class="flaticon-trophy"></i></span>
                                    </div>
                                    <div class="icon-content">
                                        <div class="wt-separator-outer separator-center">
                                            <div class="wt-separator">
                                                <span class="sep-line-one bg-white"></span>
                                            </div>
                                        </div>
                                        <div class="counter font-50 font-weight-800 m-b5">15</div>
                                        <span class="text-uppercase">Awards Won</span>
                                    </div>
                                </div>
                            </div>
                            <!-- Counter 4 -->
                            <div class="col-lg-3 col-md-6 col-sm-6 col-xs-6 m-b30">
                                <div class="wt-icon-box-wraper center text-white">
                                    <div class="icon-lg m-b20">
                                        <span class="icon-cell text-white"><i class="flaticon-factory"></i></span>
                                    </div>
                                    <div class="icon-content">
                                        <div class="wt-separator-outer separator-center">
                                            <div class="wt-separator">
                                                <span class="sep-line-one bg-white"></span>
                                            </div>
                                        </div>
                                        <div class="counter font-50 font-weight-800 m-b5">50</div>
                                        <span class="text-uppercase">Engineers</span>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <!-- /Section: Statistics Counter -->
"@

# Insert Statistics Counter
# We use a regex to be more flexible with whitespace
$target1 = '<!-- Section: Turnkey Cleanroom Services -->'
# Check if already inserted to avoid duplication
if ($content -notmatch "Section: Statistics Counter") {
    $replacement1 = $statsCounter + "`r`n" + '<!-- Section: Turnkey Cleanroom Services -->'
    $content = $content.Replace($target1, $replacement1)
    Write-Host "Statistics Counter inserted."
}
else {
    Write-Host "Statistics Counter already present."
}

Set-Content -Path $file -Value $content -Encoding UTF8
Write-Host "Script completed."
