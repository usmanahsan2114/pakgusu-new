# Home Page Design Documentation

**URL:** `/`
**Source File:** `intoriza/index.html`
**Parent Template:** `index-3.html`

## Page Overview
The main landing page for PakGusu Technology, acting as a comprehensive portal to Products, Services, and Industries. It features a modern, section-rich layout with interactive elements like a global map, solution pathways, and a news hub.

## Section-by-Section Design

### 1. Header
- **Type:** Sticky Global Header
- **Components:** Logo, Main Navigation (Desktop + Mobile), Dark Mode Toggle, Contact Slide-out Panel.

### 2. Hero Section
- **Type:** Revolution Slider (`fullscreenbanner`)
- **ID:** `rev_slider_346_1`
- **Content:**
    - Slide: "Turnkey Cleanroom Solutions" / "Build World-Class Modular Cleanrooms Locally in Pakistan."
    - Visuals: Parallax text, fade-in animations, text-swap effects.
- **Next Section Trigger:** Scroll Indicator mouse icon.

### 3. Intro / Who We Are (`#intro-hero-section`)
- **Layout:** 2-Column Split
    - **Left:** "About PakGusu" intro text + Accordion (Turnkey Design, ISO Environments, Local Support).
    - **Right:** Visual Frame with Main Slider (`#sync1`) and Thumbnail Carousel (`#sync2`).

### 4. Cleanroom Products (`#cleanroom-products-section`)
- **Header:** "Manufactured in Pakistan / Cleanroom Products"
- **Layout:** 3-Column Grid (`.products-grid`)
- **Items:**
    1.  Cleanroom Panels
    2.  Cleanroom Windows
    3.  Cleanroom Doors
    4.  Pass-Through Chambers
    5.  Aluminum Profiles
    6.  Cleanroom LED Lights
- **Visuals:** Hover cards with icons and descriptions.

### 5. Industries We Serve (`#industries-we-serve-section`)
- **Header:** "Industries We Serve"
- **Layout:** Full-width Owl Carousel (`.cleanroom-window-slider`)
- **Content:**
    - Pharmaceutical
    - Healthcare
    - Food & Beverage
    - Electronics
    - Laboratories & R&D
    - Medical Devices
- **Visuals:** Scan-line overlay effect on images.

### 6. Turnkey Services (`#turnkey-services-section`)
- **Header:** "End-to-End Solutions / Turnkey Cleanroom Services"
- **Layout:** 4-Column Row
- **Items:**
    1.  Planning & Design
    2.  Cleanroom Construction
    3.  Installation & Commissioning
    4.  After-Sales Support
- **Visuals:** Card layout with icon top and "Read More" link.

### 7. Global Presence (`#global-presence-section`)
- **Type:** Interactive Map & List
- **Layout:** Split View
    - **Left:** Map visualizations with markers (`.gp-map-card`).
    - **Right:** Filterable List (`.gp-list-panel`) with tabs (Manufacturing, Sales, Partner) and Search.
- **Data:** JS-driven location data (Pakistan, China, UAE, etc.).

### 8. Solutions Overview (`#solutions-overview`)
- **Header:** "Two Paths, One Integrated Cleanroom Solution"
- **Layout:** 2-Card "Choice" Layout
    - **Left:** Components (Modular Cleanroom Components)
    - **Right:** Turnkey (End-to-End Engineering Services)
- **Visuals:** Animated background streams, hover glow effects.

### 9. Latest News Hub (`#latest-news-section`)
- **Header:** "Insights & Updates / Latest News"
- **Layout:** News Grid (`.news-hub-grid`)
    - **Left:** Featured Article (Large card).
    - **Right:** Secondary Article Stack (2 smaller cards).
- **Style:** Wave background SVG.

### 10. Trusted Partners (`.home-client-carousel-2`)
- **Header:** "Trusted Partners / Our Clients"
- **Layout:** Logo Carousel.

### 11. Social Proof (`#social-proof-section`)
- **Layout:** Split Row
    - **Left:** Testimonial Carousel (`.testimonial-home`).
    - **Right:** Stats Grid (Turnkey Projects, Expert Engineers, Compliance Rate).
- **Scripts:** CountUp animation for stats.

### 12. Dual CTA (`#cta-dual-section`)
- **Layout:** 2-Column Split
    - **Left:** Contact CTA ("Ready to Start?").
    - **Right:** Video CTA ("Why Choose PakGusu?" with Vimeo popup).

### 13. Footer
- **Type:** Standard Global Footer
- **Components:** Get In Touch, Address, More Links, Social Icons.

## Scripts & Libraries
- **Revolution Slider:** Hero banner.
- **Owl Carousel:** Intro sync, Industries, Partners, Testimonials.
- **Magnific Popup:** Video lightboxes.
- **IntersectionObserver:** Scroll animations (`fade-in-up`, etc) and Stats counter.
- **Custom JS:** Global Presence map logic, Solution Overview hover effects.
