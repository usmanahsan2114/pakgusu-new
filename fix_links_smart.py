import os
from bs4 import BeautifulSoup
import re

# Configuration
ROOT_DIR = r"c:\xampp\htdocs\pakgusu-1\intoriza\pakgusu-new\intoriza"
# Map old filenames to their new directory paths (relative to ROOT_DIR)
# Note: These keys should match the filenames as they appear in hrefs (e.g., "about-1.html")
LINK_MAPPING = {
    "index.html": "",  # Root
    "index-2.html": "services/",
    "index-3.html": "industries/",
    "index-4.html": "careers/",
    "about-1.html": "about/",
    "news-grid.html": "resources/news-events/",
    "news-listing.html": "resources/blog/",
    "news-masonry.html": "resources/",
    "work-grid.html": "products/",
    "work-masonry.html": "case-studies/",
    "project-detail.html": "products/cleanroom-panels/", # Default product link
    "post-gallery.html": "resources/cleanroom-standards-classifications/",
    "post-right-sidebar.html": "resources/faqs/",
    "contact-1.html": "contact/",
}

# Asset folders that need prefixing
ASSET_DIRS = ["css", "js", "images", "plugins", "fonts"]

def get_depth(file_path):
    """Calculates the depth of a file relative to the ROOT_DIR."""
    rel_path = os.path.relpath(file_path, ROOT_DIR)
    # Depth is number of separators in the relative path
    # e.g., "index.html" -> 0, "about/index.html" -> 1
    if rel_path == ".": return 0
    return rel_path.count(os.sep)

def get_prefix(depth):
    """Returns the relative prefix string based on depth."""
    if depth == 0:
        return "./"
    return "../" * depth

def fix_link(href, prefix):
    """Updates a single link based on the mapping and prefix."""
    if not href or href.startswith(("http", "#", "javascript:", "mailto:", "tel:")):
        return href

    # 1. Check if it's a known page link
    for old_name, new_path in LINK_MAPPING.items():
        if href == old_name:
            return f"{prefix}{new_path}"
    
    # 2. Check if it's an asset link
    # Normalize path to use forward slashes for checking
    norm_href = href.replace("\\", "/")
    
    # If it already starts with ../, we assume it might be correct or partially correct
    # But for safety in this specific restructuring, we want to enforce the correct depth.
    # So we strip existing ../ prefixes and re-apply the correct one.
    
    clean_href = norm_href
    while clean_href.startswith("../"):
        clean_href = clean_href[3:]
    
    # Check if it starts with an asset directory
    first_part = clean_href.split("/")[0]
    if first_part in ASSET_DIRS:
        return f"{prefix}{clean_href}"

    return href

def process_file(file_path):
    print(f"Processing: {file_path}")
    depth = get_depth(file_path)
    prefix = get_prefix(depth)
    
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    soup = BeautifulSoup(content, "html.parser")
    
    # Fix <a> tags
    for a in soup.find_all("a", href=True):
        old_href = a["href"]
        new_href = fix_link(old_href, prefix)
        if old_href != new_href:
            # print(f"  [A] {old_href} -> {new_href}")
            a["href"] = new_href

    # Fix <link> tags (CSS)
    for link in soup.find_all("link", href=True):
        old_href = link["href"]
        new_href = fix_link(old_href, prefix)
        if old_href != new_href:
            # print(f"  [LINK] {old_href} -> {new_href}")
            link["href"] = new_href

    # Fix <script> tags (JS)
    for script in soup.find_all("script", src=True):
        old_src = script["src"]
        new_src = fix_link(old_src, prefix)
        if old_src != new_src:
            # print(f"  [SCRIPT] {old_src} -> {new_src}")
            script["src"] = new_src

    # Fix <img> tags
    for img in soup.find_all("img", src=True):
        old_src = img["src"]
        new_src = fix_link(old_src, prefix)
        if old_src != new_src:
            # print(f"  [IMG] {old_src} -> {new_src}")
            img["src"] = new_src

    # Save changes
    # Use prettify() sparingly as it can mess up formatting, but for now we just write str(soup)
    # However, bs4 might change formatting slightly. 
    # To be safe, we'll write it back.
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(str(soup))

def main():
    for root, dirs, files in os.walk(ROOT_DIR):
        for file in files:
            if file.lower() == "index.html":
                file_path = os.path.join(root, file)
                process_file(file_path)

if __name__ == "__main__":
    main()
