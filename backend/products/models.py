from django.db import models
from categories.models import Category
from inventories.models import Inventory

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    inventory = models.OneToOneField(Inventory, on_delete=models.CASCADE)
    brand = models.CharField(max_length=100)
    model_number = models.CharField(max_length=50, blank=True, null=True)
    technical_specs = models.JSONField(default=dict, blank=True)
    warranty_info = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_images/')
    is_primary = models.BooleanField(default=False)

    def __str__(self):
        return f"Image for {self.product.name}"