# Section Structure Guide

## Overview

All website pages follow a consistent section structure as defined in `../Page_by_Page_Section_Layout.md`. Each page type has specific sections that should be included.

## Section Markers

Each section in the HTML is marked with HTML comments for easy identification:

```html
<!-- Section: [Section Name] -->
<div class="section-full p-t80 p-b50 bg-white">
   <!-- Section content -->
</div>
<!-- /Section: [Section Name] -->
```

## Page Structure Reference

### Home Page (/)
1. Hero
2. Who We Are
3. Our Solutions
4. Product Highlights
5. Industries We Serve
6. Why Choose PakGusu
7. Latest from Resources
8. Call-to-Action Banner
9. Global Footer

### About Page (/about)
1. Hero
2. Company Snapshot
3. Our Story & Timeline
4. Partnership with GUSU China
5. Mission, Vision & Values
6. Our Facility & Capabilities
7. Quality & Compliance
8. Leadership / Expertise
9. CTA

### Product Pages
Each product detail page includes:
1. Hero
2. Overview
3. Product-specific sections (types, options, etc.)
4. Key Features & Benefits
5. Technical Specs/Applications
6. Gallery
7. Related Solutions
8. CTA

## Managing Sections

### Adding New Sections
When adding a new section:
1. Use the section marker comments
2. Follow the Bootstrap grid system (container > row > col)
3. Use consistent class names from the template
4. Add `<!-- TODO: Design/Content needed -->` for incomplete sections

### Section Styling
Standard section classes:
- `section-full` - Full-width section
- `p-t80 p-b50` - Padding top 80px, bottom 50px
- `bg-white`, `bg-gray` - Background colors

See `Page_by_Page_Section_Layout.md` for complete section requirements per page.

### Section Transitions
To create a smooth transition between sections with different background colors (e.g., White to Gray), insert an SVG wave separator at the bottom of the preceding section.

```html
<div class="wave-separator">
    <svg viewBox="0 0 1200 120" preserveAspectRatio="none">
        <path d="..." class="shape-fill [white|gray]"></path>
    </svg>
</div>
```
- Use `.shape-fill.white` if the *next* section is white.
- Use `.shape-fill.gray` if the *next* section is gray.
