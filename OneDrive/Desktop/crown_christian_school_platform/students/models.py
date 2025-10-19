from django.db import models
from common.models import TimeStampedModel

class Guardian(TimeStampedModel):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=32, blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Student(TimeStampedModel):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    grade_level = models.CharField(max_length=16)
    date_of_birth = models.DateField(null=True, blank=True)
    guardians = models.ManyToManyField(Guardian, related_name="students", blank=True)

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name
