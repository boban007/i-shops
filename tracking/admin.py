from django.contrib import admin
from .models import Visitors, UntrackedUserAgent, BannedIP

class VisitorsAdmin(admin.ModelAdmin):
    list_display = ('session_key', 'ip_address', 'url', 'language', 'created_at')

# Register your models here.
admin.site.register(Visitors, VisitorsAdmin)
admin.site.register(UntrackedUserAgent)
admin.site.register(BannedIP)