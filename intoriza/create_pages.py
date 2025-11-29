import os

base_dir = r'c:\xampp\htdocs\pakgusu-new\intoriza'

# Define all product pages
products = {
    'windows': {
        'title': 'Cleanroom Windows',
        'subtitle': 'Crystal Clear Vision',
        'description': 'Our cleanroom windows provide excellent visibility while maintaining the integrity of your controlled environment. Designed with precision engineering and high-quality materials.',
        'features': [
            'Double or triple glazing options',
            'Flush-mounted design for easy cleaning',
            'Non-porous surface prevents contamination',
            'Available in various sizes',
            'Excellent thermal insulation',
            'Impact-resistant construction'
        ]
    },
    'doors': {
        'title': 'Cleanroom Doors',
        'subtitle': 'Secure Access Solutions',
        'description': 'High-performance cleanroom doors engineered for optimal sealing and contamination control. Available in manual, automatic, and hermetic sealing options.',
        'features': [
            'Hermetic sealing technology',
            'Smooth, easy-to-clean surfaces',
            'Manual, sliding, or automatic operation',
            'Interlocking options available',
            'Fire-rated variants',
            'Vision panels available'
        ]
    },
    'transfer-window': {
        'title': 'Transfer Windows',
        'subtitle': 'Efficient Material Transfer',
        'description': 'Our transfer windows (pass boxes) facilitate the safe and contamination-free transfer of materials between cleanroom zones, maintaining pressure differentials.',
        'features': [
            'Interlocking door system',
            'UV sterilization option',
            'HEPA filtration available',
            'Stainless steel construction',
            'Multiple size options',
            'Electronic interlocking controls'
        ]
    },
    'aluminum-profile': {
        'title': 'Aluminum Profiles',
        'subtitle': 'Structural Excellence',
        'description': 'Premium aluminum profiles specifically designed for cleanroom construction. Our profiles provide structural integrity while maintaining aesthetic appeal.',
        'features': [
            'Anodized or powder-coated finish',
            'Corrosion-resistant',
            'Lightweight yet durable',
            'Easy installation',
            'Various profile designs',
            'Compatible with all panel systems'
        ]
    },
    'clean-led-lights': {
        'title': 'Clean LED Lights',
        'subtitle': 'Illumination Solutions',
        'description': 'Energy-efficient LED lighting fixtures designed specifically for cleanroom environments. Our lights provide excellent illumination while maintaining cleanliness standards.',
        'features': [
            'Sealed and gasketed design',
            'Easy to clean surfaces',
            'Low heat emission',
            'Energy-efficient LED technology',
            'Long lifespan (50,000+ hours)',
            'Available in various lux levels'
        ]
    }
}

# Define all service pages
services = {
    'planning-and-design': {
        'title': 'Planning & Design',
        'subtitle': 'Expert Consultation',
        'description': 'Our experienced team provides comprehensive planning and design services for cleanroom facilities. We work closely with clients to create optimal solutions tailored to their specific requirements.',
        'features': [
            'Initial consultation and site survey',
            'Detailed 3D design and layout',
            'Classification and compliance planning',
            'HVAC system design',
            'Cost estimation and budgeting',
            'Regulatory compliance assistance'
        ]
    },
    'clean-room-construction': {
        'title': 'Clean Room Construction',
        'subtitle': 'Professional Installation',
        'description': 'We provide complete turnkey cleanroom construction services, from initial planning to final commissioning. Our skilled technicians ensure quality installation following international standards.',
        'features': [
            'Turnkey project management',
            'Quality material procurement',
            'Professional installation team',
            'On-time project delivery',
            'Strict quality control',
            'Post-installation testing'
        ]
    },
    'installation': {
        'title': 'Installation Services',
        'subtitle': 'Expert Installation',
        'description': 'Our professional installation team ensures that every component is installed perfectly according to specifications and industry standards.',
        'features': [
            'Experienced installation team',
            'Precision installation techniques',
            'Minimal disruption to operations',
            'Complete tool and equipment',
            'Safety compliance',
            'Installation validation'
        ]
    },
    'after-sale-services': {
        'title': 'After-Sale Services',
        'subtitle': 'Ongoing Support',
        'description': 'We provide comprehensive after-sale services to ensure your cleanroom continues to operate at peak performance. Our maintenance and support team is always ready to assist.',
        'features': [
            'Regular maintenance programs',
            '24/7 technical support',
            'Spare parts availability',
            'Performance optimization',
            'Recertification services',
            'Upgrade and modification support'
        ]
    }
}

# Define all sector pages
sectors = {
    'pharmaceutical-nutraceutical': {
        'title': 'Pharmaceutical & Nutraceutical',
        'subtitle': 'GMP Compliant Solutions',
        'description': 'We provide cleanroom solutions specifically designed for the pharmaceutical and nutraceutical industries, meeting cGMP, FDA, and international standards.',
        'features': [
            'GMP compliant design',
            'Validated systems',
            'Sterile manufacturing environments',
            'Particle control solutions',
            'Full documentation support',
            'Regulatory compliance expertise'
        ]
    },
    'hospital': {
        'title': 'Hospital & Healthcare',
        'subtitle': 'Sterile Medical Environments',
        'description': 'Our cleanroom solutions for hospitals ensure the highest standards of hygiene and contamination control for operating rooms, ICUs, and sterile processing areas.',
        'features': [
            'Operating room solutions',
            'ICU and isolation rooms',
            'Sterile processing departments',
            'Dialysis centers',
            'Hospital pharmacies',
            'Infection control design'
        ]
    },
    'food-industry': {
        'title': 'Food Industry',
        'subtitle': 'Food Safety Solutions',
        'description': 'Cleanroom solutions for food processing and packaging facilities that meet HACCP, FDA, and international food safety standards.',
        'features': [
            'HACCP compliant design',
            'Hygienic construction materials',
            'Easy-to-clean surfaces',
            'Contamination prevention',
            'Temperature and humidity control',
            'Product safety assurance'
        ]
    },
    'electronics': {
        'title': 'Electronics Manufacturing',
        'subtitle': 'Precision Environments',
        'description': 'Specialized cleanroom solutions for electronics manufacturing, providing the ultra-clean environments required for semiconductor and electronic component production.',
        'features': [
            'ESD control measures',
            'Ultra-low particle counts',
            'Precision environmental control',
            'Vibration-free design',
            'Class 10 to Class 100,000 rooms',
            'Advanced filtration systems'
        ]
    },
    'laboratories': {
        'title': 'Research Laboratories',
        'subtitle': 'Controlled Research Environments',
        'description': 'Cleanroom solutions for research and testing laboratories requiring precise environmental control and contamination prevention.',
        'features': [
            'Biosafety level compliant',
            'Precise environmental control',
            'Flexible modular design',
            'Easy reconfiguration',
            'Various classification levels',
            'Advanced monitoring systems'
        ]
    },
    'medical-surgical-devices': {
        'title': 'Medical & Surgical Devices',
        'subtitle': 'Sterile Manufacturing',
        'description': 'ISO-compliant cleanroom solutions for the manufacturing and packaging of medical devices and surgical instruments.',
        'features': [
            'ISO 13485 compliant',
            'Sterile manufacturing zones',
            'Quality control areas',
            'Assembly and packaging rooms',
            'Validation support',
            'Full documentation'
        ]
    }
}

def create_product_page(slug, data):
    path = os.path.join(base_dir, 'products', slug, 'index.php')
    os.makedirs(os.path.dirname(path), exist_ok=True)
    
    features_html = '\n'.join([f'                                    <li>{feature}</li>' for feature in data['features']])
    
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
                                    <li><a href="<?php echo $path; ?>products/index.php">Products</a></li>
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
                                <p>{data['description']}</p>
                                
                                <h4>Key Features:</h4>
                                <ul class="list-checked">
{features_html}
                                </ul>
                                
                                <h4>Applications:</h4>
                                <p>Suitable for pharmaceutical facilities, hospitals, food processing units, electronics manufacturing, and research laboratories.</p>
                            </div>
                        </div>
                        
                        <div class="col-lg-4 col-md-12">
                            <aside class="side-bar">
                                <!-- CATEGORY -->
                                <div class="widget bg-white">
                                    <h4 class="widget-title">Products</h4>
                                    <ul class="list-2">
                                        <li><a href="<?php echo $path; ?>products/clean-room-panels/index.php">Clean Room Panels</a></li>
                                        <li><a href="<?php echo $path; ?>products/windows/index.php">Windows</a></li>
                                        <li><a href="<?php echo $path; ?>products/doors/index.php">Doors</a></li>
                                        <li><a href="<?php echo $path; ?>products/transfer-window/index.php">Transfer Window</a></li>
                                        <li><a href="<?php echo $path; ?>products/aluminum-profile/index.php">Aluminum Profile</a></li>
                                        <li><a href="<?php echo $path; ?>products/clean-led-lights/index.php">Clean LED Lights</a></li>
                                    </ul>
                                </div>
                                
                                <!-- CONTACT -->
                                <div class="widget bg-white">
                                    <h4 class="widget-title">Get a Quote</h4>
                                    <p>Interested in this product? Contact us for detailed information and quotation.</p>
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

def create_service_page(slug, data):
    path = os.path.join(base_dir, 'services', slug, 'index.php')
    os.makedirs(os.path.dirname(path), exist_ok=True)
    
    features_html = '\n'.join([f'                                    <li>{feature}</li>' for feature in data['features']])
    
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
                                    <li><a href="<?php echo $path; ?>services/index.php">Services</a></li>
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
                                <p>{data['description']}</p>
                                
                                <h4>What We Offer:</h4>
                                <ul class="list-checked">
{features_html}
                                </ul>
                                
                                <h4>Why Choose Us:</h4>
                                <p>With years of experience and a team of dedicated professionals, we ensure quality service delivery that meets your exact requirements and exceeds expectations.</p>
                            </div>
                        </div>
                        
                        <div class="col-lg-4 col-md-12">
                            <aside class="side-bar">
                                <!-- CATEGORY -->
                                <div class="widget bg-white">
                                    <h4 class="widget-title">Services</h4>
                                    <ul class="list-2">
                                        <li><a href="<?php echo $path; ?>services/planning-and-design/index.php">Planning & Design</a></li>
                                        <li><a href="<?php echo $path; ?>services/clean-room-construction/index.php">Clean Room Construction</a></li>
                                        <li><a href="<?php echo $path; ?>services/installation/index.php">Installation</a></li>
                                        <li><a href="<?php echo $path; ?>services/after-sale-services/index.php">After-Sale Services</a></li>
                                    </ul>
                                </div>
                                
                                <!-- CONTACT -->
                                <div class="widget bg-white">
                                    <h4 class="widget-title">Request Service</h4>
                                    <p>Need our professional services? Get in touch with our team today.</p>
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

def create_sector_page(slug, data):
    path = os.path.join(base_dir, 'sectors', slug, 'index.php')
    os.makedirs(os.path.dirname(path), exist_ok=True)
    
    features_html = '\n'.join([f'                                    <li>{feature}</li>' for feature in data['features']])
    
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
                                    <li><a href="<?php echo $path; ?>sectors/index.php">Sectors</a></li>
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
                                <p>{data['description']}</p>
                                
                                <h4>Our Solutions Include:</h4>
                                <ul class="list-checked">
{features_html}
                                </ul>
                                
                                <h4>Industry Expertise:</h4>
                                <p>Our team has extensive experience in this sector, ensuring that we understand the unique challenges and requirements of your industry.</p>
                            </div>
                        </div>
                        
                        <div class="col-lg-4 col-md-12">
                            <aside class="side-bar">
                                <!-- CATEGORY -->
                                <div class="widget bg-white">
                                    <h4 class="widget-title">Sectors We Serve</h4>
                                    <ul class="list-2">
                                        <li><a href="<?php echo $path; ?>sectors/pharmaceutical-nutraceutical/index.php">Pharmaceutical / Nutraceutical</a></li>
                                        <li><a href="<?php echo $path; ?>sectors/hospital/index.php">Hospital</a></li>
                                        <li><a href="<?php echo $path; ?>sectors/food-industry/index.php">Food Industry</a></li>
                                        <li><a href="<?php echo $path; ?>sectors/electronics/index.php">Electronics</a></li>
                                        <li><a href="<?php echo $path; ?>sectors/laboratories/index.php">Laboratories</a></li>
                                        <li><a href="<?php echo $path; ?>sectors/medical-surgical-devices/index.php">Medical / Surgical Devices</a></li>
                                    </ul>
                                </div>
                                
                                <!-- CONTACT -->
                                <div class="widget bg-white">
                                    <h4 class="widget-title">Discuss Your Project</h4>
                                    <p>Let's discuss how we can help with your cleanroom requirements.</p>
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

# Create all pages
for slug, data in products.items():
    create_product_page(slug, data)

for slug, data in services.items():
    create_service_page(slug, data)

for slug, data in sectors.items():
    create_sector_page(slug, data)

print("\nAll pages created successfully!")
