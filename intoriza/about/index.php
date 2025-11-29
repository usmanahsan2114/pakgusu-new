<?php
$path = '../';
$page_title = 'About Page 1';
include($path . 'include/head.php');
include($path . 'include/header.php');
?>

        
        <!-- CONTENT START -->
        <div class="page-content">
        
            <!-- INNER PAGE BANNER -->
            <div class="wt-bnr-inr overlay-wraper bg-center"  style="background-image:url(<?php echo $path; ?>images/banner/1.jpg);">
            	<div class="overlay-main bg-black opacity-07"></div>
                <div class="container">
                    <div class="wt-bnr-inr-entry">
                    	<div class="banner-title-outer">
                        	<div class="banner-title-name">
                        		<h2 class="text-white">About Us</h2>
                            </div>
                        </div>
                        <!-- BREADCRUMB ROW -->                            
                        
                            <div>
                                <ul class="wt-breadcrumb breadcrumb-style-2">
                                    <li><a href="<?php echo $path; ?>index.php">Home</a></li>
                                    <li>About Us</li>
                                </ul>
                            </div>
                        
                        <!-- BREADCRUMB ROW END -->                        
                    </div>
                </div>
            </div>
            <!-- INNER PAGE BANNER END -->
             
            <!-- ABOUT OVERVIEW SECTION START -->
            <div class="section-full p-t80 p-b50 bg-white">
                <div class="container">
                    <div class="section-content">
                    	<div class="row">
                        	<div class="col-lg-6 col-md-12 m-b30">
                            	<div class="wt-media">
                                    <img src="<?php echo $path; ?>images/gallery/pic1.jpg" alt="" class="img-responsive">
                                </div>
                            </div>
                    		<div class="col-lg-6 col-md-12 m-b30">
                                <div class="section-head">
                                	<div class="wt-separator-outer separator-left">
                                		<div class="wt-separator">
                                            <span class="site-text-primary text-uppercase sep-line-one ">Who We Are</span>
                                        </div>
                                    </div>
                                    <h2>Leading Cleanroom Solutions Provider</h2>
                                </div>
                                <p>PakGusu is a premier provider of modular cleanroom systems, dedicated to delivering high-quality, compliant, and innovative solutions for various industries. With a strong partnership with GUSU China, we bring world-class technology and expertise to every project.</p>
                                <p>Our mission is to ensure the highest standards of hygiene and contamination control, supporting the pharmaceutical, medical, and electronic sectors in achieving their production goals.</p>
                            </div>                            
                        </div>
                    </div>
                </div>
            </div>   
            <!-- ABOUT OVERVIEW SECTION END --> 

            <!-- SUBPAGE TEASERS SECTION START -->
            <div class="section-full p-t80 p-b50 bg-gray">
                <div class="container">
                    <div class="section-head text-center">
                        <div class="wt-separator-outer separator-center">
                            <div class="wt-separator">
                                <span class="site-text-primary text-uppercase sep-line-one ">Explore More</span>
                            </div>
                        </div>
                        <h2>Our Company Structure</h2>
                    </div>
                    <div class="section-content">
                    	<div class="row justify-content-center">
                            <!-- TEASER 1: Pak Gusu -->
                            <div class="col-lg-4 col-md-6 m-b30">
                            	<div class="hover-box-effect v-icon-effect">
                                    <div class="wt-icon-box-wraper center p-lr30 p-b50 p-t50 bg-white">
                                        <div class="icon-lg site-text-primary m-b20">
                                            <span class="icon-cell site-text-primary"><i class="v-icon flaticon-building"></i></span>
                                        </div>
                                        <div class="icon-content text-black">
                                            <h4 class="wt-tilte m-b25">About Pak Gusu</h4>
                                            <p>Learn about our history, mission, and our state-of-the-art manufacturing facilities in Lahore.</p>
                                            <a href="<?php echo $path; ?>about/pak-gusu/index.php" class="site-button-link" data-hover="Read More">Read More</a>
                                        </div>
                                    </div>
                                </div>
                            </div>                          
                            <!-- TEASER 2: GUSU China -->
                            <div class="col-lg-4 col-md-6 m-b30">
                                <div class="hover-box-effect v-icon-effect">
                                    <div class="wt-icon-box-wraper center p-lr30 p-b50 p-t50 bg-white">
                                        <div class="icon-lg site-text-primary m-b20">
                                            <span class="icon-cell site-text-primary"><i class="v-icon flaticon-factory"></i></span>
                                        </div>
                                        <div class="icon-content text-black">
                                            <h4 class="wt-tilte m-b25">About GUSU China</h4>
                                            <p>Discover our global partner, GUSU China, and their expertise in cleanroom technology.</p>
                                            <a href="<?php echo $path; ?>about/gusu-china/index.php" class="site-button-link" data-hover="Read More">Read More</a>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <!-- TEASER 3: Cleanroom Standards -->
                            <div class="col-lg-4 col-md-6 m-b30">
                            	<div class="hover-box-effect v-icon-effect">
                                    <div class="wt-icon-box-wraper center p-lr30 p-b50 p-t50 bg-white">
                                        <div class="icon-lg site-text-primary m-b20">
                                            <span class="icon-cell site-text-primary"><i class="v-icon flaticon-shield"></i></span>
                                        </div>
                                        <div class="icon-content text-black">
                                            <h4 class="wt-tilte m-b25">Cleanroom Standards</h4>
                                            <p>Understand the classification standards and compliance levels we adhere to.</p>
                                            <a href="<?php echo $path; ?>about/cleanroom-standards/index.php" class="site-button-link" data-hover="Read More">Read More</a>
                                        </div>
                                    </div>
                                 </div>
                            </div>                          
                        </div>                                
                    </div>
                </div>  
            </div>   
            <!-- SUBPAGE TEASERS SECTION END --> 
            
        </div>
        <!-- CONTENT END -->
        
        
<?php
include($path . 'include/footer.php');
?>

</body>
</html>
