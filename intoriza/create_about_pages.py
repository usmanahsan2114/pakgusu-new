import os

base_dir = r'c:\xampp\htdocs\pakgusu-new\intoriza\about'

# Define the three about sub-pages
about_pages = {
    'about-pak-gusu': {
        'title': 'About Pak Gusu',
        'subtitle': 'Your Trusted Partner in Pakistan',
        'description': 'Pak Gusu is the premier provider of cleanroom solutions in Pakistan, bringing international standards and cutting-edge technology to local industries. As the authorized partner of Gusu China, we deliver world-class cleanroom products and services tailored to meet the unique needs of Pakistani businesses.',
        'sections': {
            'Our Mission': 'To provide Pakistani industries with state-of-the-art cleanroom solutions that meet international standards, enabling them to compete globally while maintaining the highest levels of quality and compliance.',
            'Our Vision': 'To become Pakistan\'s leading cleanroom solution provider, recognized for excellence, innovation, and unwavering commitment to customer satisfaction.',
            'Our Values': '''- **Quality First:** Never compromising on product quality or service excellence
- **Innovation:** Continuously adopting the latest technologies and best practices
- **Customer Focus:** Understanding and exceeding client expectations
- **Integrity:** Conducting business with honesty and transparency
- **Expertise:** Building and maintaining technical excellence''',
            'Why Choose Us': '''- Authorized partner of Gusu China
- Local presence with international standards
- Complete turnkey solutions
- Experienced technical team
- After-sale support and maintenance
- Competitive pricing
- Timely project delivery'''
        }
    },
    'about-gusu-china': {
        'title': 'About Gusu China',
        'subtitle': 'Global Leader in Cleanroom Technology',
        'description': 'Gusu China is a world-renowned manufacturer of cleanroom equipment and systems, with decades of experience serving industries across the globe. With state-of-the-art manufacturing facilities and a commitment to innovation, Gusu China sets the standard for cleanroom excellence.',
        'sections': {
            'Company Overview': 'Established in 1995, Gusu China has grown from a small manufacturing unit to one of Asia\'s largest cleanroom solution providers. With manufacturing facilities spanning over 200,000 square meters and a workforce of 1,500+ skilled professionals, we serve clients in over 80 countries worldwide.',
            'Manufacturing Excellence': '''Gusu China operates multiple ISO-certified manufacturing facilities equipped with:
- Advanced CNC machinery for precision manufacturing
- Automated production lines
- In-house testing and quality control labs
- Research and development center
- Cleanroom demonstration facilities''',
            'Global Presence': 'With offices and authorized partners in major cities worldwide, Gusu China ensures consistent product quality and reliable service delivery. Our global network includes manufacturing hubs in China, distribution centers in key markets, and technical support teams available 24/7.',
            'Certifications & Standards': '''- ISO 9001:2015 Quality Management
- ISO 14001:2015 Environmental Management
- CE Certification
- FDA Compliance
- cGMP Guidelines
- International cleanroom standards (ISO 14644)'''
        }
    },
    'cleanroom-classifications': {
        'title': 'Cleanroom Classifications',
        'subtitle': 'Understanding Cleanroom Standards',
        'description': 'Cleanrooms are classified according to the number and size of particles permitted per volume of air. Understanding these classifications is crucial for selecting the right cleanroom solution for your specific application.',
        'sections': {
            'ISO 14644-1 Standards': '''The ISO 14644-1 is the international standard for cleanroom classification. Cleanrooms are classified by how clean the air is, based on the number of particles per cubic meter at a specified particle size.

**Classification Table:**

| ISO Class | Particle Count (≥0.5 µm per m³) | Equivalent Fed Std 209E |
|-----------|----------------------------------|-------------------------|
| ISO 1     | 10                               | -                       |
| ISO 2     | 100                              | -                       |
| ISO 3     | 1,000                            | Class 1                 |
| ISO 4     | 10,000                           | Class 10                |
| ISO 5     | 100,000                          | Class 100               |
| ISO 6     | 1,000,000                        | Class 1,000             |
| ISO 7     | -                                | Class 10,000            |
| ISO 8     | -                                | Class 100,000           |''',
            'Applications by Classification': '''**ISO Class 4-5 (Class 10-100):**
- Semiconductor manufacturing
- Pharmaceutical aseptic filling
- Medical device assembly

**ISO Class 6-7 (Class 1,000-10,000):**
- Pharmaceutical packaging
- Medical device manufacturing
- Electronics assembly
- Hospital operating rooms

**ISO Class 8 (Class 100,000):**
- Food and beverage packaging
- Cosmetics manufacturing
- General assembly areas''',
            'Environmental Parameters': '''Beyond particle count, cleanrooms must control:

**Temperature:** Typically 20-22°C (±2°C)
**Humidity:** Usually 45-55% RH (±5%)
**Pressure:** Positive differential of 10-15 Pa
**Air Changes:** 15-20 per hour (ISO 7-8) to 400-600 per hour (ISO 5)
**HEPA Filtration:** 99.97% efficiency at 0.3 µm'''
        }
    }
}

def create_about_subpage(slug, data):
    path = os.path.join(base_dir, slug, 'index.php')
    os.makedirs(os.path.dirname(path), exist_ok=True)
    
    sections_html = ''
    for heading, content in data['sections'].items():
        sections_html += f'''
                                <h4>{heading}</h4>
                                <p>{content.replace(chr(10), '<br>')}</p>
'''
    
    content = f'''<?php
$path = '../../';
$page_title = '{data['title']}';
include($path . 'include/head.php');
include($path . 'include/header.php');
?>

        <!-- CONTENT START -->
        <div class="page-content">
        
            <!-- INNER PAGE BANNER -->
            <div class="wt-bnr-inr overlay-wraper bg-center" style="background-image:url(<?php echo $path; ?>images/banner/1.jpg);">
            	<div class="overlay-main bg-black opacity-07"></div>
                <div class="container">
                    <div class="wt-bnr-inr-entry">
                    	<div class="banner-title-outer">
                        	<div class="banner-title-name">
                        		<h2 class="text-white">{data['title']}</h2>
                            </div>
                        </div>
                        <!-- BREADCRUMB ROW -->                            
                            <div>
                                <ul class="wt-breadcrumb breadcrumb-style-2">
                                    <li><a href="<?php echo $path; ?>index.php">Home</a></li>
                                    <li><a href="<?php echo $path; ?>about/index.php">About</a></li>
                                    <li>{data['title']}</li>
                                </ul>
                            </div>
                        <!-- BREADCRUMB ROW END -->                        
                    </div>
                </div>
            </div>
            <!-- INNER PAGE BANNER END -->
            
            <!-- CONTENT SECTION START -->
            <div class="section-full p-t80 p-b50 bg-white">
                <div class="container">
                    <div class="row">
                        <div class="col-lg-8 col-md-12">
                            <!-- TITLE START -->
                            <div class="section-head">
                                <div class="wt-separator-outer separator-left">
                                    <div class="wt-separator">
                                        <span class="site-text-primary text-uppercase sep-line-one">{data['subtitle']}</span>
                                    </div>
                                </div>
                                <h2>{data['title']}</h2>
                            </div>
                            <!-- TITLE END -->
                            
                            <div class="wt-post-text">
                                <p><strong>{data['description']}</strong></p>
                                {sections_html}
                            </div>
                        </div>
                         
                        <div class="col-lg-4 col-md-12">
                            <aside class="side-bar">
                                <!-- CATEGORY -->
                                <div class="widget bg-white">
                                    <h4 class="widget-title">About Us</h4>
                                    <ul class="list-2">
                                        <li><a href="<?php echo $path; ?>about/index.php">Company Overview</a></li>
                                        <li><a href="<?php echo $path; ?>about/about-pak-gusu/index.php">About Pak Gusu</a></li>
                                        <li><a href="<?php echo $path; ?>about/about-gusu-china/index.php">About Gusu China</a></li>
                                        <li><a href="<?php echo $path; ?>about/cleanroom-classifications/index.php">Cleanroom Classifications</a></li>
                                    </ul>
                                </div>
                                
                                <!-- CONTACT -->
                                <div class="widget bg-white">
                                    <h4 class="widget-title">Get In Touch</h4>
                                    <p>Have questions about our company or services? We're here to help.</p>
                                    <a href="<?php echo $path; ?>contact/index.php" class="site-button">Contact Us</a>
                                </div>
                            </aside>
                        </div>
                    </div>
                </div>
            </div>
            <!-- CONTENT SECTION END -->
            
        </div>
        <!-- CONTENT END -->

<?php
include($path . 'include/footer.php');
?>

</body>
</html>
'''
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Created: {path}")

# Create all about sub-pages
for slug, data in about_pages.items():
    create_about_subpage(slug, data)

print("\nAll about sub-pages created successfully!")
