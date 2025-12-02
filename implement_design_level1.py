import os
from bs4 import BeautifulSoup

# --- HTML Templates ---

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

PARTNERSHIP_TEMPLATE = """
<div class="section-full p-t80 p-b50 bg-white">
    <div class="container">
        <div class="section-content">
            <div class="row d-flex align-items-center">
                <div class="col-lg-6 col-md-12 m-b30">
                    <div class="section-head text-left">
                        <div class="wt-separator-outer separator-left">
                            <div class="wt-separator">
                                <span class="site-text-primary text-uppercase sep-line-one">Global Expertise</span>
                            </div>
                        </div>
                        <h2 class="text-uppercase">Partnership with GUSU China</h2>
                    </div>
                    <p>PakGusu is proud to partner with GUSU China, a world leader in cleanroom technology. This strategic alliance brings cutting-edge manufacturing capabilities and international standards to our local operations.</p>
                    <p>Together, we deliver world-class cleanroom solutions that meet the most stringent regulatory requirements.</p>
                </div>
                <div class="col-lg-6 col-md-12 m-b30">
                    <div class="wt-media">
                        <img src="../images/gallery/pic1.jpg" alt="Partnership with GUSU China" class="img-responsive"/>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
"""

MISSION_TEMPLATE = """
<div class="section-full p-t80 p-b50 bg-gray">
    <div class="container">
        <div class="section-head text-center">
            <div class="wt-separator-outer separator-center">
                <div class="wt-separator">
                    <span class="site-text-primary text-uppercase sep-line-one">Our Core Values</span>
                </div>
            </div>
            <h2>Mission, Vision & Values</h2>
        </div>
        <div class="row">
            <!-- Mission -->
            <div class="col-md-4 col-sm-6 m-b30">
                <div class="wt-icon-box-wraper center p-lr30 p-b50 p-t50 bg-white">
                    <div class="icon-lg site-text-primary m-b20">
                        <span class="icon-cell"><i class="flaticon-sketch"></i></span>
                    </div>
                    <div class="icon-content">
                        <h4 class="wt-tilte m-b25">Our Mission</h4>
                        <p>To provide superior cleanroom solutions that enhance safety, quality, and efficiency for industries worldwide.</p>
                    </div>
                </div>
            </div>
            <!-- Vision -->
            <div class="col-md-4 col-sm-6 m-b30">
                <div class="wt-icon-box-wraper center p-lr30 p-b50 p-t50 bg-white">
                    <div class="icon-lg site-text-primary m-b20">
                        <span class="icon-cell"><i class="flaticon-window"></i></span>
                    </div>
                    <div class="icon-content">
                        <h4 class="wt-tilte m-b25">Our Vision</h4>
                        <p>To be the global leader in cleanroom technology, recognized for innovation, reliability, and excellence.</p>
                    </div>
                </div>
            </div>
            <!-- Values -->
            <div class="col-md-4 col-sm-6 m-b30">
                <div class="wt-icon-box-wraper center p-lr30 p-b50 p-t50 bg-white">
                    <div class="icon-lg site-text-primary m-b20">
                        <span class="icon-cell"><i class="flaticon-plant"></i></span>
                    </div>
                    <div class="icon-content">
                        <h4 class="wt-tilte m-b25">Our Values</h4>
                        <p>Integrity, Innovation, Quality, and Customer Satisfaction are at the heart of everything we do.</p>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
"""

FACILITY_TEMPLATE = """
<div class="section-full p-t80 p-b50 bg-white">
    <div class="container">
        <div class="section-content">
            <div class="row d-flex align-items-center">
                <div class="col-lg-6 col-md-12 m-b30">
                    <div class="wt-media">
                        <img src="../images/gallery/pic2.jpg" alt="Our Facility" class="img-responsive"/>
                    </div>
                </div>
                <div class="col-lg-6 col-md-12 m-b30">
                    <div class="section-head text-left">
                        <div class="wt-separator-outer separator-left">
                            <div class="wt-separator">
                                <span class="site-text-primary text-uppercase sep-line-one">State-of-the-Art</span>
                            </div>
                        </div>
                        <h2 class="text-uppercase">Our Facility & Capabilities</h2>
                    </div>
                    <p>Our manufacturing facility is equipped with the latest technology to ensure precision and quality. From automated panel production to advanced testing labs, we have the capabilities to handle projects of any scale.</p>
                    <ul class="list-angle-right p-t15 m-b0">
                        <li>Advanced Manufacturing Lines</li>
                        <li>Strict Quality Control</li>
                        <li>High-Volume Production Capacity</li>
                    </ul>
                </div>
            </div>
        </div>
    </div>
</div>
"""

QUALITY_TEMPLATE = """
<div class="section-full p-t80 p-b50 bg-gray">
    <div class="container">
        <div class="section-content">
            <div class="row d-flex align-items-center">
                <div class="col-lg-6 col-md-12 m-b30">
                    <div class="section-head text-left">
                        <div class="wt-separator-outer separator-left">
                            <div class="wt-separator">
                                <span class="site-text-primary text-uppercase sep-line-one">Standards</span>
                            </div>
                        </div>
                        <h2 class="text-uppercase">Quality & Compliance</h2>
                    </div>
                    <p>We adhere to the highest international standards to ensure our cleanroom products meet the rigorous demands of pharmaceutical, healthcare, and industrial sectors.</p>
                    <ul class="list-angle-right p-t15 m-b0">
                        <li>ISO 9001 Certified</li>
                        <li>GMP Compliant Designs</li>
                        <li>Rigorous Testing Protocols</li>
                    </ul>
                </div>
                <div class="col-lg-6 col-md-12 m-b30">
                    <div class="wt-media">
                        <img src="../images/gallery/pic3.jpg" alt="Quality Assurance" class="img-responsive"/>
                    </div>
                </div>
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

    # Find the content after the comment until the next section or end of container
    # This is tricky with BS4 as comments are nodes. 
    # We will look for the next sibling that is a div (the section content)
    
    section_div = start_comment.find_next_sibling('div')
    
    if section_div:
        # Create new soup from template
        new_soup = BeautifulSoup(new_html, 'html.parser')
        # If the template has a root div, use it.
        if new_soup.div:
            section_div.replace_with(new_soup.div)
            print(f"Replaced content for section: {section_name}")
            return True
    
    print(f"Warning: Could not find div following section '{section_name}'")
    return False

def get_section_content(soup, section_name):
    """Extracts the content of a section."""
    for comment in soup.find_all(string=lambda text: isinstance(text, str) and text.strip() == f"Section: {section_name}"):
        section_div = comment.find_next_sibling('div')
        if section_div:
            return section_div
    return None

# --- Main Execution ---

def process_home_page():
    file_path = 'intoriza/index.html'
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    soup = BeautifulSoup(content, 'html.parser')
    
    # Update CTA
    # Note: For Home page, the CTA template needs to use ./ path for images, not ../
    cta_html_home = CTA_TEMPLATE.replace('../', './')
    replace_section(soup, "CTA", cta_html_home)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(str(soup))
    print(f"Updated {file_path}")

def process_about_page():
    file_path = 'intoriza/about/index.html'
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    soup = BeautifulSoup(content, 'html.parser')
    
    # 1. Extract Team Content (currently in Partnership section)
    team_content = get_section_content(soup, "Partnership with GUSU China")
    
    # 2. Replace Partnership Section
    replace_section(soup, "Partnership with GUSU China", PARTNERSHIP_TEMPLATE)
    
    # 3. Replace Mission Section
    replace_section(soup, "Mission, Vision & Values", MISSION_TEMPLATE)
    
    # 4. Replace Facility Section
    replace_section(soup, "Our Facility & Capabilities", FACILITY_TEMPLATE)
    
    # 5. Replace Quality Section
    replace_section(soup, "Quality & Compliance", QUALITY_TEMPLATE)
    
    # 6. Update Leadership Section with extracted Team Content
    if team_content:
        # The extracted content is a Tag object. We can insert it.
        # But first we need to find the placeholder div in Leadership section and replace it.
        leadership_placeholder = get_section_content(soup, "Leadership / Expertise")
        if leadership_placeholder:
            leadership_placeholder.replace_with(team_content)
            print("Moved Team content to Leadership section")
        else:
            print("Warning: Could not find Leadership section to move team content to.")
    
    # 7. Replace CTA Section
    replace_section(soup, "CTA", CTA_TEMPLATE)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(str(soup))
    print(f"Updated {file_path}")

if __name__ == "__main__":
    process_home_page()
    process_about_page()
