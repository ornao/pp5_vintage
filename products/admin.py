from django.contrib import admin
from .models import Product, Category


class ProductAdmin(admin.ModelAdmin):
    """class for product admin"""
    list_display = (
        'sku',
        'name',
        'price',
        'condition',
        'brand',
        'size',
    )

    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    """class for category admin"""
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
