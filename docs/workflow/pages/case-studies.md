# Case Studies Page Design Documentation

**URL:** `/case-studies/`
**Source File:** `intoriza/case-studies/index.html`
**Parent Template:** `work-masonry.html` (implied)

## Page Overview
Intended to showcase completed projects. Currently setup with a masonry grid container (content appears to be creating dynamically or is currently empty placeholder) followed by support and CTA sections.

## Section-by-Section Design

### 1. Header
- **Type:** Standard Global Header
- **Includes:** Dark Mode Toggle, Mobile Menu.

### 2. Page Title / Hero
- **Type:** Inner Page Banner (`.wt-bnr-inr`)
- **Background:** Image (`banner/1.jpg`) with black overlay.
- **Content:** Title "Work Masonry", Breadcrumb "Home / Work Masonry".

### 3. Gallery Grid Section
- **Container:** `.portfolio-wrap .mfp-gallery .work-grid .row`
- **Status:** Empty in static HTML source (likely populated via JS or manual update needed).

### 4. Support Information
- **Layout:** Centered Text Block (`.bg-gray`)
- **Content:** "Need More Information? / Support", Paragraph, "Get in Touch" button.

### 5. Primary CTA (`.video-section-full`)
- **Background:** Image (`bg-1.jpg`)
- **Content:** "Ready to Start? / Plan Your Cleanroom Project Today", "Contact Us" button.

### 6. Footer
- **Type:** Standard Global Footer
- **Includes:** Navigation links, Contact Grid, Social Icons, Copyright.
