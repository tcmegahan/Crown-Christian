from django.contrib import admin
from .models import Course, Section, Enrollment
admin.site.register(Course)
admin.site.register(Section)
admin.site.register(Enrollment)
