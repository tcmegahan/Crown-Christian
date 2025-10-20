from django.db import models

class TutoringSession(models.Model):
    student = models.CharField(max_length=120)
    tutor = models.CharField(max_length=120)
    subject = models.CharField(max_length=80)
    date = models.DateField()
    start = models.TimeField()
    end = models.TimeField()
    notes = models.TextField(blank=True, null=True)
