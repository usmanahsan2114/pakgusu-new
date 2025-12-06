import os

# Define root directory
ROOT_DIR = r"c:\xampp\htdocs\pakgusu-1\intoriza\pakgusu-new\intoriza"

def get_relative_prefix(file_path):
    # Calculate depth relative to ROOT_DIR
    rel_path = os.path.relpath(file_path, ROOT_DIR)
    
    if rel_path == "index.html":
        return "./"
        
    # Count directory separators to determine depth
    depth = rel_path.count(os.sep)
    if depth == 0:
        return "./"
        
    return "../" * depth

def fix_file(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
            
        original_content = content
        prefix = get_relative_prefix(file_path)
        
        # 1. Desktop Nav - Products
        content = content.replace(
            '<a href="javascript:;" class="gh-nav-link">Products <i',
            f'<a href="{prefix}products/" class="gh-nav-link">Products <i'
        )
        
        # 2. Desktop Nav - Industries 
        content = content.replace(
            '<a href="javascript:;" class="gh-nav-link">Industries <i',
            f'<a href="{prefix}industries/" class="gh-nav-link">Industries <i'
        )
        
        # 3. Mobile Nav - Products
        # Match the specific style attribute if present, or generic
        content = content.replace(
            '<a href="javascript:;" class="gh-mobile-link" style="flex:1;">Products</a>',
            f'<a href="{prefix}products/" class="gh-mobile-link" style="flex:1;">Products</a>'
        )
        
        # 4. Mobile Nav - Industries
        content = content.replace(
            '<a href="javascript:;" class="gh-mobile-link" style="flex:1;">Industries</a>',
            f'<a href="{prefix}industries/" class="gh-mobile-link" style="flex:1;">Industries</a>'
        )

        if content != original_content:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"Fixed: {file_path}")
        else:
            # check if it was already fixed or format didn't match
            pass
            
    except Exception as e:
        print(f"Error processing {file_path}: {e}")

def main():
    print(f"Scanning {ROOT_DIR}...")
    count = 0
    for root, dirs, files in os.walk(ROOT_DIR):
        for file in files:
            if file.endswith(".html"):
                fix_file(os.path.join(root, file))
                count += 1
    print(f"Scanned {count} files.")

if __name__ == "__main__":
    main()
