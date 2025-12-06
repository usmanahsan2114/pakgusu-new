# Services Page Design Documentation

**URL:** `/services/`
**Source File:** `intoriza/services/index.html`
**Parent Template:** N/A (Custom Layout)

## Page Overview
Details the turnkey cleanroom services offered by PakGusu, emphasizing a 3-step delivery model and a detailed workflow from consultation to validation.

## Section-by-Section Design

### 1. Header
- **Type:** Standard Global Header
- **Includes:** Dark Mode Toggle. Header is always Dark Blue (#004685) with Light Blue (#29afe3) accents.

### 2. Page Title / Breadcrumb
- **Type:** Inner Page Banner (`.wt-bnr-inr`)
- **Content:** "Turnkey Cleanroom Solutions" (h1).

### 3. Process Journey (How We Deliver)
- **ID:** `#how-we-deliver`
- **Class:** `.process-journey-section`
- **Design:** Tabbed Interface with Split Layout.
    - **Header:** "Assessment • Engineering • Delivery".
    - **Left (Desktop):** Image panel (`.journey-image-panel`) changing based on active step.
    - **Right (Desktop):** Vertical Tabs (`.journey-trigger`) that reveal content (`.journey-content`) on click or auto-rotate.
- **Workflow Steps:**
    1.  **Assessment:** Site analysis & envelope definition.
    2.  **Engineering:** ISO-compliant design & simulation.
    3.  **Delivery:** Execution & compliant handover.
- **Mobile Behavior:** Stacked layout with image in middle and content at bottom.

### 4. Cleanroom Delivery Workflow (Detailed)
- **ID:** `#cleanroom-delivery-workflow`
- **Class:** `.cdw-section`
- **Design:** Interactive Slider.
    - **Navigation:** Numbered dots (01, 02, 03) and arrows.
    - **Cards:** Slide transition effect (`.cdw-slide`). Split layout with Image (Left) and Content (Right).
- **Slides:**
    1.  **Consultation & Planning:** ISO Class & User Requirements.
    2.  **Design & Fabrication:** 3D Layouts & Local Manufacturing.
    3.  **Execution & Validation:** Installation & IQ/OQ/PQ.

### 5. Turnkey Cleanroom CTA
- **ID:** `#turnkey-cleanroom-cta`
- **Design:** Elevated card layout (`.cta-card`) with shadow and "bg-pattern" decoration.
- **Content:**
    - **Left:** "Ready to Start?" kicker, main heading, description, 3-item feature list (ISO layouts, HVAC, Validation), and button.
    - **Right:** Visual image with a floating badge ("Proposal in days, not weeks").
- **Dark Mode:** Card background changes to `#1e293b`.

### 6. Footer
- **Type:** Standard Global Footer
