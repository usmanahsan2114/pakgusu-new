# Page-by-Page Section Layout - As Implemented

## Home (`/index.php`)

1. **Hero Section**: Video background slider with headline, subheadline, and CTA button
2. **Company Overview**: Introduction to PakGusu with image and description
3. **Product Highlights**: Cards showcasing key product categories
4. **Services Overview**: Service icons with images for 4 main services
5. **Industries Served**: Icon grid showing sectors served
6. **Call-to-Action Banner**: "Plan Your Cleanroom Project" with CTA button
7. **Global Footer**: Links, contact information, social icons

---

## About Us (`/about/index.php`)

1. **Hero**: "About Us" heading + banner image
2. **About Overview**: One-paragraph introduction to PakGusu
3. **Subpage Teasers**: Three cards linking to:
   - About Pak Gusu
   - About GUSU China  
   - Cleanroom Standards

### About Pak Gusu (`/about/pak-gusu/index.php`)

1. **Hero**: Banner with title
2. **Company Background**: Introduction paragraph
3. **Mission & Vision**: Side-by-side grid layout
4. **Our Values**: Styled bullet list with quality, innovation, customer focus, integrity, expertise
5. **Facilities & Team**: Description of manufacturing facility and team
6. **Why Choose Us**: Styled bullet list of differentiators
7. **Team Section**: Team member profiles with images
8. **Sidebar**: Navigation to other About pages and contact CTA

### About GUSU China (`/about/gusu-china/index.php`)

1. **Hero**: Banner with title
2. **Company Overview**: Introduction to GUSU China
3. **Manufacturing Excellence**: Styled list of facilities and capabilities
4. **Global Presence**: Description of international reach
5. **Strategic Partnership**: Explanation of PakGusu-GUSU collaboration
6. **Certifications & Standards**: Styled list of ISO certifications, CE, FDA, cGMP
7. **Sidebar**: Navigation and contact CTA

### Cleanroom Standards (`/about/cleanroom-standards/index.php`)

1. **Hero**: Banner with title
2. **Introduction**: What cleanroom classifications are
3. **ISO 14644-1 Standards**: Explanation with HTML table showing classifications
4. **Applications by Classification**: Three card boxes showing:
   - ISO Class 4-5 applications
   - ISO Class 6-7 applications
   - ISO Class 8 applications
5. **Environmental Parameters**: Styled list (temperature, humidity, pressure, air changes, HEPA)
6. **Sidebar**: Navigation and contact CTA

---

## Products Overview (`/products/index.php`)

1. **Hero**: "Our Products" heading + banner
2. **Introduction**: "Products & Solutions" with description
3. **Product Category Grid**: 6 product cards with images:
   - Clean Room Panels
   - Windows
   - Doors
   - Transfer Window
   - Aluminum Profile
   - Clean LED Lights
4. **Quality Assurance**: Three icon boxes highlighting:
   - Certified Quality
   - Advanced Technology  
   - Expert Support
5. **CTA Banner**: "Need a Custom Solution?" with "Get a Quote" button

### Product Detail Pages (All follow same structure)

Example: Clean Room Panels (`/products/clean-room-panels/index.php`)

1. **Hero**: Product name + banner
2. **Product Gallery**: Synchronized gallery slider
3. **Overview**: Product description and introduction
4. **Key Features**: Styled bullet list
5. **Applications**: Description of typical use cases
6. **Technical Specifications**: HTML table with material, core, thickness, size specs
7. **Sidebar**: Product navigation menu and "Get a Quote" CTA

*Same structure applies to: Windows, Doors, Transfer Window, Aluminum Profile, Clean LED Lights*

---

## Services – Turnkey Solutions (`/services/index.php`)

1. **Hero**: "Our Services" heading + banner
2. **Introduction**: "Professional Services" description
3. **Service Cards Grid**: 4 service cards with icons and images:
   - Planning & Design
   - Clean Room Construction
   - Installation Services
   - After-Sale Services
4. **Our Approach**: 4-step process boxes:
   - Consultation
   - Design
   - Execution
   - Validation
5. **CTA Banner**: "Ready to Start Your Project?" with contact button

### Service Detail Pages (All follow same structure)

Example: Planning & Design (`/services/planning-design/index.php`)

1. **Hero**: Service name + banner
2. **Service Overview**: Description of service offering
3. **What We Offer**: Styled bullet list of deliverables
4. **Why Choose Us**: Quality and experience statement
5. **FAQ Section**: Accordion with frequently asked questions
6. **Sidebar**: Services navigation menu and "Request Service" CTA

*Same structure applies to: Clean Room Construction, Installation, After-Sale Services*

---

## Sectors Overview (`/sectors/index.php`)

1. **Hero**: "Industry Sectors" heading + banner
2. **Introduction**: "Sector Expertise" description
3. **Sector Cards Grid**: 6 industry cards with images:
   - Pharmaceutical / Nutraceutical
   - Hospital & Healthcare
   - Food Industry
   - Electronics Manufacturing
   - Research Laboratories
   - Medical / Surgical Devices
4. **CTA Banner**: "Industry-Specific Solutions" with "Discuss Your Project" button

### Sector Detail Pages

*Note: Individual sector pages exist but have not yet been standardized in Phase 8. These will be verified in Phase 9.*

Structure should include:
1. Hero
2. Industry challenges & requirements
3. PakGusu solutions
4. Compliance standards
5. Related products & services
6. CTA

---

## Portfolio (`/portfolio/index.php`)

1. **Hero**: "Our Work" or "Portfolio" heading + banner
2. **Introduction**: Description of projects
3. **View Switcher**: Toggle between Gallery and Masonry views
4. **Project Grid**: Project cards with images and categories
5. **Category Filter**: Filter projects by type

---

## Blog (`/blog/index.php`)

1. **Hero**: "Blog" or "Insights" heading + banner
2. **Introduction**: Blog purpose description
3. **View Switcher**: Toggle between Grid, List, and Masonry views
4. **Blog Posts**: Article cards with title, date, excerpt, and featured image
5. **Category Filter**: Filter posts by category
6. **Pagination**: Navigate through posts

---

## Contact (`/contact/index.php`)

1. **Hero**: "Contact Us" heading + banner
2. **Google Map**: Embedded map showing location
3. **Contact Information**: Three icon boxes showing:
   - Phone Number
   - Email Address  
   - Physical Address
4. **Contact Form**: Name, Email, Message fields with submit button
5. **Footer**: Standard global footer

---

## Global Elements (All Pages)

### Header
- Logo
- Primary navigation menu (Home, About, Products, Services, Sectors, Blog, Portfolio, Contact)
- Dynamic `$path` variable for correct asset loading

### Footer
- Quick links section
- Company information
- Contact details
- Social media icons
- Copyright notice

### Modular Sections (Used across pages)
- `company_overview.php` - Homepage company intro
- `product_highlights.php` - Homepage product showcase
- `industries_served.php` - Homepage sectors grid
- `cta_banner.php` - Homepage call-to-action
- `services_images.php` - Services page service cards
- `team.php` - About Pak Gusu team section
- `sync_gallery.php` - Product pages image gallery
- `accordion.php` - Service pages FAQ section

---

## Implementation Notes

### Phase 8 Completion Status
✅ **Complete**:
- Home Page
- About Section (overview + 3 subpages)
- Products Section (overview + all product pages)
- Services Section (overview + all service pages)
- Sectors Section (overview page)
- Contact Page

🔄 **In Progress** (Phase 9):
- Individual sector detail pages
- Portfolio pages
- Blog pages

### Technical Details
- All pages use PHP with `$path` variable for dynamic paths
- Modular includes used for reusable components
- Consistent breadcrumb navigation on all subpages
- Sidebar navigation on detail pages with active state indication
- Responsive design with Bootstrap grid system
- View switchers on Portfolio and Blog using JavaScript
