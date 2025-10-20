from django.db import models

class Club(models.Model):
    name = models.CharField(max_length=120)
    sponsor = models.CharField(max_length=120, blank=True, null=True)

class ClubMembership(models.Model):
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    member = models.CharField(max_length=120)
    role = models.CharField(max_length=40, default="member")
    class Meta:
        unique_together = ("club","member")
