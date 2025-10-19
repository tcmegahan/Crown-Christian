from django.db import models
from common.models import TimeStampedModel

class ChapelEvent(TimeStampedModel):
    title = models.CharField(max_length=128)
    speaker = models.CharField(max_length=128, blank=True, null=True)
    date = models.DateField()
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.title} ({self.date})"
