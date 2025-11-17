from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from .models import Product, Cart, CartItem


def home(request):
    """Home page view."""
    # Get first 8 products for carousel
    products = Product.objects.all()[:8]
    
    context = {
        'page_title': 'Home - Rosetta',
        'is_home': True,
        'products': products,
    }
    return render(request, 'home.html', context)


def products(request):
    """
    Products page with pagination and search functionality.
    
    This view displays all products in a grid layout with pagination.
    Users can search for products using the search bar.
    """
    # Get all products
    products_list = Product.objects.all()

    # Handle search
    search_query = request.GET.get('search', '')
    if search_query:
        products_list = products_list.filter(
            Q(name__icontains=search_query) | Q(description__icontains=search_query)
        )

    # Pagination
    paginator = Paginator(products_list, 6)  # Show 6 products per page
    page = request.GET.get('page')

    try:
        products_page = paginator.page(page)
    except PageNotAnInteger:
        products_page = paginator.page(1)
    except EmptyPage:
        products_page = paginator.page(paginator.num_pages)

    context = {
        'page_title': 'Products - Rosetta',
        'products': products_page,
        'search_query': search_query,
        'paginator': paginator,
        'total_products': Product.objects.count(),
    }
    return render(request, 'products.html', context)


def product_detail(request, pk):
    """Product detail view."""
    product = get_object_or_404(Product, pk=pk)
    context = {
        'page_title': f'{product.name} - Rosetta',
        'product': product,
    }
    return render(request, 'product_detail.html', context)


@login_required(login_url='admin:login')
def cart_view(request):
    """Shopping cart view."""
    cart, created = Cart.objects.get_or_create(user=request.user)
    context = {
        'page_title': 'Cart - Rosetta',
        'cart': cart,
    }
    return render(request, 'cart.html', context)


@login_required(login_url='admin:login')
def add_to_cart(request, pk):
    """Add product to cart."""
    product = get_object_or_404(Product, pk=pk)
    cart, created = Cart.objects.get_or_create(user=request.user)

    cart_item, created = CartItem.objects.get_or_create(
        cart=cart,
        product=product,
        defaults={'quantity': 1}
    )

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('cart')


@login_required(login_url='admin:login')
def remove_from_cart(request, item_id):
    """Remove item from cart."""
    cart = get_object_or_404(Cart, user=request.user)
    cart_item = get_object_or_404(CartItem, pk=item_id, cart=cart)
    cart_item.delete()
    return redirect('cart')


@login_required(login_url='admin:login')
def profile(request):
    """User profile view."""
    try:
        cart = Cart.objects.get(user=request.user)
    except Cart.DoesNotExist:
        cart = None

    context = {
        'page_title': 'Profile - Rosetta',
        'cart': cart,
    }
    return render(request, 'profile.html', context)


@login_required(login_url='admin:login')
def edit_profile(request):
    """Edit user profile view."""
    if request.method == 'POST':
        user = request.user
        user.first_name = request.POST.get('first_name', user.first_name)
        user.last_name = request.POST.get('last_name', user.last_name)
        user.email = request.POST.get('email', user.email)
        user.save()
        return redirect('profile')
    
    context = {
        'page_title': 'Edit Profile - Rosetta',
    }
    return render(request, 'edit_profile.html', context)
