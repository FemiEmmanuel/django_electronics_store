from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from orders.models import Order, OrderItem
from products.models import Product
import random

User = get_user_model()

class Command(BaseCommand):
    help = 'Populate the database with sample orders'

    def handle(self, *args, **kwargs):
        users = User.objects.all()
        products = Product.objects.all()

        for _ in range(5):  # Create 5 sample orders
            user = random.choice(users)
            order = Order.objects.create(
                user=user,
                total_amount=0,
                status=random.choice(['pending', 'processing', 'shipped', 'delivered']),
                shipping_address=f"{user.street_address}, {user.city}, {user.state}, {user.country}, {user.zip_code}"
            )

            total_amount = 0
            for _ in range(random.randint(1, 3)):  # 1 to 3 items per order
                product = random.choice(products)
                quantity = random.randint(1, 3)
                price = product.price * quantity
                total_amount += price

                OrderItem.objects.create(
                    order=order,
                    product=product,
                    quantity=quantity,
                    price=price
                )

            order.total_amount = total_amount
            order.save()

        self.stdout.write(self.style.SUCCESS('Successfully populated orders'))