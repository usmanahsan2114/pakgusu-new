# Case Studies Page Design Documentation

**URL:** `/case-studies/`
**Source File:** `intoriza/case-studies/index.html`
**Parent Template:** `work-grid.html` or `work-masonry.html`

## Page Overview
Showcases completed cleanroom projects across various industries to demonstrate PakGusu's capabilities.

## Section-by-Section Design

### 1. Header
- **Type:** Standard Global Header
- **Includes:** Dark Mode Toggle. Header is always Dark Blue (#004685) with Light Blue (#29afe3) accents. See [Dark Mode](../dark-mode.md).

### 2. Page Title / Breadcrumb
- **Type:** Inner Page Banner (`.wt-bnr-inr`)
- **Content:** "Case Studies" or "Our Projects" title and breadcrumb.

### 3. Filter Bar (Optional)
- **Layout:** Horizontal filter buttons.
- **Content:** Industry categories (Pharma, Healthcare, Food, Electronics, etc.)
- **Scripts:** Isotope.js or similar for filtering.

### 4. Projects Grid
- **Layout:** Masonry or Standard Grid (3-4 columns).
- **Content:**
    - Project thumbnail image.
    - Project title (e.g., "Pharmaceutical Cleanroom – XYZ Pharma").
    - Industry tag.
    - Link to detail page (if available).
- **Styling:** Hover effect revealing title/category (`.wt-img-overlay`).

### 5. Pagination (Optional)
- **Layout:** Standard pagination or "Load More" button.

### 6. Footer
- **Type:** Standard Global Footer (Dark Blue #004685, Light Blue #29afe3 accents, white text)

## Scripts
- **Isotope.js:** For masonry layout and filtering.
- **ImagesLoaded:** To ensure grid calculates layout after images load.
