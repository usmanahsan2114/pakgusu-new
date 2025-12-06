# Careers Page Design Documentation

**URL:** `/careers/`
**Source File:** `intoriza/careers/index.html`
**Parent Template:** `index-3.html` (based on structure)

## Page Overview
Lists career opportunities and company culture information to attract potential employees. Currently utilizes an accordion layout for job categories/teams.

## Section-by-Section Design

### 1. Header
- **Type:** Standard Global Header
- **Includes:** Dark Mode Toggle, Mobile Menu, Contact Slide-out.

### 2. Page Title / Hero
- **Type:** Revolution Slider (`fullscreenbanner`)
- **ID:** `rev_slider_346_1`
- **Content:** Video background (`video2.mp4`) with overlay text "Trust and recommed / Giving your home a new style".
- **CTA:** "Read More" button linking to `/contact/`.

### 3. Careers & Gallery Section (`.section-full`)
- **Layout:** 2-Column Split
    - **Left Column:**
        - **Title:** "Welcome to intoriza / Careers at PakGusu"
        - **Description:** "Join a team that values excellence..."
        - **Component:** Accordion (`#accordion5`) listing roles (e.g., Architectural Design, Interior Design) with "Apply Now" buttons.
    - **Right Column:**
        - **Component:** Synced Owl Carousel (`#sync1`, `#sync2`) displaying portrait gallery images.

### 4. "What we do" Services Grid (`.bg-gray`)
- **Layout:** 3-Column Grid (multiline)
- **Content:** Icon boxes with hover effects covering services like Planning, Interior, Exterior, Decoration, Furniture.
- **Link:** Each item links to products/panels page.

### 5. Latest Projects Carousel
- **Title:** "Recently finished / Our latest projects"
- **Component:** Owl Carousel (`.owl-carousel-filter3`) showing project images with hover details.

### 6. Team Section (`.small-device`)
- **Title:** "Our Best Team / Our Team"
- **Layout:** 3-Column Grid
- **Content:** Team member cards (Image, Name, Role, Social Links).

### 7. Footer
- **Type:** Standard Global Footer
- **Includes:** Navigation links, Contact Grid, Social Icons, Copyright.
