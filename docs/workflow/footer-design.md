# Footer Design Documentation

## Overview
The footer uses a consistent **dark blue design** across both light and dark modes, with white text and light blue accents.

## Footer Structure
```
footer.site-footer
├── #footer-main-section (Footer Top)
│   ├── .footer-link (Quick Links)
│   ├── .widget.getin-touch (Contact Info)
│   ├── .widget.widget_address (Address)
│   └── .new-footer-social-icon (Social Icons)
└── #footer-bottom-section (Copyright)
```

## Color Scheme
| Element | Color | Hex |
|---------|-------|-----|
| Main Background | Dark Blue | `#001528` |
| Text | White | `#ffffff` |
| Links | Light Blue | `#29afe3` |
| Link Hover | Brighter Blue | `#5dd4ff` |
| Widget Titles | White | `#ffffff` |
| Borders | Transparent Blue | `rgba(41, 175, 227, 0.2)` |

## Social Media Icons
The footer includes 6 social media icons:

| Icon | Class | Hover Color |
|------|-------|-------------|
| LinkedIn | `fa-linkedin` | `#0077b5` |
| YouTube | `fa-youtube-play` | `#ff0000` |
| Twitter | `fa-twitter` | `#1da1f2` |
| Facebook | `fa-facebook` | `#1877f2` |
| Instagram | `fa-instagram` | Gradient |
| Threads | `fa-at` | `#000000` |

### HTML Structure
```html
<div class="new-footer-social-icon">
    <a href="#" aria-label="LinkedIn"><i class="fa fa-linkedin"></i></a>
    <a href="#" aria-label="YouTube"><i class="fa fa-youtube-play"></i></a>
    <!-- ... more icons -->
</div>
```

## Layout
- **Desktop**: 75% width, centered
- **Tablet (≤1400px)**: 90% width
- **Mobile (≤991px)**: 100% width with padding

## CSS Files
- `css/footer-master.css` - Main footer styles
- `css/footer-main-master.css` - Footer-main section styles
- `css/dark-mode-global.css` - Contains footer overrides

## Footer Links (More Links Section)
- About
- Products
- Blog
- Case Studies
- Careers
- Contact Us
