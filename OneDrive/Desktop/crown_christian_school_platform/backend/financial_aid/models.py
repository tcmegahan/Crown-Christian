from django.db import models
from common.models import TimeStampedModel
from students.models import Student

class AidApplication(TimeStampedModel):
    STATUS_CHOICES = [
        ("SUBMITTED","Submitted"),
        ("REVIEW","In Review"),
        ("AWARDED","Awarded"),
        ("DENIED","Denied"),
    ]
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="aid_applications")
    year = models.CharField(max_length=9)  # e.g. 2025-2026
    requested_amount = models.DecimalField(max_digits=10, decimal_places=2)
    awarded_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    status = models.CharField(max_length=16, choices=STATUS_CHOICES, default="SUBMITTED")

    def __str__(self):
        return f"Aid {self.student} {self.year} {self.status}"
