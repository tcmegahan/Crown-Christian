from django.contrib import admin
from .models import AidApplication

@admin.register(AidApplication)
class AidApplicationAdmin(admin.ModelAdmin):
    list_display = ("student","year","requested_amount","awarded_amount","status")
    list_filter = ("year","status")
