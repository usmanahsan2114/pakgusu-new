# Full Website Page Structure

## Top-Level Pages

- Home (`/index.php`)
- About Us (`/about/index.php`)
  - About Pak Gusu (`/about/pak-gusu/index.php`)
  - About GUSU China (`/about/gusu-china/index.php`)
  - Cleanroom Standards (`/about/cleanroom-standards/index.php`)
- Products (`/products/index.php`)
  - Clean Room Panels (`/products/clean-room-panels/index.php`)
  - Windows (`/products/windows/index.php`)
  - Doors (`/products/doors/index.php`)
  - Transfer Window (`/products/transfer-window/index.php`)
  - Aluminum Profile (`/products/aluminum-profile/index.php`)
  - Clean LED Lights (`/products/clean-led-lights/index.php`)
- Services (`/services/index.php`)
  - Planning & Design (`/services/planning-design/index.php`)
  - Clean Room Construction (`/services/clean-room-construction/index.php`)
  - Installation (`/services/installation/index.php`)
  - After-Sale Services (`/services/after-sale-services/index.php`)
- Sectors (`/sectors/index.php`)
  - Pharmaceutical / Nutraceutical (`/sectors/pharmaceutical/index.php`)
  - Hospital & Healthcare (`/sectors/hospital/index.php`)
  - Food Industry (`/sectors/food-industry/index.php`)
  - Electronics Manufacturing (`/sectors/electronics/index.php`)
  - Research Laboratories (`/sectors/laboratories/index.php`)
  - Medical / Surgical Devices (`/sectors/medical-devices/index.php`)
- Portfolio (`/portfolio/index.php`)
  - Gallery View (`/portfolio/gallery/index.php`)
  - Masonry View (`/portfolio/masonry/index.php`)
- Blog (`/blog/index.php`)
  - Grid View (`/blog/grid/index.php`)
  - List View (`/blog/list/index.php`)
  - Masonry View (`/blog/masonry/index.php`)
- Contact (`/contact/index.php`)

## Notes

- All internal pages use PHP includes for header, footer, and modular sections
- The `$path` variable is used throughout for dynamic asset path resolution
- View switchers implemented for Portfolio and Blog sections
- Cleanroom Standards moved to About section instead of standalone Resources section
