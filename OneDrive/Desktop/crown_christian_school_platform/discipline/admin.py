from django.contrib import admin
from .models import DisciplineIncident

@admin.register(DisciplineIncident)
class DisciplineIncidentAdmin(admin.ModelAdmin):
    list_display = ("student","incident_type","date")
    list_filter = ("incident_type","date")
    search_fields = ("notes",)
