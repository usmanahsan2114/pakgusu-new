# Products Main Page Design Documentation

**URL:** `/products/`
**Source File:** `intoriza/products/index.html`
**Parent Template:** `work-grid.html`

## Page Overview
Overview page listing all cleanroom products manufactured by PakGusu. Serves as a gateway to individual product detail pages.

## Section-by-Section Design

### 1. Header
- **Type:** Standard Global Header
- **Includes:** Dark Mode Toggle. Header is always Dark Blue (#004685) with Light Blue (#29afe3) accents. See [Dark Mode](../dark-mode.md).

### 2. Page Title / Breadcrumb
- **Type:** Inner Page Banner (`.wt-bnr-inr`)
- **Content:** "Products" or "Cleanroom Products" title and breadcrumb.

### 3. Products Grid
- **Layout:** 3-Column Grid (6 items total).
- **Content:**
    - Cleanroom Panels
    - Cleanroom Windows
    - Cleanroom Doors
    - Pass-Through Chambers
    - Aluminum Profiles
    - Cleanroom LED Lights
- **Styling:** Each card has image, title, short description, "Read More" link.
- **Classes:** `.hover-box-effect`, `.v-icon-effect`

### 4. Call-to-Action (Optional)
- **Layout:** Full-width banner.
- **Content:** "Request a Quote" button.

### 5. Footer
- **Type:** Standard Global Footer (Dark Blue #004685, Light Blue #29afe3 accents, white text)
