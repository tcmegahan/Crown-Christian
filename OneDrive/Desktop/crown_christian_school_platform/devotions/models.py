from django.db import models
from common.models import TimeStampedModel

class Devotion(TimeStampedModel):
    title = models.CharField(max_length=128)
    scripture = models.CharField(max_length=256, blank=True, null=True)
    content = models.TextField()
    date = models.DateField()

    def __str__(self):
        return f"{self.title} ({self.date})"
