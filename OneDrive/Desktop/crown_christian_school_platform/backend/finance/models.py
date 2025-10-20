from django.db import models

class FinancialAid(models.Model):
    student = models.ForeignKey("admissions.Student", on_delete=models.CASCADE)
    category = models.CharField(max_length=60, choices=[("Need","Need"),("Merit","Merit"),("Marketing","Marketing"),("EmptySeat","EmptySeat")])
    amount_awarded = models.DecimalField(max_digits=8, decimal_places=2)
    date_awarded = models.DateField(auto_now_add=True)

class TuitionPayment(models.Model):
    student = models.ForeignKey("admissions.Student", on_delete=models.CASCADE)
    amount_due = models.DecimalField(max_digits=8, decimal_places=2)
    amount_paid = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    due_date = models.DateField()
    paid_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=30, default="Pending")

class BudgetLine(models.Model):
    category = models.CharField(max_length=120)
    description = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.CharField(max_length=10, choices=[("Income","Income"),("Expense","Expense")])
    fiscal_year = models.IntegerField()
