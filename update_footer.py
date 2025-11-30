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

def create_footer_copyright_html():
    """Create the new footer copyright section"""
    return '''<div class="row">
                            <div class="col-md-6 col-sm-6">
                                <span class="copyrights-text">© 2025 by <a href="https://pakgusu.com/" target="_blank" rel="noopener">PakGusu</a></span>
                            </div>
                            <div class="col-md-6 col-sm-6 text-right">
                                <span class="copyrights-text">
                                    Designed and Developed by <a href="https://www.apexitsolutions.co/" target="_blank" rel="noopener">Apex IT Solutions</a> | 
                                    <a href="https://apexmarketings.com/" target="_blank" rel="noopener">Apex Marketings</a>
                                </span>
                            </div>
                        </div>'''

def update_footer(file_path):
    print(f"Processing: {file_path}")
    
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    soup = BeautifulSoup(content, "html.parser")
    
    # Find footer copyright section
    footer_bottom = soup.find("div", class_="footer-bottom")
    if footer_bottom:
        container = footer_bottom.find("div", class_="container")
        if container:
            # Find existing row with copyright
            existing_row = container.find("div", class_="row")
            if existing_row:
                # Replace with new copyright HTML
                new_copyright = BeautifulSoup(create_footer_copyright_html(), "html.parser")
                existing_row.replace_with(new_copyright)
                print(f"  ✓ Updated footer copyright")
            else:
                print(f"  ⚠ No row found in footer")
        else:
            print(f"  ⚠ No container found in footer-bottom")
    else:
        print(f"  ⚠ No footer-bottom found")
    
    # Save changes
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(str(soup))

def main():
    print("=== Updating Footer Copyright ===\n")
    
    count = 0
    for root, dirs, files in os.walk(ROOT_DIR):
        # Skip the extra directory
        if "extra" in dirs:
            dirs.remove("extra")
            
        for file in files:
            if file.lower() == "index.html":
                file_path = os.path.join(root, file)
                update_footer(file_path)
                count += 1
    
    print(f"\n=== Complete! Updated {count} pages ===")

if __name__ == "__main__":
    main()
