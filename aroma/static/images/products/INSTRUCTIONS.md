# How to Add Carousel Product Images

## Step 1: Place Your Images Here
Add your product images to this folder: `static/images/products/`

**Recommended naming:**
- `product1.jpg` - First carousel product
- `product2.jpg` - Second carousel product
- `product3.jpg` - Third carousel product
- ... and so on

**Image specifications:**
- Format: JPG, PNG, or WebP
- Size: 250px × 200px (width × height) minimum
- File size: Under 500KB each for fast loading

## Step 2: Update home.html

Open `templates/home.html` and find the carousel section (around line 327-340).

### Current Code:
```html
<div class="carousel-item-image">
    🌸
</div>
```

### Replace With Your Image:
**Option A - Simple Image Reference**
```html
<div class="carousel-item-image">
    {% load static %}
    <img src="{% static 'images/products/product1.jpg' %}" alt="{{ product.name }}" style="width: 100%; height: 150px; object-fit: cover; border-bottom: 1px solid #d4af37; margin-bottom: 1rem;">
</div>
```

**Option B - Dynamic Product Images (if products have image field)**
```html
<div class="carousel-item-image">
    {% if product.image %}
        <img src="{{ product.image.url }}" alt="{{ product.name }}" style="width: 100%; height: 150px; object-fit: cover; border-bottom: 1px solid #d4af37; margin-bottom: 1rem;">
    {% else %}
        🌸
    {% endif %}
</div>
```

## Step 3: Save and Refresh

1. Add your images to `static/images/products/`
2. Update the code in `templates/home.html`
3. Refresh your browser to see the carousel with images

## File Structure

```
static/
├── images/
│   ├── products/
│   │   ├── product1.jpg    ← Your carousel images
│   │   ├── product2.jpg
│   │   ├── product3.jpg
│   │   └── ...
│   ├── Aroma.svg
│   ├── bg.png
│   └── hero.png
```

## Tips

- **Consistency**: Use images with similar aspect ratios for better alignment
- **Quality**: High-quality images look more luxurious
- **Naming**: Keep names simple and numbered for easy reference
- **Backup**: Keep original files in case you need to replace them

---

**Currently**: The carousel displays a flower emoji (🌸) as a placeholder.  
**Your task**: Replace it with your actual product images!
