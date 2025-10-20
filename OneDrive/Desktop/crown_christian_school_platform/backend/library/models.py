from django.db import models

class Book(models.Model):
    isbn = models.CharField(max_length=20, unique=True)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=120)
    copies = models.PositiveIntegerField(default=1)

class Checkout(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrower_name = models.CharField(max_length=120)
    due_date = models.DateField()
    returned = models.BooleanField(default=False)
