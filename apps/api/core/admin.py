from django.contrib import admin
from .models import (
 Family,
 Guardian,
 Student,
 Term,
 Course,
 Section,
 Enrollment,
 Attendance,
 Grade,
 Ledger,
 LedgerLine,
 Communication,
)

@admin.register(Family)
class FamilyAdmin(admin.ModelAdmin):
 list_display = ('household_id', 'name', 'phone')
 search_fields = ('name',)

@admin.register(Guardian)
class GuardianAdmin(admin.ModelAdmin):
 list_display = ('guardian_id', 'first_name', 'last_name', 'email')
 search_fields = ('first_name', 'last_name', 'email')

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
 list_display = ('student_id', 'first_name', 'last_name', 'grade_level', 'status')
 search_fields = ('first_name', 'last_name')

@admin.register(Term)
class TermAdmin(admin.ModelAdmin):
 list_display = ('term_id', 'name', 'start_date', 'end_date')

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
 list_display = ('course_id', 'code', 'name', 'credits')

@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
 list_display = ('section_id', 'course', 'term', 'teacher', 'period', 'room')

@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
 list_display = ('enrollment_id', 'student', 'section', 'status')

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
 list_display = ('attendance_id', 'student', 'section', 'date', 'code')

@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
 list_display = ('grade_id', 'student', 'section', 'term', 'score')

@admin.register(Ledger)
class LedgerAdmin(admin.ModelAdmin):
 list_display = ('ledger_id', 'family', 'opened_on')

@admin.register(LedgerLine)
class LedgerLineAdmin(admin.ModelAdmin):
 list_display = ('line_id', 'ledger', 'kind', 'amount', 'posted_on')

@admin.register(Communication)
class CommunicationAdmin(admin.ModelAdmin):
 list_display = ('comm_id', 'audience', 'channel', 'sent_on')
 search_fields = ('audience',)
