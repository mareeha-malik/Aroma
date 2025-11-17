# AROMA Luxury Perfume - Complete Design Guide

## Overview

Your e-commerce dashboard has been completely redesigned with a **luxury, elegant aesthetic** matching high-end perfume branding. The design features a sophisticated black background with gold accents throughout.

---

## Color Palette

| Color | Hex | Usage |
|-------|-----|-------|
| **Gold** | `#d4af37` | Primary accent, links, borders |
| **Pure Black** | `#000` | Background base |
| **Dark Charcoal** | `#1a1a1a` | Text on gold, deep backgrounds |
| **Light Gray** | `#f5f5f5` | Primary text |
| **Medium Gray** | `#b8b8b8` | Secondary text |
| **Dark Gray** | `#999` | Tertiary text, placeholders |

---

## Typography

### Font Family
- **Primary Font**: `'Playfair Display', 'Georgia', serif`
  - Elegant, luxury serif font
  - Used for headings and hero text
  - Light weight (300) for elegance
  
- **Secondary Font**: System fonts for body text
  - High readability on all devices

### Font Sizes & Hierarchy

```
Hero H1:     4.5rem, 300 weight, 4px letter-spacing
Section H2:  3.5rem, 300 weight, 3px letter-spacing
Card H3:     1.3rem, normal weight, 1px letter-spacing
Body Text:   1rem - 1.1rem, 300-400 weight
```

---

## Component Styles

### Buttons

**Primary Button** (Gold/White)
```css
padding: 1rem 2.8rem;
background: #d4af37;
color: #000;
border: 2px solid #d4af37;
text-transform: uppercase;
letter-spacing: 2px;
transition: 0.4s ease;

/* Hover: Hollow gold border with gold text */
background: transparent;
color: #d4af37;
```

**Secondary Button** (Outline)
```css
border: 1px solid #d4af37;
color: #d4af37;
background: transparent;

/* Hover: Filled with gold */
background: #d4af37;
color: #000;
```

### Cards

```css
background: rgba(0, 0, 0, 0.3);
border: 1px solid #d4af37;
transition: 0.4s ease;

/* Hover: Lift and glow */
transform: translateY(-8px);
box-shadow: 0 20px 60px rgba(212, 175, 55, 0.25);
```

### Input Fields

```css
background: rgba(42, 42, 42, 0.8);
border: 1px solid #d4af37;
color: #f5f5f5;
border-radius: 0;  /* Sharp edges for luxury look */

/* Focus: Enhanced glow */
box-shadow: inset 0 0 10px rgba(212, 175, 55, 0.2), 
            0 0 10px rgba(212, 175, 55, 0.2);
```

---

## Background Image Setup

### Current State
The background is prepared to accept a full-page image with a dark overlay for elegance.

### How to Add Your Image

1. **Place image file** in: `static/images/background.jpg`
2. **Update URL** in `templates/base.html` (line ~20):
   ```css
   background-image: url('/static/images/background.jpg');
   ```

### Background Features

```css
body {
    background-image: url('/static/images/background.jpg');
    background-attachment: fixed;      /* Stays fixed when scrolling */
    background-size: cover;             /* Fills entire viewport */
    background-position: center;        /* Centered on screen */
}

/* Always applies dark overlay for readability */
body::before {
    background: rgba(0, 0, 0, 0.4);    /* 40% dark overlay */
}
```

**Recommended Image Specs:**
- Resolution: 1920x1080px or larger
- Format: JPG (better compression) or WebP
- Content: Subtle, sophisticated (flowers, textures, dark tones)
- File size: Under 2MB

---

## Layout Structure

### Header
- Sticky position at top
- Semi-transparent dark background with blur effect
- Gradient border bottom
- Gold accents on logo and nav links

**Components:**
- Logo: "AROMA" (gold, large, letter-spaced)
- Navigation: Home, Shop, About, Contact (underline on hover)
- Search bar with gold border
- Cart badge (circular gold)

### Hero Section (Home Page)
- Two-column grid layout
- Left: Text content (2 columns on desktop, full width on mobile)
- Right: Image placeholder with gold border
- Uses largest typography with light weight

### Product Grid
- Auto-fill columns (260px minimum)
- 3rem gap between cards
- Smooth hover effects (lift + glow)
- Sharp borders (no border-radius)

### Footer
- Semi-transparent dark background
- Gold border top
- Multiple columns for sections
- Dynamic year and product count

---

## Responsive Design

### Desktop (1024px+)
- Full-width layouts
- Multi-column grids
- Optimal spacing and sizing

### Tablet (768px - 1024px)
- 2-column product grids
- Adjusted font sizes
- Modified header layout

### Mobile (< 768px)
- Single column layouts
- Stacked navigation
- Reduced padding and gaps
- Optimized touch targets
- 4.5rem to 2.5rem hero heading

---

## Key Design Features

### Elegance Elements

1. **Letter Spacing**: All uppercase text has generous letter-spacing (1px - 4px)
2. **Light Typography**: Headings use weight 300 for refined appearance
3. **Sharp Borders**: No border-radius on buttons and inputs (luxury, geometric)
4. **Subtle Animations**: 0.3s - 0.4s transitions for smooth feel
5. **Glass Morphism**: Header uses `backdrop-filter: blur(10px)`
6. **Gold Accents**: Every interactive element features the signature gold

### Interactive Elements

- **Hover Effects**: Smooth color transitions and lift animations
- **Underline Animations**: Nav links feature animated gold underline on hover
- **Border Animations**: Buttons transition from filled to hollow
- **Shadow Effects**: Lift effect with glow on hover (0 20px 60px with gold color)

---

## Navigation Structure

**Home Page** (`/`)
- Hero section with welcoming message
- Featured collection cards
- Call-to-action buttons

**Products Page** (`/products/`)
- Grid of product cards
- Search functionality
- Pagination (First, Prev, Next, Last)
- Stock status indicator
- Add to cart button

**Cart Page** (`/cart/`)
- Item list with quantities
- Dynamic total calculation
- Remove buttons
- Continue shopping link

**Profile Page** (`/profile/`)
- User details display
- Account settings
- Logout option

---

## Customization Quick Guide

### Change Gold Color
Find all instances of `#d4af37` and replace with your preferred color.

### Change Dark Background
Find `#000` or `#1a1a1a` and adjust darkness.

### Adjust Overlay Opacity
In `base.html`, change `rgba(0, 0, 0, 0.4)` to your preference:
- `0.3` = More image visible
- `0.5` = Darker, more text contrast
- `0.6` = Very dark, maximum readability

### Modify Typography Weight
- Change `300` to `400` for heavier text
- Change `400` to `500` for medium weight
- Keep headings at `300` for elegance

---

## Performance Notes

1. **Background Image**: Optimize before uploading (use TinyPNG or similar)
2. **Font Loading**: Uses serif fallback, no external font loading
3. **Transitions**: All CSS transitions (no JS needed)
4. **Mobile First**: Mobile layout is default, scales up efficiently

---

## Browser Compatibility

- ✅ Chrome/Edge (latest)
- ✅ Firefox (latest)
- ✅ Safari (latest)
- ✅ Mobile browsers
- Note: Older IE versions not supported (uses CSS Grid, flexbox, backdrop-filter)

---

## File Structure

```
aroma/
├── templates/
│   ├── base.html              ← Main styles and background setup
│   ├── home.html              ← Hero section styling
│   ├── products.html          ← Product grid styling
│   ├── cart.html              ← Cart styling
│   ├── profile.html           ← Profile styling
│   ├── product_detail.html    ← Detail page styling
│   └── includes/
│       ├── header.html        ← Navigation styling
│       ├── footer.html        ← Footer styling
│       └── product_card.html  ← Card component
├── static/
│   ├── images/
│   │   ├── background.jpg     ← Your background image goes here
│   │   └── README.md          ← Instructions
│   └── css/
│       └── style.css          ← Additional custom styles
```

---

## Next Steps

1. ✅ Design is complete and running
2. **Add background image** to `static/images/` folder
3. **Update image URL** in `base.html`
4. **Test on mobile** to verify responsive design
5. **Add product images** via admin panel
6. Customize as needed!

---

**Design Version**: 1.0 - Luxury Perfume Edition  
**Last Updated**: November 17, 2025  
**Framework**: Django 5.2.8 with CSS Grid & Flexbox
