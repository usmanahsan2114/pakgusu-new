import os
from bs4 import BeautifulSoup
import urllib.parse

def check_links(start_dir):
    base_path = os.path.abspath(start_dir)
    errors = []
    checked_count = 0
    error_count = 0

    print(f"Starting link verification in: {base_path}")

    for root, dirs, files in os.walk(base_path):
        for file in files:
            if not file.endswith(".html"):
                continue

            file_path = os.path.join(root, file)
            # print(f"Checking: {file_path}")
            
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    soup = BeautifulSoup(f, 'html.parser')
            except Exception as e:
                print(f"Error reading {file_path}: {e}")
                continue

            # Check hrefs and srcs
            for tag in soup.find_all(['a', 'link', 'img', 'script', 'source']):
                attr = 'href' if tag.name in ['a', 'link'] else 'src'
                link = tag.get(attr)

                if not link:
                    continue

                link = link.strip()

                # Skip ignore cases
                if (link.startswith(('http://', 'https://', 'mailto:', 'tel:', 'javascript:', '#')) or 
                    link == ''):
                    continue

                # Handle anchors in links (e.g., page.html#section)
                url_parts = urllib.parse.urlparse(link)
                path_part = url_parts.path
                
                if not path_part: # Just an anchor or query
                    continue

                # Resolve path
                # If it starts with /, it's relative to web root (assuming intoriza/ is root for this check, or we need to be careful)
                # In this project, it seems mostly relative paths are used (../)
                
                target_path = None
                if path_part.startswith('/'):
                    # Assuming / refers to the root of the drive or server root. 
                    # For this local check, let's assume it might be relative to the project root if that was the intent, 
                    # but standard filesystem / is root. 
                    # However, usually in these static sites ./ or ../ is used.
                    # Let's flag absolute paths as potential issues if they don't exist on disk relative to drive
                    # But often /images/foo.jpg implies webroot. 
                    # Let's assume webroot is `c:\xampp\htdocs\pakgusu-1\intoriza\pakgusu-new\intoriza`
                    # But for now, let's stick to relative resolution.
                    pass 
                else:
                    # Relative path
                    target_path = os.path.normpath(os.path.join(os.path.dirname(file_path), path_part))

                if target_path:
                    if not os.path.exists(target_path):
                        # Try decoding URL encoding (e.g. %20)
                        target_path_decoded = urllib.parse.unquote(target_path)
                        if not os.path.exists(target_path_decoded):
                            errors.append(f"[MISSING] File: {os.path.relpath(file_path, base_path)} -> Link: {link} (Target: {target_path})")
                            error_count += 1
                
                checked_count += 1

    with open('link_report.txt', 'w', encoding='utf-8') as f:
        f.write(f"Verification Complete.\\n")
        f.write(f"Links Checked: {checked_count}\\n")
        f.write(f"Broken Links Found: {error_count}\\n")
        
        if errors:
            f.write("\\n--- Broken Links Report ---\\n")
            for e in errors:
                f.write(e + "\\n")
        else:
            f.write("\\nNo broken links found!\\n")
    
    print("Report written to link_report.txt")

if __name__ == "__main__":
    # Run on the 'intoriza' directory where the site lives
    check_links("intoriza")
