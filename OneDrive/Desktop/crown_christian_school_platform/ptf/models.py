from django.db import models
from common.models import TimeStampedModel
from students.models import Student

class VolunteerSignup(TimeStampedModel):
    parent_name = models.CharField(max_length=128)
    email = models.EmailField()
    event_name = models.CharField(max_length=128)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.parent_name} - {self.event_name}"
