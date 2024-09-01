from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from users.models import UserProfile

User = get_user_model()

class Command(BaseCommand):
    help = 'Populate the database with sample users'

    def handle(self, *args, **kwargs):
        users = [
            {
                'username': 'john_doe',
                'email': 'john@example.com',
                'password': 'password123',
                'first_name': 'John',
                'last_name': 'Doe',
                'phone_number': '1234567890',
                'street_address': '123 Main St',
                'city': 'Anytown',
                'state': 'CA',
                'country': 'USA',
                'zip_code': '12345'
            },
            {
                'username': 'jane_smith',
                'email': 'jane@example.com',
                'password': 'password456',
                'first_name': 'Jane',
                'last_name': 'Smith',
                'phone_number': '9876543210',
                'street_address': '456 Elm St',
                'city': 'Othertown',
                'state': 'NY',
                'country': 'USA',
                'zip_code': '67890'
            }
        ]

        for user_data in users:
            user = User.objects.create_user(
                username=user_data['username'],
                email=user_data['email'],
                password=user_data['password'],
                first_name=user_data['first_name'],
                last_name=user_data['last_name'],
                phone_number=user_data['phone_number'],
                street_address=user_data['street_address'],
                city=user_data['city'],
                state=user_data['state'],
                country=user_data['country'],
                zip_code=user_data['zip_code']
            )
            UserProfile.objects.create(user=user, bio='Sample bio', technical_expertise='intermediate')

        self.stdout.write(self.style.SUCCESS('Successfully populated users'))