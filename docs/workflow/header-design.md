# Header Design Documentation

## Overview
The header uses a fixed **dark blue design** across both light and dark modes, providing consistent branding.

## Header Structure
```
header.site-header.header-style-1
├── .sticky-header.main-bar-wraper
│   └── .main-bar.bg-white
│       ├── .logo-header (Logo)
│       ├── .header-nav (Navigation)
│       └── .extra-nav (Contact Button + Dark Mode Toggle)
```

## Color Scheme
| Element | Color | Hex |
|---------|-------|-----|
| Background | Dark Blue | `#004685` |
| Nav Text | White | `#ffffff` |
| Nav Hover | Light Blue | `#29afe3` |
| Dropdown BG | Dark Blue | `#004685` |
| Dropdown Text | White | `#ffffff` |
| Dropdown Hover | Light Blue | `#29afe3` |

## Navigation Structure
```
Home | About Us | Products ▼ | Services | Industries ▼ | Resources ▼ | Contact
```

### Dropdown Menus
- **Products**: 6 items
- **Industries**: 6 items  
- **Resources**: 4 items

## Layout
- **Desktop**: 75% width, centered
- **Tablet (≤1400px)**: 90% width
- **Mobile (≤991px)**: 100% width

## Dark Mode Toggle
Located in the header's extra-nav section:
- Moon icon (☾) for light mode
- Sun icon (☀) for dark mode
- Stored in `localStorage`

## Mobile Navigation
- Dark blue background (#004685)
- White text
- Light blue hover state

## Contact Slide-out Panel
| Mode | Background | Text |
|------|------------|------|
| Light | White | Dark Gray |
| Dark | Dark Blue | Near White |

## CSS Files
- `css/style.css` - Base header styles
- `css/dark-mode-global.css` - Contains header overrides
