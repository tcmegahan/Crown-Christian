from django.db import models

class AdultCourse(models.Model):
    title = models.CharField(max_length=120)
    instructor = models.CharField(max_length=120)
    schedule = models.CharField(max_length=200)
    tuition = models.DecimalField(max_digits=8, decimal_places=2)
    seats = models.IntegerField(default=15)
