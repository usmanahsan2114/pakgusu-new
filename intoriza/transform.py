import os
import re

base_dir = r'c:\xampp\htdocs\pakgusu-new\intoriza'
files_to_process = [
    ('index.html', 'index.php', ''),
    ('about-1.html', 'about/index.php', '../'),
    ('contact-1.html', 'contact/index.php', '../'),
    ('index-2.html', 'extra/index-2.php', '../'),
    ('index-3.html', 'extra/index-3.php', '../'),
    ('index-4.html', 'extra/index-4.php', '../'),
    ('news-grid.html', 'extra/news-grid.php', '../'),
    ('news-listing.html', 'extra/news-listing.php', '../'),
    ('news-masonry.html', 'extra/news-masonry.php', '../'),
    ('post-gallery.html', 'extra/post-gallery.php', '../'),
    ('post-right-sidebar.html', 'extra/post-right-sidebar.php', '../'),
    ('project-detail.html', 'extra/project-detail.php', '../'),
    ('work-grid.html', 'extra/work-grid.php', '../'),
    ('work-masonry.html', 'extra/work-masonry.php', '../')
]

link_mappings = {
    'index.html': 'index.php',
    'about-1.html': 'about/index.php',
    'contact-1.html': 'contact/index.php',
    'index-2.html': 'extra/index-2.php',
    'index-3.html': 'extra/index-3.php',
    'index-4.html': 'extra/index-4.php',
    'news-grid.html': 'extra/news-grid.php',
    'news-listing.html': 'extra/news-listing.php',
    'news-masonry.html': 'extra/news-masonry.php',
    'post-gallery.html': 'extra/post-gallery.php',
    'post-right-sidebar.html': 'extra/post-right-sidebar.php',
    'project-detail.html': 'extra/project-detail.php',
    'work-grid.html': 'extra/work-grid.php',
    'work-masonry.html': 'extra/work-masonry.php'
}

def process_file(filename, target_rel_path, path_prefix):
    file_path = os.path.join(base_dir, filename)
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract Title
    title_match = re.search(r'<title>(.*?)</title>', content, re.IGNORECASE)
    page_title = title_match.group(1) if title_match else 'intoriza Template'
    page_title = page_title.replace('intoriza Template | ', '')

    # Extract Content (between HEADER END and FOOTER START)
    # Note: HEADER END is around line 214, FOOTER START around 1356 in index.html
    # We need robust markers.
    
    header_end_marker = '<!-- HEADER END -->'
    footer_start_marker = '<!-- FOOTER START -->'
    
    parts = content.split(header_end_marker)
    if len(parts) < 2:
        print(f"Header end marker not found in {filename}")
        # Fallback or skip
        return
    
    body_part = parts[1]
    
    parts2 = body_part.split(footer_start_marker)
    if len(parts2) < 2:
        print(f"Footer start marker not found in {filename}")
        return
        
    main_content = parts2[0]
    
    # Extract only page-specific inline scripts
    # Footer.php already includes: scroltop button, preloader, style switcher, and all common JS
    # We only want to keep inline <script>...</script> blocks that are page-specific
    
    footer_end_marker = '<!-- FOOTER END -->'
    parts3 = content.split(footer_end_marker)
    footer_suffix = parts3[1] if len(parts3) > 1 else ''
    
    # Extract only inline scripts and page-specific revolution scripts
    suffix_lines = footer_suffix.split('\n')
    page_scripts_lines = []
    in_inline_script = False
    
    for line in suffix_lines:
        # Skip common elements (button, loading area, style switcher)
        if '<!-- BUTTON TOP START -->' in line or 'class="scroltop"' in line:
            continue
        if '<!-- LOADING AREA' in line or 'class="loading-area"' in line or 'class="loading-box"' in line or 'cssload-box-loading' in line:
            continue
        if 'class="styleswitcher"' in line or 'switcher-btn-bx' in line:
            continue
        if '<!-- STYLE SWITCHER' in line:
            continue
            
        # Skip common JS includes
        if '<script' in line and 'src=' in line:
            # Keep only page-specific revolution scripts
            if 'rev-script-' in line and 'rev-script-2.js' not in line:
                page_scripts_lines.append(line)
            continue
            
        # Keep inline scripts
        if '<script' in line and 'src=' not in line:
            in_inline_script = True
            page_scripts_lines.append(line)
            continue
        
        if in_inline_script:
            page_scripts_lines.append(line)
            if '</script>' in line:
                in_inline_script = False
                
        # Skip closing tags
        if '</body>' in line or '</html>' in line:
            continue
            
    page_scripts = '\n'.join(page_scripts_lines).strip()
    
    # Replacements in Main Content
    # 1. Images
    main_content = main_content.replace('src="images/', f'src="<?php echo $path; ?>images/')
    main_content = main_content.replace('url(images/', f'url(<?php echo $path; ?>images/')
    
    # 2. Links
    for old_link, new_link in link_mappings.items():
        # Handle href="old_link"
        main_content = main_content.replace(f'href="{old_link}"', f'href="<?php echo $path; ?>{new_link}"')
        
    # Construct PHP
    php_content = f"""<?php
$path = '{path_prefix}';
$page_title = '{page_title}';
include($path . 'include/head.php');
include($path . 'include/header.php');
?>
{main_content}
<?php
include($path . 'include/footer.php');
?>
{page_scripts}
</body>
</html>
"""

    target_path = os.path.join(base_dir, target_rel_path)
    os.makedirs(os.path.dirname(target_path), exist_ok=True)
    
    with open(target_path, 'w', encoding='utf-8') as f:
        f.write(php_content)
    
    print(f"Processed {filename} -> {target_rel_path}")

for filename, target, prefix in files_to_process:
    process_file(filename, target, prefix)
