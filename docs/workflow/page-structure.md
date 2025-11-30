# Page Structure Documentation

## Complete Website Structure

The website now follows this structure:

### Top-Level Pages
- **Home** (`/`) - Main landing page
- **About Us** (`/about`) - Company information
- **Services** (`/services`) - Turnkey cleanroom solutions
- **Careers** (`/careers`) - Job opportunities
- **Case Studies** (`/case-studies`) - Project portfolio
- **Contact** (`/contact`) - Contact form and information

### Products (`/products`)
Main products page with grid view, plus individual pages for each product:
- Cleanroom Panels (`/products/cleanroom-panels`)
- Cleanroom Windows (`/products/cleanroom-windows`)
- Cleanroom Doors (`/products/cleanroom-doors`)
- Pass-Through Chambers (`/products/pass-through-chambers`)
- Aluminum Profiles (`/products/aluminum-profiles`)
- Cleanroom LED Lights (`/products/cleanroom-led-lights`)

### Industries (`/industries`)
Main industries page, plus individual pages for each industry:
- Pharmaceutical & Nutraceutical (`/industries/pharmaceutical-nutraceutical`)
- Healthcare & Hospitals (`/industries/healthcare-hospitals`)
- Food & Beverage (`/industries/food-beverage`)
- Electronics Manufacturing (`/industries/electronics-manufacturing`)
- Laboratories & R&D (`/industries/laboratories-rnd`)
- Medical & Surgical Devices (`/industries/medical-surgical-devices`)

### Resources (`/resources`)
Main resources page, plus individual resource pages:
- Cleanroom Standards & Classifications (`/resources/cleanroom-standards-classifications`)
- Blog (`/resources/blog`)
- News & Events (`/resources/news-events`)
- FAQs (`/resources/faqs`)

## URL Structure

All pages use the "directory + index.html" pattern:
- URLs are clean: `example.com/about/` instead of `example.com/about.html`
- Each directory contains its own `index.html` file
- All asset links (CSS, JS, images) use relative paths with appropriate `../` prefixes

## Template Source Files

Each page was populated from these original files:
- Product detail pages → `project-detail.html`
- Industry detail pages → `project-detail.html`
- Main products page → `work-grid.html`
- Main industries page → `index-3.html`
- Resources blog → `news-listing.html`
- Resources news/events → `news-grid.html`
- And so on (see `complete_structure_and_fix.py` for full mapping)
