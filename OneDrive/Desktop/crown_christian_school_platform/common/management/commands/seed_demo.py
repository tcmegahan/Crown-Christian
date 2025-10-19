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

            # --- EXTENDED MOCK DATA FOR ALL MODULES ---
            from faker import Faker
            from admissions.models import Application
            from staff.models import StaffMember
            from curriculum.models import Course, Enrollment
            from events.models import Event
            from communications.models import CommunicationMessage
            from devotions.models import Devotion
            fake = Faker()

            self.stdout.write("Seeding admissions applications...")
            grades = [f"PK{i}" for i in range(3)] + [str(i) for i in range(1, 13)]
            for grade in grades:
                for _ in range(3):
                    Application.objects.create(
                        first_name=fake.first_name(),
                        last_name=fake.last_name(),
                        grade_applied=grade,
                        status=random.choice(["Received", "Review", "Accepted", "Waitlist", "Declined"]),
                    )

            self.stdout.write("Seeding staff members...")
            roles = ["Administrator", "Principal"] + [f"Teacher {g}" for g in grades]
            for role in roles:
                StaffMember.objects.create(
                    first_name=fake.first_name(),
                    last_name=fake.last_name(),
                    role=role,
                )

            self.stdout.write("Seeding curriculum courses and enrollments...")
            course_objs = []
            for grade in grades:
                for i in range(2):
                    course = Course.objects.create(
                        code=f"{grade}-C{i+1}",
                        title=f"{grade} Course {i+1}",
                        grade_band=grade,
                        description=fake.sentence(),
                    )
                    course_objs.append(course)
            # Enroll students in courses
            for student in students:
                for course in random.sample(course_objs, k=min(2, len(course_objs))):
                    Enrollment.objects.get_or_create(
                        student=student,
                        course=course,
                        year=str(datetime.datetime.now().year),
                    )

            self.stdout.write("Seeding events...")
            for _ in range(10):
                Event.objects.create(
                    title=fake.catch_phrase(),
                    date=fake.date_between(start_date="-1y", end_date="today"),
                    location=fake.company(),
                    description=fake.text(max_nb_chars=100),
                )

            self.stdout.write("Seeding communications...")
            for _ in range(15):
                CommunicationMessage.objects.create(
                    channel=random.choice(["Email", "SMS", "Teams"]),
                    subject=fake.sentence(nb_words=6),
                    body=fake.text(max_nb_chars=200),
                    sent_at=fake.date_time_this_year(),
                )

            self.stdout.write("Seeding devotions...")
            for _ in range(10):
                Devotion.objects.create(
                    title=fake.sentence(nb_words=4),
                    scripture=fake.sentence(nb_words=6),
                    content=fake.text(max_nb_chars=300),
                    date=fake.date_between(start_date="-1y", end_date="today"),
                )

            self.stdout.write(self.style.SUCCESS("Demo data seeded."))
