import os
import re

# Base content from index.html (Source of Truth)
# We use a template where './' is the placeholder for relative path prefix
FOOTER_TEMPLATE = """    <!-- FOOTER START -->
    <footer class="site-footer footer-large footer-light footer-wide">
        <!-- FOOTER MAIN BLOCK -->
        <div id="footer-main-section" class="footer-top">
            <div class="container">
                
                <!-- 1. Top Navigation Row -->
                <div class="footer-link text-center">
                    <ul>
                        <li><a href="{prefix}about/">About</a></li>
                        <li><a href="{prefix}products/">Products</a></li>
                        <li><a href="{prefix}resources/blog/">Blog</a></li>
                        <li><a href="{prefix}case-studies/">Case Studies</a></li>
                        <li><a href="{prefix}careers/">Careers</a></li>
                        <li><a href="{prefix}contact/">Contact Us</a></li>
                    </ul>
                </div>

                <!-- 2. Main Content Grid (3 Columns) -->
                <div class="row">
                    <!-- Get In Touch -->
                    <div class="col-lg-4 col-md-4 text-center">
                        <div class="widget getin-touch">
                            <h4 class="widget-title">Get In Touch</h4>
                            <div class="widget-section">
                                <ul>
                                    <li><a href="mailto:info@pakgusu.com">info@pakgusu.com</a></li>
                                    <li><a href="tel:+923218073738">+92 321 8073738</a></li>
                                </ul>
                            </div>
                        </div>
                    </div>
                    
                    <!-- Address -->
                    <div class="col-lg-4 col-md-4 text-center">
                        <div class="widget widget_address">
                            <h4 class="widget-title">Address</h4>
                            <div class="widget-section">
                                <ul>
                                    <li>8-Km, Sundar-Raiwand Road,<br>Lahore, Pakistan</li>
                                </ul>
                            </div>
                        </div>
                    </div>
                    
                    <!-- More Links -->
                    <div class="col-lg-4 col-md-4 text-center">
                        <div class="widget">
                            <h4 class="widget-title">More Links</h4>
                            <div class="widget-section">
                                <ul>
                                    <li><a href="{prefix}about/">Terms &amp; Conditions</a></li>
                                    <li><a href="{prefix}resources/cleanroom-standards-classifications/">Privacy Policy</a></li>
                                </ul>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- 3. Social Icons Row (New Layout) -->
                <div class="row m-t30">
                    <div class="col-12 text-center">
                        <div class="new-footer-social-icon">
                            <ul>
                                <li><a href="https://linkedin.com/company/pakgusu" target="_blank" aria-label="LinkedIn"><i class="fa fa-linkedin"></i></a></li>
                                <li><a href="https://youtube.com/@pakgusu" target="_blank" aria-label="YouTube"><i class="fa fa-youtube-play"></i></a></li>
                                <li><a href="https://twitter.com/pakgusu" target="_blank" aria-label="Twitter"><i class="fa fa-twitter"></i></a></li>
                                <li><a href="https://facebook.com/pakgusu" target="_blank" aria-label="Facebook"><i class="fa fa-facebook"></i></a></li>
                                <li><a href="https://instagram.com/pakgusu" target="_blank" aria-label="Instagram"><i class="fa fa-instagram"></i></a></li>
                                <li><a href="https://threads.net/@pakgusu" target="_blank" aria-label="Threads"><i class="fa fa-at"></i></a></li>
                            </ul>
                        </div>
                    </div>
                </div>

            </div>
        </div>

        <!-- FOOTER BOTTOM COPYRIGHT -->
        <div id="footer-bottom-section" class="footer-bottom">
            <div class="container">
                <div class="row">
                    <div class="col-md-6 text-left">
                        <span class="copyrights-text">© 2025 by <a href="https://pakgusu.com/" rel="noopener" target="_blank">PakGusu</a></span>
                    </div>
                    <div class="col-md-6 text-right">
                        <span class="copyrights-text">
                            Designed by <a href="https://www.apexitsolutions.co/" rel="noopener" target="_blank">Apex IT Solutions</a> | 
                            <a href="https://apexmarketings.com/" rel="noopener" target="_blank">Apex Marketings</a>
                        </span>
                    </div>
                </div>
            </div>
        </div>
    </footer>
    <!-- FOOTER END -->"""

def update_footer_in_files(root_dir):
    # Regex to find existing footer block
    footer_regex = re.compile(r'<!-- FOOTER START -->.*?<!-- FOOTER END -->', re.DOTALL)
    
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.endswith('.html'):
                filepath = os.path.join(dirpath, filename)
                
                # Calculate relative path prefix
                rel_path = os.path.relpath(filepath, root_dir)
                depth = rel_path.count(os.sep)
                
                # If file is index.html at root, simple ./
                if rel_path == 'index.html':
                     prefix = './'
                else:
                    # For subdirectories: ../ for each level deep
                    # e.g. about/index.html -> ../
                    # products/cleanroom-panels/index.html -> ../../
                    prefix = '../' * depth
                
                # Generate new footer for this file
                new_footer = FOOTER_TEMPLATE.format(prefix=prefix)
                
                # Read content with fallback encoding
                try:
                    with open(filepath, 'r', encoding='utf-8') as f:
                        content = f.read()
                except UnicodeDecodeError:
                    with open(filepath, 'r', encoding='latin-1') as f:
                        content = f.read()
                
                # Check if file has footer to replace
                if '<!-- FOOTER START -->' in content:
                    # Replace
                    new_content = footer_regex.sub(new_footer, content)
                    
                    # Write back (always as utf-8)
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    print(f"Updated: {rel_path} (Prefix: {prefix})")
                else:
                    print(f"Skipped (No Footer): {rel_path}")

if __name__ == "__main__":
    # Assuming script is run from project root or we point to it
    # Agent typically runs from CWD which might be root
    # We will hardcode the path based on user environment
    ROOT_DIR = r"c:\xampp\htdocs\pakgusu-1\intoriza\pakgusu-new\intoriza"
    update_footer_in_files(ROOT_DIR)
