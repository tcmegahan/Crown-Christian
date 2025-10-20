from django.db import models

class DaycareChild(models.Model):
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    age = models.IntegerField()
    guardian = models.ForeignKey("admissions.Family", on_delete=models.CASCADE)
    enrolled = models.BooleanField(default=True)

class AttendanceRecord(models.Model):
    child = models.ForeignKey(DaycareChild, on_delete=models.CASCADE)
    date = models.DateField()
    check_in = models.TimeField()
    check_out = models.TimeField()
