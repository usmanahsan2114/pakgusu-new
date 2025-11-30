# Complete UI/UX Visual Plan (HTML/CSS - Intoriza Theme Aligned)

This UI/UX plan integrates the aesthetic and interaction elements of the Intoriza WordPress theme, adapted for a pure HTML/CSS implementation for Pakgusu.

## Theme Overview

- **Primary Colors**: Dark Blue `#004685`, Light Blue `#29afe3`
- **Typography**: Sans-serif fonts; modern, clean, and readable.
- **Layout Base**: Intoriza's grid, card, and masonry system.
- **Structure**: Static HTML using semantic HTML5 tags. CSS handles all layout and animation.

---

## Global Elements

### Navigation
- Sticky header with dropdowns.
- On-scroll shrink effect.
- Hover underline animation for nav items.
- Mobile menu with slide-in effect.

### Footer
- 3-column layout with links, contact form, and newsletter.
- Hover reveal effect on links.
- Background wave SVG pattern animated using `@keyframes`.

### Hero Banners
- Full-screen section with parallax background scroll.
- Animated text and CTA fade-in with delay.
- Use `scroll-reveal.js` or custom `@keyframes` CSS for fade/slide effects.

---

## Page-Wise UI Details

### 1. Home Page
- Sections: Hero, About, Products Preview, Industries, Testimonials, News, Contact CTA.
- Animations:
  - Hero: Text fade-in + button bounce.
  - Product cards: Staggered fade-in.
  - Scroll indicators using SVG path animation.

### 2. About Us
- Timeline animation for company history.
- Section divider lines that animate on scroll.
- Team cards with hover flip or fade.

### 3. Products
- Masonry layout using CSS Grid.
- Product cards with hover zoom + shadow effect.
- Filterable categories with animation.

### 4. Services
- Icon cards with float-on-hover.
- Background micro-interactions (CSS wave pulse).
- Accordion for service detail toggles.

### 5. Industries
- Horizontal scroll section for logos/clients.
- Category navigation with tab-like UX.
- Custom SVG backgrounds per industry.

### 6. Blog & News
- Blog listing: Fade-on-scroll, image scale on hover.
- Detail page: Featured image scroll-reveal.
- Sidebar: Sticky behavior with CTA button.

### 7. Case Studies
- Gallery-style layout with hover-reveal project title.
- Modal popup for detail (HTML/CSS modal or lightbox).

### 8. FAQs
- Accordion with smooth expand/collapse.
- Icons change on toggle (plus/minus animation).

### 9. Careers
- Job listing cards with floating application button.
- Filter by department or role.

### 10. Contact
- Input fields with animated underline focus.
- Map background with pin animation.
- Submit button expands on hover with arrow slide-in.

---

## Responsiveness
- Uses CSS Flexbox and Grid.
- Mobile-first layout with burger navigation.
- Breakpoints for: 768px, 992px, 1200px.

## Microinteractions
- Hover/Focus animations on all links and buttons.
- Section dividers animate in when visible.
- Smooth scrolling enabled across site.

## Libraries & Tools (optional)
- ScrollReveal.js (or pure CSS animation).
- Swiper.js for sliders.
- AOS.css if preferring lightweight animation on scroll.

---

## Animation Principles
- Use `transition: all 0.3s ease-in-out` for smoothness.
- Delay animations to guide user attention.
- Keep interactions lightweight for performance.