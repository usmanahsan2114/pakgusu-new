import os
import shutil
from bs4 import BeautifulSoup

# Configuration
ROOT_DIR = r"c:\xampp\htdocs\pakgusu-1\intoriza\pakgusu-new\intoriza"
ORIGINALS_DIR = os.path.join(ROOT_DIR, "extra", "originals")

# Structure Mapping: New Path (relative to ROOT_DIR) -> Source File (in ORIGINALS_DIR)
STRUCTURE_MAPPING = {
    "": "index.html",
    "about": "about-1.html",
    "products": "work-grid.html",
    "products/cleanroom-panels": "project-detail.html",
    "products/cleanroom-windows": "project-detail.html",
    "products/cleanroom-doors": "project-detail.html",
    "products/pass-through-chambers": "project-detail.html",
    "products/aluminum-profiles": "project-detail.html",
    "products/cleanroom-led-lights": "project-detail.html",
    "services": "index-2.html",
    "industries": "index-3.html",
    "industries/pharmaceutical-nutraceutical": "project-detail.html",
    "industries/healthcare-hospitals": "project-detail.html",
    "industries/food-beverage": "project-detail.html",
    "industries/electronics-manufacturing": "project-detail.html",
    "industries/laboratories-rnd": "project-detail.html",
    "industries/medical-surgical-devices": "project-detail.html",
    "resources": "news-masonry.html",
    "resources/cleanroom-standards-classifications": "post-gallery.html",
    "resources/blog": "news-listing.html",
    "resources/news-events": "news-grid.html",
    "resources/faqs": "post-right-sidebar.html",
    "case-studies": "work-masonry.html",
    "careers": "index-4.html",
    "contact": "contact-1.html",
}

# Link Mapping for fixing hrefs
LINK_MAPPING = {
    "index.html": "",
    "index-2.html": "services/",
    "index-3.html": "industries/",
    "index-4.html": "careers/",
    "about-1.html": "about/",
    "news-grid.html": "resources/news-events/",
    "news-listing.html": "resources/blog/",
    "news-masonry.html": "resources/",
    "work-grid.html": "products/",
    "work-masonry.html": "case-studies/",
    "project-detail.html": "products/cleanroom-panels/", # Default to one product page if generic
    "post-gallery.html": "resources/cleanroom-standards-classifications/",
    "post-right-sidebar.html": "resources/faqs/",
    "contact-1.html": "contact/",
}

ASSET_DIRS = ["css", "js", "images", "plugins", "fonts", "media", "phpmailer"]

def get_depth(file_path):
    rel_path = os.path.relpath(file_path, ROOT_DIR)
    if rel_path == ".": return 0
    return rel_path.count(os.sep)

def get_prefix(depth):
    if depth == 0: return "./"
    return "../" * depth

def fix_link(href, prefix):
    if not href or href.startswith(("http", "#", "javascript:", "mailto:", "tel:")):
        return href

    # 1. Check known page links
    for old_name, new_path in LINK_MAPPING.items():
        if href == old_name:
            return f"{prefix}{new_path}"
    
    # 2. Check asset links
    norm_href = href.replace("\\", "/")
    clean_href = norm_href
    while clean_href.startswith("../"):
        clean_href = clean_href[3:]
    
    first_part = clean_href.split("/")[0]
    if first_part in ASSET_DIRS:
        return f"{prefix}{clean_href}"

    return href

def setup_structure():
    print("--- Setting up Structure ---")
    for rel_path, source_file in STRUCTURE_MAPPING.items():
        target_dir = os.path.join(ROOT_DIR, rel_path)
        target_file = os.path.join(target_dir, "index.html")
        source_path = os.path.join(ORIGINALS_DIR, source_file)

        if not os.path.exists(target_dir):
            os.makedirs(target_dir)
            print(f"Created directory: {rel_path}")
        
        # Always copy to ensure we have the clean original file
        # But wait, if we overwrite, we lose previous fixes?
        # The user said "copy files... same as before". 
        # Ideally we start fresh from originals to ensure consistency, then fix links.
        if os.path.exists(source_path):
            shutil.copy2(source_path, target_file)
            print(f"Copied {source_file} -> {rel_path}/index.html")
        else:
            print(f"Warning: Source file not found: {source_path}")

def fix_links_in_file(file_path):
    depth = get_depth(file_path)
    prefix = get_prefix(depth)
    print(f"Fixing links in: {file_path} (Depth: {depth})")
    
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    soup = BeautifulSoup(content, "html.parser")
    
    for tag_name, attr in [("a", "href"), ("link", "href"), ("script", "src"), ("img", "src")]:
        for tag in soup.find_all(tag_name, **{attr: True}):
            old_val = tag[attr]
            new_val = fix_link(old_val, prefix)
            if old_val != new_val:
                tag[attr] = new_val

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(str(soup))

def main():
    # 1. Setup Structure
    setup_structure()
    
    # 2. Fix Links
    print("\n--- Fixing Links ---")
    for root, dirs, files in os.walk(ROOT_DIR):
        # Skip the extra directory to avoid processing backups
        if "extra" in dirs:
            dirs.remove("extra")
            
        for file in files:
            if file.lower() == "index.html":
                file_path = os.path.join(root, file)
                fix_links_in_file(file_path)

if __name__ == "__main__":
    main()
