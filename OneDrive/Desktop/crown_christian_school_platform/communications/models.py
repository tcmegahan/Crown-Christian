from django.db import models
from common.models import TimeStampedModel

class CommunicationMessage(TimeStampedModel):
    channel = models.CharField(max_length=32, default="Email")  # Email, SMS, Teams
    subject = models.CharField(max_length=128)
    body = models.TextField()
    sent_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.channel}: {self.subject}"
