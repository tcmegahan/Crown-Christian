from django.db import models

class Course(models.Model):
    code = models.CharField(max_length=10)
    title = models.CharField(max_length=120)
    curriculum_source = models.CharField(max_length=80, choices=[
        ("BJU","BJU Press"),("Abeka","Abeka"),("PAC","Positive Action for Christ"),("PD","Purposeful Design")])
    grade_level = models.IntegerField()
    credits = models.DecimalField(max_digits=4, decimal_places=1, default=1.0)

class LessonPlan(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    week = models.IntegerField()
    topic = models.CharField(max_length=200)
    objectives = models.TextField()
    scripture_integration = models.CharField(max_length=255, blank=True)
