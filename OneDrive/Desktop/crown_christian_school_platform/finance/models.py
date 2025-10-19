from django.db import models
from common.models import TimeStampedModel
from students.models import Student

class FinanceRecord(TimeStampedModel):
    CATEGORY_CHOICES = [
        ("TUITION","Tuition"),
        ("AID","Financial Aid"),
        ("DONATION","Donation"),
        ("FEE","Fee"),
    ]
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="finance_records", null=True, blank=True)
    category = models.CharField(max_length=16, choices=CATEGORY_CHOICES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.category} ${self.amount} on {self.date}"
