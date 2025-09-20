from django.contrib import admin

from apps.products.models import Product, Category


# Register your models here.
@admin.register(Product)
class ProductAdminModel(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'price']

@admin.register(Category)
class CategoryAdminModel(admin.ModelAdmin):
    list_display = ['id', 'name', 'description']