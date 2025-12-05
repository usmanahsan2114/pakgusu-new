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
| Dropdown BG | Dark Blue | `#004685` |

### Footer (Fixed for Both Modes)
| Element | Color | Hex |
|---------|-------|-----|
| Background | Dark Blue | `#001528` |
| Widget Text | White | `#ffffff` |
| Links | Light Blue | `#29afe3` |
| Social Icons | White with accent hover | `#ffffff` → platform colors |

### Light Mode (Default)
| Element | Color | Hex |
|---------|-------|-----|
| Body Background | White | `#ffffff` |
| Surface/Cards | White | `#ffffff` |
| Text Headings | Near Black | `#1a1a2e` |
| Text Paragraphs | Dark Gray | `#333333` |
| Links | Dark Blue | `#004685` |
| Borders | Light Gray | `#e5e5e5` |
| Contact Panel BG | White | `#ffffff` |
| Contact Panel Text | Dark | `#333333` |

### Dark Mode (3-Tier Section Colors)
| Element | Color | Hex |
|---------|-------|-----|
| Primary BG | Darkest Blue | `#0a1628` |
| Secondary BG | Dark Blue | `#0d1d33` |
| Tertiary BG | Rich Dark Blue | `#0f2240` |
| Cards/Boxes | Rich Dark Blue | `#0f2240` |
| Headings | Pure White | `#ffffff` |
| Paragraphs | Near White | `#e8eef4` |
| Links | Light Blue | `#29afe3` |
| Borders | Blue-Gray | `#1e3a5f` |
| Accent | Light Blue | `#29afe3` |

## Section Color Separation
Dark mode uses alternating backgrounds for visual hierarchy:
1. **Primary (.bg-white)** → `#0a1628` (darkest)
2. **Secondary (.bg-gray)** → `#0d1d33` (medium)
3. **Tertiary (.section-full)** → `#0f2240` (lightest)

## Implementation

### CSS File
**`css/dark-mode-global.css`** - Comprehensive dark mode stylesheet containing:
- CSS custom properties
- Compact header/footer layout (75% width desktop)
- Section color separation
- Typography overrides
- Form styling
- Card/box styling
- Mobile navigation
- Contact slide-out panel

### CSS Selectors
Dark mode is activated via:
```css
html[data-theme="dark"] { }
body.dark-mode { }
```

### JavaScript
Located in `js/ui-ux-enhancements.js`:
- Toggle button injected into header
- User preference saved to `localStorage`
- No system preference detection

## Text Visibility
| Element | Light Mode | Dark Mode |
|---------|------------|-----------|
| Headings (h1-h6) | `#1a1a2e` | `#ffffff` |
| Paragraphs | `#333333` | `#e8eef4` |
| Bold/Strong | `#000000` | `#ffffff` |
| Links | `#004685` | `#29afe3` |
| Placeholders | `#666666` | `#6b8299` |

## Layout Features
- **Header/Footer Width**: 75% (desktop), 90% (tablet), 100% (mobile)
- **Footer Social Icons**: 6 icons (LinkedIn, YouTube, Twitter, Facebook, Instagram, Threads)
- **Dropdown Menus**: Dark blue with white text

> [!IMPORTANT]
> Do NOT use `prefers-color-scheme` media query. Always use class-based selectors.
