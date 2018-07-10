from django.contrib import admin
from .models import GenericName

class GenericNameAdmin(admin.ModelAdmin):
    list_display = ('named_id',)

# Register your models here.
admin.site.register(GenericName, GenericNameAdmin)
