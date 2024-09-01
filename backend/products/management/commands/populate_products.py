from django.core.management.base import BaseCommand
from products.models import Product, ProductImage
from categories.models import Category
from inventory.models import Inventory
import random

class Command(BaseCommand):
    help = 'Populate the database with sample products and inventory'

    def handle(self, *args, **kwargs):
        products = [
            {
                'name': 'iPhone 13',
                'description': 'Latest iPhone model with A15 Bionic chip',
                'price': 799.99,
                'category': 'iOS',
                'brand': 'Apple',
                'model_number': 'A2482',
                'technical_specs': {'screen': '6.1 inch', 'storage': '128GB'},
                'warranty_info': '1 year limited warranty'
            },
            {
                'name': 'Samsung Galaxy S21',
                'description': 'Flagship Android smartphone with 5G',
                'price': 699.99,
                'category': 'Android',
                'brand': 'Samsung',
                'model_number': 'SM-G991U',
                'technical_specs': {'screen': '6.2 inch', 'storage': '128GB'},
                'warranty_info': '1 year limited warranty'
            },
            {
                'name': 'Dell XPS 15',
                'description': 'Powerful laptop for professionals',
                'price': 1499.99,
                'category': 'Business Laptops',
                'brand': 'Dell',
                'model_number': 'XPS 15-9510',
                'technical_specs': {'processor': 'Intel i7', 'ram': '16GB'},
                'warranty_info': '1 year limited warranty'
            },
            {
                'name': 'Sony WH-1000XM4',
                'description': 'Wireless noise-cancelling headphones',
                'price': 349.99,
                'category': 'Headphones',
                'brand': 'Sony',
                'model_number': 'WH-1000XM4',
                'technical_specs': {'battery': '30 hours', 'connectivity': 'Bluetooth 5.0'},
                'warranty_info': '1 year limited warranty'
            }
        ]

        for product_data in products:
            category = Category.objects.get(name=product_data['category'])
            inventory = Inventory.objects.create(quantity=random.randint(10, 100))
            product = Product.objects.create(
                name=product_data['name'],
                description=product_data['description'],
                price=product_data['price'],
                category=category,
                inventory=inventory,
                brand=product_data['brand'],
                model_number=product_data['model_number'],
                technical_specs=product_data['technical_specs'],
                warranty_info=product_data['warranty_info']
            )
            ProductImage.objects.create(product=product, image='product_images/placeholder.jpg', is_primary=True)

        self.stdout.write(self.style.SUCCESS('Successfully populated products and inventory'))