import os
from bs4 import BeautifulSoup

ROOT_DIR = r"c:\xampp\htdocs\pakgusu-1\intoriza\pakgusu-new\intoriza"

def get_depth(file_path):
    rel_path = os.path.relpath(file_path, ROOT_DIR)
    if rel_path == ".": return 0
    return rel_path.count(os.sep)

def get_prefix(depth):
    if depth == 0: return "./"
    return "../" * depth

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

def fix_navigation_and_footer(file_path):
    print(f"Processing: {file_path}")
    depth = get_depth(file_path)
    prefix = get_prefix(depth)
    
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    soup = BeautifulSoup(content, "html.parser")
    
    # Fix Navigation Menu
    nav_ul = soup.find("ul", class_="nav navbar-nav nav-line-animation")
    if nav_ul:
        new_nav = BeautifulSoup(create_navigation_html(prefix), "html.parser")
        nav_ul.replace_with(new_nav)
        print(f"  ✓ Updated navigation menu (depth: {depth})")
    
    # Fix Footer Links
    footer_link_div = soup.find("div", class_="footer-link")
    if footer_link_div:
        footer_ul = footer_link_div.find("ul")
        if footer_ul:
            new_footer = BeautifulSoup(create_footer_links_html(prefix), "html.parser")
            footer_ul.replace_with(new_footer)
            print(f"  ✓ Updated footer links")
    
    # Save changes
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(str(soup))

def main():
    print("=== Fixing Navigation and Footer Menus ===\n")
    
    for root, dirs, files in os.walk(ROOT_DIR):
        # Skip the extra directory to avoid processing backups
        if "extra" in dirs:
            dirs.remove("extra")
            
        for file in files:
            if file.lower() == "index.html":
                file_path = os.path.join(root, file)
                fix_navigation_and_footer(file_path)
    
    print("\n=== Complete! ===")

if __name__ == "__main__":
    main()
