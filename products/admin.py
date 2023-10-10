from django.contrib import admin
from products.models import ProductModel
from products.models import CategoryModel


@admin.register(CategoryModel)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']


@admin.register(ProductModel)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'created_at']
    search_field = ['title', 'price']
    list_filter = ['created_at']