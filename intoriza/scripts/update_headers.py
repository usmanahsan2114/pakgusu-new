import os
import re

# Template of the New Header (Copied from index.html)
# Used {{ROOT}} as a placeholder for the relative path prefix (e.g., "./" or "../../")
HEADER_TEMPLATE = """        <!-- HEADER START -->
        <header class="gh-site-header">
            <div class="gh-bg-anim"></div>
            <div class="gh-container">
                <!-- Mobile Toggle -->
                <button class="gh-mobile-toggle" aria-label="Toggle Menu">
                    <div class="gh-bar"></div>
                    <div class="gh-bar"></div>
                    <div class="gh-bar"></div>
                </button>

                <!-- Logo -->
                <div class="gh-logo">
                    <a href="{{ROOT}}">
                        <img src="{{ROOT}}images/logo-dark.png" alt="PakGusu Intoriza">
                    </a>
                </div>

                <!-- Desktop Nav -->
                <nav class="gh-nav-desktop">
                    <ul class="gh-nav-list">
                        <li class="gh-nav-item"><a href="{{ROOT}}" class="gh-nav-link">Home</a></li>
                        <li class="gh-nav-item"><a href="{{ROOT}}about/" class="gh-nav-link">About Us</a></li>
                        <li class="gh-nav-item">
                            <a href="javascript:;" class="gh-nav-link">Products <i class="fa fa-angle-down m-l5"></i></a>
                            <div class="gh-dropdown">
                                <a href="{{ROOT}}products/cleanroom-panels/" class="gh-dropdown-link">Cleanroom Panels</a>
                                <a href="{{ROOT}}products/cleanroom-windows/" class="gh-dropdown-link">Cleanroom Windows</a>
                                <a href="{{ROOT}}products/cleanroom-doors/" class="gh-dropdown-link">Cleanroom Doors</a>
                                <a href="{{ROOT}}products/pass-through-chambers/" class="gh-dropdown-link">Pass-Through Chambers</a>
                                <a href="{{ROOT}}products/aluminum-profiles/" class="gh-dropdown-link">Aluminum Profiles</a>
                                <a href="{{ROOT}}products/cleanroom-led-lights/" class="gh-dropdown-link">Cleanroom LED Lights</a>
                            </div>
                        </li>
                        <li class="gh-nav-item"><a href="{{ROOT}}services/" class="gh-nav-link">Services</a></li>
                        <li class="gh-nav-item">
                            <a href="javascript:;" class="gh-nav-link">Industries <i class="fa fa-angle-down m-l5"></i></a>
                            <div class="gh-dropdown">
                                <a href="{{ROOT}}industries/pharmaceutical-nutraceutical/" class="gh-dropdown-link">Pharmaceutical & Nutraceutical</a>
                                <a href="{{ROOT}}industries/healthcare-hospitals/" class="gh-dropdown-link">Healthcare & Hospitals</a>
                                <a href="{{ROOT}}industries/food-beverage/" class="gh-dropdown-link">Food & Beverage</a>
                                <a href="{{ROOT}}industries/electronics-manufacturing/" class="gh-dropdown-link">Electronics Manufacturing</a>
                                <a href="{{ROOT}}industries/laboratories-rnd/" class="gh-dropdown-link">Laboratories & R&D</a>
                                <a href="{{ROOT}}industries/medical-surgical-devices/" class="gh-dropdown-link">Medical & Surgical Devices</a>
                            </div>
                        </li>
                        <li class="gh-nav-item">
                            <a href="javascript:;" class="gh-nav-link">Resources <i class="fa fa-angle-down m-l5"></i></a>
                            <div class="gh-dropdown">
                                <a href="{{ROOT}}resources/cleanroom-standards-classifications/" class="gh-dropdown-link">Cleanroom Standards</a>
                                <a href="{{ROOT}}resources/blog/" class="gh-dropdown-link">Blog</a>
                                <a href="{{ROOT}}resources/news-events/" class="gh-dropdown-link">News & Events</a>
                                <a href="{{ROOT}}resources/faqs/" class="gh-dropdown-link">FAQs</a>
                            </div>
                        </li>
                        <li class="gh-nav-item"><a href="{{ROOT}}contact/" class="gh-nav-link">Contact</a></li>
                    </ul>
                </nav>

                <!-- Right Actions -->
                <div class="gh-actions">
                    <!-- Dark Mode Toggle -->
                    <button class="gh-action-btn" data-action="theme-toggle" aria-label="Toggle Dark Mode">
                        <i class="fa fa-moon-o"></i>
                    </button>
                    <!-- Existing Contact Arrow Func -->
                    <button class="gh-action-btn contact-slide-show" aria-label="Open Contact Panel">
                        <i class="fa fa-angle-left"></i>
                    </button>
                </div>
            </div>
            
            <!-- Mobile Menu Panel -->
            <div class="gh-mobile-menu">
                <ul class="gh-mobile-list">
                    <li class="gh-mobile-item"><a href="{{ROOT}}" class="gh-mobile-link">Home</a></li>
                    <li class="gh-mobile-item"><a href="{{ROOT}}about/" class="gh-mobile-link">About Us</a></li>
                    <li class="gh-mobile-item">
                        <div class="gh-mobile-link-wrapper" style="display:flex; justify-content:space-between; align-items:center;">
                            <a href="javascript:;" class="gh-mobile-link" style="flex:1;">Products</a>
                            <button class="gh-submenu-toggle"><i class="fa fa-angle-down"></i></button>
                        </div>
                        <div class="gh-mobile-submenu">
                            <a href="{{ROOT}}products/cleanroom-panels/" class="gh-mobile-submenu-link">Cleanroom Panels</a>
                            <a href="{{ROOT}}products/cleanroom-windows/" class="gh-mobile-submenu-link">Cleanroom Windows</a>
                            <a href="{{ROOT}}products/cleanroom-doors/" class="gh-mobile-submenu-link">Cleanroom Doors</a>
                            <a href="{{ROOT}}products/pass-through-chambers/" class="gh-mobile-submenu-link">Pass-Through Chambers</a>
                            <a href="{{ROOT}}products/aluminum-profiles/" class="gh-mobile-submenu-link">Aluminum Profiles</a>
                            <a href="{{ROOT}}products/cleanroom-led-lights/" class="gh-mobile-submenu-link">Cleanroom LED Lights</a>
                        </div>
                    </li>
                    <li class="gh-mobile-item"><a href="{{ROOT}}services/" class="gh-mobile-link">Services</a></li>
                    <li class="gh-mobile-item">
                        <div class="gh-mobile-link-wrapper" style="display:flex; justify-content:space-between; align-items:center;">
                            <a href="javascript:;" class="gh-mobile-link" style="flex:1;">Industries</a>
                            <button class="gh-submenu-toggle"><i class="fa fa-angle-down"></i></button>
                        </div>
                        <div class="gh-mobile-submenu">
                            <a href="{{ROOT}}industries/pharmaceutical-nutraceutical/" class="gh-mobile-submenu-link">Pharmaceutical & Nutraceutical</a>
                            <a href="{{ROOT}}industries/healthcare-hospitals/" class="gh-mobile-submenu-link">Healthcare & Hospitals</a>
                            <a href="{{ROOT}}industries/food-beverage/" class="gh-mobile-submenu-link">Food & Beverage</a>
                            <a href="{{ROOT}}industries/electronics-manufacturing/" class="gh-mobile-submenu-link">Electronics Manufacturing</a>
                            <a href="{{ROOT}}industries/laboratories-rnd/" class="gh-mobile-submenu-link">Laboratories & R&D</a>
                            <a href="{{ROOT}}industries/medical-surgical-devices/" class="gh-mobile-submenu-link">Medical & Surgical Devices</a>
                        </div>
                    </li>
                    <li class="gh-mobile-item">
                        <div class="gh-mobile-link-wrapper" style="display:flex; justify-content:space-between; align-items:center;">
                            <a href="javascript:;" class="gh-mobile-link" style="flex:1;">Resources</a>
                            <button class="gh-submenu-toggle"><i class="fa fa-angle-down"></i></button>
                        </div>
                        <div class="gh-mobile-submenu">
                            <a href="{{ROOT}}resources/cleanroom-standards-classifications/" class="gh-mobile-submenu-link">Standards</a>
                            <a href="{{ROOT}}resources/blog/" class="gh-mobile-submenu-link">Blog</a>
                            <a href="{{ROOT}}resources/news-events/" class="gh-mobile-submenu-link">News & Events</a>
                            <a href="{{ROOT}}resources/faqs/" class="gh-mobile-submenu-link">FAQs</a>
                        </div>
                    </li>
                    <li class="gh-mobile-item"><a href="{{ROOT}}contact/" class="gh-mobile-link">Contact</a></li>
                </ul>
            </div>
            
            <!-- Mobile Overlay -->
            <div class="gh-overlay"></div>
            
            <!-- KEEP EXISTING CONTACT SLIDE DRAWER UNCHANGED - IT IS TRIGGERED BY .contact-slide-show -->
            <!-- Contact Nav -->
            <div class="contact-slide-hide">
                <div class="contact-nav">
                    <a class="contact_close" href="javascript:void(0)">×</a>
                    <div class="contact-nav-form p-a30">
                        <form action="form-handler.php" class="cons-contact-form" method="post">
                            <div class="m-b30">
                                <!-- TITLE START -->
                                <div class="section-head text-left">
                                    <h4 class="m-b5">Get In Touch</h4>
                                </div>
                                <!-- TITLE END -->
                                <div class="input input-animate">
                                    <label for="name">Name</label>
                                    <input id="name" name="username" required="" type="text" />
                                    <span class="spin"></span>
                                </div>
                                <div class="input input-animate">
                                    <label for="email">Email</label>
                                    <input id="email" name="email" required="" type="email" />
                                    <span class="spin"></span>
                                </div>
                                <div class="input input-animate">
                                    <label for="message">Textarea</label>
                                    <textarea id="message" name="message" required=""></textarea>
                                    <span class="spin"></span>
                                </div>
                                <div class="text-right">
                                    <button class="btn-half site-button m-b15" name="submit" type="submit"
                                        value="Submit">
                                        <span>Submit</span>
                                    </button>
                                </div>
                            </div>
                        </form>
                        <div class="contact-info text-black m-b30">
                            <!-- TITLE START -->
                            <div class="section-head text-left">
                                <h4 class="m-b5">Contact Info</h4>
                            </div>
                            <!-- TITLE END -->
                            <div class="wt-icon-box-wraper left p-b40 icon-shake-outer">
                                <div class="icon-xs"><i class="flaticon-smartphone icon-shake"></i></div>
                                <div class="icon-content">
                                    <h5 class="m-t0 font-weight-500">Phone number</h5>
                                    <p>92 321 8073738</p>
                                </div>
                            </div>
                            <div class="wt-icon-box-wraper left p-b40 icon-shake-outer">
                                <div class="icon-xs"><i class="flaticon-email icon-shake"></i></div>
                                <div class="icon-content">
                                    <h5 class="m-t0 font-weight-500">Email address</h5>
                                    <p>info@pakgusu.com</p>
                                </div>
                            </div>
                            <div class="wt-icon-box-wraper left icon-shake-outer">
                                <div class="icon-xs"><i class="flaticon-placeholder icon-shake"></i></div>
                                <div class="icon-content">
                                    <h5 class="m-t0 font-weight-500">Address info</h5>
                                    <p>8-Km, Sundar-Raiwand Road, Lahore, Pakistan</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </header>
        <!-- HEADER END -->"""

ROOT_DIR = r"c:\xampp\htdocs\pakgusu-1\intoriza\pakgusu-new\intoriza"

def get_relative_root(file_path):
    # Calculate depth relative to ROOT_DIR
    rel_path = os.path.relpath(file_path, ROOT_DIR)
    depth = rel_path.count(os.sep)
    if depth == 0:
        return "./"
    return "../" * depth

def update_file(file_path):
    print(f"Processing: {file_path}")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Determine Correct Path Prefix
    root_prefix = get_relative_root(file_path)
    
    # 1. Update CSS Link
    css_link = f'<link href="{root_prefix}css/header-master.css" rel="stylesheet" />'
    if 'header-master.css' not in content:
        # Insert before </head>
        content = content.replace('</head>', f'    {css_link}\n</head>')
    
    # 2. Update JS Script
    js_script = f'<script src="{root_prefix}js/header-custom.js"></script>'
    if 'header-custom.js' not in content:
        # Insert before </body>
        content = content.replace('</body>', f'    {js_script}\n</body>')

    # 3. Replace Header Block
    # Regex to find <header ...> ... </header>
    # Note: Using non-greedy match including newlines
    header_pattern = re.compile(r'<header[^>]*>.*?</header>', re.DOTALL)
    
    # Prepare New Header Template with Correct Paths
    new_header = HEADER_TEMPLATE.replace('{{ROOT}}', root_prefix)
    
    # Perform Replacement
    if header_pattern.search(content):
        content = header_pattern.sub(new_header, content)
    else:
        print(f"WARNING: No header found in {file_path}")
        return

    # Write Back
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("  -> Updated.")

def main():
    skip_files = ['header_template.html'] # Skip utility files if any

    for root, dirs, files in os.walk(ROOT_DIR):
        for file in files:
            if file.endswith(".html") and file not in skip_files:
                full_path = os.path.join(root, file)
                # Ensure we don't double-process index.html (though idempotency is good)
                # But index.html is essentially the source, so we can self-update it
                # to ensure it strictly follows the template logic too
                update_file(full_path)

if __name__ == "__main__":
    main()
