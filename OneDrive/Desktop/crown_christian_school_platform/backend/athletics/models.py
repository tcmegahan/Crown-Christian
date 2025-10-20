from django.db import models

class Team(models.Model):
    name = models.CharField(max_length=120)
    sport = models.CharField(max_length=80)
    coach = models.CharField(max_length=120, blank=True, null=True)

class Game(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    opponent = models.CharField(max_length=200)
    date = models.DateField()
    time = models.TimeField(blank=True, null=True)
    location = models.CharField(max_length=200, blank=True, null=True)
    result = models.CharField(max_length=40, blank=True, null=True)
