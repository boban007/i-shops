from django.contrib import admin
from .models import Product, ProductCategory, ProductGeneric, Pack

class ProductAdmin(admin.ModelAdmin):
    list_display = ('named_id', 'container_type', 'per_item', 'is_brand', 'is_sale')

class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('product_id', 'category_id')

class ProductGenericAdmin(admin.ModelAdmin):
    list_display = ('product_id', 'generic_id')

class PackAdmin(admin.ModelAdmin):
    list_display = ('uid', 'product_id', 'is_active', 'dosage', 'measure', 'quantity', 'price')

admin.site.register(Product, ProductAdmin)
admin.site.register(ProductCategory, ProductCategoryAdmin)
admin.site.register(ProductGeneric, ProductGenericAdmin)
admin.site.register(Pack, PackAdmin)
