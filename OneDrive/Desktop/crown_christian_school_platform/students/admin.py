from django.contrib import admin
from .models import Student, Guardian

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("first_name","last_name","grade_level")
    search_fields = ("first_name","last_name","grade_level")

@admin.register(Guardian)
class GuardianAdmin(admin.ModelAdmin):
    list_display = ("first_name","last_name","email","phone")
    search_fields = ("first_name","last_name","email","phone")
