from django.core.management.base import BaseCommand
from categories.models import Category

class Command(BaseCommand):
    help = 'Populate the database with sample categories'

    def handle(self, *args, **kwargs):
        categories = [
            {'name': 'Smartphones', 'parent': None},
            {'name': 'Laptops', 'parent': None},
            {'name': 'Audio', 'parent': None},
            {'name': 'Android', 'parent': 'Smartphones'},
            {'name': 'iOS', 'parent': 'Smartphones'},
            {'name': 'Gaming Laptops', 'parent': 'Laptops'},
            {'name': 'Business Laptops', 'parent': 'Laptops'},
            {'name': 'Headphones', 'parent': 'Audio'},
            {'name': 'Speakers', 'parent': 'Audio'},
        ]

        for category in categories:
            parent = None
            if category['parent']:
                parent = Category.objects.get(name=category['parent'])
            Category.objects.get_or_create(name=category['name'], parent=parent)

        self.stdout.write(self.style.SUCCESS('Successfully populated categories'))