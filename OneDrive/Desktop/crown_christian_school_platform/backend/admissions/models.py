from django.db import models

class Family(models.Model):
    father_name = models.CharField(max_length=120, blank=True)
    mother_name = models.CharField(max_length=120, blank=True)
    email = models.EmailField()
    phone = models.CharField(max_length=40)
    address = models.CharField(max_length=255)

class Student(models.Model):
    family = models.ForeignKey(Family, on_delete=models.CASCADE, related_name="students")
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    grade = models.IntegerField()
    birth_date = models.DateField()
    enrolled = models.BooleanField(default=False)
    financial_aid_applied = models.BooleanField(default=False)

class Application(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date_submitted = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=40, default="Pending")
    notes = models.TextField(blank=True)

class AdmissionDecision(models.Model):
    application = models.OneToOneField(Application, on_delete=models.CASCADE)
    decision = models.CharField(max_length=40, choices=[("Accepted","Accepted"),("Waitlisted","Waitlisted"),("Declined","Declined")])
    decision_date = models.DateField(auto_now_add=True)
    scholarship_amount = models.DecimalField(max_digits=8, decimal_places=2, default=0)
