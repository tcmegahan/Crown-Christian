from django.db import models

class MaintenanceRequest(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    submitted_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, default='Open')

    def __str__(self):
        return f"{self.title} ({self.status})"