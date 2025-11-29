<?php
$path = '../../';
$page_title = 'Cleanroom Classifications';
include($path . 'include/head.php');
include($path . 'include/header.php');
?>

        <!-- CONTENT START -->
        <div class="page-content">
        
            <!-- INNER PAGE BANNER -->
            <div class="wt-bnr-inr overlay-wraper bg-center" style="background-image:url(<?php echo $path; ?>images/banner/1.jpg);">
            	<div class="overlay-main bg-black opacity-07"></div>
                <div class="container">
                    <div class="wt-bnr-inr-entry">
                    	<div class="banner-title-outer">
                        	<div class="banner-title-name">
                        		<h2 class="text-white">Cleanroom Classifications</h2>
                            </div>
                        </div>
                        <!-- BREADCRUMB ROW -->                            
                            <div>
                                <ul class="wt-breadcrumb breadcrumb-style-2">
                                    <li><a href="<?php echo $path; ?>index.php">Home</a></li>
                                    <li><a href="<?php echo $path; ?>about/index.php">About</a></li>
                                    <li>Cleanroom Classifications</li>
                                </ul>
                            </div>
                        <!-- BREADCRUMB ROW END -->                        
                    </div>
                </div>
            </div>
            <!-- INNER PAGE BANNER END -->
            
            <!-- CONTENT SECTION START -->
            <div class="section-full p-t80 p-b50 bg-white">
                <div class="container">
                    <div class="row">
                        <div class="col-lg-8 col-md-12">
                            <!-- TITLE START -->
                            <div class="section-head">
                                <div class="wt-separator-outer separator-left">
                                    <div class="wt-separator">
                                        <span class="site-text-primary text-uppercase sep-line-one">Understanding Cleanroom Standards</span>
                                    </div>
                                </div>
                                <h2>Cleanroom Classifications</h2>
                            </div>
                            <!-- TITLE END -->
                            
                            <div class="wt-post-text">
                                <p><strong>Cleanrooms are classified according to the number and size of particles permitted per volume of air. Understanding these classifications is crucial for selecting the right cleanroom solution for your specific application.</strong></p>
                                
                                <h4>ISO 14644-1 Standards</h4>
                                <p>The ISO 14644-1 is the international standard for cleanroom classification. Cleanrooms are classified by how clean the air is, based on the number of particles per cubic meter at a specified particle size.</p>
                                
                                <h5>Classification Table</h5>
                                <div class="table-responsive m-b30">
                                    <table class="table table-bordered">
                                        <thead>
                                            <tr>
                                                <th>ISO Class</th>
                                                <th>Particle Count (≥0.5 µm per m³)</th>
                                                <th>Equivalent Fed Std 209E</th>
                                            </tr>
                                        </thead>
                                        <tbody>
                                            <tr><td>ISO 1</td><td>10</td><td>-</td></tr>
                                            <tr><td>ISO 2</td><td>100</td><td>-</td></tr>
                                            <tr><td>ISO 3</td><td>1,000</td><td>Class 1</td></tr>
                                            <tr><td>ISO 4</td><td>10,000</td><td>Class 10</td></tr>
                                            <tr><td>ISO 5</td><td>100,000</td><td>Class 100</td></tr>
                                            <tr><td>ISO 6</td><td>1,000,000</td><td>Class 1,000</td></tr>
                                            <tr><td>ISO 7</td><td>-</td><td>Class 10,000</td></tr>
                                            <tr><td>ISO 8</td><td>-</td><td>Class 100,000</td></tr>
                                        </tbody>
                                    </table>
                                </div>

                                <h4>Applications by Classification</h4>
                                <div class="row m-b30">
                                    <div class="col-md-4">
                                        <div class="wt-icon-box-wraper p-a20 bg-gray">
                                            <h5 class="wt-tilte">ISO Class 4-5</h5>
                                            <span class="site-text-primary">(Class 10-100)</span>
                                            <ul class="list-check-circle primary m-t15">
                                                <li>Semiconductor manufacturing</li>
                                                <li>Pharmaceutical aseptic filling</li>
                                                <li>Medical device assembly</li>
                                            </ul>
                                        </div>
                                    </div>
                                    <div class="col-md-4">
                                        <div class="wt-icon-box-wraper p-a20 bg-gray">
                                            <h5 class="wt-tilte">ISO Class 6-7</h5>
                                            <span class="site-text-primary">(Class 1,000-10,000)</span>
                                            <ul class="list-check-circle primary m-t15">
                                                <li>Pharmaceutical packaging</li>
                                                <li>Medical device manufacturing</li>
                                                <li>Electronics assembly</li>
                                                <li>Hospital operating rooms</li>
                                            </ul>
                                        </div>
                                    </div>
                                    <div class="col-md-4">
                                        <div class="wt-icon-box-wraper p-a20 bg-gray">
                                            <h5 class="wt-tilte">ISO Class 8</h5>
                                            <span class="site-text-primary">(Class 100,000)</span>
                                            <ul class="list-check-circle primary m-t15">
                                                <li>Food and beverage packaging</li>
                                                <li>Cosmetics manufacturing</li>
                                                <li>General assembly areas</li>
                                            </ul>
                                        </div>
                                    </div>
                                </div>

                                <h4>Environmental Parameters</h4>
                                <p>Beyond particle count, cleanrooms must control:</p>
                                <ul class="list-check-circle primary m-b30">
                                    <li><strong>Temperature:</strong> Typically 20-22°C (±2°C)</li>
                                    <li><strong>Humidity:</strong> Usually 45-55% RH (±5%)</li>
                                    <li><strong>Pressure:</strong> Positive differential of 10-15 Pa</li>
                                    <li><strong>Air Changes:</strong> 15-20 per hour (ISO 7-8) to 400-600 per hour (ISO 5)</li>
                                    <li><strong>HEPA Filtration:</strong> 99.97% efficiency at 0.3 µm</li>
                                </ul>

                            </div>
                        </div>
                         
                        <div class="col-lg-4 col-md-12">
                            <aside class="side-bar">
                                <!-- CATEGORY -->
                                <div class="widget bg-white">
                                    <h4 class="widget-title">About Us</h4>
                                    <ul class="list-2">
                                        <li><a href="<?php echo $path; ?>about/index.php">Company Overview</a></li>
                                        <li><a href="<?php echo $path; ?>about/pak-gusu/index.php">About Pak Gusu</a></li>
                                        <li><a href="<?php echo $path; ?>about/gusu-china/index.php">About Gusu China</a></li>
                                        <li><a href="<?php echo $path; ?>about/cleanroom-standards/index.php" class="active">Cleanroom Standards</a></li>
                                    </ul>
                                </div>
                                
                                <!-- CONTACT -->
                                <div class="widget bg-white">
                                    <h4 class="widget-title">Get In Touch</h4>
                                    <p>Have questions about our company or services? We're here to help.</p>
                                    <a href="<?php echo $path; ?>contact/index.php" class="site-button">Contact Us</a>
                                </div>
                            </aside>
                        </div>
                    </div>
                </div>
            </div>
            <!-- CONTENT SECTION END -->
            
        </div>
        <!-- CONTENT END -->

<?php
include($path . 'include/footer.php');
?>

</body>
</html>
