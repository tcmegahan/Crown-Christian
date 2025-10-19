from django.db import models
from common.models import TimeStampedModel

class StaffMember(TimeStampedModel):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    role = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.role}"
