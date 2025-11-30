# Website Template Comments

## General Overview

The website uses a standard Bootstrap-based HTML template ("intoriza"). It relies heavily on jQuery and various plugins for sliders, carousels, and popups.

## CSS Architecture

*   **`css/bootstrap.min.css`**: Core framework.
*   **`css/style.css`**: Main custom styles for the template. This is where most global style changes should happen.
*   **`css/skin/skin-1.css`**: Theme color scheme. Edit this file to change the primary/secondary colors of the site.
*   **`css/custom.css`** (if exists) or add one: Recommended for your own custom overrides to avoid modifying the original template files too heavily.

## JavaScript & Plugins

*   **`js/custom.js`**: Contains the main initialization logic for the template's features (mobile menu, sticky header, etc.).
*   **Revolution Slider**: Used for the main hero banner on the homepage. Configuration is in `js/rev-script-2.js` (or similar, check the specific page).
*   **Owl Carousel**: Used for client logos, testimonials, and other sliders.

## Known Quirks & Considerations

1.  **Relative Paths**: The template uses relative paths for assets. When moving files into subdirectories (e.g., `about/index.html`), all links to `css/`, `js/`, and `images/` must be updated to step up one level (e.g., `../css/style.css`). **Use the `fix_links_smart.py` script to handle this automatically.**
2.  **Static Header/Footer**: As mentioned in `workflow.md`, the header and footer are hardcoded in every file. This increases maintenance effort for navigation changes.
3.  **Mobile Menu**: The mobile menu is generated/handled by JavaScript in `custom.js`. Ensure the HTML structure for the navigation (`.header-nav`) remains consistent for it to work correctly.
4.  **Loader**: The site includes a preloader (`.loading-area`). If it gets stuck or you want to remove it, check `css/loader.min.css` and the relevant JS in `custom.js`.
