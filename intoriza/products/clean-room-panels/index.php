<?php
$path = '../../';
$page_title = 'Clean Room Panels';
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
                        		<h2 class="text-white">Clean Room Panels</h2>
                            </div>
                        </div>
                        <!-- BREADCRUMB ROW -->                            
                            <div>
                                <ul class="wt-breadcrumb breadcrumb-style-2">
                                    <li><a href="<?php echo $path; ?>index.php">Home</a></li>
                                    <li><a href="<?php echo $path; ?>products/index.php">Products</a></li>
                                    <li>Clean Room Panels</li>
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
                                        <span class="site-text-primary text-uppercase sep-line-one">Premium Quality</span>
                                    </div>
                                </div>
                                <h2>Clean Room Panels</h2>
                            </div>
                            <!-- TITLE END -->
                            
                            <!-- PRODUCT GALLERY START -->
                            <div class="m-b30">
                                <?php include($path . 'include/sections/sync_gallery.php'); ?>
                            </div>
                            <!-- PRODUCT GALLERY END -->
                            
                            <div class="wt-post-text">
                                <p>Our clean room panels are designed to meet the highest standards of cleanliness and contamination control. Manufactured using advanced technology and premium materials, these panels provide exceptional performance in controlled environments.</p>
                                
                                <h4>Key Features:</h4>
                                <ul class="list-checked">
                                    <li>High-density insulation for superior thermal performance</li>
                                    <li>Seamless joints to prevent particle accumulation</li>
                                    <li>Corrosion-resistant materials</li>
                                    <li>Easy to clean and maintain</li>
                                    <li>Fire-resistant construction</li>
                                    <li>Available in various thicknesses and finishes</li>
                                </ul>
                                
                                <h4>Applications:</h4>
                                <p>Ideal for pharmaceutical manufacturing, hospital operating rooms, food processing facilities, electronics manufacturing, and research laboratories.</p>
                                
                                <h4>Specifications:</h4>
                                <div class="table-responsive">
                                    <table class="table table-bordered">
                                        <tbody>
                                            <tr>
                                                <td><strong>Material</strong></td>
                                                <td>Galvanized steel / Stainless steel</td>
                                            </tr>
                                            <tr>
                                                <td><strong>Core Material</strong></td>
                                                <td>Rock wool / PU / EPS</td>
                                            </tr>
                                            <tr>
                                                <td><strong>Thickness</strong></td>
                                                <td>50mm / 75mm / 100mm</td>
                                            </tr>
                                            <tr>
                                                <td><strong>Standard Size</strong></td>
                                                <td>1150mm width (customizable)</td>
                                            </tr>
                                        </tbody>
                                    </table>
                                </div>
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
                                    <p>Interested in our clean room panels? Contact us for a detailed quotation.</p>
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
