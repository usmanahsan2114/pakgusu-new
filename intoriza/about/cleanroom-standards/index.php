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
                                <p>The ISO 14644-1 is the international standard for cleanroom classification. Cleanrooms are classified by how clean the air is, based on the number of particles per cubic meter at a specified particle size.<br><br>**Classification Table:**<br><br>| ISO Class | Particle Count (≥0.5 µm per m³) | Equivalent Fed Std 209E |<br>|-----------|----------------------------------|-------------------------|<br>| ISO 1     | 10                               | -                       |<br>| ISO 2     | 100                              | -                       |<br>| ISO 3     | 1,000                            | Class 1                 |<br>| ISO 4     | 10,000                           | Class 10                |<br>| ISO 5     | 100,000                          | Class 100               |<br>| ISO 6     | 1,000,000                        | Class 1,000             |<br>| ISO 7     | -                                | Class 10,000            |<br>| ISO 8     | -                                | Class 100,000           |</p>

                                <h4>Applications by Classification</h4>
                                <p>**ISO Class 4-5 (Class 10-100):**<br>- Semiconductor manufacturing<br>- Pharmaceutical aseptic filling<br>- Medical device assembly<br><br>**ISO Class 6-7 (Class 1,000-10,000):**<br>- Pharmaceutical packaging<br>- Medical device manufacturing<br>- Electronics assembly<br>- Hospital operating rooms<br><br>**ISO Class 8 (Class 100,000):**<br>- Food and beverage packaging<br>- Cosmetics manufacturing<br>- General assembly areas</p>

                                <h4>Environmental Parameters</h4>
                                <p>Beyond particle count, cleanrooms must control:<br><br>**Temperature:** Typically 20-22°C (±2°C)<br>**Humidity:** Usually 45-55% RH (±5%)<br>**Pressure:** Positive differential of 10-15 Pa<br>**Air Changes:** 15-20 per hour (ISO 7-8) to 400-600 per hour (ISO 5)<br>**HEPA Filtration:** 99.97% efficiency at 0.3 µm</p>

                            </div>
                        </div>
                         
                        <div class="col-lg-4 col-md-12">
                            <aside class="side-bar">
                                <!-- CATEGORY -->
                                <div class="widget bg-white">
                                    <h4 class="widget-title">About Us</h4>
                                    <ul class="list-2">
                                        <li><a href="<?php echo $path; ?>about/index.php">Company Overview</a></li>
                                        <li><a href="<?php echo $path; ?>about/about-pak-gusu/index.php">About Pak Gusu</a></li>
                                        <li><a href="<?php echo $path; ?>about/about-gusu-china/index.php">About Gusu China</a></li>
                                        <li><a href="<?php echo $path; ?>about/cleanroom-classifications/index.php">Cleanroom Classifications</a></li>
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
