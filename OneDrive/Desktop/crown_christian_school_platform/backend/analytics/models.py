from django.db import models

class MetricSnapshot(models.Model):
    captured_at = models.DateTimeField(auto_now_add=True)
    key = models.CharField(max_length=120)
    value = models.FloatField(default=0)
