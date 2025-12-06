# About Page Design Documentation

**URL:** `/about/`
**Source File:** `intoriza/about/index.html`
**Parent Template:** `about-1.html`

## Page Overview
The About page tells the PakGusu story, highlighting its transition to local manufacturing, its partnership with GUSU China, and its commitment to quality and compliance. It features a narrative-driven layout with specific sections for history, company values, and manufacturing capabilities.

## Section-by-Section Design

### 1. Header
- **Type:** Sticky Global Header
- **Components:** Logo, Main Navigation, Dark Mode Toggle.

### 2. Page Title / Breadcrumb
- **Background:** Image (`banner-1.jpg`) with overlay.
- **Content:** "About" title, "Home / About" breadcrumb.

### 3. Company Introduction (`#intro-section`)
- **Layout:** 2-Column Split
    - **Left:** Image Slider (Owl Carousel `.about-home`) with navigation dots.
    - **Right:** Text Content ("Welcome to PakGusu").
- **Content:** Story of localization ("Technological Independence"), partnership mention, and core mission.
- **Signature:** "CEO, PakGusu" signature image.

### 4. Governance & Leadership (`#governance-section`)
- **Header:** "Leadership & Governance / Governance"
- **Layout:** 3-Card Row (`.gov-card`)
    - **Cards:** Board of Directors, Executive Committee, Compliance Board.
- **Visuals:** Hover effects (`.hover-line`), icons (`flaticon-sketch`, etc.).

### 5. Quality & Compliance (`#quality-compliance-redesign`)
- **Header:** "Quality & Compliance"
- **Background:** Grid pattern animation (`.qc-grid-dots`).
- **Layout:** Split Dashboard Card
    - **Left:** "Compliance Pillars" narrative, ISO chips (ISO 14644, ISO 9001, GMP).
    - **Right:** Tabbed Details (ISO Standards, Certifications, QA Philosophy).
- **KPI Band:** Badges for "Years operating", "Non-conformance rate", "On-time completion".
- **Interaction:** Javascript tabs and KPI number count-up.

### 6. Corporate History (`#story-timeline`)
- **Header:** "Our Journey / Our Story"
- **Layout:** Interactive Timeline
    - **Top:** Horizontal Step Navigation (2018, 2020, 2022, 2023, 2024).
    - **Bottom:** Dynamic Content Panel (`.timeline-panels`).
- **Content:** Milestones from "The Beginning" to "Global Standards".

### 7. Process Overview
- **Header:** "How We Work / Our Process"
- **Layout:** 4-Column Icon Grid
    1.  Consultation
    2.  Design
    3.  Manufacturing
    4.  Installation

### 8. Global Partnership (`#global-partnership`)
- **Header:** "Global Expertise / Partnership with GUSU China"
- **Background:** Revolving globe animation.
- **Layout:** Split
    - **Left:** Narrative, Alliance Strip (PakGusu ~ GUSU China), Action Badges.
    - **Right:** Hero Visual Card with "20+ Joint Projects" overlay.

### 9. Mission, Vision, Values (`#mission-vision-values`)
- **Header:** "Our Core Values / Mission, Vision & Values"
- **Layout:** "Culture Panel" (Split Card)
    - **Left:** Vertical Pillar Selector (Mission, Vision, Values).
    - **Right:** Dynamic Detail Panel with descriptions and tags.
- **Visuals:** Subtle beam background animation.

### 10. Facility & Capabilities (`#facility-overview`)
- **Header:** "State-of-the-Art / Our Facility & Capabilities"
- **Background:** Blueprint grid animation (`.facility-grid-lines`).
- **Layout:** Split
    - **Left:** Media Card with stats overlay (Facility size, Production Ops, ISO).
    - **Right:** Description + 4-Tile Grid (Adv. Mfg Lines, In-Line QC, High-Throughput, Custom Engineering).

### 11. Team
- **Header:** "Our Best Team / Our Team"
- **Layout:** 4-Column Grid
- **Content:** Team member cards with photos and social links.

### 12. Footer
- **Type:** Standard Global Footer.

## Scripts & Libraries
- **Owl Carousel:** Intro slider.
- **IntersectionObserver:** Animate elements on scroll (timeline, KPIs).
- **Custom JS:** Tab switching logic for Governance, Compliance, Timeline, MVV, and Facility sections. Number counters.
