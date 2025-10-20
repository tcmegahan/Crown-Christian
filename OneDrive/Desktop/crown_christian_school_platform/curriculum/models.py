
from django.db import models
from common.models import TimeStampedModel
from students.models import Student

class LessonPlan(TimeStampedModel):
    course = models.ForeignKey('Course', on_delete=models.CASCADE, related_name='lesson_plans')
    teacher = models.ForeignKey('staff.StaffMember', on_delete=models.SET_NULL, null=True, blank=True, related_name='lesson_plans')
    title = models.CharField(max_length=128)
    publisher = models.CharField(max_length=64, blank=True, null=True)
    content = models.TextField()
    date = models.DateField()

    def __str__(self):
        return f"{self.title} ({self.publisher}) - {self.course}"


class Course(TimeStampedModel):
    code = models.CharField(max_length=16, unique=True)
    title = models.CharField(max_length=128)
    grade_band = models.CharField(max_length=32)  # e.g., 9-12
    description = models.TextField(blank=True, null=True)
    teacher = models.ForeignKey('staff.StaffMember', on_delete=models.SET_NULL, null=True, blank=True, related_name='courses')

    def __str__(self):
        return f"{self.code}: {self.title}"

class Enrollment(TimeStampedModel):
    student = models.ForeignKey("students.Student", on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    year = models.CharField(max_length=9)

    class Meta:
        unique_together = ("student","course","year")
