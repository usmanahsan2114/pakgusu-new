import os
import re
from bs4 import BeautifulSoup

ROOT_DIR = r"c:\xampp\htdocs\pakgusu-1\intoriza\pakgusu-new\intoriza"

CONTACT_INFO = {
    "phone": "(+92) 321 8073738",
    "email": "info@pakgusu.com",
    "address": "8-Km, Sundar-Raiwand Road, Lahore, Pakistan",
    "copyright_year": "2025"
}

def get_depth(file_path):
    rel_path = os.path.relpath(file_path, ROOT_DIR)
    if rel_path == ".": return 0
    return rel_path.count(os.sep)

def get_prefix(depth):
    if depth == 0: return "./"
    return "../" * depth

def create_header_html(prefix):
    return f'''<!-- HEADER START -->
<header class="site-header header-style-1 nav-wide mobile-sider-drawer-menu">
<div class="sticky-header main-bar-wraper">
<div class="main-bar bg-white">
<div class="container header-center">
<div class="wt-header-left">
<div class="logo-header">
<div class="logo-header-inner logo-header-one">
<a href="{prefix}">
<img alt="" height="49" src="{prefix}images/logo-dark.png" width="171"/>
</a>
</div>
</div>
</div>
<div class="wt-header-center">
<!-- NAV Toggle Button -->
<button class="navbar-toggler collapsed" data-target=".header-nav" data-toggle="collapse" id="mobile-side-drawer" type="button">
<span class="sr-only">Toggle navigation</span>
<span class="icon-bar icon-bar-first"></span>
<span class="icon-bar icon-bar-two"></span>
<span class="icon-bar icon-bar-three"></span>
</button>
<!-- MAIN Vav -->
<div class="header-nav navbar-collapse collapse nav-dark">
<ul class="nav navbar-nav nav-line-animation">
<li>
<a href="{prefix}">Home</a>
</li>
<li>
<a href="{prefix}about/">About Us</a>
</li>
<li>
<a href="javascript:;">Products</a>
<ul class="sub-menu">
<li><a href="{prefix}products/cleanroom-panels/">Cleanroom Panels</a></li>
<li><a href="{prefix}products/cleanroom-windows/">Cleanroom Windows</a></li>
<li><a href="{prefix}products/cleanroom-doors/">Cleanroom Doors</a></li>
<li><a href="{prefix}products/pass-through-chambers/">Pass-Through Chambers</a></li>
<li><a href="{prefix}products/aluminum-profiles/">Aluminum Profiles</a></li>
<li><a href="{prefix}products/cleanroom-led-lights/">Cleanroom LED Lights</a></li>
</ul>
</li>
<li>
<a href="{prefix}services/">Services</a>
</li>
<li>
<a href="javascript:;">Industries</a>
<ul class="sub-menu">
<li><a href="{prefix}industries/pharmaceutical-nutraceutical/">Pharmaceutical &amp; Nutraceutical</a></li>
<li><a href="{prefix}industries/healthcare-hospitals/">Healthcare &amp; Hospitals</a></li>
<li><a href="{prefix}industries/food-beverage/">Food &amp; Beverage</a></li>
<li><a href="{prefix}industries/electronics-manufacturing/">Electronics Manufacturing</a></li>
<li><a href="{prefix}industries/laboratories-rnd/">Laboratories &amp; R&amp;D</a></li>
<li><a href="{prefix}industries/medical-surgical-devices/">Medical &amp; Surgical Devices</a></li>
</ul>
</li>
<li>
<a href="javascript:;">Resources</a>
<ul class="sub-menu">
<li><a href="{prefix}resources/cleanroom-standards-classifications/">Cleanroom Standards &amp; Classifications</a></li>
<li><a href="{prefix}resources/blog/">Blog</a></li>
<li><a href="{prefix}resources/news-events/">News &amp; Events</a></li>
<li><a href="{prefix}resources/faqs/">FAQs</a></li>
</ul>
</li>

<li>
<a href="{prefix}contact/">Contact</a>
</li>
</ul>
</div>
</div>
<div class="wt-header-right">
<div class="site-bg-primary wt-header-right-child">
<!-- ETRA Nav -->
<div class="extra-nav">
<div class="extra-cell">
<a class="site-search-btn" href="#search"><i class="fa fa-search"></i></a>
</div>
</div>
<!-- ETRA Nav -->
<div class="extra-nav">
<div class="extra-cell">
<div class="right-arrow-btn">
<button class="btn-open contact-slide-show text-white notification-animate" type="button"><i class="fa fa-angle-left"></i></button>
</div>
</div>
</div>
</div>
</div>
<!-- Contact Nav -->
<div class="contact-slide-hide">
<div class="contact-nav">
<a class="contact_close" href="javascript:void(0)">×</a>
<div class="contact-nav-form p-a30">
<form action="form-handler.php" class="cons-contact-form" method="post">
<div class="m-b30">
<!-- TITLE START -->
<div class="section-head text-left">
<h4 class="m-b5">Get In Touch</h4>
</div>
<!-- TITLE END -->
<div class="input input-animate">
<label for="name">Name</label>
<input id="name" name="username" required="" type="text"/>
<span class="spin"></span>
</div>
<div class="input input-animate">
<label for="email">Email</label>
<input id="email" name="email" required="" type="email"/>
<span class="spin"></span>
</div>
<div class="input input-animate">
<label for="message">Textarea</label>
<textarea id="message" name="message" required=""></textarea>
<span class="spin"></span>
</div>
<div class="text-right">
<button class="btn-half site-button m-b15" name="submit" type="submit" value="Submit">
<span>Submit</span>
</button>
</div>
</div>
</form>
<div class="contact-info text-black m-b30">
<!-- TITLE START -->
<div class="section-head text-left">
<h4 class="m-b5">Contact Info</h4>
</div>
<!-- TITLE END -->
<div class="wt-icon-box-wraper left p-b40 icon-shake-outer">
<div class="icon-xs"><i class="flaticon-smartphone icon-shake"></i></div>
<div class="icon-content">
<h5 class="m-t0 font-weight-500">Phone number</h5>
<p>{CONTACT_INFO['phone']}</p>
</div>
</div>
<div class="wt-icon-box-wraper left p-b40 icon-shake-outer">
<div class="icon-xs"><i class="flaticon-email icon-shake"></i></div>
<div class="icon-content">
<h5 class="m-t0 font-weight-500">Email address</h5>
<p>{CONTACT_INFO['email']}</p>
</div>
</div>
<div class="wt-icon-box-wraper left icon-shake-outer">
<div class="icon-xs"><i class="flaticon-placeholder icon-shake"></i></div>
<div class="icon-content">
<h5 class="m-t0 font-weight-500">Address info</h5>
<p>{CONTACT_INFO['address']}</p>
</div>
</div>
</div>
</div>
</div>
</div>
<!-- Search popup -->
<div id="search">
<span class="close"></span>
<form action="{prefix}search/" class="radius-xl" id="searchform" method="get" role="search">
<div class="input-group">
<input name="q" placeholder="Type to search" type="search" value=""/>
<span class="input-group-btn"><button class="search-btn" type="button"><i class="fa fa-search"></i></button></span>
</div>
</form>
</div>
</div>
</div>
</header>
<!-- HEADER END -->'''

def create_footer_html(prefix):
    return f'''<!-- FOOTER START -->
<footer class="site-footer footer-large footer-light footer-wide">
<!-- FOOTER BLOCKES START -->
<div class="footer-top overlay-wraper">
<div class="overlay-main"></div>
<div class="container">
<div class="text-center">
<div class="footer-link">
<ul>
<li><a data-hover="About" href="{prefix}about/">About</a></li>
<li><a data-hover="Products" href="{prefix}products/">Products</a></li>
<li><a data-hover="Blog" href="{prefix}resources/blog/">Blog</a></li>
<li><a data-hover="Case Studies" href="{prefix}case-studies/">Case Studies</a></li>
<li><a data-hover="Careers" href="{prefix}careers/">Careers</a></li>
<li><a data-hover="Contact Us" href="{prefix}contact/">Contact Us</a></li>
</ul>
</div>
</div>
<div class="row">
<!-- ABOUT COMPANY -->
<div class="col-lg-4 col-md-4 col-sm-12">
<div class="widget text-center getin-touch">
<h4 class="widget-title">Get In Touch</h4>
<div class="widget-section">
<ul>
<li>{CONTACT_INFO['email']}</li>
<li>{CONTACT_INFO['phone']}</li>
</ul>
</div>
</div>
</div>
<!-- TAGS -->
<div class="col-lg-4 col-md-4 col-sm-12">
<div class="widget text-center widget_address m-b20">
<h4 class="widget-title">Address</h4>
<div class="widget-section">
<ul>
<li>{CONTACT_INFO['address']}</li>
</ul>
</div>
<div class="footer-social-icon">
<ul class="social-icons f-social-link">
<li><a class="fa fa-facebook" href="javascript:void(0);"></a></li>
<li><a class="fa fa-twitter" href="javascript:void(0);"></a></li>
<li><a class="fa fa-linkedin" href="javascript:void(0);"></a></li>
<li><a class="fa fa-instagram" href="javascript:void(0);"></a></li>
</ul>
</div>
</div>
</div>
<!-- USEFUL LINKS -->
<div class="col-lg-4 col-md-4 col-sm-12">
<div class="widget text-center">
<h4 class="widget-title">Legal</h4>
<div class="widget-section">
<ul>
<li><a href="{prefix}about/">Terms of Condition</a></li>
<li><a href="{prefix}about/">Privacy Policy</a></li>
</ul>
</div>
</div>
</div>
<!-- NEWSLETTER -->
</div>
</div>
</div>
<!-- FOOTER COPYRIGHT -->
<div class="footer-bottom overlay-wraper">
<div class="overlay-main"></div>
<div class="container">
<div class="row">
<div class="col-md-6 col-sm-6">
<span class="copyrights-text">© {CONTACT_INFO['copyright_year']} by <a href="{prefix}" rel="noopener" target="_blank">PakGusu</a></span>
</div>
<div class="col-md-6 col-sm-6 text-right">
<span class="copyrights-text">
                            Designed and Developed by <a href="https://www.apexitsolutions.co/" rel="noopener" target="_blank">Apex IT Solutions</a> | 
                            <a href="https://apexmarketings.com/" rel="noopener" target="_blank">Apex Marketings</a>
</span>
</div>
</div>
</div>
</div>
</footer>
<!-- FOOTER END -->'''

def update_file(file_path):
    print(f"Processing: {file_path}")
    depth = get_depth(file_path)
    prefix = get_prefix(depth)
    
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Regex to replace Header
    # Matches <!-- HEADER START --> ... <!-- HEADER END -->
    # We use re.DOTALL to match newlines
    header_pattern = re.compile(r'<!-- HEADER START -->.*?<!-- HEADER END -->', re.DOTALL)
    new_header = create_header_html(prefix)
    
    if header_pattern.search(content):
        content = header_pattern.sub(new_header, content)
        print(f"  ✓ Updated Header")
    else:
        # Fallback: try to find <header ... </header> if markers missing
        print(f"  ! Markers not found, attempting fallback for Header...")
        header_pattern_fallback = re.compile(r'<header.*?</header>', re.DOTALL)
        if header_pattern_fallback.search(content):
             # This is risky because it might miss the contact slide out if it's outside
             # But our new header INCLUDES the contact slide out inside the replacement string
             # So we should try to replace the whole block if possible.
             # Let's stick to markers first. If markers fail, we might need manual intervention or smarter regex.
             pass

    # Regex to replace Footer
    footer_pattern = re.compile(r'<!-- FOOTER START -->.*?<!-- FOOTER END -->', re.DOTALL)
    new_footer = create_footer_html(prefix)
    
    if footer_pattern.search(content):
        content = footer_pattern.sub(new_footer, content)
        print(f"  ✓ Updated Footer")
    
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

def main():
    print("=== Updating Global Header & Footer ===\n")
    
    for root, dirs, files in os.walk(ROOT_DIR):
        if "extra" in dirs:
            dirs.remove("extra")
            
        for file in files:
            if file.lower().endswith(".html"):
                file_path = os.path.join(root, file)
                update_file(file_path)
    
    print("\n=== Complete! ===")

if __name__ == "__main__":
    main()
