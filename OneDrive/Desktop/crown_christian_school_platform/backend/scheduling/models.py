from django.db import models

class Course(models.Model):
    code = models.CharField(max_length=20, unique=True)
    title = models.CharField(max_length=200)
    credits = models.DecimalField(max_digits=4, decimal_places=1, default=0.5)
    grade_min = models.PositiveIntegerField(default=6)
    grade_max = models.PositiveIntegerField(default=12)
    dual_enrollment = models.BooleanField(default=False)

class Section(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    term = models.CharField(max_length=20, default="FY")
    teacher = models.CharField(max_length=120, blank=True, null=True)
    room = models.CharField(max_length=20, blank=True, null=True)
    capacity = models.PositiveIntegerField(default=28)
    schedule_pattern = models.CharField(max_length=20, default="standard")
    m = models.BooleanField(default=True)
    t = models.BooleanField(default=True)
    w = models.BooleanField(default=True)
    th = models.BooleanField(default=True)
    f = models.BooleanField(default=True)
    start_time = models.TimeField(blank=True, null=True)
    end_time = models.TimeField(blank=True, null=True)

class Enrollment(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name="enrollments")
    student = models.CharField(max_length=120)
    status = models.CharField(max_length=20, default="enrolled")
    class Meta:
        unique_together = ("section","student")
