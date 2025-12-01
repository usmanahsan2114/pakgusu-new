# Adding New Sections

To add a new section to a page (e.g., a new "Services" block, a "Testimonials" row, or a "Call to Action"), follow these steps:

## 1. Identify a Similar Section

Look at `intoriza/index.html` or other existing pages to find a section that looks similar to what you want. The template comes with many pre-designed blocks:
-   **Hero/Banner**: Top of the page.
-   **Icon Boxes**: For services or features.
-   **Text + Image**: For "About" sections.
-   **Counters**: For statistics.
-   **Team Members**: For "Our Team".
-   **Testimonials**: Carousel of reviews.
-   **Latest News**: Blog post previews.

## 2. Copy the HTML Code

1.  Open the source file (e.g., `index.html`).
2.  Locate the start and end of the section. It usually starts with a comment like `<!-- SECTION START -->` or a `div` with a class like `section-full`.
3.  Copy the entire block of HTML.

**Example Section Structure:**
```html
<!-- SECTION START -->
<div class="section-full p-t80 p-b50 bg-gray">
    <div class="container">
        <!-- Section Head -->
        <div class="section-head text-center">
            <h2 class="text-uppercase">Our Services</h2>
            <div class="wt-separator-outer">
                <div class="wt-separator style-square">
                    <span class="separator-left bg-primary"></span>
                    <span class="separator-right bg-primary"></span>
                </div>
            </div>
        </div>
        <!-- Section Content -->
        <div class="row">
            <!-- Content Columns -->
            <div class="col-md-4 col-sm-6">
                ...
            </div>
        </div>
    </div>
</div>
<!-- SECTION END -->
```

## 3. Paste and Customize

1.  Paste the code into your target file (e.g., `services/index.html`) where you want it to appear.
2.  **Update Text**: Change headings, paragraphs, and button text.
3.  **Update Images**: Change `src` attributes to point to your new images. **Remember to use correct relative paths** (e.g., `../images/my-new-image.jpg`).
4.  **Update Links**: Update `href` attributes for buttons or links.

## 4. Adjust Styling (Optional)

If you need to change background colors or spacing:
-   **Padding**: Use helper classes like `p-t80` (padding-top: 80px), `p-b50` (padding-bottom: 50px) if available, or add your own inline style/custom class.
-   **Background**: Change `bg-gray` to `bg-white` or `bg-primary` (defined in `skin-1.css`).
-   **Text Color**: Use `text-white`, `text-black`, `text-primary`.

## 5. Verify Responsiveness

After adding the section, check the page in a browser and resize the window to ensuring it looks good on mobile devices. The template uses Bootstrap grid (`col-md-4`, `col-sm-6`, etc.), so it should handle responsiveness automatically if you stick to the grid structure.

## 6. Section Transitions (SVG Waves)

To create smooth visual transitions between sections with different background colors (e.g., White to Gray), use the SVG wave separator.

**HTML Structure:**
Insert this block at the very end of the section (inside the section container):

```html
<div class="wave-separator">
    <svg viewBox="0 0 1200 120" preserveAspectRatio="none">
        <path d="..." class="shape-fill [COLOR_CLASS]"></path>
    </svg>
</div>
```

**Color Classes:**
-   `white`: Use when the *next* section is White (or if the current section is White and you want to transition to Gray, use the wave color matching the *next* section? No, usually the wave matches the *current* section's background to "spill over" or matches the *next* section to "cut into"?
    -   Actually, the implementation uses `shape-fill` to color the wave.
    -   If Current is White and Next is Gray: Use **Gray** wave at the bottom of Current (to look like Gray is rising up? Or White is dripping down?).
    -   Let's check `index.html` usage.
    -   Hero (Dark) -> Who We Are (White). Wave is White. (White wave at bottom of Hero).
    -   Who We Are (White) -> Cleanroom Products (Gray). Wave is Gray. (Gray wave at bottom of Who We Are).
    -   Cleanroom Products (Gray) -> Industries (White). Wave is White. (White wave at bottom of Cleanroom Products).
    -   **Rule:** The wave color should match the **background color of the NEXT section**.

**Usage Rule:**
-   If the **NEXT** section is **White**, use `class="shape-fill white"`.
-   If the **NEXT** section is **Gray**, use `class="shape-fill gray"`.

