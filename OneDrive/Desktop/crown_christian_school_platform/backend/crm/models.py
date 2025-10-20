from django.db import models

class ContactLog(models.Model):
    user = models.CharField(max_length=120)
    date = models.DateTimeField(auto_now_add=True)
    contact_type = models.CharField(max_length=50, choices=[("Email","Email"),("Phone","Phone"),("InPerson","InPerson")])
    notes = models.TextField()

class BoardReport(models.Model):
    title = models.CharField(max_length=120)
    created = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    file = models.FileField(upload_to="board_reports/", blank=True, null=True)
