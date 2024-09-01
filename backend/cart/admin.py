from django.contrib import admin
from .models import Cart, CartItem

class CartItemInline(admin.TabularInline):
    model = CartItem
    extra = 1
    readonly_fields = ('subtotal',)

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'created_at', 'updated_at', 'total_amount', 'total_items')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('user__username', 'user__email')
    readonly_fields = ('total_amount', 'total_items')
    inlines = [CartItemInline]

    def total_amount(self, obj):
        return obj.total_amount
    total_amount.short_description = 'Total Amount'

    def total_items(self, obj):
        return obj.total_items
    total_items.short_description = 'Total Items'

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'cart', 'product', 'quantity', 'subtotal', 'added_at', 'updated_at')
    list_filter = ('added_at', 'updated_at')
    search_fields = ('cart__user__username', 'product__name')
    readonly_fields = ('subtotal',)

    def subtotal(self, obj):
        return obj.subtotal
    subtotal.short_description = 'Subtotal'