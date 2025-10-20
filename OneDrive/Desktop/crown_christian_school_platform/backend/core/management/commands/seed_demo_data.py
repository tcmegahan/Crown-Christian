from django.core.management.base import BaseCommand
import csv, os
from backend.admissions.models import Student as AdmissionsStudent
from students.models import Student as StudentsStudent
from backend.finance.models import TuitionPayment
from backend.financial_aid.models import AidApplication
from backend.finance.models import FinancialAid
from backend.donations.models import Donation
from backend.discipline.models import DisciplineIncident

class Command(BaseCommand):
    help = 'Seed demo data from CSV files in data/demo/'

    def handle(self, *args, **options):
        import logging
        logger = logging.getLogger("seed_demo_data")
        from backend.admissions.models import Family
        demo_family, _ = Family.objects.get_or_create(email='demo@school.com', defaults={
            'father_name': 'Demo Father',
            'mother_name': 'Demo Mother',
            'phone': '555-5555',
            'address': '123 Demo St.'
        })
        # Clear all related demo data for a clean import
        TuitionPayment.objects.all().delete()
        FinancialAid.objects.all().delete()
        Donation.objects.all().delete()
        DisciplineIncident.objects.all().delete()
        AdmissionsStudent.objects.all().delete()
        StudentsStudent.objects.all().delete()
        project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
        base_path = os.path.join(project_root, 'data', 'demo')
        # Build student index to PK mapping and create students in both admissions and students apps
        student_map = {}
        students_student_map = {}
        with open(os.path.join(base_path, 'students.csv'), newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for idx, row in enumerate(reader, start=1):
                try:
                    grade_val = row['grade_level']
                    if grade_val == 'K':
                        grade_val = 0
                    else:
                        try:
                            grade_val = int(grade_val)
                        except Exception:
                            grade_val = 0
                    # Create in admissions
                    admissions_student, _ = AdmissionsStudent.objects.update_or_create(
                        family=demo_family,
                        first_name=row['first_name'],
                        last_name=row['last_name'],
                        grade=grade_val,
                        birth_date=row.get('birth_date', '2010-01-01'),
                        defaults={}
                    )
                    student_map[str(idx)] = admissions_student.pk
                    # Create in students app
                    students_student, _ = StudentsStudent.objects.update_or_create(
                        first_name=row['first_name'],
                        last_name=row['last_name'],
                        grade_level=row['grade_level'],
                        date_of_birth=row.get('birth_date', '2010-01-01'),
                        defaults={}
                    )
                    students_student_map[str(idx)] = students_student.pk
                except Exception as e:
                    logger.error(f"Student row {idx} failed: {e}")
                    self.stdout.write(self.style.WARNING(f"Student row {idx} failed: {e}"))

        # Tuition Payments
        with open(os.path.join(base_path, 'finance.csv'), newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                student_pk = student_map.get(row['student_index'])
                if not student_pk:
                    self.stdout.write(self.style.WARNING(f"No student for index {row['student_index']}"))
                    continue
                TuitionPayment.objects.update_or_create(
                    student=AdmissionsStudent.objects.get(pk=student_pk),
                    amount_due=row.get('amount_due', row['amount']),
                    amount_paid=row['amount'],
                    due_date=row['date'],
                    defaults={"status": "Paid"}
                )

        # Financial Aid
        with open(os.path.join(base_path, 'aid.csv'), newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                student_pk = student_map.get(row['student_index'])
                if not student_pk:
                    self.stdout.write(self.style.WARNING(f"No student for index {row['student_index']}"))
                    continue
                date_val = row['year']
                try:
                    import datetime
                    datetime.datetime.strptime(date_val, '%Y-%m-%d')
                except Exception:
                    date_val = '2025-01-01'
                FinancialAid.objects.update_or_create(
                    student=AdmissionsStudent.objects.get(pk=student_pk),
                    amount_awarded=row['awarded'],
                    date_awarded=date_val,
                    defaults={"category": "Need"}
                )

        # Donations (no student mapping needed)
        with open(os.path.join(base_path, 'donations.csv'), newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                Donation.objects.update_or_create(
                    donor_name=row['donor_name'],
                    amount=row['amount'],
                    date=row['date'],
                    defaults={}
                )

        # Discipline
        with open(os.path.join(base_path, 'discipline.csv'), newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                try:
                    student_pk = students_student_map.get(row['student_index'])
                    if not student_pk:
                        self.stdout.write(self.style.WARNING(f"No student for index {row['student_index']}"))
                        continue
                    DisciplineIncident.objects.update_or_create(
                        student=StudentsStudent.objects.get(pk=student_pk),
                        incident_type=row['incident_type'],
                        date=row['date'],
                        defaults={"notes": row.get('notes', '')}
                    )
                except Exception as e:
                    logger.error(f"Discipline row failed: {e}")
                    self.stdout.write(self.style.WARNING(f"Discipline row failed: {e}"))
        # --- SCHEDULE TEMPLATES AND PERIODS ---
        try:
            from backend.schedulemaster.models import ScheduleTemplate, ClassPeriod
            import datetime
            # Clear existing schedule data
            ScheduleTemplate.objects.all().delete()
            # Standard 45-min schedule
            std_template = ScheduleTemplate.objects.create(
                name="Standard Day",
                structure="Standard",
                description="Standard 7-period day, 45 minutes each."
            )
            for i, (day, periods) in enumerate([
                ("Monday", [
                    ("08:00", "08:45"), ("08:50", "09:35"), ("09:40", "10:25"), ("10:30", "11:15"), ("11:20", "12:05"), ("12:10", "12:55"), ("13:00", "13:45")
                ]),
                ("Tuesday", [
                    ("08:00", "08:45"), ("08:50", "09:35"), ("09:40", "10:25"), ("10:30", "11:15"), ("11:20", "12:05"), ("12:10", "12:55"), ("13:00", "13:45")
                ]),
                ("Wednesday", [
                    ("08:00", "08:45"), ("08:50", "09:35"), ("09:40", "10:25"), ("10:30", "11:15"), ("11:20", "12:05"), ("12:10", "12:55"), ("13:00", "13:45")
                ]),
                ("Thursday", [
                    ("08:00", "08:45"), ("08:50", "09:35"), ("09:40", "10:25"), ("10:30", "11:15"), ("11:20", "12:05"), ("12:10", "12:55"), ("13:00", "13:45")
                ]),
                ("Friday", [
                    ("08:00", "08:45"), ("08:50", "09:35"), ("09:40", "10:25"), ("10:30", "11:15"), ("11:20", "12:05"), ("12:10", "12:55"), ("13:00", "13:45")
                ]),
            ]):
                for idx, (start, end) in enumerate(periods, 1):
                    ClassPeriod.objects.create(
                        template=std_template,
                        day=day,
                        start_time=datetime.time.fromisoformat(start),
                        end_time=datetime.time.fromisoformat(end),
                        subject=None
                    )
            # Block 90-min schedule
            block_template = ScheduleTemplate.objects.create(
                name="Block Schedule",
                structure="Block",
                description="Block schedule with 4 periods, 90 minutes each."
            )
            for day, periods in [
                ("Monday", [("08:00", "09:30"), ("09:40", "11:10"), ("11:20", "12:50"), ("13:00", "14:30")]),
                ("Wednesday", [("08:00", "09:30"), ("09:40", "11:10"), ("11:20", "12:50"), ("13:00", "14:30")]),
                ("Friday", [("08:00", "09:30"), ("09:40", "11:10"), ("11:20", "12:50"), ("13:00", "14:30")]),
            ]:
                for idx, (start, end) in enumerate(periods, 1):
                    ClassPeriod.objects.create(
                        template=block_template,
                        day=day,
                        start_time=datetime.time.fromisoformat(start),
                        end_time=datetime.time.fromisoformat(end),
                        subject=None
                    )
            # Hybrid (Modified Block) schedule
            hybrid_template = ScheduleTemplate.objects.create(
                name="Hybrid Wednesday",
                structure="Hybrid",
                description="Modified block schedule for Wednesdays."
            )
            for day, periods in [
                ("Wednesday", [("08:00", "09:00"), ("09:10", "10:10"), ("10:20", "11:20"), ("11:30", "12:30"), ("13:00", "14:00")]),
            ]:
                for idx, (start, end) in enumerate(periods, 1):
                    ClassPeriod.objects.create(
                        template=hybrid_template,
                        day=day,
                        start_time=datetime.time.fromisoformat(start),
                        end_time=datetime.time.fromisoformat(end),
                        subject=None
                    )
            self.stdout.write(self.style.SUCCESS('Schedule templates and periods seeded.'))
        except Exception as e:
            self.stdout.write(self.style.WARNING(f"Schedule seeding failed: {e}"))
        self.stdout.write(self.style.SUCCESS('Demo data seeded successfully.'))
