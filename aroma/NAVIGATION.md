# Rosetta E-Commerce Dashboard - Quick Navigation Guide

## 🌐 Application URLs

### Public Pages
- **Home** - http://localhost:8000/
  - Hero section with welcome message
  - Featured collection showcase
  - Dynamic welcome for authenticated users

- **Products** - http://localhost:8000/products/
  - Grid layout with all products
  - Pagination (6 per page)
  - Search bar in header
  - Stock status indicators
  - Add to cart buttons

- **Product Detail** - http://localhost:8000/products/<id>/
  - Full product information
  - Detailed description
  - Product metadata
  - Related products (placeholder)

### Authenticated Pages (Requires Login)
- **Cart** - http://localhost:8000/cart/
  - View cart items
  - Remove items
  - Order summary
  - Checkout button
  - Auto-redirects to admin login if not authenticated

- **Profile** - http://localhost:8000/profile/
  - User account details
  - Shopping activity
  - Cart summary
  - Account settings
  - Auto-redirects to admin login if not authenticated

### Admin Pages
- **Admin Dashboard** - http://localhost:8000/admin/
  - Manage products
  - View users
  - Monitor orders
  - User: `admin`
  - Password: `admin123`

---

## 🔍 How to Navigate the Application

### From Home Page
1. Click "Shop Now" button → Goes to Products page
2. Click "Products" in navigation → Goes to Products page
3. Click "Rosetta" logo → Stays on Home

### On Products Page
1. **Search Products:**
   - Use search bar in header
   - Enter product name or description
   - Results update dynamically
   - Previous search persists in pagination

2. **Browse Products:**
   - Scroll through grid
   - Click any product to view details
   - Click "Add to Cart" to add item
   - Redirects to login if not authenticated

3. **Navigate Pages:**
   - Use pagination buttons at bottom
   - "Previous/Next" for adjacent pages
   - "First/Last" for endpoints
   - Click page number to jump to specific page

### On Product Detail Page
1. View full product information
2. Read detailed description
3. See product specifications
4. Click "Add to Cart" if in stock
5. Click "Save for Later" for wishlist (placeholder)
6. Click breadcrumb to go back

### Shopping Cart (Login Required)
1. Click "Cart" in navigation
2. View all items added
3. See individual prices and quantities
4. View order summary on right side
5. Remove items with "Remove" button
6. Click "Proceed to Checkout" (placeholder)
7. Click "Continue Shopping" to return to products

### User Profile (Login Required)
1. Click "Profile" in navigation
2. View account details:
   - Username
   - Email
   - Full name
   - Member since date
   - Last login time
3. View shopping activity:
   - Total items in cart
   - Cart total
4. Manage account settings
5. Sign out

---

## 🔐 Authentication Flow

### Not Logged In
- Home page accessible
- Products page accessible
- Product details accessible
- Search functionality works
- Cart/Profile redirect to admin login
- Navigation shows "Sign In" link

### Logged In (Admin User)
- All pages accessible
- Cart shows items and badge
- Profile displays your information
- Navigation shows "Logout" link
- Welcome message on home page

### Logout
- Click "Logout" in navigation
- Redirected to home page
- Session cleared
- Cart persists until new session

---

## 🛍️ Shopping Workflow Example

### Step 1: Browse Products
1. Go to http://localhost:8000/
2. Click "Shop Now" or "Products" in navigation

### Step 2: Search & Filter
1. Type "Velour" in search bar
2. See filtered results
3. Or browse all products with pagination

### Step 3: View Details
1. Click on product card
2. Read full description
3. Check stock availability
4. See pricing information

### Step 4: Add to Cart
1. Click "Add to Cart" button
2. Auto-redirects to login if needed
3. Cart count badge updates in header

### Step 5: View Cart
1. Click "Cart" in navigation
2. See all items
3. Verify totals
4. Remove items if needed

### Step 6: User Profile
1. Click "Profile" in navigation
2. View account details
3. See shopping summary
4. Manage settings

---

## 💡 Feature Highlights

### Search Functionality
- Real-time filtering
- Searches product name AND description
- Preserves search in pagination
- "No results" message with help

### Pagination
- Shows 6 products per page
- Smart page range display
- Remembers search term when changing pages
- First/Last shortcuts
- Previous/Next navigation

### Cart System
- Session-based per user
- Add/Remove items
- Quantity tracking
- Dynamic total calculation
- Cart badge in header
- Empty cart message

### Authentication
- Uses Django's built-in User system
- Session-based (not token)
- Required for cart/profile
- Redirects to admin login
- Welcome message for known users

### Responsive Design
- Works on mobile (< 768px)
- Works on tablet (768px - 1024px)
- Works on desktop (> 1024px)
- Mobile navigation adapts
- Grid layouts responsive
- Touch-friendly buttons

---

## 🎨 Design Features

### Colors
- **Gold Accent:** #d4af37 (buttons, headings, links)
- **Dark Background:** #1a1a1a (main background)
- **Light Text:** #e0e0e0 (readable text)
- **Secondary:** #2a2a2a (subtle backgrounds)

### Interactive Elements
- Hover effects on all links and buttons
- Smooth transitions (0.3s)
- Box shadows for depth
- Color changes on hover
- Transform effects on buttons

### Visual Hierarchy
- Large headings (1.8-3.5rem)
- Gold for important elements
- Clear contrast for readability
- Organized grid layouts
- Whitespace for breathing room

---

## ⚙️ Admin Features

### Managing Products
1. Go to http://localhost:8000/admin/
2. Login with admin credentials
3. Click "Products" section
4. Add new products with:
   - Name
   - Description
   - Price
   - Stock quantity
   - Optional image

### Managing Users
1. Go to Admin dashboard
2. Click "Users" section
3. Create new users
4. Manage permissions
5. View user activity

### Monitoring Orders
1. View cart information
2. See user shopping patterns
3. Track product popularity

---

## 🐛 Troubleshooting

### Pages Not Loading
- Check server is running: `python manage.py runserver`
- Verify URL is correct
- Check console for error messages

### Login Issues
- Clear browser cookies
- Ensure admin user exists
- Check admin password

### Cart Not Working
- Login to account first
- Check browser JavaScript enabled
- Clear browser cache

### Search Not Finding Items
- Check search is using correct query
- Verify products exist in database
- Try partial product names

### Images Not Showing
- Upload images in admin
- Check file permissions
- Verify image paths

---

## 📊 Database

### Sample Data Included
10 luxury fragrances pre-loaded:
1. Elegance ($125) - 15 in stock
2. Velour ($135) - 20 in stock
3. Divine ($145) - 10 in stock
4. Opulent ($155) - 8 in stock
5. Ethereal ($110) - 25 in stock
6. Mystic ($140) - OUT OF STOCK
7. Passion ($130) - 12 in stock
8. Serenity ($115) - 18 in stock
9. Crown Jewel ($175) - 5 in stock
10. Twilight ($125) - 14 in stock

### Reset Database
```bash
# Delete database and migrations
rm db.sqlite3
rm store/migrations/0*.py

# Recreate fresh database
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py populate_products
```

---

## 📱 Mobile Experience

### Header on Mobile
- Logo centered
- Navigation vertical
- Search bar full width
- Cart badge visible

### Products on Mobile
- Grid: 1-2 columns
- Touch-friendly buttons
- Scroll for pagination
- Search remains accessible

### Cart on Mobile
- Single column layout
- Order summary below items
- Large buttons for touch
- Easy remove buttons

### Profile on Mobile
- Stacked layout
- Larger touch targets
- Clear sections
- Readable text

---

## ✨ Tips & Tricks

1. **Quick Login:** Use credentials displayed on admin login page
2. **Product Tips:** Search by partial names (e.g., "Vel" finds "Velour")
3. **Cart Persistence:** Cart saved in session until logout
4. **Stock Checking:** Out of stock products show disabled button
5. **Price Format:** All prices displayed as $X,XXX.XX format
6. **Mobile First:** Always test on mobile for best experience
7. **Browser Cache:** Clear cache if styles don't update

---

## 🚀 Next Steps

After exploring the application:

1. **Customize Content**
   - Edit product descriptions
   - Add/remove products
   - Update company information

2. **Extend Features**
   - Add review system
   - Implement wishlist
   - Add order tracking
   - Create coupon codes

3. **Deploy**
   - Use production server
   - Set DEBUG = False
   - Configure domain
   - Setup SSL certificate

4. **Integrate Payment**
   - Add Stripe/PayPal
   - Process transactions
   - Send order emails
   - Track shipments

---

**Enjoy exploring Rosetta - Your Luxury Perfume Dashboard! 🌟**
