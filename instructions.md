# Antigravity Website Design Prompt: LightGallery Dark Portfolio

## Role
Senior Frontend Developer & UI/UX Designer.

## Objective
Build a single-page responsive photo album website using **LightGallery.js** for the image viewing experience.

## Design Aesthetic
- **Theme:** Premium Dark Luxury / Minimalist Portfolio.
- **Color Palette:** - Background: `#0a0a0a` (Near black)
    - Surface: `#161616` (Card/Grid background)
    - Text: `#ffffff` (High contrast headers)
    - Accent: Subtle gold or gray for meta-info.
- **Layout:** A clean, responsive grid using `CSS Grid` with `auto-fill` and a `20px` gap. Use `object-fit: cover` to ensure all thumbnails are uniform and professional.
- **Micro-interactions:** - Smooth scaling on hover: `transform: scale(1.03)`.
    - A semi-transparent overlay that fades in on hover with the text "VIEW IMAGE" in minimalist sans-serif typography.

## Technical Specifications
1. **Dependencies:** - Integrate **LightGallery.js** (v2.x) via CDN.
   - Include **lg-zoom** and **lg-thumbnail** plugins.
2. **Core Functionality:**
   - **One-Page Listing:** List all photo thumbnails on the primary landing page.
   - **Enlargement Logic:** Clicking a thumbnail must trigger the LightGallery lightbox.
   - **Navigation:** Enable seamless "Next/Previous" navigation within the lightbox, including support for touch swipes and keyboard arrow keys.
   - **Backdrop Styling:** The lightbox background must use glassmorphism: `background: rgba(0, 0, 0, 0.8)` with `backdrop-filter: blur(12px)`.
3. **Responsive Design:** - Mobile: 1 column.
   - Tablet: 2 columns.
   - Desktop: 3 to 4 columns.

## Content Setup
- Use high-resolution placeholder images (e.g., from Unsplash) to demonstrate the gallery.
- Add a minimalist header section:
    - **H1 Title:** "VISIONS 2026"
    - **Sub-headline:** "A curated visual exploration of form and light."

## Expected Output
Generate the complete HTML, CSS, and JavaScript files necessary to deploy this gallery.