from django.db import models
from common.models import TimeStampedModel

class Application(TimeStampedModel):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    grade_applied = models.CharField(max_length=16)
    status = models.CharField(max_length=32, default="Received")  # Received, Review, Accepted, Waitlist, Declined

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.grade_applied})"
