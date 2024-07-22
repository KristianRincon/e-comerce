from django.contrib import admin
from .models import Category, Product, CartItem, Cart


admin.site.register(Category)
admin.site.register(Product)

# Personalizar la visualización del modelo CartItem en el admin
class CartItemInline(admin.TabularInline):
    model = CartItem
    extra = 0

# Personalizar la visualización del modelo Cart en el admin
class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at')
    inlines = [CartItemInline]

admin.site.register(Cart, CartAdmin)

