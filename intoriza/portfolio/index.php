<?php
$path = '../';
$page_title = 'Portfolio';
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
                        		<h2 class="text-white">Our Portfolio</h2>
                            </div>
                        </div>
                        <!-- BREADCRUMB ROW -->                            
                            <div>
                                <ul class="wt-breadcrumb breadcrumb-style-2">
                                    <li><a href="<?php echo $path; ?>index.php">Home</a></li>
                                    <li>Portfolio</li>
                                </ul>
                            </div>
                        <!-- BREADCRUMB ROW END -->                        
                    </div>
                </div>
            </div>
            <!-- INNER PAGE BANNER END -->
            
            <!-- PORTFOLIO LISTING START -->
            <div class="section-full p-t80 p-b50 bg-white">
                <div class="container">
                    
                    <!-- VIEW SWITCHER -->
                    <div class="wt-post-filter-bar m-b30">
                        <div class="row">
                            <div class="col-md-6">
                                <h3>Our Cleanroom Projects</h3>
                            </div>
                            <div class="col-md-6 text-right">
                                <div class="view-switcher btn-group" role="group">
                                    <button type="button" class="btn btn-outline-primary active" data-view="grid">
                                        <i class="fa fa-th"></i> Grid
                                    </button>
                                    <button type="button" class="btn btn-outline-primary" data-view="masonry">
                                        <i class="fa fa-th-large"></i> Masonry
                                    </button>
                                </div>
                            </div>
                        </div>
                    </div>
                    
                    <!-- PORTFOLIO GRID -->
                    <div class="portfolio-wrap mfp-gallery work-grid row clearfix" id="portfolio-items" data-current-view="grid">
                        
                        <!-- PROJECT 1 -->
                        <div class="masonry-item col-lg-4 col-md-6 col-sm-6 m-b30">
                            <div class="wt-box work-hover-content">
                                <div class="wt-thum-bx img-center-icon">
                                    <a href="<?php echo $path; ?>portfolio/pharmaceutical-facility/index.php">
                                        <img src="<?php echo $path; ?>images/our-work/s-1.jpg" alt="Pharmaceutical Facility">
                                    </a>
                                </div>
                                <div class="wt-info p-t20">
                                    <h4 class="wt-tilte m-b10 m-t0">
                                        <a href="<?php echo $path; ?>portfolio/pharmaceutical-facility/index.php">Pharmaceutical Cleanroom</a>
                                    </h4>
                                    <p class="m-b0">ISO Class 5 Facility - Pakistan</p>
                                </div>
                           </div>
                        </div>
                        
                        <!-- PROJECT 2 -->
                        <div class="masonry-item col-lg-4 col-md-6 col-sm-6 m-b30">
                            <div class="wt-box work-hover-content">
                                <div class="wt-thum-bx img-center-icon">
                                    <a href="<?php echo $path; ?>portfolio/pharmaceutical-facility/index.php">
                                        <img src="<?php echo $path; ?>images/our-work/s-2.jpg" alt="">
                                    </a>
                                </div>
                                <div class="wt-info p-t20">
                                    <h4 class="wt-tilte m-b10 m-t0">
                                        <a href="<?php echo $path; ?>portfolio/pharmaceutical-facility/index.php">Hospital Operating Room</a>
                                    </h4>
                                    <p class="m-b0">Modern Healthcare Facility</p>
                                </div>
                            </div>
                        </div>
                        
                        <!-- PROJECT 3 -->
                        <div class="masonry-item col-lg-4 col-md-6 col-sm-6 m-b30">
                            <div class="wt-box work-hover-content">
                                <div class="wt-thum-bx img-center-icon">
                                    <a href="<?php echo $path; ?>portfolio/pharmaceutical-facility/index.php">
                                        <img src="<?php echo $path; ?>images/our-work/s-3.jpg" alt="">
                                    </a>
                                </div>
                                <div class="wt-info p-t20">
                                    <h4 class="wt-tilte m-b10 m-t0">
                                        <a href="<?php echo $path; ?>portfolio/pharmaceutical-facility/index.php">Electronics Manufacturing</a>
                                    </h4>
                                    <p class="m-b0">Class 1000 Cleanroom</p>
                                </div>
                            </div>
                        </div>
                        
                    </div>
                    
                </div>
            </div>
            <!-- PORTFOLIO LISTING END -->
            
        </div>
        <!-- CONTENT END -->

<?php
include($path . 'include/footer.php');
?>

<script>
// View switcher functionality
document.querySelectorAll('.view-switcher button').forEach(btn => {
    btn.addEventListener('click', function() {
        const view = this.getAttribute('data-view');
        const portfolioContainer = document.getElementById('portfolio-items');
        
        // Update active button
        document.querySelectorAll('.view-switcher button').forEach(b => b.classList.remove('active'));
        this.classList.add('active');
        
        // Update view
        portfolioContainer.setAttribute('data-current-view', view);
    });
});
</script>

</body>
</html>
