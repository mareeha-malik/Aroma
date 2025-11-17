from django import template
from store.models import Product

register = template.Library()


@register.filter
def format_price(value):
    """
    Format price with comma separators and 2 decimal places.
    Example: 1200.5 becomes 1,200.50
    """
    try:
        value = float(value)
        return "{:,.2f}".format(value)
    except (ValueError, TypeError):
        return value


@register.simple_tag
def total_products():
    """
    Custom template tag to return total number of products.
    Used in footer to display product count.
    """
    return Product.objects.count()
