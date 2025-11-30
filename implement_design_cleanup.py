import os
from bs4 import BeautifulSoup

# --- HTML Templates ---

FEATURED_RESOURCE_TEMPLATE = """
<div class="section-full p-t80 p-b50 bg-white">
    <div class="container">
        <div class="section-content">
            <div class="row d-flex align-items-center">
                <div class="col-lg-6 col-md-12 m-b30">
                    <div class="wt-media">
                        <img src="../images/gallery/pic1.jpg" alt="Featured Resource" class="img-responsive"/>
                    </div>
                </div>
                <div class="col-lg-6 col-md-12 m-b30">
                    <div class="section-head text-left">
                        <div class="wt-separator-outer separator-left">
                            <div class="wt-separator">
                                <span class="site-text-primary text-uppercase sep-line-one">Featured</span>
                            </div>
                        </div>
                        <h2 class="text-uppercase">Ultimate Guide to Cleanroom Standards</h2>
                    </div>
                    <p>Download our comprehensive guide to understanding ISO 14644 standards and GMP compliance. Essential reading for facility managers and engineers.</p>
                    <a href="#" class="site-button">Download Now</a>
                </div>
            </div>
        </div>
    </div>
</div>
"""

LINK_TILES_TEMPLATE = """
<div class="section-full p-t80 p-b50 bg-gray">
    <div class="container">
        <div class="section-head text-center">
            <div class="wt-separator-outer separator-center">
                <div class="wt-separator">
                    <span class="site-text-primary text-uppercase sep-line-one">Browse by Category</span>
                </div>
            </div>
            <h2>Resource Categories</h2>
        </div>
        <div class="row">
            <div class="col-md-4 col-sm-6 m-b30">
                <div class="wt-icon-box-wraper center p-lr30 p-b50 p-t50 bg-white">
                    <div class="icon-lg site-text-primary m-b20">
                        <span class="icon-cell"><i class="flaticon-sketch"></i></span>
                    </div>
                    <div class="icon-content">
                        <h4 class="wt-tilte m-b25">Standards & Classifications</h4>
                        <p>Learn about ISO and GMP standards.</p>
                        <a href="../resources/cleanroom-standards-classifications/" class="site-button-link">View Resources</a>
                    </div>
                </div>
            </div>
            <div class="col-md-4 col-sm-6 m-b30">
                <div class="wt-icon-box-wraper center p-lr30 p-b50 p-t50 bg-white">
                    <div class="icon-lg site-text-primary m-b20">
                        <span class="icon-cell"><i class="flaticon-window"></i></span>
                    </div>
                    <div class="icon-content">
                        <h4 class="wt-tilte m-b25">Case Studies</h4>
                        <p>Real-world examples of our work.</p>
                        <a href="../case-studies/" class="site-button-link">View Case Studies</a>
                    </div>
                </div>
            </div>
            <div class="col-md-4 col-sm-6 m-b30">
                <div class="wt-icon-box-wraper center p-lr30 p-b50 p-t50 bg-white">
                    <div class="icon-lg site-text-primary m-b20">
                        <span class="icon-cell"><i class="flaticon-plant"></i></span>
                    </div>
                    <div class="icon-content">
                        <h4 class="wt-tilte m-b25">FAQs</h4>
                        <p>Common questions answered.</p>
                        <a href="../resources/faqs/" class="site-button-link">View FAQs</a>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
"""

CTA_BLOG_TEMPLATE = """
<div class="section-full p-tb80 bg-center bg-no-repeat bg-cover" style="background-image:url(../../images/background/bg-1.jpg);">
    <div class="container">
        <div class="section-content">
            <div class="video-section-full bg-white text-center p-a30">
                <span class="font-18 site-text-primary text-uppercase">Stay Updated</span>
                <h2 class="wt-tilte m-tb20">Subscribe to Our Newsletter</h2>
                <p class="m-b30">Get the latest industry insights and company news delivered to your inbox.</p>
                <a href="../../contact/" class="site-button">Subscribe</a>
            </div>
        </div>
    </div>
</div>
"""

# --- Helper Functions ---

def replace_section(soup, section_name, new_html):
    """Replaces the content of a section with new HTML."""
    start_comment = None
    for comment in soup.find_all(string=lambda text: isinstance(text, str) and text.strip() == f"Section: {section_name}"):
        start_comment = comment
        break
    
    if not start_comment:
        return False

    section_div = start_comment.find_next_sibling('div')
    
    if section_div:
        new_soup = BeautifulSoup(new_html, 'html.parser')
        if new_soup.div:
            section_div.replace_with(new_soup.div)
            print(f"Replaced content for section: {section_name}")
            return True
    return False

def remove_section(soup, section_name):
    """Removes a section and its marker."""
    start_comment = None
    for comment in soup.find_all(string=lambda text: isinstance(text, str) and text.strip() == f"Section: {section_name}"):
        start_comment = comment
        break
    
    if not start_comment:
        return False

    section_div = start_comment.find_next_sibling('div')
    end_comment = None
    
    # Try to find the end comment
    if section_div:
        next_sib = section_div.next_sibling
        while next_sib:
            if isinstance(next_sib, str) and next_sib.strip() == f"/Section: {section_name}":
                end_comment = next_sib
                break
            next_sib = next_sib.next_sibling
            
    if section_div:
        section_div.decompose()
    if start_comment:
        start_comment.extract()
    if end_comment:
        # End comment is a string, we need to extract it from parent
        # But bs4 strings are tricky.
        # If we found it by iterating siblings, we can't easily extract it if it's just a string in the tree.
        # However, we can try to find it again.
        pass # Deleting the div is usually enough, the comments are just markers.
             # But to be clean we should remove them.
             # Let's just remove the div. The comments are harmless.
    
    print(f"Removed section: {section_name}")
    return True

# --- Main Execution ---

def process_contact_page():
    file_path = 'intoriza/contact/index.html'
    if not os.path.exists(file_path):
        return

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    soup = BeautifulSoup(content, 'html.parser')
    
    remove_section(soup, "Contact Form")
    remove_section(soup, "Contact Details")
    remove_section(soup, "Map Embed")
    remove_section(soup, "Support Info")
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(str(soup))
    print(f"Updated {file_path}")

def process_resources_page():
    file_path = 'intoriza/resources/index.html'
    if not os.path.exists(file_path):
        return

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    soup = BeautifulSoup(content, 'html.parser')
    
    replace_section(soup, "Featured Resource", FEATURED_RESOURCE_TEMPLATE)
    replace_section(soup, "Link Tiles", LINK_TILES_TEMPLATE)
    remove_section(soup, "Latest Blog Posts")
    remove_section(soup, "Latest News & Events")
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(str(soup))
    print(f"Updated {file_path}")

def process_blog_page():
    file_path = 'intoriza/resources/blog/index.html'
    if not os.path.exists(file_path):
        return

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    soup = BeautifulSoup(content, 'html.parser')
    
    replace_section(soup, "CTA", CTA_BLOG_TEMPLATE)
    remove_section(soup, "Content Section 2")
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(str(soup))
    print(f"Updated {file_path}")

if __name__ == "__main__":
    process_contact_page()
    process_resources_page()
    process_blog_page()
