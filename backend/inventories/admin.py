from django.contrib import admin
from .models import Inventory

class InventoryAdmin(admin.ModelAdmin):
    list_display = ['product', 'quantity', 'last_updated']
    list_filter = ['last_updated']
    search_fields = ['product__name']

admin.site.register(Inventory, InventoryAdmin)