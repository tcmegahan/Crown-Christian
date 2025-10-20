from django.db import models

class LunchMenu(models.Model):
    date = models.DateField()
    items = models.TextField()

    def __str__(self):
        return f"Menu for {self.date}"
