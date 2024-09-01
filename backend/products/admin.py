from django.contrib import admin
from .models import Product, ProductImage

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'category', 'brand']
    list_filter = ['category', 'brand']
    search_fields = ['name', 'description', 'brand']
    inlines = [ProductImageInline]

admin.site.register(Product, ProductAdmin)