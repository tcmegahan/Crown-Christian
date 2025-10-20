from django.db import models

class TransportRoute(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class TransportAssignment(models.Model):
    route = models.ForeignKey(TransportRoute, on_delete=models.CASCADE, related_name='assignments')
    student_id = models.IntegerField()
    assigned_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student_id} on {self.route.name}"
