# Home Page Design Documentation

**URL:** `/`
**Source File:** `intoriza/index.html`
**Parent Template:** `index-3.html` (Likely based on structure)

## Page Overview
The main landing page for PakGusu Technology, designed to showcase turnkey cleanroom solutions, products, and industries served. It serves as the primary gateway for potential clients.

## Section-by-Section Design

### 1. Header
- **Type:** Sticky Header (`.sticky-header`, `.header-style-1`)
- **Components:**
    - Logo (`.logo-header`)
    - Main Navigation (`.header-nav`)
    - **Dark Mode Toggle** (`.dark-mode-toggle`) - User-activated, defaults to Light Mode. See [Dark Mode Feature](../dark-mode.md).
    - "Get In Touch" Slide-out Panel (`.contact-slide-hide`)

### 2. Hero Section
- **Type:** Revolution Slider (`#rev_slider_346_1_wrapper`)
- **Content:**
    - Slide 1: "Turnkey Cleanroom Solutions" - "Build World-Class Modular Cleanrooms Locally in Pakistan."
    - Background: Image with parallax effect.
    - Animation: Text fades in with 3D effects.

### 3. Who We Are Section
- **ID:** `#who-we-are-section`
- **Layout:** 2-Column Split
    - **Left Column:** "About PakGusu" intro text with an Accordion (`#accordion5`) featuring:
        - Turnkey Design & Build
        - ISO-Classified Environments
        - Local Manufacturing Support
    - **Right Column:** Synced Owl Carousel Gallery (`#sync1`, `#sync2`) displaying project/product images.
- **Visuals:** Wave background animation (`.wave-container`).

### 4. Cleanroom Products Section
- **ID:** `#cleanroom-products-section`
- **Layout:** Grid of 6 items (3 columns on desktop).
- **Content:**
    - Cleanroom Panels
    - Cleanroom Windows
    - Cleanroom Doors
    - Pass-Through Chambers
    - Aluminum Profiles
    - Cleanroom LED Lights
- **Styling:** Hover effects on cards (`.hover-box-effect`, `.v-icon-effect`).
- **Visuals:** Background "blobs" animation (`.cp-background`).

### 5. Industries We Serve Section
- **ID:** `#industries-we-serve-section`
- **Layout:** Carousel (`.owl-carousel-filter3`)
- **Content:**
    - Pharmaceutical & Nutraceutical
    - Healthcare & Hospitals
    - Food & Beverage
    - Electronics Manufacturing
    - Laboratories & R&D
    - Medical & Surgical Devices
- **Styling:** Cards with background images and hover descriptions (`.hover-effect-1`).

### 6. Turnkey Cleanroom Services
- **ID:** `#turnkey-services-section`
- **Layout:** 4 Columns.
- **Content:**
    - Planning & Design
    - Cleanroom Construction
    - Installation & Commissioning
    - Validation & Certification
- **Styling:** Image cards with text overlay on hover (`.our-team-two`).

### 7. Why Choose PakGusu
- **ID:** `#why-choose-pakgusu-section`
- **Layout:** 2-Column (Text Left, Image/Video Right).
- **Content:**
    - Accordion listing advantages (Expertise, Cost-Effective, Compliance, Support).
    - Video popup (`.mfp-video`) linking to a corporate video.

### 8. Latest News (Blog)
- **ID:** `#latest-news-section`
- **Layout:** 3-Column Grid.
- **Content:** Recent blog posts with dates, titles, and snippets.

### 9. Footer
- **Type:** Main Footer (`footer-dark`)
- **Components:**
    - About widget
    - Useful Links
    - Recent Posts
    - Newsletter Signup
    - Copyright and Social Icons

## Scripts & Interactive Elements
- **Revolution Slider:** Main hero banner.
- **Owl Carousel:** Product gallery, Industries carousel, Blog carousel.
- **Magnific Popup:** Video lightboxes.
- **Waypoints:** Scroll animations (`.fade-in-up`).
