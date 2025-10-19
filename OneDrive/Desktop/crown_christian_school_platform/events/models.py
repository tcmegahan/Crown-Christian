from django.db import models
from common.models import TimeStampedModel

class Event(TimeStampedModel):
    title = models.CharField(max_length=128)
    date = models.DateField()
    location = models.CharField(max_length=128, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.title} on {self.date}"
