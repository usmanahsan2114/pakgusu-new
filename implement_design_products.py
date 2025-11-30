import os
from bs4 import BeautifulSoup

# --- HTML Templates ---

PRODUCT_GRID_TEMPLATE = """
<div class="section-full p-t80 p-b50 bg-white">
    <div class="container">
        <div class="section-head text-center">
            <div class="wt-separator-outer separator-center">
                <div class="wt-separator">
                    <span class="site-text-primary text-uppercase sep-line-one">Our Solutions</span>
                </div>
            </div>
            <h2>Explore Our Products</h2>
        </div>
        <div class="row">
            <!-- Category 1 -->
            <div class="col-md-4 col-sm-6 m-b30">
                <div class="wt-box p-a20 border-1 bg-gray">
                    <div class="wt-media m-b20">
                        <a href="../products/cleanroom-panels/"><img src="../images/gallery/pic1.jpg" alt=""></a>
                    </div>
                    <div class="wt-info">
                        <h4 class="wt-title m-t0"><a href="../products/cleanroom-panels/">Cleanroom Panels</a></h4>
                        <p>High-quality modular panels for sterile environments.</p>
                        <a href="../products/cleanroom-panels/" class="site-button-link">Learn More</a>
                    </div>
                </div>
            </div>
            <!-- Category 2 -->
            <div class="col-md-4 col-sm-6 m-b30">
                <div class="wt-box p-a20 border-1 bg-gray">
                    <div class="wt-media m-b20">
                        <a href="../products/cleanroom-doors/"><img src="../images/gallery/pic2.jpg" alt=""></a>
                    </div>
                    <div class="wt-info">
                        <h4 class="wt-title m-t0"><a href="../products/cleanroom-doors/">Cleanroom Doors</a></h4>
                        <p>Durable and airtight doors for controlled access.</p>
                        <a href="../products/cleanroom-doors/" class="site-button-link">Learn More</a>
                    </div>
                </div>
            </div>
            <!-- Category 3 -->
            <div class="col-md-4 col-sm-6 m-b30">
                <div class="wt-box p-a20 border-1 bg-gray">
                    <div class="wt-media m-b20">
                        <a href="../products/cleanroom-windows/"><img src="../images/gallery/pic3.jpg" alt=""></a>
                    </div>
                    <div class="wt-info">
                        <h4 class="wt-title m-t0"><a href="../products/cleanroom-windows/">Cleanroom Windows</a></h4>
                        <p>Flush-mounted windows for easy cleaning and visibility.</p>
                        <a href="../products/cleanroom-windows/" class="site-button-link">Learn More</a>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
"""

INTEGRATION_TEMPLATE = """
<div class="section-full p-t80 p-b50 bg-gray">
    <div class="container">
        <div class="section-content">
            <div class="row d-flex align-items-center">
                <div class="col-lg-6 col-md-12 m-b30">
                    <div class="section-head text-left">
                        <div class="wt-separator-outer separator-left">
                            <div class="wt-separator">
                                <span class="site-text-primary text-uppercase sep-line-one">Integration</span>
                            </div>
                        </div>
                        <h2 class="text-uppercase">Seamless Integration</h2>
                    </div>
                    <p>Our cleanroom components are designed to work together perfectly. From panels to doors and windows, every element fits precisely to ensure air tightness and structural integrity.</p>
                    <ul class="list-angle-right p-t15 m-b0">
                        <li>Modular Design for Flexibility</li>
                        <li>Easy Installation and Maintenance</li>
                        <li>Compatible with HVAC Systems</li>
                    </ul>
                </div>
                <div class="col-lg-6 col-md-12 m-b30">
                    <div class="wt-media">
                        <img src="../images/gallery/pic4.jpg" alt="Product Integration" class="img-responsive"/>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
"""

CTA_TEMPLATE = """
<div class="section-full p-tb80 bg-center bg-no-repeat bg-cover" style="background-image:url(../images/background/bg-1.jpg);">
    <div class="container">
        <div class="section-content">
            <div class="video-section-full bg-white text-center p-a30">
                <span class="font-18 site-text-primary text-uppercase">Ready to Start?</span>
                <h2 class="wt-tilte m-tb20">Plan Your Cleanroom Project Today</h2>
                <p class="m-b30">Contact our experts to discuss your requirements and get a quote.</p>
                <a href="../contact/" class="site-button">Contact Us</a>
            </div>
        </div>
    </div>
</div>
"""

# --- Helper Functions ---

def replace_section(soup, section_name, new_html):
    """Replaces the content of a section with new HTML."""
    # Find the comment that starts the section
    start_comment = None
    for comment in soup.find_all(string=lambda text: isinstance(text, str) and text.strip() == f"Section: {section_name}"):
        start_comment = comment
        break
    
    if not start_comment:
        print(f"Warning: Section '{section_name}' not found.")
        return False

    section_div = start_comment.find_next_sibling('div')
    
    if section_div:
        new_soup = BeautifulSoup(new_html, 'html.parser')
        if new_soup.div:
            section_div.replace_with(new_soup.div)
            print(f"Replaced content for section: {section_name}")
            return True
    
    print(f"Warning: Could not find div following section '{section_name}'")
    return False

# --- Main Execution ---

def process_products_page():
    file_path = 'intoriza/products/index.html'
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    soup = BeautifulSoup(content, 'html.parser')
    
    # 1. Replace Product Category Grid
    replace_section(soup, "Product Category Grid", PRODUCT_GRID_TEMPLATE)
    
    # 2. Replace How Our Products Integrate
    replace_section(soup, "How Our Products Integrate", INTEGRATION_TEMPLATE)
    
    # 3. Replace CTA
    replace_section(soup, "CTA", CTA_TEMPLATE)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(str(soup))
    print(f"Updated {file_path}")

if __name__ == "__main__":
    process_products_page()
