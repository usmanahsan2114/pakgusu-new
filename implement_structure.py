import os
from bs4 import BeautifulSoup
import re

ROOT_DIR = r"c:\xampp\htdocs\pakgusu-1\intoriza\pakgusu-new\intoriza"

# Define standard section layouts
LAYOUTS = {
    "index.html": [
        "Hero", "Who We Are", "Our Solutions", "Product Highlights", 
        "Industries We Serve", "Why Choose PakGusu", "Latest from Resources", 
        "Call-to-Action Banner"
    ],
    "about/index.html": [
        "Hero", "Company Snapshot", "Our Story & Timeline", "Partnership with GUSU China",
        "Mission, Vision & Values", "Our Facility & Capabilities", "Quality & Compliance",
        "Leadership / Expertise", "CTA"
    ],
    "products/index.html": [
        "Hero", "Intro", "Product Category Grid", "How Our Products Integrate", "CTA"
    ],
    "services/index.html": [
        "Hero", "Overview", "Process Strip / Timeline", "Planning & Design",
        "Construction", "Installation & Commissioning", "After-Sales & Maintenance",
        "Project Workflow Diagram", "CTA"
    ],
    "industries/index.html": [
        "Hero", "Intro Paragraph", "Industry Cards Grid", "CTA"
    ],
    "resources/index.html": [
        "Hero", "Intro", "Featured Resource", "Latest Blog Posts", 
        "Latest News & Events", "Link Tiles"
    ],
    "contact/index.html": [
        "Hero", "Intro", "Contact Form", "Contact Details", "Map Embed", "Support Info"
    ],
    "default_product": [
        "Hero", "Overview", "Panel Types / Options", "Key Features & Benefits",
        "Technical Specs", "Gallery", "Related Solutions", "CTA"
    ],
    "default_industry": [
        "Hero", "Industry Challenges", "PakGusu Solutions", "Typical Cleanroom Classes",
        "Example Use Cases", "Related Products & Services", "CTA"
    ],
    "default": [
        "Hero", "Content Section 1", "Content Section 2", "CTA"
    ]
}

def get_layout_for_file(rel_path):
    # Check exact matches
    if rel_path in LAYOUTS:
        return LAYOUTS[rel_path]
    
    # Check directory-based matches
    if rel_path.startswith("products/"):
        return LAYOUTS["default_product"]
    if rel_path.startswith("industries/"):
        return LAYOUTS["default_industry"]
    
    return LAYOUTS["default"]

def create_placeholder_section(title):
    return f'''
    <!-- Section: {title} -->
    <div class="section-full p-t80 p-b50 bg-white">
        <div class="container">
            <div class="section-head text-center">
                <h2>{title}</h2>
                <div class="wt-separator-outer separator-center">
                    <div class="wt-separator">
                        <span class="site-text-primary text-uppercase sep-line-one">Coming Soon</span>
                    </div>
                </div>
                <p><!-- TODO: Design and content needed for {title} --></p>
            </div>
        </div>
    </div>
    <!-- /Section: {title} -->
    '''

def update_footer_copyright(soup):
    footer_bottom = soup.find("div", class_="footer-bottom")
    if footer_bottom:
        container = footer_bottom.find("div", class_="container")
        if container:
            row = container.find("div", class_="row")
            if row:
                new_copyright = BeautifulSoup('''
                <div class="row">
                    <div class="col-md-6 col-sm-6">
                        <span class="copyrights-text">© 2025 by <a href="https://pakgusu.com/" target="_blank" rel="noopener">PakGusu</a></span>
                    </div>
                    <div class="col-md-6 col-sm-6 text-right">
                        <span class="copyrights-text">
                            Designed and Developed by <a href="https://www.apexitsolutions.co/" target="_blank" rel="noopener">Apex IT Solutions</a> | 
                            <a href="https://apexmarketings.com/" target="_blank" rel="noopener">Apex Marketings</a>
                        </span>
                    </div>
                </div>
                ''', "html.parser").div
                row.replace_with(new_copyright)
                return True
    return False

def process_file(file_path):
    rel_path = os.path.relpath(file_path, ROOT_DIR).replace("\\", "/")
    print(f"Processing: {rel_path}")
    
    layout = get_layout_for_file(rel_path)
    
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    soup = BeautifulSoup(content, "html.parser")
    
    # 1. Update Footer
    if update_footer_copyright(soup):
        print("  ✓ Footer updated")
    else:
        print("  ⚠ Footer update failed")

    # 2. Identify Content Blocks
    page_content = soup.find("div", class_="page-content")
    if not page_content:
        print("  ⚠ No page-content div found")
        return

    # Extract existing blocks (Banner, Slider, Sections)
    blocks = []
    
    # Check for Slider
    slider = page_content.find("div", class_="rev_slider_wrapper")
    if slider:
        blocks.append({"type": "Hero", "elem": slider, "used": False})
    
    # Check for Banner
    banner = page_content.find("div", class_="wt-bnr-inr")
    if banner:
        blocks.append({"type": "Hero", "elem": banner, "used": False})
        
    # Check for Sections
    for section in page_content.find_all("div", class_="section-full"):
        # Try to identify section type by content
        text = section.get_text().lower()
        stype = "Content"
        if "welcome" in text or "about" in text: stype = "Intro"
        elif "what we do" in text or "services" in text: stype = "Solutions"
        elif "project" in text or "gallery" in text: stype = "Highlights"
        elif "team" in text or "choose" in text: stype = "Why Choose"
        elif "news" in text or "blog" in text: stype = "Resources"
        elif "contact" in text: stype = "Contact"
        
        blocks.append({"type": stype, "elem": section, "used": False})

    # 3. Reconstruct Page Content
    new_content_div = soup.new_tag("div", **{"class": "page-content"})
    
    # Add blocks according to layout
    for section_name in layout:
        # Find best matching unused block
        matched_block = None
        
        # Priority 1: Exact type match (e.g., Hero -> Hero)
        for block in blocks:
            if not block["used"]:
                if section_name == "Hero" and block["type"] == "Hero":
                    matched_block = block
                    break
                # Add more specific matching logic here if needed
        
        # Priority 2: Loose match (e.g., "Who We Are" -> "Intro")
        if not matched_block:
            for block in blocks:
                if not block["used"]:
                    if section_name == "Who We Are" and block["type"] == "Intro": matched_block = block; break
                    if section_name == "Company Snapshot" and block["type"] == "Intro": matched_block = block; break
                    if section_name == "Overview" and block["type"] == "Intro": matched_block = block; break
                    if section_name == "Our Solutions" and block["type"] == "Solutions": matched_block = block; break
                    if section_name == "Product Highlights" and block["type"] == "Highlights": matched_block = block; break
                    if section_name == "Latest from Resources" and block["type"] == "Resources": matched_block = block; break
        
        # Priority 3: Take next available content block (preserve order)
        if not matched_block:
            for block in blocks:
                if not block["used"] and block["type"] not in ["Hero"]: # Don't reuse Hero as content
                    matched_block = block
                    break
        
        if matched_block:
            matched_block["used"] = True
            # Add comment
            comment = BeautifulSoup(f"<!-- Section: {section_name} -->", "html.parser")
            new_content_div.append(comment)
            new_content_div.append(matched_block["elem"])
            # Add closing comment
            comment_end = BeautifulSoup(f"<!-- /Section: {section_name} -->", "html.parser")
            new_content_div.append(comment_end)
            print(f"  ✓ Mapped existing block to '{section_name}'")
        else:
            # Create placeholder
            placeholder_html = create_placeholder_section(section_name)
            placeholder_soup = BeautifulSoup(placeholder_html, "html.parser")
            new_content_div.append(placeholder_soup)
            print(f"  + Created placeholder for '{section_name}'")

    # Append any remaining unused blocks (to ensure nothing is deleted)
    unused_count = 0
    for block in blocks:
        if not block["used"]:
            new_content_div.append(block["elem"])
            unused_count += 1
    if unused_count > 0:
        print(f"  ! Appended {unused_count} unused blocks")

    # Replace old page-content with new one
    page_content.replace_with(new_content_div)
    
    # Save
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(str(soup))

def main():
    print("=== Implementing Page Structure ===\n")
    
    for root, dirs, files in os.walk(ROOT_DIR):
        if "extra" in dirs: dirs.remove("extra")
        
        for file in files:
            if file.lower() == "index.html":
                process_file(os.path.join(root, file))
    
    print("\n=== Complete! ===")

if __name__ == "__main__":
    main()
