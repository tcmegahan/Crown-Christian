from django.contrib import admin
from .models import Curriculum, Standard, LessonPlan


@admin.register(Curriculum)
class CurriculumAdmin(admin.ModelAdmin):
 list_display = ('name', 'description')
 search_fields = ('name',)


@admin.register(Standard)
class StandardAdmin(admin.ModelAdmin):
 list_display = ('code', 'curriculum')
 search_fields = ('code', 'description')


@admin.register(LessonPlan)
class LessonPlanAdmin(admin.ModelAdmin):
 list_display = ('title', 'curriculum', 'created_on')
 list_filter = ('curriculum',)
 search_fields = ('title', 'objectives')
