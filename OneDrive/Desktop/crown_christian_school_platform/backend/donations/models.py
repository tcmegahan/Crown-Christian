from django.db import models
from common.models import TimeStampedModel

class Donation(TimeStampedModel):
    donor_name = models.CharField(max_length=128)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.donor_name} ${self.amount}"
