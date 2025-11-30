import os
from bs4 import BeautifulSoup

ROOT_DIR = r"c:\xampp\htdocs\pakgusu-1\intoriza\pakgusu-new\intoriza"

# Define the STRICT required sections for each page type
# This maps exactly to Page_by_Page_Section_Layout.md
PAGE_LAYOUTS = {
    "home": [
        "Hero",
        "Who We Are",
        "Our Solutions",
        "Product Highlights",
        "Industries We Serve",
        "Why Choose PakGusu",
        "Latest from Resources",
        "Call-to-Action Banner"
    ],
    "about": [
        "Hero",
        "Company Snapshot",
        "Our Story & Timeline",
        "Partnership with GUSU China",
        "Mission, Vision & Values",
        "Our Facility & Capabilities",
        "Quality & Compliance",
        "Leadership / Expertise",
        "CTA"
    ],
    "products_overview": [
        "Hero",
        "Intro",
        "Product Category Grid",
        "How Our Products Integrate",
        "CTA"
    ],
    "product_detail": [
        "Hero",
        "Overview",
        "Product Specifics",
        "Key Features & Benefits",
        "Technical Specs / Applications",
        "Gallery",
        "Related Solutions",
        "CTA"
    ],
    "services_overview": [
        "Hero",
        "Overview",
        "Process Strip / Timeline",
        "Planning & Design",
        "Construction",
        "Installation & Commissioning",
        "After-Sales & Maintenance",
        "Project Workflow Diagram",
        "CTA"
    ],
    "industries_overview": [
        "Hero",
        "Intro Paragraph",
        "Industry Cards Grid",
        "CTA"
    ],
    "industry_detail": [
        "Hero",
        "Industry Challenges & Regulatory Context",
        "PakGusu Solutions",
        "Specific Details",
        "Example Use Cases",
        "Related Products & Services",
        "CTA"
    ],
    "resources_overview": [
        "Hero",
        "Intro",
        "Featured Resource",
        "Latest Blog Posts",
        "Latest News & Events",
        "Link Tiles"
    ],
    "resource_sub": [
        "Hero",
        "Content",
        "CTA"
    ],
    "case_studies": [
        "Hero",
        "Intro",
        "Case Study Cards List",
        "Filters",
        "CTA"
    ],
    "careers": [
        "Hero",
        "Intro",
        "Why Work With Us",
        "Open Positions List",
        "Application CTA"
    ],
    "contact": [
        "Hero",
        "Intro",
        "Contact Form",
        "Contact Details",
        "Map Embed",
        "Support Info"
    ]
}

def create_section_html(name):
    """Creates a placeholder section with the correct marker."""
    return f'''
    <!-- Section: {name} -->
    <div class="section-full p-t80 p-b50 bg-white placeholder-section" id="section-{name.lower().replace(' ', '-').replace('&', 'and')}">
        <div class="container">
            <div class="section-head text-center">
                <h2>{name}</h2>
                <div class="wt-separator-outer separator-center">
                    <div class="wt-separator">
                        <span class="site-text-primary text-uppercase sep-line-one">Pending Content</span>
                    </div>
                </div>
                <p><!-- TODO: Design and content needed for {name} --></p>
                <div class="alert alert-warning">
                    <strong>Pending Design:</strong> This section ({name}) requires implementation.
                </div>
            </div>
        </div>
    </div>
    <!-- /Section: {name} -->
    '''

def identify_page_type(file_path):
    filename = os.path.basename(file_path).lower()
    dir_name = os.path.basename(os.path.dirname(file_path)).lower()
    path_parts = file_path.lower().split(os.sep)
    
    # Home
    if filename == "index.html" and dir_name == "intoriza":
        return "home"
    
    # Top Level Pages
    if "about" in dir_name: return "about"
    if "services" in dir_name: return "services_overview" # Assuming index.html in services/ is overview
    if "careers" in dir_name: return "careers"
    if "contact" in dir_name: return "contact"
    if "case-studies" in dir_name: return "case_studies"
    
    # Products
    if "products" in dir_name:
        return "products_overview"
    if "products" in path_parts:
        return "product_detail"

    # Industries
    if "industries" in dir_name: return "industries_overview"
    if "industries" in path_parts:
        return "industry_detail"

    # Resources
    if "resources" in dir_name: return "resources_overview"
    if "resources" in path_parts:
        return "resource_sub"

    return "default"

def process_page(file_path):
    page_type = identify_page_type(file_path)
    if page_type == "default":
        print(f"Skipping {file_path} (Unknown type)")
        return

    print(f"Processing {file_path} as {page_type}...")
    
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    soup = BeautifulSoup(content, "html.parser")
    
    # Locate Page Content Container
    page_content = soup.find("div", class_="page-content")
    if not page_content:
        print(f"  ⚠ No .page-content found in {file_path}")
        return

    # Preserve Hero/Banner if it exists in the layout
    # We assume the first section in .page-content is usually the Hero/Slider/Banner
    # We will try to extract it.
    hero_section = None
    
    # Try to find common hero classes
    hero_candidates = page_content.select(".rev_slider_wrapper, .wt-bnr-inr")
    if hero_candidates:
        hero_section = hero_candidates[0]
        print("  ✓ Found existing Hero section")
    
    # Generate New Content
    new_html = ""
    layout = PAGE_LAYOUTS.get(page_type, [])
    
    for section_name in layout:
        if section_name == "Hero":
            if hero_section:
                new_html += f"\n<!-- Section: Hero -->\n{str(hero_section)}\n<!-- /Section: Hero -->\n"
            else:
                new_html += create_section_html("Hero (Missing)")
        else:
            new_html += create_section_html(section_name)
            
    # Replace Content
    # We create a new soup fragment
    new_soup = BeautifulSoup(new_html, "html.parser")
    page_content.clear()
    page_content.append(new_soup)
    
    # Save
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(str(soup))
    print(f"  ✓ Updated structure for {file_path}")

def main():
    print("=== Strict Structure Manager ===\n")
    
    for root, dirs, files in os.walk(ROOT_DIR):
        if "extra" in dirs:
            dirs.remove("extra") # Skip backup folder
            
        for file in files:
            if file.lower() == "index.html":
                file_path = os.path.join(root, file)
                process_page(file_path)

    print("\n=== Complete! ===")

if __name__ == "__main__":
    main()
