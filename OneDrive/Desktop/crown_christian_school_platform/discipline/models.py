from django.db import models
from common.models import TimeStampedModel
from students.models import Student

class DisciplineIncident(TimeStampedModel):
    INCIDENT_CHOICES = [
        ("TARDY","Tardy"),
        ("DISRUPTION","Disruption"),
        ("DRESS_CODE","Dress Code"),
        ("OTHER","Other"),
    ]
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="incidents")
    date = models.DateField()
    incident_type = models.CharField(max_length=32, choices=INCIDENT_CHOICES)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.student} {self.incident_type} {self.date}"
