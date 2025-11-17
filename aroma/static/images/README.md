# Background Image Setup

## How to Add Your Background Image

### Step 1: Add Image File
Place your background image in this folder (`static/images/`)

Recommended:
- File name: `background.jpg` or `hero-bg.jpg`
- Format: JPG, PNG, or WebP
- Size: 1920x1080px or larger (for full coverage)
- File size: Keep under 2MB for web performance

### Step 2: Update base.html

Open `templates/base.html` and find this line (around line 20):

```css
background-image: url('') /* Add your background image URL here */;
```

Replace it with your image path:

```css
background-image: url('/static/images/background.jpg');
```

### Step 3: Optional - Configure Background Properties

You can customize how the image appears:

```css
body {
    background-image: url('/static/images/background.jpg');
    background-attachment: fixed;        /* Parallax effect when scrolling */
    background-size: cover;               /* Cover entire viewport */
    background-position: center;          /* Center the image */
    background-repeat: no-repeat;         /* Don't repeat */
}
```

### Example File Structure

```
aroma/
├── static/
│   ├── images/
│   │   └── background.jpg  ← Place your image here
│   └── css/
└── templates/
```

### Tips for Best Results

1. **Use High Quality Images**: The luxury aesthetic requires sharp, professional imagery
2. **Dark Toned Images**: Pair well with the gold (#d4af37) and white text
3. **Test Responsiveness**: Make sure image looks good on mobile (check 768px breakpoint)
4. **Performance**: Optimize images to reduce load time

### Alternative: Gradient Overlay Only (No Image)

If you want to use only the dark overlay without an image:

```css
background-image: none;
background-color: #000;
```

The overlay will maintain the elegant dark aesthetic.

---

**Need Help?**
The dark overlay is always active (opacity: 0.4) over the background, so your image should complement this darker aesthetic.
