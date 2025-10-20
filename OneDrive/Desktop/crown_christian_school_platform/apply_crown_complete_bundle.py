# ================================================================
#  Crown Christian School Solutions – Complete Platform Installer
# ================================================================
#  Creates the entire backend skeleton + modules for:
#   Admissions, Finance, Academics, Scheduling, Chapel, Activities,
#   CRM, Field Trips, Board Dashboard, Daycare, Fundraising,
#   Devotions, and Social Automation.
# ================================================================

import os, textwrap, sys

ROOT = os.path.abspath(os.path.dirname(__file__))
BACKEND = os.path.join(ROOT, "backend")
APPS = [
    "admissions","finance","academics","schedulemaster",
    "chapel","activities","crm","board","daycare",
    "fundraising","mission","integrations"
]

def make_dirs():
    for app in APPS:
        path = os.path.join(BACKEND, app)
        os.makedirs(path, exist_ok=True)
        os.makedirs(os.path.join(path, "management", "commands"), exist_ok=True)
        os.makedirs(os.path.join(path, "utils"), exist_ok=True)

def write(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path,"w",encoding="utf-8") as f: f.write(content.strip()+"\n")
    print("✔", os.path.relpath(path, ROOT))

# ----------------------------------------------------------------
# 1. Admissions & Enrollment
# ----------------------------------------------------------------
ADMISSIONS_MODELS = r'''
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
'''

# ----------------------------------------------------------------
# 2. Finance + Aid + Budget
# ----------------------------------------------------------------
FINANCE_MODELS = r'''
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
'''

# ----------------------------------------------------------------
# 3. Academics + Curriculum
# ----------------------------------------------------------------
ACADEMICS_MODELS = r'''
from django.db import models

class Course(models.Model):
    code = models.CharField(max_length=10)
    title = models.CharField(max_length=120)
    curriculum_source = models.CharField(max_length=80, choices=[
        ("BJU","BJU Press"),("Abeka","Abeka"),("PAC","Positive Action for Christ"),("PD","Purposeful Design")])
    grade_level = models.IntegerField()
    credits = models.DecimalField(max_digits=4, decimal_places=1, default=1.0)

class LessonPlan(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    week = models.IntegerField()
    topic = models.CharField(max_length=200)
    objectives = models.TextField()
    scripture_integration = models.CharField(max_length=255, blank=True)
'''

# ----------------------------------------------------------------
# 4. ScheduleMaster
# ----------------------------------------------------------------
SCHEDULE_MODELS = r'''
from django.db import models

class ScheduleTemplate(models.Model):
    name = models.CharField(max_length=120)
    structure = models.CharField(max_length=40, choices=[("Standard","Standard 45-min"),("Block","Block 90-min"),("Hybrid","Hybrid Wed Model")])
    description = models.TextField(blank=True)

class ClassPeriod(models.Model):
    template = models.ForeignKey(ScheduleTemplate, on_delete=models.CASCADE)
    day = models.CharField(max_length=10)
    start_time = models.TimeField()
    end_time = models.TimeField()
    subject = models.ForeignKey("academics.Course", on_delete=models.SET_NULL, null=True, blank=True)
'''

# ----------------------------------------------------------------
# 5. Chapel, Devotions, Activities (imports from previous build)
# ----------------------------------------------------------------
MISSION_UTILS = "from mission.utils.pdf_bulletin import generate_weekly_bulletin\n"  # placeholder, actual utils already built
# ----------------------------------------------------------------
# 6. CRM + Board + FieldTrips
# ----------------------------------------------------------------
CRM_MODELS = r'''
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
'''

FIELDTRIP_MODELS = r'''
from django.db import models

class FieldTrip(models.Model):
    title = models.CharField(max_length=120)
    date = models.DateField()
    location_name = models.CharField(max_length=200)
    address = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()
    description = models.TextField()
    teacher = models.ForeignKey("admissions.Family", on_delete=models.SET_NULL, null=True, blank=True)
'''

# ----------------------------------------------------------------
# 7. Daycare, Fundraising, Adult Learning
# ----------------------------------------------------------------
DAYCARE_MODELS = r'''
from django.db import models

class DaycareChild(models.Model):
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    age = models.IntegerField()
    guardian = models.ForeignKey("admissions.Family", on_delete=models.CASCADE)
    enrolled = models.BooleanField(default=True)

class AttendanceRecord(models.Model):
    child = models.ForeignKey(DaycareChild, on_delete=models.CASCADE)
    date = models.DateField()
    check_in = models.TimeField()
    check_out = models.TimeField()
'''

FUNDRAISING_MODELS = r'''
from django.db import models

class Campaign(models.Model):
    name = models.CharField(max_length=120)
    goal = models.DecimalField(max_digits=10, decimal_places=2)
    raised = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
'''

ADULT_ED_MODELS = r'''
from django.db import models

class AdultCourse(models.Model):
    title = models.CharField(max_length=120)
    instructor = models.CharField(max_length=120)
    schedule = models.CharField(max_length=200)
    tuition = models.DecimalField(max_digits=8, decimal_places=2)
    seats = models.IntegerField(default=15)
'''

# ----------------------------------------------------------------
# 8. Installer Logic
# ----------------------------------------------------------------
def main():
    make_dirs()
    write(os.path.join(BACKEND,"admissions","models.py"), ADMISSIONS_MODELS)
    write(os.path.join(BACKEND,"finance","models.py"), FINANCE_MODELS)
    write(os.path.join(BACKEND,"academics","models.py"), ACADEMICS_MODELS)
    write(os.path.join(BACKEND,"schedulemaster","models.py"), SCHEDULE_MODELS)
    write(os.path.join(BACKEND,"crm","models.py"), CRM_MODELS)
    write(os.path.join(BACKEND,"activities","models.py"), FIELDTRIP_MODELS)
    write(os.path.join(BACKEND,"daycare","models.py"), DAYCARE_MODELS)
    write(os.path.join(BACKEND,"fundraising","models.py"), FUNDRAISING_MODELS)
    write(os.path.join(BACKEND,"adultlearning","models.py"), ADULT_ED_MODELS)
    print("\n🎉 Crown Christian School Solutions core + modules created.")
    print(textwrap.dedent("""
        NEXT STEPS:
        1. Add each app to INSTALLED_APPS in backend/settings.py
        2. Run: python manage.py makemigrations && python manage.py migrate
        3. Start the server: python manage.py runserver
        4. Proceed to seed demo data using seed_demo_data_to_files.py
        5. Add the previously installed Mission & Social Automation bundle (already built)
    """))

if __name__ == "__main__":
    main()
