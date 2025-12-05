# Dark Mode Feature

## Overview
The website includes a **user-controlled dark mode toggle**. Dark mode is **NOT** activated based on system preferences—the site defaults to **Light Mode** for all users until they manually click the dark mode button.

## Color Scheme

### Header (Fixed for Both Modes)
| Element | Color | Hex |
|---------|-------|-----|
| Background | Dark Blue | `#004685` |
| Accent/Hover | Light Blue | `#29afe3` |
| Text | White | `#ffffff` |

### Footer (Fixed for Both Modes)
| Element | Color | Hex |
|---------|-------|-----|
| Background | Dark Blue | `#004685` |
| Bottom Section | Darker Blue | `#003366` |
| Accent/Hover | Light Blue | `#29afe3` |
| Text | White | `#ffffff` |

### Light Mode (Default)
| Element | Color | Hex |
|---------|-------|-----|
| Background | White | `#ffffff` |
| Surface/Cards | White | `#ffffff` |
| Text Primary | Near Black | `#1a1a1a` |
| Text Secondary | Gray | `#525252` |
| Borders | Light Gray | `#e5e5e5` |

### Dark Mode
| Element | Color | Hex |
|---------|-------|-----|
| Background | Very Dark Blue | `#0a1628` |
| Surface/Cards | Dark Blue | `#0f2240` |
| Text Primary | Near White | `#f0f4f8` |
| Text Secondary | Light Blue-Gray | `#a0b3c6` |
| Borders | Blue-Gray | `#1e3a5f` |
| Accent | Light Blue | `#29afe3` |

## Implementation

### CSS Files
- **`css/dark-mode-global.css`** - Main dark mode stylesheet (applies to all pages)
- Individual section CSS files have class-based dark mode overrides

### CSS Selectors
Dark mode is activated via:
- `html[data-theme="dark"]`
- `body.dark-mode`

### JavaScript
Located in `js/ui-ux-enhancements.js`:
- Toggle button injected into header
- User preference saved to `localStorage`
- No system preference detection (`prefers-color-scheme` removed)

## Files Modified
- All 25+ `index.html` pages - linked `dark-mode-global.css`
- Removed `@media (prefers-color-scheme: dark)` from all CSS files

> [!IMPORTANT]
> Do NOT use `prefers-color-scheme` media query. Always use class-based selectors.
