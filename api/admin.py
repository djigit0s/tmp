from django.contrib import admin

from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'stock', 'measure', 'price', 'updated_at')
    fields = ('title', 'stock', 'measure', 'price')
