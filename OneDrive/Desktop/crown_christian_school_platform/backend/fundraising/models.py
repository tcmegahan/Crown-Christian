from django.db import models

class Campaign(models.Model):
    name = models.CharField(max_length=120)
    goal = models.DecimalField(max_digits=10, decimal_places=2)
    raised = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
