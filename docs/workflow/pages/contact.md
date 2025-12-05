# Contact Page Design Documentation

**URL:** `/contact/`
**Source File:** `intoriza/contact/index.html`
**Parent Template:** `contact-1.html`

## Page Overview
Provides contact information and a form for users to get in touch with PakGusu Technology.

## Section-by-Section Design

### 1. Header
- **Type:** Standard Global Header
- **Includes:** Dark Mode Toggle. Header is always Dark Blue (#004685) with Light Blue (#29afe3) accents. See [Dark Mode](../dark-mode.md).

### 2. Page Title / Breadcrumb
- **Type:** Inner Page Banner (`.wt-bnr-inr`)
- **Background:** Image overlay (`.overlay-primary`).
- **Content:** "Contact" text and breadcrumb navigation.

### 3. Contact Info & Form Section
- **Layout:** 2-Column
    - **Left Column:** Contact Form (`.cons-contact-form`)
        - Fields: Username, Email, Message.
        - Button: "Submit".
    - **Right Column:** Contact Details (`.contact-info`)
        - Phone, Email, Address iconic boxes (`.wt-icon-box-wraper`).

### 4. Google Map
- **Type:** Full-width Map (`.map-section`)
- **Implementation:** Embedded Google Maps iframe or API integration.

### 5. Footer
- **Type:** Standard Global Footer (Dark Blue #004685, Light Blue #29afe3 accents, white text)

## Scripts
- **Form Validation:** Likely uses standard HTML5 or a JS validator.
- **Map:** Google Maps script (if API based).
