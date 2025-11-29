<?php
$path = '../';
$page_title = 'Our Services';
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
                        		<h2 class="text-white">Our Services</h2>
                            </div>
                        </div>
                        <!-- BREADCRUMB ROW -->                            
                            <div>
                                <ul class="wt-breadcrumb breadcrumb-style-2">
                                    <li><a href="<?php echo $path; ?>index.php">Home</a></li>
                                    <li>Services</li>
                                </ul>
                            </div>
                        <!-- BREADCRUMB ROW END -->                        
                    </div>
                </div>
            </div>
            <!-- INNER PAGE BANNER END -->
            
            <!-- SERVICES SECTION START -->
            <?php include($path . 'include/sections/services_images.php'); ?>
            <!-- SERVICES SECTION END -->

            <!-- APPROACH SECTION START -->
            <div class="section-full p-t80 p-b50 bg-white">
                <div class="container">
                    <div class="section-head text-center">
                        <div class="wt-separator-outer separator-center">
                            <div class="wt-separator">
                                <span class="site-text-primary text-uppercase sep-line-one">How We Work</span>
                            </div>
                        </div>
                        <h2>Our Approach</h2>
                        <p>A systematic process ensuring project success from start to finish</p>
                    </div>
                    <div class="row">
                        <div class="col-md-3 col-sm-6 m-b30">
                            <div class="wt-icon-box-wraper center p-a30 bg-gray">
                                <div class="icon-md site-text-primary m-b20">
                                    <span class="icon-cell">1</span>
                                </div>
                                <div class="icon-content">
                                    <h5 class="wt-tilte">Consultation</h5>
                                    <p>Understanding your specific requirements and constraints.</p>
                                </div>
                            </div>
                        </div>
                        <div class="col-md-3 col-sm-6 m-b30">
                            <div class="wt-icon-box-wraper center p-a30 bg-gray">
                                <div class="icon-md site-text-primary m-b20">
                                    <span class="icon-cell">2</span>
                                </div>
                                <div class="icon-content">
                                    <h5 class="wt-tilte">Design</h5>
                                    <p>Creating detailed 3D layouts and technical specifications.</p>
                                </div>
                            </div>
                        </div>
                        <div class="col-md-3 col-sm-6 m-b30">
                            <div class="wt-icon-box-wraper center p-a30 bg-gray">
                                <div class="icon-md site-text-primary m-b20">
                                    <span class="icon-cell">3</span>
                                </div>
                                <div class="icon-content">
                                    <h5 class="wt-tilte">Execution</h5>
                                    <p>Precision manufacturing and professional installation.</p>
                                </div>
                            </div>
                        </div>
                        <div class="col-md-3 col-sm-6 m-b30">
                            <div class="wt-icon-box-wraper center p-a30 bg-gray">
                                <div class="icon-md site-text-primary m-b20">
                                    <span class="icon-cell">4</span>
                                </div>
                                <div class="icon-content">
                                    <h5 class="wt-tilte">Validation</h5>
                                    <p>Testing and commissioning to ensure compliance.</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <!-- APPROACH SECTION END -->

            <!-- CTA SECTION START -->
            <div class="section-full p-t80 p-b80 bg-primary overlay-wraper" style="background-image:url(<?php echo $path; ?>images/background/bg-7.jpg);">
                <div class="overlay-main bg-primary opacity-09"></div>
                <div class="container">
                    <div class="row">
                        <div class="col-md-8">
                            <div class="text-left text-white">
                                <h2>Ready to Start Your Project?</h2>
                                <p>Contact our experts today for a free consultation and quote.</p>
                            </div>
                        </div>
                        <div class="col-md-4">
                            <div class="text-right">
                                <a href="<?php echo $path; ?>contact/index.php" class="site-button-secondry site-btn-effect">Contact Us</a>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <!-- CTA SECTION END -->
            
        </div>
        <!-- CONTENT END -->

<?php
include($path . 'include/footer.php');
?>

</body>
</html>
