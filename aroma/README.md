# Rosetta - Luxury E-Commerce Dashboard

A dynamic e-commerce dashboard built with Django and modern web technologies for a luxury perfume store called "Rosetta".

## 📋 Project Features

### 1. **Base Template & Includes**
- ✅ Reusable `base.html` with template inheritance
- ✅ Header with site name "Rosetta" and navigation links
- ✅ Footer displaying current year dynamically using Django date filters
- ✅ Custom template tag to show total number of products in footer
- ✅ Elegant, luxurious black and gold design

### 2. **Home Page**
- ✅ Welcome message using Django variables
- ✅ If-else logic to check user authentication
  - Authenticated users: "Welcome back, {{ user.username }}!"
  - Anonymous users: "Sign in to start shopping."
- ✅ Hero section with perfume bottle SVG illustration
- ✅ Featured collection showcase
- ✅ Call-to-action buttons

### 3. **Products Page**
- ✅ Dynamic grid layout displaying all products
- ✅ Pagination with 6 products per page
- ✅ Each product shows: Name, Price, Stock Status
- ✅ Loop comments explaining the iteration logic
- ✅ Conditional rendering for "Out of Stock" items
- ✅ Search functionality to filter products dynamically
- ✅ Responsive design for mobile and desktop

### 4. **Product Card (Reusable Include Template)**
- ✅ `product_card.html` template for consistent product display
- ✅ Used with {% include %} tag in products loop
- ✅ Shows product image, name, description, price
- ✅ Stock status with conditional button styling
- ✅ Add to cart functionality

### 5. **Cart Page**
- ✅ Display all items added to cart
- ✅ Dynamic total price calculation using template logic
- ✅ Item quantity display
- ✅ Remove from cart functionality
- ✅ Order summary section
- ✅ Checkout call-to-action
- ✅ Empty cart message with link to continue shopping

### 6. **Profile Page**
- ✅ Display authenticated user details
- ✅ Account information (username, email, join date, last login)
- ✅ Shopping activity summary
- ✅ Cart status and total
- ✅ Account settings links
- ✅ Profile avatar
- ✅ Sign out and continue shopping options

### 7. **Custom Template Features**
- ✅ **Custom Filter**: `format_price` - formats prices with comma separators and 2 decimal places
  - Example: `1200.5` becomes `1,200.50`
- ✅ **Custom Template Tag**: `total_products` - returns total number of products
  - Used in footer to display product count dynamically

### 8. **Advanced Features**
- ✅ User authentication integration with Django's auth system
- ✅ Session-based shopping cart
- ✅ Product search with form submission
- ✅ Pagination system for large product lists
- ✅ Responsive design (mobile, tablet, desktop)
- ✅ Elegant black and gold color scheme
- ✅ Smooth hover effects and transitions
- ✅ Sticky header during scroll
- ✅ Product stock management

## 🗂️ Project Structure

```
aroma/
├── manage.py
├── db.sqlite3
├── templates/
│   ├── base.html                 # Main template with header/footer
│   ├── home.html                # Home page template
│   ├── products.html             # Products listing with pagination
│   ├── product_detail.html       # Single product detail
│   ├── cart.html                 # Shopping cart page
│   ├── profile.html              # User profile page
│   └── includes/
│       ├── header.html           # Reusable header
│       ├── footer.html           # Reusable footer
│       └── product_card.html     # Reusable product card
├── static/
│   ├── css/
│   │   └── style.css             # Global styles
│   ├── js/
│   └── images/
├── store/                        # Main app
│   ├── models.py                 # Product, Cart, CartItem models
│   ├── views.py                  # View functions
│   ├── urls.py                   # URL routing
│   ├── admin.py                  # Admin configuration
│   ├── forms.py                  # Forms (if needed)
│   ├── migrations/               # Database migrations
│   ├── templatetags/
│   │   └── store_tags.py         # Custom filters and tags
│   └── management/commands/
│       └── populate_products.py  # Command to seed sample data
└── aroma/                        # Project settings
    ├── settings.py               # Django settings
    ├── urls.py                   # Root URL configuration
    ├── wsgi.py
    └── asgi.py
```

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- Django 5.2+
- pip

### Installation

1. **Clone or navigate to the project:**
```bash
cd aroma
```

2. **Create and activate virtual environment (if not already done):**
```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

3. **Install dependencies:**
```bash
pip install django
```

4. **Run migrations:**
```bash
python manage.py makemigrations
python manage.py migrate
```

5. **Create superuser (admin account):**
```bash
python manage.py createsuperuser
# Username: admin
# Email: admin@rosetta.com
# Password: admin123
```

6. **Populate sample data:**
```bash
python manage.py populate_products
```

7. **Run development server:**
```bash
python manage.py runserver
```

8. **Access the application:**
- Home: `http://localhost:8000/`
- Products: `http://localhost:8000/products/`
- Cart: `http://localhost:8000/cart/` (requires login)
- Profile: `http://localhost:8000/profile/` (requires login)
- Admin: `http://localhost:8000/admin/`

## 🔐 Admin Credentials
- **Username:** admin
- **Password:** admin123

## 📱 Features in Detail

### Authentication
- Uses Django's built-in authentication system
- Login required for cart and profile pages
- Session-based user tracking

### Products Database
The system comes pre-populated with 10 luxury fragrances:
1. Elegance - $125.00
2. Velour - $135.00
3. Divine - $145.00
4. Opulent - $155.00
5. Ethereal - $110.00
6. Mystic - $140.00 (Out of Stock)
7. Passion - $130.00
8. Serenity - $115.00
9. Crown Jewel - $175.00
10. Twilight - $125.00

### Search Functionality
- Real-time search through products by name and description
- Search queries preserved in pagination links
- No results message with helpful information

### Pagination
- 6 products per page
- Previous/Next navigation
- First/Last page shortcuts
- Current page highlighting
- Search query preservation

### Cart System
- Add/Remove items
- Quantity tracking
- Automatic subtotal calculation
- Cart item count in header badge
- Session-based (no database persistence for active carts)

### Design Theme
- **Colors:**
  - Primary: #d4af37 (Gold)
  - Background: #1a1a1a (Dark)
  - Text: #e0e0e0 (Light Gray)
  - Accents: #2a2a2a (Dark Gray)

- **Typography:**
  - Font: Segoe UI, Tahoma, Geneva, Verdana, sans-serif
  - Professional and elegant appearance
  - Clear hierarchy with size and color differentiation

## 🔧 Customization

### Adding New Products
Use the Django admin interface:
1. Go to `http://localhost:8000/admin/`
2. Login with admin credentials
3. Add new products with name, price, stock, and optional image

### Modifying Design
Edit these files to customize the theme:
- `templates/base.html` - Change global styles and layout
- `templates/includes/header.html` - Customize navigation
- `templates/includes/footer.html` - Update footer content
- `static/css/style.css` - Global CSS rules

### Creating New Pages
1. Create a new view function in `store/views.py`
2. Create corresponding template in `templates/`
3. Add URL pattern in `store/urls.py`
4. Add navigation link in `templates/includes/header.html`

## 📝 Template Tags and Filters Usage

### Custom Filter - Format Price
```django
{{ product.price|format_price }}
{# Output: 125.00 #}
```

### Custom Template Tag - Total Products
```django
{% load store_tags %}
{% total_products %}
{# Output: 10 #}
```

## 🎯 Django Template Features Demonstrated

1. **Template Inheritance** - All pages extend `base.html`
2. **Include Tags** - Reusable header, footer, and product card
3. **For Loops** - Iterate through products with comments
4. **If-Else Statements** - Conditional rendering for auth status and stock
5. **Filters** - Custom price formatting and built-in date filters
6. **Custom Tags** - Product count display
7. **URL Reversal** - Dynamic URL generation with `{% url %}`
8. **Context Variables** - Pass data from views to templates

## 🌐 Responsive Design
- Mobile-first approach
- Breakpoints at 768px
- Flexible grid layouts
- Touch-friendly buttons and navigation

## 💻 Technologies Used
- **Backend:** Django 5.2
- **Frontend:** HTML5, CSS3, SVG illustrations
- **Database:** SQLite3
- **Authentication:** Django's built-in auth system
- **Templating:** Django Template Language (DTL)

## 📄 License
This project is for educational purposes. Feel free to modify and use as needed.

## 🤝 Support
For issues or questions, refer to the Django documentation:
- https://docs.djangoproject.com/
- https://docs.djangoproject.com/en/5.2/topics/templates/

---

**Created with ✨ for a luxury perfume store experience**
