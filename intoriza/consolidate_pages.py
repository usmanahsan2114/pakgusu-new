import os
import shutil
from pathlib import Path

base_dir = r'c:\xampp\htdocs\pakgusu-new\intoriza'

# Blog: Consolidate grid content into main index
blog_index_content = '''<?php
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
'''

# Write blog index
with open(os.path.join(base_dir, 'blog', 'index.php'), 'w', encoding='utf-8') as f:
    f.write(blog_index_content)
print("Created: blog/index.php")

# Portfolio index
portfolio_index_content = '''<?php
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
'''

# Write portfolio index
with open(os.path.join(base_dir, 'portfolio', 'index.php'), 'w', encoding='utf-8') as f:
    f.write(portfolio_index_content)
print("Created: portfolio/index.php")

# Create sample blog post
os.makedirs(os.path.join(base_dir, 'blog', 'cleanroom-design-tips'), exist_ok=True)

sample_blog_content = '''<?php
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
'''

with open(os.path.join(base_dir, 'blog', 'cleanroom-design-tips', 'index.php'), 'w', encoding='utf-8') as f:
    f.write(sample_blog_content)
print("Created: blog/cleanroom-design-tips/index.php")

# Create sample portfolio project
os.makedirs(os.path.join(base_dir, 'portfolio', 'pharmaceutical-facility'), exist_ok=True)

sample_portfolio_content = '''<?php
$path = '../../';
$page_title = 'Pharmaceutical Cleanroom Facility';
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
                        		<h2 class="text-white">Project Details</h2>
                            </div>
                        </div>
                        <!-- BREADCRUMB ROW -->                            
                            <div>
                                <ul class="wt-breadcrumb breadcrumb-style-2">
                                    <li><a href="<?php echo $path; ?>index.php">Home</a></li>
                                    <li><a href="<?php echo $path; ?>portfolio/index.php">Portfolio</a></li>
                                    <li>Pharmaceutical Facility</li>
                                </ul>
                            </div>
                        <!-- BREADCRUMB ROW END -->                        
                    </div>
                </div>
            </div>
            <!-- INNER PAGE BANNER END -->
            
            <!-- PROJECT DETAILS START -->
            <div class="section-full p-t80 p-b50 bg-white">
                <div class="container">
                    <div class="row">
                        <div class="col-lg-8 col-md-12">
                            <div class="project-detail-outer">
                                <div class="project-detail-pic m-b30">
                                    <img src="<?php echo $path; ?>images/our-work/s-1.jpg" alt="">
                                </div>
                                <div class="project-detail-containt">
                                    <h3>Pharmaceutical Cleanroom Facility</h3>
                                    <p>A state-of-the-art ISO Class 5 cleanroom facility designed and installed for a leading pharmaceutical manufacturer in Pakistan.</p>
                                    
                                    <h4>Project Overview</h4>
                                    <p>This project involved the complete design, construction, and validation of a 2,000 sq ft cleanroom facility meeting GMP standards.</p>
                                    
                                    <h4>Key Features</h4>
                                    <ul class="list-checked">
                                        <li>ISO Class 5 clean manufacturing area</li>
                                        <li>Advanced HVAC system with HEPA filtration</li>
                                        <li>Modular cleanroom panels for easy expansion</li>
                                        <li>Validated to international GMP standards</li>
                                        <li>Energy-efficient design</li>
                                    </ul>
                                </div>
                            </div>
                        </div>
                        
                        <div class="col-lg-4 col-md-12">
                            <aside class="side-bar">
                                <div class="widget bg-white">
                                    <h4 class="widget-title">Project Info</h4>
                                    <ul class="list-2">
                                        <li><strong>Client:</strong> Pharmaceutical Co.</li>
                                        <li><strong>Location:</strong> Lahore, Pakistan</li>
                                        <li><strong>Year:</strong> 2024</li>
                                        <li><strong>Classification:</strong> ISO Class 5</li>
                                        <li><strong>Size:</strong> 2,000 sq ft</li>
                                    </ul>
                                </div>
                                
                                <div class="widget bg-white">
                                    <h4 class="widget-title">Related Projects</h4>
                                    <ul class="list-2">
                                        <li><a href="<?php echo $path; ?>portfolio/index.php">View All Projects</a></li>
                                    </ul>
                                </div>
                            </aside>
                        </div>
                    </div>
                </div>
            </div>
            <!-- PROJECT DETAILS END -->
            
        </div>
        <!-- CONTENT END -->

<?php
include($path . 'include/footer.php');
?>

</body>
</html>
'''

with open(os.path.join(base_dir, 'portfolio', 'pharmaceutical-facility', 'index.php'), 'w', encoding='utf-8') as f:
    f.write(sample_portfolio_content)
print("Created: portfolio/pharmaceutical-facility/index.php")

# Remove old subdirectories (grid, listing, masonry, etc)
old_dirs_to_remove = [
    os.path.join(base_dir, 'blog', 'grid'),
    os.path.join(base_dir, 'blog', 'listing'),
    os.path.join(base_dir, 'blog', 'masonry'),
    os.path.join(base_dir, 'blog', 'post-detail'),
    os.path.join(base_dir, 'blog', 'post-gallery'),
    os.path.join(base_dir, 'portfolio', 'grid'),
    os.path.join(base_dir, 'portfolio', 'masonry'),
    os.path.join(base_dir, 'portfolio', 'detail'),
]

for old_dir in old_dirs_to_remove:
    if os.path.exists(old_dir):
        shutil.rmtree(old_dir)
        print(f"Removed: {old_dir}")

print("\n✅ Consolidation complete!")
print("- Created blog/index.php with view switcher")
print("- Created portfolio/index.php with view switcher")
print("- Created sample blog post")
print("- Created sample portfolio project")
print("- Removed old view-specific subdirectories")
