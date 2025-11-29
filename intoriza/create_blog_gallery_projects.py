import os
import re
from bs4 import BeautifulSoup

base_dir = r'c:\xampp\htdocs\pakgusu-new\intoriza'

# Define the file mappings
file_mappings = {
    # Blog listing pages
    'news-grid.html': 'blogs/grid/index.php',
    'news-listing.html': 'blogs/listing/index.php',
    'news-masonry.html': 'blogs/masonry/index.php',
    # Blog detail pages
    'post-gallery.html': 'blogs/post-gallery/index.php',
    'post-right-sidebar.html': 'blogs/post-detail/index.php',
    # Project pages
    'project-detail.html': 'projects/detail/index.php',
    'work-grid.html': 'projects/grid/index.php',
    'work-masonry.html': 'projects/masonry/index.php',
}

def extract_page_title(soup):
    """Extract page title from the HTML"""
    title_tag = soup.find('title')
    if title_tag:
        title_text = title_tag.get_text().strip()
        # Remove "intoriza Template | " prefix if exists
        title_text = re.sub(r'^intoriza Template \| ', '', title_text)
        return title_text
    return 'Page'

def calculate_path_depth(target_path):
    """Calculate the depth for $path variable"""
    depth = target_path.count('/')
    return '../' * depth

def transform_html_to_php(html_file, php_file):
    """Transform HTML file to PHP with includes"""
    
    # Read the HTML file
    with open(html_file, 'r', encoding='utf-8') as f:
        html_content = f.read()
    
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Extract page title
    page_title = extract_page_title(soup)
    
    # Calculate path depth
    relative_dir = os.path.dirname(php_file).replace(base_dir + '\\', '').replace('\\', '/')
    path_value = calculate_path_depth(relative_dir)
    
    # Find the body content (everything after header and before footer)
    body = soup.find('body')
    if not body:
        print(f"No body found in {html_file}")
        return
    
    # Extract the page content (between header and footer)
    page_content_div = body.find('div', class_='page-content')
    
    if not page_content_div:
        print(f"No page-content div found in {html_file}")
        return
    
    # Get the page content HTML
    page_content_html = str(page_content_div)
    
    # Update image and link paths
    page_content_html = re.sub(r'src="images/', f'src="<?php echo $path; ?>images/', page_content_html)
    page_content_html = re.sub(r'href="images/', f'href="<?php echo $path; ?>images/', page_content_html)
    page_content_html = re.sub(r"background-image:url\(images/", r"background-image:url(<?php echo $path; ?>images/", page_content_html)
    
    # Update internal links
    page_content_html = re.sub(r'href="([^"#]+)\.html"', lambda m: f'href="<?php echo $path; ?>{m.group(1)}.php"' if not m.group(1).startswith('http') else m.group(0), page_content_html)
    
    # Extract page-specific scripts
    page_scripts = []
    scripts = body.find_all('script')
    for script in scripts:
        if script.string and 'owl' in script.string.lower():
            page_scripts.append(str(script))
    
    # Create PHP content
    php_content = f"""<?php
$path = '{path_value}';
$page_title = '{page_title}';
include($path . 'include/head.php');
include($path . 'include/header.php');
?>

{page_content_html}
        <!-- CONTENT END -->

<?php
include($path . 'include/footer.php');
?>

{''.join(page_scripts)}

</body>
</html>
"""
    
    # Create directory if it doesn't exist
    os.makedirs(os.path.dirname(php_file), exist_ok=True)
    
    # Write PHP file
    with open(php_file, 'w', encoding='utf-8') as f:
        f.write(php_content)
    
    print(f"Created: {php_file}")

# Process all files
for html_file, php_path in file_mappings.items():
    source_file = os.path.join(base_dir, html_file)
    target_file = os.path.join(base_dir, php_path)
    
    if os.path.exists(source_file):
        transform_html_to_php(source_file, target_file)
    else:
        print(f"Source file not found: {source_file}")

print("\nAll files transformed successfully!")
