# Navigation Menu Structure

The website navigation menu follows this structure across all pages:

## Main Navigation

1. **Home** - Links to root (`/`)
2. **About Us** - Links to about page (`/about`)
3. **Products** *(dropdown)* - Product categories
   - Cleanroom Panels
   - Cleanroom Windows
   - Cleanroom Doors
   - Pass-Through Chambers
   - Aluminum Profiles
   - Cleanroom LED Lights
4. **Services** - Turnkey cleanroom solutions (`/services`)
5. **Industries** *(dropdown)* - Industry sectors
   - Pharmaceutical & Nutraceutical
   - Healthcare & Hospitals
   - Food & Beverage
   - Electronics Manufacturing
   - Laboratories & R&D
   - Medical & Surgical Devices
6. **Resources** *(dropdown)* - Information and blog
   - Cleanroom Standards & Classifications
   - Blog
   - News & Events
   - FAQs
7. **Case Studies** - Portfolio (`/case-studies`)
8. **Careers** - Job opportunities (`/careers`)
9. **Contact** - Contact form (`/contact`)

## Footer Quick Links

The footer contains a simplified navigation:
- About
- Products
- Blog
- Case Studies
- Contact Us

## Technical Implementation

The navigation is implemented using:
- **Static HTML** - Each page has its own navigation HTML (not dynamically included)
- **Relative Paths** - All links use relative paths adjusted for file depth
- **BeautifulSoup Script** - Use `fix_navigation.py` to update navigation across all pages

### Updating Navigation

If you need to add or modify navigation items:

1. Modify the `create_navigation_html()` function in `fix_navigation.py`
2. Modify the `create_footer_links_html()` function for footer changes
3. Run the script: `python fix_navigation.py`
4. Verify changes in your browser

**Note:** Because this is a static HTML template, navigation changes must be applied to every page. The script handles this automatically.

### Styling
- **Hover Effect:** Navigation links have a 5px border radius on hover (`.nav-line-animation > li > a:before`, `.nav-line-animation > li > a:after`).
