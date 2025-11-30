import os
from bs4 import BeautifulSoup

# ==========================================
# CONTENT DATA
# ==========================================

CONTENT_UPDATES = [
    # --- HOME ---
    {
        "file": "intoriza/index.html",
        "updates": [
            {"section": "Who We Are", "selector": ".section-head h2", "text": "Turnkey Cleanroom Solutions in Pakistan"},
            {"section": "Who We Are", "selector": ".section-head p", "html": """PakGusu Technology (Pvt) Ltd is a leading <strong>cleanroom manufacturer in Pakistan</strong>, delivering turnkey <strong>modular cleanroom solutions</strong> for pharmaceutical, healthcare, electronics, food, and research industries. Backed by our strategic partnership with <strong>GUSU Purification (China)</strong>, we combine global cleanroom expertise with local manufacturing and on-ground support."""},
            {"section": "Our Solutions", "selector": ".section-head h2", "text": "Build World-Class Modular Cleanrooms Locally"},
            {"section": "Our Solutions", "selector": ".section-head .site-text-primary", "text": "Our Expertise"},
            {"section": "Our Solutions", "action": "insert_after_header", "html": """<p class="text-center m-b30">We design, manufacture, and install complete cleanroom systems – from insulated wall panels and doors to lighting and pass-through chambers. Our solutions are engineered to meet <strong>ISO 14644-1 cleanroom classes</strong> and <strong>GMP guidelines</strong>, helping you pass audits with confidence and protect your products, patients, and processes.</p>"""}
        ]
    },
    # --- ABOUT ---
    {
        "file": "intoriza/about/index.html",
        "updates": [
            {"section": "Company Snapshot", "selector": ".section-head h2", "text": "About PakGusu – Cleanroom Manufacturer in Pakistan"},
            {"section": "Company Snapshot", "selector": ".section-head .site-text-primary", "text": "Who We Are"},
            {"section": "Company Snapshot", "selector": ".col-lg-5 p", "html": """<strong>PakGusu Technology (Pvt) Ltd</strong> is a specialized <strong>cleanroom solution provider</strong> based in Lahore, Pakistan. We design, manufacture, and install <strong>modular cleanroom systems</strong> that meet international standards for cleanliness, safety, and regulatory compliance."""},
            {"section": "Our Story & Timeline", "selector": ".section-head h2", "text": "Our Story"},
            {"section": "Partnership with GUSU China", "selector": ".section-head h2", "text": "Partnership with GUSU China"},
            {"section": "Partnership with GUSU China", "selector": ".col-lg-6 p", "html": """PakGusu is proud to partner with GUSU China, a world leader in cleanroom technology. This strategic alliance brings cutting-edge manufacturing capabilities and international standards to our local operations.<br><br>Together, we deliver world-class cleanroom solutions that meet the most stringent regulatory requirements."""},
            {"section": "Mission, Vision & Values", "selector": ".section-head h2", "text": "Mission, Vision & Values"},
            {"section": "Our Facility & Capabilities", "selector": ".section-head h2", "text": "Our Facility & Capabilities"},
            {"section": "Quality & Compliance", "selector": ".section-head h2", "text": "Quality & Compliance"}
        ]
    },
    # --- PRODUCTS MAIN ---
    {
        "file": "intoriza/products/index.html",
        "updates": [
            {"section": "Overview", "selector": ".section-head h2", "text": "Cleanroom Products & Modular Components"},
            {"section": "Overview", "selector": ".section-head p", "html": """PakGusu manufactures a complete range of <strong>cleanroom components</strong> that work together to form robust, modular cleanroom systems. All products are designed for easy installation, reliable performance, and compatibility with <strong>ISO-classified cleanroom</strong> environments."""}
        ]
    },
    # --- PRODUCTS SUB-PAGES ---
    {
        "file": "intoriza/products/cleanroom-panels/index.html",
        "updates": [
            {"section": "Panel Types / Options", "selector": ".section-head h2", "text": "Cleanroom Panels – Modular Wall & Ceiling Systems"},
            {"section": "Panel Types / Options", "selector": ".section-head p", "html": """PakGusu <strong>cleanroom panels</strong> are engineered to create airtight, thermally stable, and easy-to-clean walls and ceilings for ISO 5–8 cleanrooms. Using locally manufactured panels reduces lead time and provides excellent value without sacrificing performance."""},
            # Update the "Project Details" text area with Panel Construction info
            {"section": "Overview", "selector": ".project-detail-containt", "html": """
                <div class="bg-white text-black">
                    <div class="row">
                        <div class="col-md-12 col-sm-12">
                            <h4 class="m-b15">Panel Construction</h4>
                            <p>Each panel is precision-engineered for performance and durability:</p>
                            <ul class="list-angle-right">
                                <li><strong>Core:</strong> High-density PU, XPS, or Rockwool insulation selected according to fire rating and thermal requirements.</li>
                                <li><strong>Skins:</strong> Powder-coated GI steel or stainless steel with a smooth, non-shedding finish resistant to cleaning agents.</li>
                                <li><strong>Edges:</strong> Designed for tight tongue-and-groove or cam-lock joints with concealed fasteners, ensuring a flush interior surface.</li>
                            </ul>
                            <h4 class="m-t20 m-b15">Applications</h4>
                            <ul class="list-check-circle primary m-b0">
                                <li>Pharmaceutical production suites</li>
                                <li>Hospital pharmacies and operating theatres</li>
                                <li>Food processing rooms and packaging lines</li>
                                <li>Electronics and semiconductor assembly areas</li>
                            </ul>
                        </div>
                    </div>
                </div>
            """},
            # Remove or update the "Client/Date" block. For now, let's replace it with a summary box.
            {"section": "Overview", "selector": ".product-block", "html": """
                    <div class="row">
                        <div class="col-md-6 col-sm-6 m-b30">
                            <h4 class="m-b10">Material</h4>
                            <p>GI Steel / Stainless Steel</p>
                        </div>
                        <div class="col-md-6 col-sm-6 m-b30">
                            <h4 class="m-b10">Insulation</h4>
                            <p>PU / Rockwool / XPS</p>
                        </div>
                        <div class="col-md-6 col-sm-6 m-b30">
                            <h4 class="m-b10">Thickness</h4>
                            <p>50mm / 75mm / 100mm</p>
                        </div>
                        <div class="col-md-6 col-sm-6 m-b30">
                            <h4 class="m-b10">Fire Rating</h4>
                            <p>B1 / A2 Available</p>
                        </div>
                    </div>
            """}
        ]
    },
    {
        "file": "intoriza/products/cleanroom-windows/index.html",
        "updates": [
            {"section": "Window Types / Options", "selector": ".section-head h2", "text": "Cleanroom Windows"},
            {"section": "Window Types / Options", "selector": ".section-head p", "html": """PakGusu <strong>cleanroom windows</strong> are fully flush with wall panels, enabling visibility between areas without compromising cleanliness. Features include double-glazed safety glass and flush frames to eliminate dust traps."""},
            {"section": "Overview", "selector": ".project-detail-containt", "html": """
                <div class="bg-white text-black">
                    <div class="row">
                        <div class="col-md-12 col-sm-12">
                            <h4 class="m-b15">Key Benefits</h4>
                            <ul class="list-angle-right">
                                <li><strong>Flush Design:</strong> Fully flush with wall panels to eliminate ledges and dust accumulation.</li>
                                <li><strong>Double Glazing:</strong> High-quality safety glass for durability and sound insulation.</li>
                                <li><strong>Integrated Blinds:</strong> Optional magnetic or motorized blinds for privacy.</li>
                                <li><strong>Airtight:</strong> Sealed construction to maintain room pressure differentials.</li>
                            </ul>
                        </div>
                    </div>
                </div>
            """},
            {"section": "Overview", "selector": ".product-block", "action": "remove"}
        ]
    },
    {
        "file": "intoriza/products/cleanroom-doors/index.html",
        "updates": [
            {"section": "Door Types / Options", "selector": ".section-head h2", "text": "Cleanroom Doors"},
            {"section": "Door Types / Options", "selector": ".section-head p", "html": """Our <strong>cleanroom doors</strong> provide reliable sealing, robustness, and high-frequency usage capability. Available in swing and sliding variants with smooth, non-porous surfaces for easy cleaning."""},
            {"section": "Overview", "selector": ".project-detail-containt", "html": """
                <div class="bg-white text-black">
                    <div class="row">
                        <div class="col-md-12 col-sm-12">
                            <h4 class="m-b15">Key Benefits</h4>
                            <ul class="list-angle-right">
                                <li><strong>Hygienic Surface:</strong> Smooth, non-porous finish resistant to disinfectants.</li>
                                <li><strong>Sealing:</strong> Perimeter gaskets and drop seals to ensure airtightness.</li>
                                <li><strong>Interlocks:</strong> Optional mechanical or electronic interlocking for airlocks.</li>
                                <li><strong>Variety:</strong> Swing, sliding, and rapid roll-up options available.</li>
                            </ul>
                        </div>
                    </div>
                </div>
            """},
            {"section": "Overview", "selector": ".product-block", "action": "remove"}
        ]
    },
    {
        "file": "intoriza/products/pass-through-chambers/index.html",
        "updates": [
            {"section": "Chamber Types / Options", "selector": ".section-head h2", "text": "Pass-Through Chambers"},
            {"section": "Chamber Types / Options", "selector": ".section-head p", "html": """PakGusu <strong>pass-through chambers</strong> (transfer windows) help move materials between rooms while maintaining cleanliness and pressure balance. Featuring mechanical or electronic interlocks."""},
            {"section": "Overview", "selector": ".project-detail-containt", "html": """
                <div class="bg-white text-black">
                    <div class="row">
                        <div class="col-md-12 col-sm-12">
                            <h4 class="m-b15">Key Benefits</h4>
                            <ul class="list-angle-right">
                                <li><strong>Interlocking Doors:</strong> Prevents cross-contamination by ensuring only one door opens at a time.</li>
                                <li><strong>Easy Cleaning:</strong> Stainless steel interior with coved corners.</li>
                                <li><strong>Options:</strong> Available with HEPA filtration, UV lights, or air showers.</li>
                            </ul>
                        </div>
                    </div>
                </div>
            """},
            {"section": "Overview", "selector": ".product-block", "action": "remove"}
        ]
    },
    {
        "file": "intoriza/products/aluminum-profiles/index.html",
        "updates": [
            {"section": "Profile Types / Options", "selector": ".section-head h2", "text": "Aluminum Profiles"},
            {"section": "Profile Types / Options", "selector": ".section-head p", "html": """Our <strong>aluminum profile systems</strong> are the structural backbone of the modular cleanroom. Includes extruded profiles for wall, ceiling, and floor junctions, and cove profiles to eliminate 90° corners."""},
            {"section": "Overview", "selector": ".project-detail-containt", "html": """
                <div class="bg-white text-black">
                    <div class="row">
                        <div class="col-md-12 col-sm-12">
                            <h4 class="m-b15">Key Benefits</h4>
                            <ul class="list-angle-right">
                                <li><strong>Hygienic Junctions:</strong> Coving profiles eliminate sharp corners where dirt can accumulate.</li>
                                <li><strong>Durable:</strong> Anodized or powder-coated aluminum for corrosion resistance.</li>
                                <li><strong>Modular:</strong> Designed for easy assembly and modification of cleanroom walls.</li>
                            </ul>
                        </div>
                    </div>
                </div>
            """},
            {"section": "Overview", "selector": ".product-block", "action": "remove"}
        ]
    },
    {
        "file": "intoriza/products/cleanroom-led-lights/index.html",
        "updates": [
            {"section": "Light Types / Options", "selector": ".section-head h2", "text": "Cleanroom LED Lights"},
            {"section": "Light Types / Options", "selector": ".section-head p", "html": """PakGusu <strong>cleanroom LED lights</strong> are sealed, energy-efficient fixtures designed for IP-rated, low-particulate performance. Flush-mounted into ceilings for smooth, uniform surfaces."""},
            {"section": "Overview", "selector": ".project-detail-containt", "html": """
                <div class="bg-white text-black">
                    <div class="row">
                        <div class="col-md-12 col-sm-12">
                            <h4 class="m-b15">Key Benefits</h4>
                            <ul class="list-angle-right">
                                <li><strong>IP Rated:</strong> Sealed against dust and moisture ingress (IP54/IP65).</li>
                                <li><strong>Flush Mount:</strong> Installs flush with the ceiling grid for easy cleaning.</li>
                                <li><strong>Energy Efficient:</strong> High-performance LEDs reduce energy consumption and heat load.</li>
                            </ul>
                        </div>
                    </div>
                </div>
            """},
            {"section": "Overview", "selector": ".product-block", "action": "remove"}
        ]
    },
    # --- SERVICES ---
    {
        "file": "intoriza/services/index.html",
        "updates": [
            {"section": "Overview", "selector": ".section-head h2", "text": "Turnkey Cleanroom Services – From Design to Validation"},
            {"section": "Overview", "selector": ".section-head p", "html": """PakGusu provides <strong>end-to-end cleanroom services</strong> that take your project from concept to a fully operational, validated facility. Our turnkey approach reduces project risk, simplifies coordination, and accelerates time-to-operation."""}
        ]
    },
    # --- INDUSTRIES MAIN ---
    {
        "file": "intoriza/industries/index.html",
        "updates": [
            {"section": "Overview", "selector": ".section-head h2", "text": "Industries We Serve"},
            {"section": "Overview", "selector": ".section-head p", "html": """PakGusu designs and builds <strong>industry-specific cleanroom environments</strong> across pharmaceutical, healthcare, food, electronics, laboratories, and medical device sectors. Each industry has unique contamination risks and regulatory requirements; our team tailors solutions accordingly."""}
        ]
    },
    # --- INDUSTRIES SUB-PAGES ---
    {
        "file": "intoriza/industries/pharmaceutical-nutraceutical/index.html",
        "updates": [
            {"section": "PakGusu Solutions", "selector": ".section-head h2", "text": "GMP-Compliant Pharmaceutical Cleanrooms"},
            {"section": "PakGusu Solutions", "selector": ".section-head p", "html": """PakGusu delivers <strong>GMP pharmaceutical cleanrooms</strong> for solid dosage, sterile injectable, and nutraceutical manufacturing. We design Grade A/B/C/D rooms aligned with EU and WHO guidelines and match them to corresponding <strong>ISO 14644-1 classes</strong>."""}
        ]
    },
    {
        "file": "intoriza/industries/healthcare-hospitals/index.html",
        "updates": [
            {"section": "PakGusu Solutions", "selector": ".section-head h2", "text": "Healthcare & Hospital Cleanrooms"},
            {"section": "PakGusu Solutions", "selector": ".section-head p", "html": """We provide specialized cleanroom solutions for operating theatres, isolation rooms, and hospital pharmacies, ensuring patient safety and infection control."""}
        ]
    },
    {
        "file": "intoriza/industries/food-beverage/index.html",
        "updates": [
            {"section": "PakGusu Solutions", "selector": ".section-head h2", "text": "Food & Beverage Cleanrooms"},
            {"section": "PakGusu Solutions", "selector": ".section-head p", "html": """Hygienic production environments for food processing and packaging. Our designs focus on wash-down capability and preventing cross-contamination."""}
        ]
    },
    {
        "file": "intoriza/industries/electronics-manufacturing/index.html",
        "updates": [
            {"section": "PakGusu Solutions", "selector": ".section-head h2", "text": "Electronics Manufacturing Cleanrooms"},
            {"section": "PakGusu Solutions", "selector": ".section-head p", "html": """Ultra-clean, ESD-safe spaces for sensitive electronics assembly and semiconductor manufacturing. We control particulate levels to ensure product yield and reliability."""}
        ]
    },
    {
        "file": "intoriza/industries/laboratories-rd/index.html",
        "updates": [
            {"section": "PakGusu Solutions", "selector": ".section-head h2", "text": "Laboratory & R&D Cleanrooms"},
            {"section": "PakGusu Solutions", "selector": ".section-head p", "html": """Controlled environments for analysis, testing, and experiments. We design for precise temperature, humidity, and pressure control."""}
        ]
    },
    {
        "file": "intoriza/industries/medical-surgical-devices/index.html",
        "updates": [
            {"section": "PakGusu Solutions", "selector": ".section-head h2", "text": "Medical Device Cleanrooms"},
            {"section": "PakGusu Solutions", "selector": ".section-head p", "html": """Clean assembly and sterile packaging areas for medical devices. Our solutions meet ISO 13485 and FDA requirements."""}
        ]
    },
    # --- RESOURCES ---
    {
        "file": "intoriza/resources/index.html",
        "updates": [
            {"section": "Overview", "selector": ".section-head h2", "text": "Cleanroom Resources & Knowledge Hub"},
            {"section": "Overview", "selector": ".section-head p", "html": """PakGusu’s <strong>Resources</strong> section provides practical information to help you plan, build, and maintain your cleanroom. Learn about cleanroom standards, design best practices, and industry trends."""}
        ]
    },
    {
        "file": "intoriza/resources/cleanroom-standards-classifications/index.html",
        "updates": [
            {"section": "Content Section 1", "selector": ".section-head h2", "text": "Cleanroom Standards & Classifications"},
            {"section": "Content Section 1", "selector": ".section-head p", "html": """Understanding <strong>ISO 14644-1</strong> and how it applies to your industry is critical. We help you navigate the standards to choose the right classification for your needs."""}
        ]
    },
    {
        "file": "intoriza/resources/blog/index.html",
        "updates": [
            {"section": "Content Section 1", "selector": ".section-head h2", "text": "PakGusu Blog"},
            {"section": "Content Section 1", "selector": ".section-head p", "html": """The PakGusu blog shares <strong>cleanroom insights, design tips, regulatory updates, and project stories</strong> to help engineers, QA teams, and facility managers make informed decisions."""}
        ]
    },
    {
        "file": "intoriza/resources/news-events/index.html",
        "updates": [
            {"section": "Content Section 1", "selector": ".section-head h2", "text": "News & Events"},
            {"section": "Content Section 1", "selector": ".section-head p", "html": """Stay up to date with <strong>PakGusu news, cleanroom project announcements, and industry events</strong>. Learn where you can meet our team and see our solutions first-hand."""}
        ]
    },
    {
        "file": "intoriza/resources/faqs/index.html",
        "updates": [
            {"section": "Content Section 1", "selector": ".section-head h2", "text": "Frequently Asked Questions"},
            {"section": "Content Section 1", "selector": ".section-head p", "html": """Our <strong>cleanroom FAQ</strong> answers the most common questions we receive about design, construction, classification, and maintenance."""}
        ]
    },
    # --- OTHERS ---
    {
        "file": "intoriza/case-studies/index.html",
        "updates": [
            {"section": "Overview", "selector": ".section-head h2", "text": "Cleanroom Case Studies"},
            {"section": "Overview", "selector": ".section-head p", "html": """Explore our real-world projects. From pharmaceutical plants to electronics labs, see how PakGusu delivers compliant, high-performance cleanroom environments."""}
        ]
    },
    {
        "file": "intoriza/careers/index.html",
        "updates": [
            {"section": "Content Section 1", "selector": ".section-head h2", "text": "Careers at PakGusu"},
            {"section": "Content Section 1", "selector": ".section-head p", "html": """Join PakGusu and help build the next generation of <strong>cleanroom facilities in Pakistan</strong>. We’re looking for engineers, technicians, and professionals who are passionate about quality, innovation, and customer success."""}
        ]
    },
    {
        "file": "intoriza/contact/index.html",
        "updates": [
            {"section": "Contact Info", "selector": ".section-head h2", "text": "Contact PakGusu"},
            {"section": "Contact Info", "selector": ".section-head p", "html": """Do you have a cleanroom project or question? <strong>Contact PakGusu</strong> today – our team will help you choose the right solution for your facility."""}
        ]
    },
    # --- CLEANUP / SECONDARY UPDATES ---
    {
        "file": "intoriza/about/index.html",
        "updates": [
             # Fix the "Making it look like readable English" paragraph
            {"section": "Company Snapshot", "selector": ".col-lg-5 p:nth-of-type(2)", "action": "remove"},
            # Update the "Our Story" / Process section to be "Our Process"
            {"section": "Our Story & Timeline", "selector": ".section-head h2", "text": "Our Process"},
            {"section": "Our Story & Timeline", "selector": ".section-head .site-text-primary", "text": "How We Work"},
            # Card 1
            {"section": "Our Story & Timeline", "selector": ".col-lg-3:nth-child(1) .wt-tilte", "text": "Consultation"},
            {"section": "Our Story & Timeline", "selector": ".col-lg-3:nth-child(1) p", "text": "We assess your specific needs, industry standards, and regulatory requirements."},
            # Card 2
            {"section": "Our Story & Timeline", "selector": ".col-lg-3:nth-child(2) .wt-tilte", "text": "Design"},
            {"section": "Our Story & Timeline", "selector": ".col-lg-3:nth-child(2) p", "text": "Creating detailed blueprints, airflow schematics, and 3D models for your facility."},
            # Card 3
            {"section": "Our Story & Timeline", "selector": ".col-lg-3:nth-child(3) .wt-tilte", "text": "Manufacturing"},
            {"section": "Our Story & Timeline", "selector": ".col-lg-3:nth-child(3) p", "text": "Precision fabrication of modular panels, doors, and windows in our Lahore facility."},
            # Card 4
            {"section": "Our Story & Timeline", "selector": ".col-lg-3:nth-child(4) .wt-tilte", "text": "Installation"},
            {"section": "Our Story & Timeline", "selector": ".col-lg-3:nth-child(4) p", "text": "Expert on-site assembly, sealing, and final validation to ensure compliance."},
        ]
    },
    {
        "file": "intoriza/services/index.html",
        "updates": [
            # Remove the "Making it look like readable English" paragraph under the header
            {"section": "Overview", "selector": ".section-head + p", "action": "remove"},
            # Update the Tabs
            {"section": "Overview", "selector": ".nav-tabs .nav-item:nth-child(1) a", "text": "Design"},
            {"section": "Overview", "selector": "#web-design-7 p", "text": "Our design team creates comprehensive cleanroom layouts, including HVAC sizing, pressure cascades, and material specifications aligned with ISO 14644 standards."},
            {"section": "Overview", "selector": "#web-design-7 ul", "html": """<ul class="list-angle-right p-t15 m-b0"><li>Conceptual Layouts</li><li>3D Modeling</li><li>Airflow Simulation</li></ul>"""},

            {"section": "Overview", "selector": ".nav-tabs .nav-item:nth-child(2) a", "text": "Fabrication"},
            {"section": "Overview", "selector": "#graphic-design-7 p", "text": "We manufacture high-quality modular components locally, ensuring rapid delivery and strict quality control for panels, doors, and windows."},
            {"section": "Overview", "selector": "#graphic-design-7 ul", "html": """<ul class="list-angle-right p-t15 m-b0"><li>Sandwich Panels</li><li>Cleanroom Doors</li><li>Pass Boxes</li></ul>"""},

            {"section": "Overview", "selector": ".nav-tabs .nav-item:nth-child(3) a", "text": "Validation"},
            {"section": "Overview", "selector": "#developement-7 p", "text": "Our service doesn't end at installation. We provide full IQ/OQ/PQ validation support to ensure your cleanroom meets all certification requirements."},
            {"section": "Overview", "selector": "#developement-7 ul", "html": """<ul class="list-angle-right p-t15 m-b0"><li>Particle Counting</li><li>Filter Integrity Testing</li><li>Air Velocity Testing</li></ul>"""},

            # Update the "What we do" section (Process Strip) - Reuse the same logic as About page if structure matches
             {"section": "Process Strip / Timeline", "selector": ".section-head h2", "text": "Why Choose Us"},
             {"section": "Process Strip / Timeline", "selector": ".section-head .site-text-primary", "text": "Our Advantage"},
             # Card 1
            {"section": "Process Strip / Timeline", "selector": ".col-md-4:nth-child(1) .wt-tilte", "text": "Local Expert"},
            {"section": "Process Strip / Timeline", "selector": ".col-md-4:nth-child(1) p", "text": "Based in Pakistan, we offer faster lead times and accessible support compared to importers."},
             # Card 2
            {"section": "Process Strip / Timeline", "selector": ".col-md-4:nth-child(2) .wt-tilte", "text": "Global Quality"},
            {"section": "Process Strip / Timeline", "selector": ".col-md-4:nth-child(2) p", "text": "Partnered with GUSU China to bring world-class cleanroom technology to the local market."},
             # Card 3
            {"section": "Process Strip / Timeline", "selector": ".col-md-4:nth-child(3) .wt-tilte", "text": "Turnkey Solution"},
            {"section": "Process Strip / Timeline", "selector": ".col-md-4:nth-child(3) p", "text": "From initial design to final validation, we handle every aspect of your project."},
        ]
    },
    # --- CLEANUP: INDUSTRIES ---
    {
        "file": "intoriza/industries/pharmaceutical-nutraceutical/index.html",
        "updates": [
            {"section": "Hero", "selector": ".banner-title-name h2", "text": "Pharmaceutical & Nutraceutical"},
            {"section": "Hero", "selector": ".wt-breadcrumb li:last-child", "text": "Pharmaceutical"},
            {"section": "Industry Challenges", "selector": ".product-block", "action": "remove"},
            {"section": "Industry Challenges", "selector": ".project-detail-containt h4", "text": "Strict Contamination Control"},
            {"section": "Industry Challenges", "selector": ".project-detail-containt p", "text": "In pharmaceutical manufacturing, contamination control is critical. Our cleanrooms are designed to meet GMP Grade A-D requirements, ensuring product safety and regulatory compliance."}
        ]
    },
    {
        "file": "intoriza/industries/healthcare-hospitals/index.html",
        "updates": [
            {"section": "Hero", "selector": ".banner-title-name h2", "text": "Healthcare & Hospitals"},
            {"section": "Hero", "selector": ".wt-breadcrumb li:last-child", "text": "Healthcare"},
            {"section": "Industry Challenges", "selector": ".product-block", "action": "remove"},
            {"section": "Industry Challenges", "selector": ".project-detail-containt h4", "text": "Patient Safety First"},
            {"section": "Industry Challenges", "selector": ".project-detail-containt p", "text": "Hospitals require sterile environments to prevent infections. We provide modular operating theatres and isolation rooms that meet the highest hygiene standards."}
        ]
    },
    {
        "file": "intoriza/industries/food-beverage/index.html",
        "updates": [
            {"section": "Hero", "selector": ".banner-title-name h2", "text": "Food & Beverage"},
            {"section": "Hero", "selector": ".wt-breadcrumb li:last-child", "text": "Food & Beverage"},
            {"section": "Industry Challenges", "selector": ".product-block", "action": "remove"},
            {"section": "Industry Challenges", "selector": ".project-detail-containt h4", "text": "Hygienic Processing"},
            {"section": "Industry Challenges", "selector": ".project-detail-containt p", "text": "Food safety is paramount. Our cleanroom solutions help prevent cross-contamination and ensure compliance with HACCP and ISO 22000 standards."}
        ]
    },
    {
        "file": "intoriza/industries/electronics-manufacturing/index.html",
        "updates": [
            {"section": "Hero", "selector": ".banner-title-name h2", "text": "Electronics Manufacturing"},
            {"section": "Hero", "selector": ".wt-breadcrumb li:last-child", "text": "Electronics"},
            {"section": "Industry Challenges", "selector": ".product-block", "action": "remove"},
            {"section": "Industry Challenges", "selector": ".project-detail-containt h4", "text": "ESD & Particulate Control"},
            {"section": "Industry Challenges", "selector": ".project-detail-containt p", "text": "Semiconductor and electronics assembly requires ultra-clean environments. We offer anti-static (ESD) cleanrooms with precise temperature and humidity control."}
        ]
    },
    {
        "file": "intoriza/industries/laboratories-rnd/index.html",
        "updates": [
            {"section": "Hero", "selector": ".banner-title-name h2", "text": "Laboratories & R&D"},
            {"section": "Hero", "selector": ".wt-breadcrumb li:last-child", "text": "Laboratories"},
            {"section": "Industry Challenges", "selector": ".product-block", "action": "remove"},
            {"section": "Industry Challenges", "selector": ".project-detail-containt h4", "text": "Precision Environments"},
            {"section": "Industry Challenges", "selector": ".project-detail-containt p", "text": "Research labs demand stable conditions. Our modular systems allow for flexible layouts and integration of fume hoods and biosafety cabinets."}
        ]
    },
    {
        "file": "intoriza/industries/medical-surgical-devices/index.html",
        "updates": [
            {"section": "Hero", "selector": ".banner-title-name h2", "text": "Medical Devices"},
            {"section": "Hero", "selector": ".wt-breadcrumb li:last-child", "text": "Medical Devices"},
            {"section": "Industry Challenges", "selector": ".product-block", "action": "remove"},
            {"section": "Industry Challenges", "selector": ".project-detail-containt h4", "text": "Sterile Assembly"},
            {"section": "Industry Challenges", "selector": ".project-detail-containt p", "text": "Medical device manufacturing requires ISO 13485 compliance. We build cleanrooms that ensure sterility during assembly and packaging processes."}
        ]
    },
    # --- CLEANUP: NEWS & SERVICES ---
    {
        "file": "intoriza/resources/news-events/index.html",
        "updates": [
            # Replace all Lorem Ipsum excerpts. Since we can't easily target all 'p' in a loop with this script structure without adding a 'replace_all' feature, 
            # we'll target the specific containers we saw or use a broad selector if the script supports it.
            # The script updates the *first* match of a selector in a section.
            # We'll update the first few visible ones.
            {"section": "Content Section 1", "selector": ".cat-1 .wt-post-text p", "text": "Discover the latest trends in cleanroom technology and how they impact manufacturing standards globally."},
            {"section": "Content Section 1", "selector": ".cat-2 .wt-post-text p", "text": "PakGusu announces new partnership with GUSU China to bring advanced modular cleanroom solutions to Pakistan."},
            {"section": "Content Section 1", "selector": ".cat-3 .wt-post-text p", "text": "Understanding ISO 14644-1 classifications: A guide to choosing the right cleanroom class for your industry."},
            {"section": "Content Section 1", "selector": ".cat-4 .wt-post-text p", "text": "Best practices for maintaining cleanroom hygiene and preventing contamination in pharmaceutical facilities."},
            {"section": "Content Section 1", "selector": ".cat-5 .wt-post-text p", "text": "Energy-efficient cleanroom design: How to reduce operational costs while maintaining compliance."},
            {"section": "Content Section 1", "selector": ".cat-6 .wt-post-text p", "text": "The importance of proper airflow design in controlling particulate levels in critical environments."},
        ]
    },
    {
        "file": "intoriza/services/index.html",
        "updates": [
             # Fix remaining cards in "Why Choose Us"
            {"section": "Process Strip / Timeline", "selector": ".col-md-4:nth-child(4) .wt-tilte", "text": "Compliance"},
            {"section": "Process Strip / Timeline", "selector": ".col-md-4:nth-child(4) p", "text": "We ensure your facility meets all relevant local and international standards (ISO, GMP, WHO)."},
            {"section": "Process Strip / Timeline", "selector": ".col-md-4:nth-child(5) .wt-tilte", "text": "Support"},
            {"section": "Process Strip / Timeline", "selector": ".col-md-4:nth-child(5) p", "text": "Dedicated after-sales support and maintenance services to keep your cleanroom running smoothly."},
             # Remove the 6th card if it exists and is dummy, or update it. The file showed "Furniture"
            {"section": "Process Strip / Timeline", "selector": ".col-md-4:nth-child(6) .wt-tilte", "text": "Innovation"},
            {"section": "Process Strip / Timeline", "selector": ".col-md-4:nth-child(6) p", "text": "Continuously adopting the latest technologies in cleanroom construction and control systems."},
        ]
    },
    # --- CLEANUP: RESOURCES & OTHERS ---
    {
        "file": "intoriza/resources/blog/index.html",
        "updates": [
            {"section": "Content Section 1", "selector": ".wt-post-text p", "text": "Stay tuned for the latest insights on cleanroom technology and industry standards.", "action": "update_all"},
            {"section": "Content Section 1", "selector": ".masonry-item:nth-child(n+7)", "action": "remove_all"},
        ]
    },
    {
        "file": "intoriza/resources/news-events/index.html",
        "updates": [
            {"section": "Content Section 1", "selector": ".wt-post-text p", "text": "Latest news and updates from PakGusu Technology.", "action": "update_all"},
            {"section": "Content Section 1", "selector": ".masonry-item:nth-child(n+7)", "action": "remove_all"},
        ]
    },
    {
        "file": "intoriza/resources/index.html",
        "updates": [
             {"section": "Intro", "selector": ".wt-post-text p", "text": "Explore our latest articles and updates on cleanroom technology.", "action": "update_all"},
        ]
    },
    {
        "file": "intoriza/resources/faqs/index.html",
        "updates": [
            {"section": "Content Section 1", "selector": ".wt-accordion-content p", "text": "Cleanroom classification is determined by the concentration of airborne particles. ISO 14644-1 defines classes from ISO 1 (cleanest) to ISO 9 (dirtiest).", "action": "update_all"},
        ]
    },
    {
        "file": "intoriza/resources/cleanroom-standards-classifications/index.html",
        "updates": [
            {"section": "Content Section 1", "selector": ".wt-post-text p", "text": "ISO 14644-1 is the global standard for cleanroom classification. It specifies the maximum allowable number of particles per cubic meter of air for each class.", "action": "update_all"},
        ]
    },
    {
        "file": "intoriza/careers/index.html",
        "updates": [
            {"section": "Content Section 1", "selector": ".wt-post-text p", "text": "We are looking for experienced cleanroom engineers and technicians to join our growing team. If you have a passion for quality and innovation, apply today.", "action": "update_all"},
            {"section": "Content Section 1", "selector": ".acod-content", "text": "We offer a dynamic work environment, competitive salaries, and opportunities for professional growth. Join us to shape the future of cleanroom technology.", "action": "update_all"},
            {"section": "Content Section 1", "selector": ".index-about3 > p", "text": "Join a team that values excellence and innovation.", "action": "update_all"},
        ]
    },
    {
        "file": "intoriza/industries/index.html",
        "updates": [
            {"section": "Intro Paragraph", "selector": ".index-about3 > p", "text": "We provide specialized cleanroom solutions tailored to the unique needs of various industries, ensuring compliance and efficiency.", "action": "update_all"},
            {"section": "Intro Paragraph", "selector": ".acod-content", "text": "Our designs integrate the latest standards and technologies to optimize your production environment.", "action": "update_all"},
            {"section": "Industry Cards Grid", "selector": ".icon-content p", "text": "Specialized solutions for this sector.", "action": "update_all"},
            {"section": "CTA", "selector": ".hover-effect-content p", "text": "State-of-the-art cleanroom facility.", "action": "update_all"},
            {"section": "Latest News", "selector": ".wt-post-text p", "text": "Latest industry news and updates.", "action": "update_all"},
        ]
    },
    {
        "file": "intoriza/index.html",
        "updates": [
            {"section": "Latest News", "selector": ".wt-post-text p", "text": "Read our latest insights on cleanroom design and construction.", "action": "update_all"},
        ]
    },
    {
        "file": "intoriza/services/index.html",
        "updates": [
            {"section": "Planning & Design", "selector": ".hover-effect-content p", "text": "Delivering excellence in every project.", "action": "update_all"},
        ]
    }
]

# ==========================================
# LOGIC
# ==========================================

def update_section(soup, update):
    section_name = update.get("section")
    selector = update.get("selector")
    text = update.get("text")
    html = update.get("html")
    action = update.get("action")

    # Find the section by comment
    start_comment = None
    for comment in soup.find_all(string=lambda text: isinstance(text, str) and text.strip() == f"Section: {section_name}"):
        start_comment = comment
        break
    
    if not start_comment:
        print(f"  [WARN] Section comment 'Section: {section_name}' not found.")
        # Debug: print all comments found
        for c in soup.find_all(string=lambda text: isinstance(text, str) and "Section:" in text):
           print(f"    Found comment: '{c.strip()}'")
        return False



    # Find the container div immediately following the comment
    section_div = start_comment.find_next_sibling('div')
    if not section_div:
        print(f"  [WARN] Section div for '{section_name}' not found. Next sibling is: {start_comment.next_sibling}")
        return False

    target = None
    
    if action == "remove":
        if selector:
            target = section_div.select_one(selector)
            if target:
                target.decompose()
                print(f"  Removed element: {section_name} -> {selector}")
                return True
            else:
                print(f"  [WARN] Target '{selector}' to remove not found in '{section_name}'.")
                return False

    if action == "remove_all":
        if selector:
            targets = section_div.select(selector)
            if targets:
                count = 0
                for t in targets:
                    t.decompose()
                    count += 1
                print(f"  Removed {count} elements: {section_name} -> {selector}")
                return True
            else:
                print(f"  [WARN] Targets '{selector}' to remove_all not found in '{section_name}'.")
                return False

    if action == "insert_after_header":
        header_div = section_div.select_one(".section-head")
        if header_div:
            new_tag = BeautifulSoup(html, 'html.parser')
            # Check if we already inserted it to avoid duplicates if run multiple times
            # A simple check is if the last child text matches roughly
            header_div.append(new_tag)
            print(f"  Inserted HTML after header in: {section_name}")
            return True
        else:
             print(f"  [WARN] Header div not found in '{section_name}' for insertion.")
             return False

    if action == "update_all":
        if selector:
            targets = section_div.select(selector)
            if targets:
                count = 0
                for target in targets:
                    if text:
                        target.string = text
                    elif html is not None:
                        new_tag = BeautifulSoup(html, 'html.parser')
                        target.clear()
                        target.append(new_tag)
                    count += 1
                print(f"  Updated {count} elements in: {section_name} -> {selector}")
                return True
            else:
                print(f"  [WARN] Targets '{selector}' for update_all not found in '{section_name}'.")
                return False

    if selector:
        target = section_div.select_one(selector)
    
    if target:
        if text:
            target.string = text
            print(f"  Updated text in: {section_name} -> {selector}")
        elif html is not None:
            new_tag = BeautifulSoup(html, 'html.parser')
            target.clear()
            target.append(new_tag)
            print(f"  Updated HTML in: {section_name} -> {selector}")
        return True
    else:
        print(f"  [WARN] Target '{selector}' not found in section '{section_name}'.")
        return False

def process_page(page_data):
    file_path = page_data["file"]
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return

    print(f"Processing {file_path}...")
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    soup = BeautifulSoup(content, 'html.parser')
    modified = False
    
    for update in page_data["updates"]:
        if update_section(soup, update):
            modified = True
            
    if modified:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(str(soup))
        print(f"  Saved changes to {file_path}")
    else:
        print(f"  No changes made to {file_path}")

def main():
    for page in CONTENT_UPDATES:
        process_page(page)

if __name__ == "__main__":
    main()
