<?php
$path = '../';
$page_title = 'Work grid';
include($path . 'include/head.php');
include($path . 'include/header.php');
?>

        
        <!-- CONTENT START -->
        <div class="page-content">
            <!-- INNER PAGE BANNER -->
            <div class="wt-bnr-inr overlay-wraper bg-center"  style="background-image:url(<?php echo $path; ?>images/banner/2.jpg);">
            	<div class="overlay-main bg-black opacity-07"></div>
                <div class="container">
                    <div class="wt-bnr-inr-entry">
                    	<div class="banner-title-outer">
                        	<div class="banner-title-name">
                        		<h2 class="text-white">Work Grid</h2>
                            </div>
                        </div>
                        <!-- BREADCRUMB ROW -->                            
                        
                            <div>
                                <ul class="wt-breadcrumb breadcrumb-style-2">
                                    <li><a href="<?php echo $path; ?>index.php">Home</a></li>
                                    <li>Work Grid</li>
                                </ul>
                            </div>
                        
                        <!-- BREADCRUMB ROW END -->                        
                    </div>
                </div>
            </div>
            <!-- INNER PAGE BANNER END -->
            
			<!-- SECTION CONTENT START -->
            <div class="section-full small-device  p-t80 p-b50 bg-gray">
            	<div class="container">
                    <!-- PAGINATION START -->
                    <div class="filter-wrap p-b30 text-center">
                        <ul class="filter-navigation masonry-filter text-uppercase">
                            <li class="active"><a data-filter="*" data-hover="All" href="#">All</a></li>
                            <li><a data-filter=".cat-1" data-hover="Bathroom" href="javascript:;">Bathroom</a></li>
                            <li><a data-filter=".cat-4" data-hover="Spa" href="javascript:;">Spa</a></li>
                            <li><a data-filter=".cat-2" data-hover="Furniture" href="javascript:;">Furniture</a></li>
                            <li><a data-filter=".cat-3" data-hover="Decor" href="javascript:;">Decor</a></li>
                            <li><a data-filter=".cat-5" data-hover="Building" href="javascript:;">Building</a></li>
                            <li><a data-filter=".cat-6" data-hover="Living" href="javascript:;">Living </a></li>
                        </ul>
                    </div>
                    <!-- PAGINATION END -->
                    <!-- GALLERY CONTENT START -->
                     <div class="portfolio-wrap mfp-gallery work-grid row clearfix">
                        <!-- COLUMNS 1 -->
                        <div class="masonry-item cat-1 col-lg-4 col-md-6 m-b30">
                            <div class="wt-box">
                                <div class="work-hover-grid">
                                	<img src="<?php echo $path; ?>images/gallery/pic1.jpg" alt=""/>
                                      <div class="work-hover-discription">
                                          <h4>Rooms & Halls</h4>
                                          <h5>North House</h5>
                                      </div>
                                  <a href="<?php echo $path; ?>extra/project-detail.php"></a>
                                </div>                            
                            </div>
                        </div>
                        <!-- COLUMNS 2 -->
                        <div class="masonry-item cat-2 col-lg-4 col-md-6 m-b30">
                            <div class="wt-box">
                                <div class="work-hover-grid">
                                	<img src="<?php echo $path; ?>images/gallery/pic2.jpg" alt=""/>
                                      <div class="work-hover-discription">
                                          <h4>To-Do Dashboard</h4>
                                          <h5>Aqaba, Jordan</h5>
                                      </div>
                                  <a href="<?php echo $path; ?>extra/project-detail.php"></a>
                                </div>                            
                            </div>                            
                        </div>
                        <!-- COLUMNS 3 -->
                        <div class="masonry-item cat-3 col-lg-4 col-md-6 m-b30">
                            <div class="wt-box">
                                <div class="work-hover-grid">
                                	<img src="<?php echo $path; ?>images/gallery/pic3.jpg" alt=""/>
                                      <div class="work-hover-discription">
                                          <h4>WhereTO App</h4>
                                          <h5>Perth, Australia </h5>
                                      </div>
                                  <a href="<?php echo $path; ?>extra/project-detail.php"></a>
                                </div>                            
                            </div>                            
                        </div>
                        <!-- COLUMNS 4 -->
                        <div class="masonry-item cat-4 col-lg-4 col-md-6 m-b30">
                            <div class="wt-box">
                                <div class="work-hover-grid">
                                	<img src="<?php echo $path; ?>images/gallery/pic4.jpg" alt=""/>
                                      <div class="work-hover-discription">
                                          <h4>Rooms & Halls</h4>
                                          <h5>Aqaba, Jordan</h5>
                                      </div>
                                  <a href="<?php echo $path; ?>extra/project-detail.php"></a>
                                </div>                            
                            </div>                            
                        </div>
                        <!-- COLUMNS 5 -->
                        <div class="masonry-item cat-5 col-lg-4 col-md-6 m-b30">
                            <div class="wt-box">
                                <div class="work-hover-grid">
                                	<img src="<?php echo $path; ?>images/gallery/pic5.jpg" alt=""/>
                                      <div class="work-hover-discription">
                                          <h4>Events and More</h4>
                                          <h5>Sultanate of Oman</h5>
                                      </div>
                                  <a href="<?php echo $path; ?>extra/project-detail.php"></a>
                                </div>                            
                            </div>                            
                        </div>
                        <!-- COLUMNS 6 -->
                        <div class="masonry-item cat-6 col-lg-4 col-md-6 m-b30">
                            <div class="wt-box">
                                <div class="work-hover-grid">
                                	<img src="<?php echo $path; ?>images/gallery/pic6.jpg" alt=""/>
                                      <div class="work-hover-discription">
                                          <h4>Remind~Me More</h4>
                                          <h5>Ultanate of Oman</h5>
                                      </div>
                                  <a href="<?php echo $path; ?>extra/project-detail.php"></a>
                                </div>                            
                            </div>                            
                        </div>
                        <!-- COLUMNS 7 -->
                        <div class="masonry-item cat-1 col-lg-4 col-md-6 m-b30">
                            <div class="wt-box">
                                <div class="work-hover-grid">
                                	<img src="<?php echo $path; ?>images/gallery/pic7.jpg" alt=""/>
                                      <div class="work-hover-discription">
                                          <h4>Workout Buddy</h4>
                                          <h5>Aqaba, Jordan</h5>
                                      </div>
                                  <a href="<?php echo $path; ?>extra/project-detail.php"></a>
                                </div>                            
                            </div>                            
                        </div>
                        <!-- COLUMNS 8 -->
                        <div class="masonry-item cat-2 col-lg-4 col-md-6 m-b30">
                            <div class="wt-box">
                                <div class="work-hover-grid">
                                	<img src="<?php echo $path; ?>images/gallery/pic8.jpg" alt=""/>
                                      <div class="work-hover-discription">
                                          <h4>Speed Detector</h4>
                                          <h5>Sultanate of Oman</h5>
                                      </div>
                                  <a href="<?php echo $path; ?>extra/project-detail.php"></a>
                                </div>                            
                            </div>                            
                        </div>
                        <!-- COLUMNS 9 -->
                        <div class="masonry-item cat-3 col-lg-4 col-md-6 m-b30">
                            <div class="wt-box">
                                <div class="work-hover-grid">
                                	<img src="<?php echo $path; ?>images/gallery/pic1.jpg" alt=""/>
                                      <div class="work-hover-discription">
                                          <h4>Generic Apps</h4>
                                          <h5>Aqaba, Jordan</h5>
                                      </div>
                                  <a href="<?php echo $path; ?>extra/project-detail.php"></a>
                                </div>                            
                            </div>                            
                        </div>                                   
                     </div>
                    <!-- GALLERY CONTENT END -->                    
            	</div>
            </div>
            <!-- SECTION CONTENT END  -->

        </div>
        <!-- CONTENT END -->
        
        
<?php
include($path . 'include/footer.php');
?>

</body>
</html>
