import os
import shutil
from bs4 import BeautifulSoup

# Paths
ROOT_DIR = r"c:\xampp\htdocs\pakgusu-1\intoriza\pakgusu-new\intoriza"
INDEX_FILE = os.path.join(ROOT_DIR, "index.html")

# Asset directories
ASSET_DIRS = ["css", "js", "images", "plugins", "fonts", "media", "phpmailer"]

def create_navigation_html(prefix):
    """Create the correct navigation menu HTML with proper relative paths"""
    return f'''<ul class="nav navbar-nav nav-line-animation">
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
                                            <li><a href="{prefix}industries/pharmaceutical-nutraceutical/">Pharmaceutical & Nutraceutical</a></li>
                                            <li><a href="{prefix}industries/healthcare-hospitals/">Healthcare & Hospitals</a></li>
                                            <li><a href="{prefix}industries/food-beverage/">Food & Beverage</a></li>
                                            <li><a href="{prefix}industries/electronics-manufacturing/">Electronics Manufacturing</a></li>
                                            <li><a href="{prefix}industries/laboratories-rnd/">Laboratories & R&D</a></li>
                                            <li><a href="{prefix}industries/medical-surgical-devices/">Medical & Surgical Devices</a></li>
                                        </ul>
                                    </li>
                                    <li>
                                        <a href="javascript:;">Resources</a>
                                        <ul class="sub-menu">
                                            <li><a href="{prefix}resources/cleanroom-standards-classifications/">Cleanroom Standards & Classifications</a></li>
                                            <li><a href="{prefix}resources/blog/">Blog</a></li>
                                            <li><a href="{prefix}resources/news-events/">News & Events</a></li>
                                            <li><a href="{prefix}resources/faqs/">FAQs</a></li>
                                        </ul>
                                    </li>
                                    <li>
                                        <a href="{prefix}case-studies/">Case Studies</a>
                                    </li>
                                    <li>
                                        <a href="{prefix}careers/">Careers</a>
                                    </li>
                                    <li>
                                        <a href="{prefix}contact/">Contact</a>
                                    </li>
                                </ul>'''

def create_footer_links_html(prefix):
    """Create the correct footer links HTML with proper relative paths"""
    return f'''<ul>
                                <li><a href="{prefix}about/" data-hover="About">About</a></li>
                                <li><a href="{prefix}products/" data-hover="Products">Products</a></li>
                                <li><a href="{prefix}resources/blog/" data-hover="Blog">Blog</a></li>
                                <li><a href="{prefix}case-studies/" data-hover="Case Studies">Case Studies</a></li>
                                <li><a href="{prefix}contact/" data-hover="Contact Us">Contact Us</a></li>
                            </ul>'''

def fix_index_file():
    print("Processing index.html...")
    
    with open(INDEX_FILE, "r", encoding="utf-8") as f:
        content = f.read()
    
    soup = BeautifulSoup(content, "html.parser")
    
    # Fix all asset links (remove any ../ prefixes since we're at root)
    prefix = "./"
    
    # Fix link tags (CSS)
    for link in soup.find_all("link", href=True):
        href = link["href"]
        if not href.startswith(("http", "#", "javascript:", "mailto:", "tel:")):
            # Clean up any ../ prefixes
            clean_href = href
            while clean_href.startswith("../"):
                clean_href = clean_href[3:]
            
            # Check if it's an asset
            first_part = clean_href.split("/")[0]
            if first_part in ASSET_DIRS or clean_href.startswith(("css/", "js/", "images/", "plugins/", "fonts/")):
                link["href"] = prefix + clean_href
    
    # Fix script tags (JS)
    for script in soup.find_all("script", src=True):
        src = script["src"]
        if not src.startswith(("http", "#", "javascript:", "mailto:", "tel:")):
            clean_src = src
            while clean_src.startswith("../"):
                clean_src = clean_src[3:]
            
            first_part = clean_src.split("/")[0]
            if first_part in ASSET_DIRS or clean_src.startswith(("css/", "js/", "images/", "plugins/", "fonts/")):
                script["src"] = prefix + clean_src
    
    # Fix img tags
    for img in soup.find_all("img", src=True):
        src = img["src"]
        if not src.startswith(("http", "#", "data:")):
            clean_src = src
            while clean_src.startswith("../"):
                clean_src = clean_src[3:]
            
            if clean_src.startswith("images/"):
                img["src"] = prefix + clean_src
    
    # Fix inline style background images
    for tag in soup.find_all(style=True):
        style = tag["style"]
        if "background-image:url(" in style or "background-image: url(" in style:
            # This is a simple fix for images/ paths
            if "images/" in style and not "http" in style:
                # Clean it up
                style = style.replace("url(images/", f"url({prefix}images/")
                tag["style"] = style
    
    # Fix Navigation Menu
    nav_ul = soup.find("ul", class_="nav navbar-nav nav-line-animation")
    if nav_ul:
        new_nav = BeautifulSoup(create_navigation_html(prefix), "html.parser")
        nav_ul.replace_with(new_nav)
        print("  ✓ Updated navigation menu")
    
    # Fix Footer Links
    footer_link_div = soup.find("div", class_="footer-link")
    if footer_link_div:
        footer_ul = footer_link_div.find("ul")
        if footer_ul:
            new_footer = BeautifulSoup(create_footer_links_html(prefix), "html.parser")
            footer_ul.replace_with(new_footer)
            print("  ✓ Updated footer links")
    
    # Save changes
    with open(INDEX_FILE, "w", encoding="utf-8") as f:
        f.write(str(soup))
    
    print("✓ Complete!")

if __name__ == "__main__":
    fix_index_file()
