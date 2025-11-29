<?php
$path = '../../';
$page_title = 'After-Sale Services';
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
                        		<h2 class="text-white">After-Sale Services</h2>
                            </div>
                        </div>
                        <!-- BREADCRUMB ROW -->                            
                            <div>
                                <ul class="wt-breadcrumb breadcrumb-style-2">
                                    <li><a href="<?php echo $path; ?>index.php">Home</a></li>
                                    <li><a href="<?php echo $path; ?>services/index.php">Services</a></li>
                                    <li>After-Sale Services</li>
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
                                        <span class="site-text-primary text-uppercase sep-line-one">Ongoing Support</span>
                                    </div>
                                </div>
                                <h2>After-Sale Services</h2>
                            </div>
                            <!-- TITLE END -->
                            
                            <div class="wt-post-text">
                                <p>We provide comprehensive after-sale services to ensure your cleanroom continues to operate at peak performance. Our maintenance and support team is always ready to assist.</p>
                                
                                <h4>What We Offer:</h4>
                                <ul class="list-checked">
                                    <li>Regular maintenance programs</li>
                                    <li>24/7 technical support</li>
                                    <li>Spare parts availability</li>
                                    <li>Performance optimization</li>
                                    <li>Recertification services</li>
                                    <li>Upgrade and modification support</li>
                                </ul>
                                
                                <h4>Why Choose Us:</h4>
                                <p>With years of experience and a team of dedicated professionals, we ensure quality service delivery that meets your exact requirements and exceeds expectations.</p>
                                
                                <div class="m-t30">
                                    <h4>Frequently Asked Questions</h4>
                                    <?php include($path . 'include/sections/accordion.php'); ?>
                                </div>
                            </div>
                        </div>
                        
                        <div class="col-lg-4 col-md-12">
                            <aside class="side-bar">
                                <!-- CATEGORY -->
                                <div class="widget bg-white">
                                    <h4 class="widget-title">Services</h4>
                                    <ul class="list-2">
                                        <li><a href="<?php echo $path; ?>services/planning-and-design/index.php">Planning & Design</a></li>
                                        <li><a href="<?php echo $path; ?>services/clean-room-construction/index.php">Clean Room Construction</a></li>
                                        <li><a href="<?php echo $path; ?>services/installation/index.php">Installation</a></li>
                                        <li><a href="<?php echo $path; ?>services/after-sale-services/index.php">After-Sale Services</a></li>
                                    </ul>
                                </div>
                                
                                <!-- CONTACT -->
                                <div class="widget bg-white">
                                    <h4 class="widget-title">Request Service</h4>
                                    <p>Need our professional services? Get in touch with our team today.</p>
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
