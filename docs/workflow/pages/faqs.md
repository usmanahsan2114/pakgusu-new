# FAQs Page Design Documentation

**URL:** `/resources/faqs/`
**Source File:** `intoriza/resources/faqs/index.html`
**Parent Template:** Blog Detail / Sidebar Layout

## Page Overview
Currently structured as a "Post Gallery" or Blog-style page rather than a standard Accordion FAQ list. It features a main content area with a blog post and a "Frequently Asked Questions" section that displays blog grid items, plus a sidebar.

## Section-by-Section Design

### 1. Header
- **Type:** Standard Global Header

### 2. Page Title / Hero
- **Type:** Inner Page Banner (`.wt-bnr-inr`)
- **Background:** Image (`banner/3.jpg`).
- **Content:** Title "Post right sidebar", Breadcrumb "Home / Post Gallery".

### 3. Main Content Area (Left Column 8/12)
- **Primary Post:** Large blog post (`.blog-post`) with owl-carousel slider images (`.owl-fade-slider-one`) and text content.
- **FAQ Grid:** Section titled "Frequently Asked Questions".
    - **Content:** 2-column grid of blog/article cards (`.blog-grid-1`) with images, titles, meta data, and "Read More" buttons.
- **Comments Section:** List of comments and "Leave a Comments" form.

### 4. Sidebar (Right Column 4/12)
- **Search:** Input field.
- **Recent Posts:** List of recent articles with dates (`.recent-posts-entry`).
- **Tags:** Tag Cloud.
- **Categories:** List of categories.
- **Gallery:** Small thumbnail grid (`.widget_gallery`).

### 5. Support Section
- **Location:** Below main content content (`.bg-gray`).
- **Content:** "Need More Information?", "Get in Touch" button.

### 6. CTA Section
- **Background:** Image (`bg-1.jpg`).
- **Content:** "Ready to Start?", "Contact Us" button.

### 7. Footer
- **Type:** Standard Global Footer
