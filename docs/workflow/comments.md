# Website Template Comments

## General Overview

The website uses a standard Bootstrap-based HTML template ("intoriza"). It relies heavily on jQuery and various plugins for sliders, carousels, and popups.

1.  **Relative Paths**: The template uses relative paths for assets. When moving files into subdirectories (e.g., `about/index.html`), all links to `css/`, `js/`, and `images/` must be updated to step up one level (e.g., `../css/style.css`). **Use the `fix_links_smart.py` script to handle this automatically.**
2.  **Static Header/Footer**: As mentioned in `workflow.md`, the header and footer are hardcoded in every file. This increases maintenance effort for navigation changes.
3.  **Mobile Menu**: The mobile menu is generated/handled by JavaScript in `custom.js`. Ensure the HTML structure for the navigation (`.header-nav`) remains consistent for it to work correctly.
4.  **Loader**: The site includes a preloader (`.loading-area`). If it gets stuck or you want to remove it, check `css/loader.min.css` and the relevant JS in `custom.js`. **Note:** A fallback timeout (3 seconds) has been added to `custom.js` to ensure the loader disappears even if `window.load` hangs.
