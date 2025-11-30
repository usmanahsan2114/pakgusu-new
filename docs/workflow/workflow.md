# Website Workflow Documentation

**Note:** See [`page-structure.md`](./page-structure.md) for the complete website structure and page hierarchy.
**Note:** See [`navigation-structure.md`](./navigation-structure.md) for navigation menu details and how to update it.

## Directory Structure

The website follows a structured directory layout where each page is its own directory containing an `index.html` file. This allows for clean URLs (e.g., `example.com/about/` instead of `example.com/about.html`).

### Key Directories:
- **`intoriza/`**: The root of the website.
  - **`index.html`**: The main homepage.
  - **`css/`**: Stylesheets.
  - **`js/`**: JavaScript files.
  - **`images/`**: Image assets.
  - **`fonts/`**: Font files.
  - **`plugins/`**: Third-party plugins (e.g., Revolution Slider).
  - **`[page-name]/`**: Directories for individual pages (e.g., `about/`, `services/`, `products/`). Each contains an `index.html`.

## Editing Existing Pages

To edit a page, navigate to its corresponding directory and open `index.html`.

**Example:** To edit the "About Us" page:
1.  Go to `intoriza/about/`.
2.  Open `index.html` in your code editor.
3.  Make your changes to the HTML content.
4.  Save the file.

## Adding New Pages

To add a new page to the website:

1.  **Create a Directory:** Create a new folder in `intoriza/` with the desired URL slug (e.g., `new-page`).
2.  **Copy Template:** Copy an existing `index.html` (e.g., from `about/` or `services/`) into your new folder.
3.  **Update Content:** Edit the new `index.html` to change the title, content, and meta tags.
4.  **Fix Links:** Ensure all relative links to CSS, JS, and images are correct. Since the file is one level deep, links should generally start with `../` (e.g., `../css/style.css`).
    *   *Note:* If you copy from a sibling directory (like `about/`), the links should already be correct.
5.  **Update Navigation:** Add a link to your new page in the header/navigation menu of **all** pages (since this is a static site, the header is repeated in every file).

## Updating Header and Footer

Since this is a static HTML website without a backend or build process that uses partials/includes:

*   The **Header** and **Footer** code is repeated in every `index.html` file.
*   **To make a global change** (e.g., adding a menu item or changing the footer address), you must update the HTML in **every single page** of the website.
*   Use "Find and Replace in Files" in your code editor to make this easier, but be careful to match the exact HTML structure.

## Link Management

Since the website uses a nested directory structure, managing relative links manually can be error-prone.

### The `fix_links_smart.py` Script

We have included a Python script `fix_links_smart.py` in the root directory to automate link updates.
**Usage:**
```bash
python fix_links_smart.py
```

## Git Workflow

1.  **Pull Latest Changes:** `git pull origin main` (or your working branch).
2.  **Make Changes:** Edit files as needed.
3.  **Run Link Fixer:** `python fix_links_smart.py` (optional but recommended).
4.  **Stage Changes:** `git add .`
5.  **Commit:** `git commit -m "Description of changes"`
6.  **Push:** `git push origin [branch-name]`
