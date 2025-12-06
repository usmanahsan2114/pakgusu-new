# Products Main Page Design Documentation

**URL:** `/products/`
**Source File:** `intoriza/products/index.html`
**Parent Template:** `work-grid.html` (approximate structure)

## Page Overview
Overview page listing all cleanroom products manufactured by PakGusu. Features a filterable gallery and an interactive system integration showcase.

## Section-by-Section Design

### 1. Header
- **Type:** Standard Global Header
- **Includes:** Dark Mode Toggle. Header is always Dark Blue (#004685) with Light Blue (#29afe3) accents.

### 2. Page Title / Breadcrumb
- **Type:** Inner Page Banner
- **Content:** "Cleanroom Components Gallery" (h1).

### 3. Product Gallery (Filterable)
- **ID:** `#products-page`
- **Class:** `.products-section`
- **Interactive Elements:**
    - **Filter Tabs:** `.product-filter` (All, Panels, Windows, Doors, Pass-Throughs, Profiles, Lighting). Uses tailored JavaScript for filtering and simple fade animations.
    - **Grid:** `.product-grid` displaying `.product-card` items.
- **Card Design:**
    - **Image:** 16:10 aspect ratio with hover zoom effect.
    - **Overlay:** Gradient overlay with "View Details" button on hover.
    - **Content:** Tag (Category), Title, and short description.
    - **Dark Mode:** Cards transition to dark blue backgrounds (`#162436`).

### 4. System Integration Showcase
- **ID:** `#integration-section`
- **Design:** Split layout (Content Left, Interactive Visual Right).
- **Background:** Grid animation and floating "nodes".
- **Interactive Visual:**
    - **Hotspots:** Pulsing dots (`.hotspot`) on a main system image.
    - **Tooltips:** Clicking/Hovering hotspots reveals details about Panels, Windows, HVAC, and Doors integration.
- **Content:** "Seamless Integration" heading, descriptive text, and 3 feature columns (Modular Design, Easy Installation, HVAC Compatible).

### 5. Call-to-Action (CTA)
- **ID:** `#cta-cleanroom-project`
- **Design:** Full-width background image with a glassmorphism card (`.cta-panel`) overlay.
- **Content:**
    - **Heading:** "Plan Your Cleanroom Project Today"
    - **Checklist:** ISO Guidance, HVAC Integration, Validation Docs.
    - **Buttons:** Primary ("Request Free Consultation") and Secondary ("Download Specs").

### 6. Footer
- **Type:** Standard Global Footer
