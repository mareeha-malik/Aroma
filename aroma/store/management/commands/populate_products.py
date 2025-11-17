from django.core.management.base import BaseCommand
from store.models import Product


class Command(BaseCommand):
    help = 'Populate database with sample perfume products'

    def handle(self, *args, **options):
        # Delete existing products to avoid duplicates
        Product.objects.all().delete()

        products = [
            {
                'name': 'Elegance',
                'description': 'A timeless fragrance that embodies grace and sophistication. Notes of rose and sandalwood create an unforgettable experience.',
                'price': 125.00,
                'stock': 15,
            },
            {
                'name': 'Velour',
                'description': 'Luxurious and sensual, this eau de parfum wraps you in comfort and elegance. A blend of jasmine and amber.',
                'price': 135.00,
                'stock': 20,
            },
            {
                'name': 'Divine',
                'description': 'An exquisite fragrance for those who embrace their inner luxury. Rich floral notes with hints of vanilla.',
                'price': 145.00,
                'stock': 10,
            },
            {
                'name': 'Opulent',
                'description': 'Bold and mysterious, this scent commands attention. Featuring oud, musk, and dark florals.',
                'price': 155.00,
                'stock': 8,
            },
            {
                'name': 'Ethereal',
                'description': 'Light and airy, perfect for those who prefer subtle elegance. Citrus and white florals predominate.',
                'price': 110.00,
                'stock': 25,
            },
            {
                'name': 'Mystic',
                'description': 'An enchanting fragrance with mysterious oriental notes. Patchouli, saffron, and incense blend harmoniously.',
                'price': 140.00,
                'stock': 0,  # Out of stock
            },
            {
                'name': 'Passion',
                'description': 'A sensual and intoxicating scent that captures the essence of desire and romance. Red fruits and woods.',
                'price': 130.00,
                'stock': 12,
            },
            {
                'name': 'Serenity',
                'description': 'Calm and peaceful, this fragrance brings tranquility to your day. Lavender, chamomile, and cedarwood.',
                'price': 115.00,
                'stock': 18,
            },
            {
                'name': 'Crown Jewel',
                'description': 'The pinnacle of luxury perfumery. A rich composition of precious florals and rare spices.',
                'price': 175.00,
                'stock': 5,
            },
            {
                'name': 'Twilight',
                'description': 'Captured in a bottle, the magic of dusk. A sophisticated blend of florals, amber, and vanilla.',
                'price': 125.00,
                'stock': 14,
            },
        ]

        for product_data in products:
            product = Product.objects.create(**product_data)
            self.stdout.write(
                self.style.SUCCESS(f'Created product: {product.name}')
            )

        self.stdout.write(
            self.style.SUCCESS('Successfully populated database with sample products!')
        )
