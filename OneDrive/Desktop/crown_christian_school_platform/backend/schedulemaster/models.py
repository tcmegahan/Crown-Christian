from django.db import models

class ScheduleTemplate(models.Model):
    name = models.CharField(max_length=120)
    structure = models.CharField(max_length=40, choices=[("Standard","Standard 45-min"),("Block","Block 90-min"),("Hybrid","Hybrid Wed Model")])
    description = models.TextField(blank=True)

class ClassPeriod(models.Model):
    template = models.ForeignKey(ScheduleTemplate, on_delete=models.CASCADE)
    day = models.CharField(max_length=10)
    start_time = models.TimeField()
    end_time = models.TimeField()
    subject = models.ForeignKey("academics.Course", on_delete=models.SET_NULL, null=True, blank=True)
