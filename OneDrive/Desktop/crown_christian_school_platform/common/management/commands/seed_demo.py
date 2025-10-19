from django.core.management.base import BaseCommand
from django.db import transaction
import csv, random, datetime
from pathlib import Path
from students.models import Student, Guardian
from donations.models import Donation
from financial_aid.models import AidApplication
from finance.models import FinanceRecord
from discipline.models import DisciplineIncident

DATA_DIR = Path("data/demo")

class Command(BaseCommand):
    help = "Seed demo data from CSV files"

    def handle(self, *args, **options):
        with transaction.atomic():
            self.stdout.write("Seeding students & guardians...")
            guardians = []
            with open(DATA_DIR / "guardians.csv", newline="", encoding="utf-8") as f:
                for row in csv.DictReader(f):
                    g = Guardian.objects.create(
                        first_name=row["first_name"],
                        last_name=row["last_name"],
                        email=row["email"] or None,
                        phone=row["phone"] or None,
                    )
                    guardians.append(g)

            students = []
            with open(DATA_DIR / "students.csv", newline="", encoding="utf-8") as f:
                for row in csv.DictReader(f):
                    s = Student.objects.create(
                        first_name=row["first_name"],
                        last_name=row["last_name"],
                        grade_level=row["grade_level"],
                    )
                    # randomly attach a guardian
                    if guardians:
                        s.guardians.add(random.choice(guardians))
                    students.append(s)

            self.stdout.write("Seeding donations...")
            with open(DATA_DIR / "donations.csv", newline="", encoding="utf-8") as f:
                for row in csv.DictReader(f):
                    Donation.objects.create(
                        donor_name=row["donor_name"],
                        amount=row["amount"],
                        date=row["date"],
                        designation=row["designation"] or None,
                    )

            self.stdout.write("Seeding financial aid applications...")
            with open(DATA_DIR / "aid.csv", newline="", encoding="utf-8") as f:
                for row in csv.DictReader(f):
                    idx = int(row["student_index"]) - 1
                    if 0 <= idx < len(students):
                        AidApplication.objects.create(
                            student=students[idx],
                            year=row["year"],
                            requested_amount=row["requested"],
                            awarded_amount=row["awarded"],
                            status=row["status"],
                        )

            self.stdout.write("Seeding finance records...")
            with open(DATA_DIR / "finance.csv", newline="", encoding="utf-8") as f:
                for row in csv.DictReader(f):
                    idx = int(row["student_index"]) - 1
                    s = students[idx] if 0 <= idx < len(students) else None
                    FinanceRecord.objects.create(
                        student=s,
                        category=row["category"],
                        amount=row["amount"],
                        date=row["date"],
                        notes=row["notes"] or None,
                    )

            self.stdout.write("Seeding discipline incidents...")
            with open(DATA_DIR / "discipline.csv", newline="", encoding="utf-8") as f:
                for row in csv.DictReader(f):
                    idx = int(row["student_index"]) - 1
                    s = students[idx] if 0 <= idx < len(students) else None
                    DisciplineIncident.objects.create(
                        student=s,
                        date=row["date"],
                        incident_type=row["incident_type"],
                        notes=row["notes"] or None,
                    )

            self.stdout.write(self.style.SUCCESS("Demo data seeded."))
