<?php
$path = '../';
$page_title = 'Gallery';
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
                        		<h2 class="text-white">Photo Gallery</h2>
                            </div>
                        </div>
                        <!-- BREADCRUMB ROW -->                            
                            <div>
                                <ul class="wt-breadcrumb breadcrumb-style-2">
                                    <li><a href="<?php echo $path; ?>index.php">Home</a></li>
                                    <li>Gallery</li>
                                </ul>
                            </div>
                        <!-- BREADCRUMB ROW END -->                        
                    </div>
                </div>
            </div>
            <!-- INNER PAGE BANNER END -->
            
            <!-- GALLERY SECTION START -->
            <div class="section-full p-t80 p-b50 bg-white">
                <div class="container">
                    
                    <!-- TITLE START -->
                    <div class="section-head text-center">
                        <div class="wt-separator-outer separator-center">
                            <div class="wt-separator">
                                <span class="site-text-primary text-uppercase sep-line-one">Visual Showcase</span>
                            </div>
                        </div>
                        <h2>Our Gallery</h2>
                        <p>Explore our collection of cleanroom installations, products, and project highlights</p>
                    </div>
                    <!-- TITLE END -->
                    
                    <div class="row justify-content-center">
                        <div class="col-lg-8">
                            <div class="wt-box text-center p-a30">
                                <p class="m-b30">Browse through our comprehensive gallery showcasing cleanroom products, installations, and completed projects. Click below to view detailed galleries organized by blog posts.</p>
                                <a href="<?php echo $path; ?>blogs/post-gallery/index.php" class="site-button m-r15">View Photo Gallery</a>
                                <a href="<?php echo $path; ?>projects/grid/index.php" class="site-button-secondry">View Projects</a>
                            </div>
                        </div>
                    </div>
                    
                </div>
            </div>
            <!-- GALLERY SECTION END -->
            
        </div>
        <!-- CONTENT END -->

<?php
include($path . 'include/footer.php');
?>

</body>
</html>
