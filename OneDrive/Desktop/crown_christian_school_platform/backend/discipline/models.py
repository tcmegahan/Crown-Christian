from django.db import models
from common.models import TimeStampedModel
from students.models import Student

class DisciplineIncident(TimeStampedModel):
    INCIDENT_CHOICES = [
        ("TARDY","Tardy"),
        ("ABSENT","Absent"),
        ("BEHAVIOR","Behavior"),
        ("OTHER","Other"),
    ]
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="discipline_incidents")
    incident_type = models.CharField(max_length=16, choices=INCIDENT_CHOICES)
    date = models.DateField()
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.student} {self.incident_type} {self.date}"
