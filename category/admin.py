from django.contrib import admin
from .models import Category

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('named_id', 'is_active', 'position')

# Register your models here.
admin.site.register(Category, CategoryAdmin)
