from django.db import models

class FieldTrip(models.Model):
    title = models.CharField(max_length=120)
    date = models.DateField()
    location_name = models.CharField(max_length=200)
    address = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()
    description = models.TextField()
    teacher = models.ForeignKey("admissions.Family", on_delete=models.SET_NULL, null=True, blank=True)
