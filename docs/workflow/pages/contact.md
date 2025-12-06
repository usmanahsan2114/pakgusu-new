# Contact Page Design Documentation

**URL:** `/contact/`
**Source File:** `intoriza/contact/index.html`

## Page Overview
Primary contact interface featuring a redesigned location showcase, contact grid, and inquiry form.

## Section-by-Section Design

### 1. Header
- **Type:** Standard Global Header
- **Includes:** Dark Mode Toggle, Mobile Menu.

### 2. Page Title / Hero
- **Type:** Inner Page Banner (`.wt-bnr-inr`)
- **Background:** Image (`banner/4.jpg`) with black overlay.
- **Content:** Title "Contact Us", Breadcrumb "Home / Contact Us".

### 3. Location & Map Section (`.new-location-section`)
- **Layout:** Duo-Card Wrapper (`.new-location-wrapper`)
    - **Location Card:** "Visit Us / Lahore Office", Address, Phone/Email links, "Get Directions" button.
    - **Map Card:** Embedded Google Map iframe (showing New York placeholder/custom location).

### 4. Contact Ways Grid (`.new-contact-section`)
- **Header:** "Trust & Recommend / Contact Us"
- **Layout:** 4-Column Grid (`.new-contact-grid`)
- **Items:**
    1.  **Phone Support:** Icon, Number +92..., Link.
    2.  **Email Us:** Icon, info@pakgusu.com link.
    3.  **Office Address:** Icon, Address text, "View on map" link.
    4.  **WhatsApp:** Icon, direct WA link.

### 5. Contact Form Section (`.new-form-section`)
- **Header:** "Let's Connect / Get In Touch"
- **Form Wrapper:** `.new-form-wrapper`
- **Fields:** Name, Email, Message (Textarea).
- **Button:** "Send Message" (Submit).

### 6. Footer
- **Type:** Standard Global Footer
- **Features:** "Get In Touch", Address, More Links columns, Social Icon row, Copyright bar.
