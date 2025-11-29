<?php
$path = '../';
$page_title = 'Blog';
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
                        		<h2 class="text-white">Our Blog</h2>
                            </div>
                        </div>
                        <!-- BREADCRUMB ROW -->                            
                            <div>
                                <ul class="wt-breadcrumb breadcrumb-style-2">
                                    <li><a href="<?php echo $path; ?>index.php">Home</a></li>
                                    <li>Blog</li>
                                </ul>
                            </div>
                        <!-- BREADCRUMB ROW END -->                        
                    </div>
                </div>
            </div>
            <!-- INNER PAGE BANNER END -->
            
            <!-- BLOG LISTING START -->
            <div class="section-full p-t80 p-b50 bg-white">
                <div class="container">
                    
                    <!-- VIEW SWITCHER -->
                    <div class="wt-post-filter-bar m-b30">
                        <div class="row">
                            <div class="col-md-6">
                                <h3>Latest News & Insights</h3>
                            </div>
                            <div class="col-md-6 text-right">
                                <div class="view-switcher btn-group" role="group">
                                    <button type="button" class="btn btn-outline-primary active" data-view="grid">
                                        <i class="fa fa-th"></i> Grid
                                    </button>
                                    <button type="button" class="btn btn-outline-primary" data-view="list">
                                        <i class="fa fa-list"></i> List
                                    </button>
                                    <button type="button" class="btn btn-outline-primary" data-view="masonry">
                                        <i class="fa fa-th-large"></i> Masonry
                                    </button>
                                </div>
                            </div>
                        </div>
                    </div>
                    
                    <!-- BLOG POSTS GRID -->
                    <div class="blog-posts-grid row" id="blog-posts" data-current-view="grid">
                        
                        <!-- POST 1 -->
                        <div class="col-lg-4 col-md-6 m-b30 blog-post-item">
                            <div class="blog-post latest-blog-1 date-style-1">
                                <div class="wt-post-media wt-img-effect zoom-slow">
                                    <a href="<?php echo $path; ?>blog/cleanroom-design-tips/index.php">
                                        <img src="<?php echo $path; ?>images/blog/latest-blog/pic1.jpg" alt="Cleanroom Design Tips">
                                    </a>
                                </div>
                                <div class="wt-post-info">
                                    <div class="post-date"><strong>15 Nov 2024</strong></div>
                                    <div class="wt-post-title">
                                        <h4 class="post-title">
                                            <a href="<?php echo $path; ?>blog/cleanroom-design-tips/index.php">
                                                Essential Cleanroom Design Tips for Modern Facilities
                                            </a>
                                        </h4>
                                    </div>
                                    <div class="wt-post-text">
                                        <p>Discover the key principles of cleanroom design that ensure optimal performance and compliance.</p>
                                    </div>
                                    <div class="wt-post-meta">
                                        <ul class="clearfix">
                                            <li class="post-author">By Admin</li>
                                            <li class="post-comment"><i class="fa fa-comments"></i> 5 Comments</li>
                                        </ul>
                                    </div>
                                </div>
                            </div>
                        </div>
                        
                        <!-- POST 2 -->
                        <div class="col-lg-4 col-md-6 m-b30 blog-post-item">
                            <div class="blog-post latest-blog-1 date-style-1">
                                <div class="wt-post-media wt-img-effect zoom-slow">
                                    <a href="<?php echo $path; ?>blog/sample-post/index.php">
                                        <img src="<?php echo $path; ?>images/blog/latest-blog/pic2.jpg" alt="">
                                    </a>
                                </div>
                                <div class="wt-post-info">
                                    <div class="post-date"><strong>10 Nov 2024</strong></div>
                                    <div class="wt-post-title">
                                        <h4 class="post-title">
                                            <a href="<?php echo $path; ?>blog/sample-post/index.php">
                                                Understanding GMP Standards in Cleanroom Manufacturing
                                            </a>
                                        </h4>
                                    </div>
                                    <div class="wt-post-text">
                                        <p>Learn about Good Manufacturing Practice standards and their importance in the pharmaceutical industry.</p>
                                    </div>
                                    <div class="wt-post-meta">
                                        <ul class="clearfix">
                                            <li class="post-author">By Admin</li>
                                            <li class="post-comment"><i class="fa fa-comments"></i> 8 Comments</li>
                                        </ul>
                                    </div>
                                </div>
                            </div>
                        </div>
                        
                        <!-- POST 3 -->
                        <div class="col-lg-4 col-md-6 m-b30 blog-post-item">
                            <div class="blog-post latest-blog-1 date-style-1">
                                <div class="wt-post-media wt-img-effect zoom-slow">
                                    <a href="<?php echo $path; ?>blog/sample-post/index.php">
                                        <img src="<?php echo $path; ?>images/blog/latest-blog/pic3.jpg" alt="">
                                    </a>
                                </div>
                                <div class="wt-post-info">
                                    <div class="post-date"><strong>05 Nov 2024</strong></div>
                                    <div class="wt-post-title">
                                        <h4 class="post-title">
                                            <a href="<?php echo $path; ?>blog/sample-post/index.php">
                                                Latest Innovations in Cleanroom Technology
                                            </a>
                                        </h4>
                                    </div>
                                    <div class="wt-post-text">
                                        <p>Explore the cutting-edge technologies transforming cleanroom operations and efficiency.</p>
                                    </div>
                                    <div class="wt-post-meta">
                                        <ul class="clearfix">
                                            <li class="post-author">By Admin</li>
                                            <li class="post-comment"><i class="fa fa-comments"></i> 12 Comments</li>
                                        </ul>
                                    </div>
                                </div>
                            </div>
                        </div>
                        
                    </div>
                    
                </div>
            </div>
            <!-- BLOG LISTING END -->
            
        </div>
        <!-- CONTENT END -->

<?php
include($path . 'include/footer.php');
?>

<style>
.view-switcher {
    display: inline-flex;
    gap: 5px;
}
.view-switcher .btn {
    padding: 8px 15px;
}
.blog-posts-grid[data-current-view="list"] .blog-post-item {
    width: 100%;
    max-width: 100%;
    flex: 0 0 100%;
}
</style>

<script>
// View switcher functionality
document.querySelectorAll('.view-switcher button').forEach(btn => {
    btn.addEventListener('click', function() {
        const view = this.getAttribute('data-view');
        const postsContainer = document.getElementById('blog-posts');
        
        // Update active button
        document.querySelectorAll('.view-switcher button').forEach(b => b.classList.remove('active'));
        this.classList.add('active');
        
        // Update view
        postsContainer.setAttribute('data-current-view', view);
        
        // Update grid classes
        if (view === 'list') {
            postsContainer.classList.remove('row');
            postsContainer.classList.add('list-view');
        } else {
            postsContainer.classList.add('row');
            postsContainer.classList.remove('list-view');
        }
    });
});
</script>

</body>
</html>
