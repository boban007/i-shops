from django.contrib import admin
from .models import Products, ProductCategory, ProductGeneric

class ProductsAdmin(admin.ModelAdmin):
    list_display = ('named_id', 'container_type', 'per_item', 'is_brand', 'is_sale')

class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('product_id', 'category_id')

class ProductGenericAdmin(admin.ModelAdmin):
    list_display = ('product_id', 'generic_id')

admin.site.register(Products, ProductsAdmin)
admin.site.register(ProductCategory, ProductCategoryAdmin)
admin.site.register(ProductGeneric, ProductGenericAdmin)
