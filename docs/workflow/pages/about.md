# About Page Design Documentation

**URL:** `/about/`
**Source File:** `intoriza/about/index.html`
**Parent Template:** `about-1.html`

## Page Overview
Provides comprehensive information about PakGusu Technology, its mission, partnership with GUSU Purification, and commitment to cleanroom excellence.

## Section-by-Section Design

### 1. Header
- **Type:** Standard Global Header (Sticky, Dark Navigation)
- **Includes:** Dark Mode Toggle. Header is always Dark Blue (#004685) with Light Blue (#29afe3) accents. See [Dark Mode](../dark-mode.md).

### 2. Page Title / Breadcrumb
- **Type:** Inner Page Banner (`.wt-bnr-inr`)
- **Background:** Overlay image with primary color tint.
- **Content:** "About Us" title and breadcrumb links.

### 3. Company Introduction Section
- **Layout:** 2-Column (Image Left, Text Right)
- **Content:**
    - Company history and mission statement.
    - "About PakGusu" separator title.
    - Paragraph describing cleanroom manufacturing expertise.
- **Visuals:** Company/facility image.

### 4. Our Partnership Section
- **Layout:** Text with supporting image/iconography.
- **Content:**
    - Details on the strategic partnership with GUSU Purification (China).
    - Benefits of the partnership (global expertise + local manufacturing).

### 5. Why Choose Us / Key Differentiators
- **Layout:** Icon Boxes / Feature Grid
- **Content:**
    - Turnkey Solutions
    - ISO-Classified Environments
    - Local Manufacturing
    - After-Sales Support
- **Styling:** Icon boxes with hover effects.

### 6. Statistics / Counter Section (Optional)
- **Layout:** Row of animated counters.
- **Content:** Years of experience, projects completed, satisfied clients, etc.
- **Scripts:** CounterUp.js for number animation.

### 7. Footer
- **Type:** Standard Global Footer (Dark Blue #004685, Light Blue #29afe3 accents, white text)

## Scripts & Interactive Elements
- **CounterUp:** For animated statistics.
- **Waypoints:** Scroll-triggered animations.
