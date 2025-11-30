
# Complete UI/UX Visual Plan

## Global Design System

- **Framework:** React SPA or multi-page app with client-side routing (e.g., React Router).
- **Theme Colors:**
  - Primary: Dark Blue `#004685`
  - Accent: Light Blue `#29afe3`
  - Neutrals: White, light grey backgrounds, dark grey text
- **Typography:**
  - Headings: Modern sans-serif (e.g., Inter / Poppins), bold
  - Body: Readable sans-serif (e.g., Inter / Roboto), regular
  - Minimum base font-size: 16px
- **Grid & Spacing:**
  - 12-column responsive grid
  - Generous vertical spacing between sections (64–96px desktop)
- **Navigation:**
  - Sticky top nav with semi-transparent dark-blue background
  - Logo left, menu center/right, primary CTA (“Contact”) as outlined button
  - Mobile: Hamburger menu with full-screen slide-down panel
- **Footer:**
  - Dark-blue background, white text
  - Columns: About snippet, key links, contact info, social icons

## Global Interactions & Animations

- **Page Load:**
  - Fade-in of hero content and slight upward motion of CTAs (200–300ms)
- **Scroll Reveal:**
  - Sections animate in with `opacity` and `translateY` (30–40px) once on first view
- **Hover States:**
  - Buttons: Background shifts from #29afe3 to slightly darker shade; subtle box-shadow
  - Cards: Light elevation + border highlight in #29afe3
  - Links: Underline or bottom border animation
- **Background Motion:**
  - Subtle animated SVG “waves” in light blue behind select sections (home hero, CTAs)
  - Very slow movement to avoid distraction (CSS keyframes, reduced-motion respected)
- **Accessibility:**
  - Respect `prefers-reduced-motion` (disable non-essential animations)
  - High contrast for text vs background
  - Keyboard-focus outlines on interactive elements

---

## Home Page UI/UX

- **Hero:**
  - Full-height section, dark-blue overlay on cleanroom image
  - Left-aligned content on desktop; centered on mobile
  - Elements:
    - H1 headline
    - 1–2 line subheadline
    - Primary CTA button (“Request a Quote”)
    - Secondary CTA (“View Solutions”)
  - Animation: Staggered; heading -> subheading -> buttons

- **Who We Are:**
  - Two-column layout: Text (left), image (right)
  - Short stat row below (e.g., years experience, projects delivered)
  - Scroll reveal from bottom; numbers can count-up

- **Our Solutions (Products + Services):**
  - Two large cards side-by-side (stacked on mobile)
  - Icons at top, heading, 2-line description, deep-link CTA
  - Hover: Raise + accent border glow

- **Product Highlights:**
  - Horizontal card carousel with arrows (desktop) / swipe (mobile)
  - Each card: product image, title, bullet of benefits
  - Auto-scroll (optional) with pause on hover

- **Industries We Serve:**
  - Icon grid 2×3
  - Each icon inside circular light-blue background
  - On hover: subtle rotation/scale of icon

- **Why Choose PakGusu:**
  - Dark-blue band with 3–4 large metrics (counters)
  - White text, minimal decoration
  - Counters animate from 0 to target upon scroll

- **Latest from Resources:**
  - Two-column: Blog and News lists (2 cards each)
  - Cards: category label, date, title, short snippet

- **CTA Banner:**
  - Light-blue strip near footer
  - Short line + single primary CTA button
  - Full-width, text centered on mobile

---

## About Us Page UI/UX

- **Hero:**
  - Medium-height banner; subtle pattern over dark blue
  - Title + one-line descriptor

- **Company Snapshot:**
  - 3-column summary (founded, facility, industries)
  - Each with icon + label + value

- **Timeline:**
  - Horizontal on desktop, vertical stacked on mobile
  - Stepper dots connected by line
  - Clicking/hovering a year highlights description

- **Partnership Section:**
  - Split layout with PakGusu & GUSU logos
  - Structured text explaining partnership
  - Optional “view partner site” link

- **Mission & Values:**
  - Card grid; each value card uses icon and 2–3 lines
  - Scroll animation: cards staggered row by row

- **Facility & Quality Sections:**
  - Alternating image/text sections for visual rhythm
  - Use photos of plant or equipment
  - Info boxes highlight certifications and standards

- **CTA:**
  - Centered block with “Download Profile” + “Contact” buttons

---

## Products UI/UX

### Products Overview

- **Category Grid:**
  - 3×2 cards, equal height
  - Each card: image top, title, 2–3 lines, “View Product” link
  - Hover: card lifts, overlay tint in light blue

### Product Detail Pages

- **Hero:**
  - Narrow banner with product shot
  - Breadcrumb navigation above title: `Home / Products / Cleanroom Panels`

- **Content Layout:**
  - Overview text full-width for readability
  - Secondary sections use two-column layout where possible
  - On small screens, stack vertically

- **Tabs / Accordions:**
  - For variants (e.g., PU/XPS/Rockwool) and technical specs
  - Tabs at top with underlined active tab
  - Accordion in mobile view to conserve space

- **Spec Table:**
  - Striped table styling
  - On mobile, horizontal scroll or stacked rows for accessibility

- **Gallery:**
  - Masonry or standard grid
  - Click opens lightbox carousel

- **CTA Stripe:**
  - Thin full-width bar: “Need detailed specs?” + button

---

## Services Page UI/UX

- **Hero & Overview:**
  - Visual of team planning or cleanroom under construction
  - Short bullet list of what’s covered

- **Process Timeline:**
  - Horizontal stepped progress bar on desktop
  - Each step clickable to scroll to corresponding section
  - On mobile: vertical list of phases with micro icons

- **Phase Sections:**
  - Each phase uses consistent section layout:
    - Icon
    - Phase title
    - 2–3 short paragraphs
    - Bullet benefits

- **Workflow Diagram:**
  - Simple React SVG or static image
  - Optionally animated arrow hints

- **CTA:**
  - Card with small form trigger: button opens contact modal prefilled with “Turnkey Project Inquiry”

---

## Industries UI/UX

### Industries Overview

- **Card Grid:**
  - Visual emphasis on imagery: each card uses full-bleed background image of industry
  - Title overlay at bottom with gradient for readability

### Industry Detail Pages

- **Hero:**
  - Industry-specific hero image
  - Tag showing “Industry” type

- **Sections:**
  - Use warning/info callout boxes for regulations
  - Use icon-labeled bullets for challenges vs solutions

- **Related Content:**
  - Sidebar on desktop showing related products & case studies
  - On mobile, this becomes “Related” section at bottom

---

## Resources, Blog & News UI/UX

### Resources Hub

- **Layout:**
  - Intro text + three feature tiles (Standards, Blog, News, FAQs)
  - Each tile uses icon + short explanation

### Cleanroom Standards & Classifications

- **Visuals:**
  - Diagram illustrating class differences
  - Table styled for clarity
  - Callout cards showing “Typical class by industry”

### Blog

- **Listing:**
  - Card list with featured image, category tag, title, excerpt, date
  - Pagination or “Load More” button

- **Filters:**
  - Horizontal chip filters (e.g., “Pharma”, “HVAC”, “Regulations”)
  - Selected filter highlighted in light blue

### News & Events

- **Layout:**
  - Similar to blog but prioritizing date + event type badges
  - “Upcoming” section pinned at top when events present

### FAQs

- **Interaction:**
  - Accordion items grouped by category
  - Only one accordion open at a time (optional)
  - Clear “+ / –” icons for open/close state

---

## Case Studies UI/UX

- **Listing Page:**
  - Card layout with industry tag, project title, short result (“30% fewer defects”)
  - Filter bar (industry, solution type)

- **Detail Template:**
  - Top section with summary stats highlighted in badges
  - Structured layout: Challenge → Solution → Results → Testimonial
  - Pull quotes styled prominently

---

## Careers UI/UX

- **Hero:**
  - Friendly imagery of team collaboration
  - Short employer-brand message

- **Open Roles:**
  - Accordion or list, each role expandable
  - “Apply Now” button opens application form or mailto

- **Culture Section:**
  - Icon-based highlights (growth, learning, impact)

---

## Contact Page UI/UX

- **Layout:**
  - Two-column on desktop: form (left), info + map (right)
  - Stacked on mobile

- **Form UX:**
  - Floating labels or clear labels above inputs
  - Inline validation messages
  - Success banner replacing form or appearing above after submission

- **Map:**
  - Embedded map with grayscale styling to match theme (optional)

- **Support Info:**
  - Emphasize response time and channels (email, phone, WhatsApp)
