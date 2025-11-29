<?php
$path = '../../';
$page_title = 'Essential Cleanroom Design Tips';
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
                        		<h2 class="text-white">Blog Post</h2>
                            </div>
                        </div>
                        <!-- BREADCRUMB ROW -->                            
                            <div>
                                <ul class="wt-breadcrumb breadcrumb-style-2">
                                    <li><a href="<?php echo $path; ?>index.php">Home</a></li>
                                    <li><a href="<?php echo $path; ?>blog/index.php">Blog</a></li>
                                    <li>Cleanroom Design Tips</li>
                                </ul>
                            </div>
                        <!-- BREADCRUMB ROW END -->                        
                    </div>
                </div>
            </div>
            <!-- INNER PAGE BANNER END -->
            
            <!-- BLOG POST START -->
            <div class="section-full p-t80 p-b50 bg-white">
                <div class="container">
                    <div class="row">
                        <div class="col-lg-8 col-md-12">
                            <div class="blog-post-single">
                                <div class="wt-post-media">
                                    <img src="<?php echo $path; ?>images/blog/latest-blog/pic1.jpg" alt="">
                                </div>
                                <div class="wt-post-info">
                                    <div class="post-date"><strong>15 Nov 2024</strong></div>
                                    <div class="wt-post-title">
                                        <h2>Essential Cleanroom Design Tips for Modern Facilities</h2>
                                    </div>
                                    <div class="wt-post-text">
                                        <p>Designing a cleanroom requires careful planning and attention to detail. Here are essential tips to ensure your cleanroom meets the highest standards...</p>
                                        
                                        <h3>1. Understand ISO Classifications</h3>
                                        <p>Before designing your cleanroom, determine the ISO classification required for your specific application.</p>
                                        
                                        <h3>2. Choose Appropriate Materials</h3>
                                        <p>Select materials that are non-porous, easy to clean, and resistant to chemicals.</p>
                                        
                                        <h3>3. Plan Air Flow Carefully</h3>
                                        <p>Proper air flow design is crucial for maintaining cleanroom standards.</p>
                                    </div>
                                </div>
                            </div>
                        </div>
                        
                        <div class="col-lg-4 col-md-12">
                            <aside class="side-bar">
                                <div class="widget bg-white">
                                    <h4 class="widget-title">Recent Posts</h4>
                                    <ul class="list-2">
                                        <li><a href="<?php echo $path; ?>blog/index.php">Back to Blog</a></li>
                                    </ul>
                                </div>
                            </aside>
                        </div>
                    </div>
                </div>
            </div>
            <!-- BLOG POST END -->
            
        </div>
        <!-- CONTENT END -->

<?php
include($path . 'include/footer.php');
?>

</body>
</html>
