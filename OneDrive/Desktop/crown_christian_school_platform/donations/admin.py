from django.contrib import admin
from .models import Donation

@admin.register(Donation)
class DonationAdmin(admin.ModelAdmin):
    list_display = ("donor_name","amount","date","designation")
    list_filter = ("date",)
    search_fields = ("donor_name","designation")
