<?php
$path = '../../';
$page_title = 'Clean LED Lights';
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
                        		<h2 class="text-white">Clean LED Lights</h2>
                            </div>
                        </div>
                        <!-- BREADCRUMB ROW -->                            
                            <div>
                                <ul class="wt-breadcrumb breadcrumb-style-2">
                                    <li><a href="<?php echo $path; ?>index.php">Home</a></li>
                                    <li><a href="<?php echo $path; ?>products/index.php">Products</a></li>
                                    <li>Clean LED Lights</li>
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
                                        <span class="site-text-primary text-uppercase sep-line-one">Illumination Solutions</span>
                                    </div>
                                </div>
                                <h2>Clean LED Lights</h2>
                            </div>
                            <!-- TITLE END -->
                            
                            <!-- PRODUCT GALLERY START -->
                            <div class="m-b30">
                                <?php include($path . 'include/sections/sync_gallery.php'); ?>
                            </div>
                            <!-- PRODUCT GALLERY END -->
                            
                            <div class="wt-post-text">
                                <p>Energy-efficient LED lighting fixtures designed specifically for cleanroom environments. Our lights provide excellent illumination while maintaining cleanliness standards.</p>
                                
                                <h4>Key Features:</h4>
                                <ul class="list-checked">
                                    <li>Sealed and gasketed design</li>
                                    <li>Easy to clean surfaces</li>
                                    <li>Low heat emission</li>
                                    <li>Energy-efficient LED technology</li>
                                    <li>Long lifespan (50,000+ hours)</li>
                                    <li>Available in various lux levels</li>
                                </ul>
                                
                                <h4>Applications:</h4>
                                <p>Suitable for pharmaceutical facilities, hospitals, food processing units, electronics manufacturing, and research laboratories.</p>
                            </div>
                        </div>
                        
                        <div class="col-lg-4 col-md-12">
                            <aside class="side-bar">
                                <!-- CATEGORY -->
                                <div class="widget bg-white">
                                    <h4 class="widget-title">Products</h4>
                                    <ul class="list-2">
                                        <li><a href="<?php echo $path; ?>products/clean-room-panels/index.php">Clean Room Panels</a></li>
                                        <li><a href="<?php echo $path; ?>products/windows/index.php">Windows</a></li>
                                        <li><a href="<?php echo $path; ?>products/doors/index.php">Doors</a></li>
                                        <li><a href="<?php echo $path; ?>products/transfer-window/index.php">Transfer Window</a></li>
                                        <li><a href="<?php echo $path; ?>products/aluminum-profile/index.php">Aluminum Profile</a></li>
                                        <li><a href="<?php echo $path; ?>products/clean-led-lights/index.php">Clean LED Lights</a></li>
                                    </ul>
                                </div>
                                
                                <!-- CONTACT -->
                                <div class="widget bg-white">
                                    <h4 class="widget-title">Get a Quote</h4>
                                    <p>Interested in this product? Contact us for detailed information and quotation.</p>
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
