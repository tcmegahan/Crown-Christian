from django.contrib import admin
from .models import FinanceRecord

@admin.register(FinanceRecord)
class FinanceRecordAdmin(admin.ModelAdmin):
    list_display = ("category","amount","date","student")
    list_filter = ("category","date")
    search_fields = ("notes",)
