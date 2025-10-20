from django.core.management.base import BaseCommand
from django.conf import settings
from django.apps import apps
from django.db import connection

class Command(BaseCommand):
    help = "Validate Crown platform installation and demo data."

    def handle(self, *args, **options):
        errors = []
        # Check INSTALLED_APPS
        required_apps = [
            'backend.crm','backend.admissions','backend.sis','backend.finance','backend.communications',
            'backend.calendarx','backend.admin_dashboard','backend.analytics','backend.mission',
            'backend.scheduling','backend.academics','backend.library','backend.tutoring',
            'backend.athletics','backend.clubs','backend.field_trips','backend.transport',
            'backend.maintenance','backend.store','backend.lunch','backend.events','backend.fundraising',
            'backend.daycare','backend.surveys','backend.board','backend.ptf','backend.adult_learning',
            'backend.summer_camp','backend.integrations'
        ]
        missing = [app for app in required_apps if app not in settings.INSTALLED_APPS]
        if missing:
            errors.append(f"Missing apps in INSTALLED_APPS: {missing}")
        # Check migrations
        unmigrated = []
        for app in required_apps:
            try:
                app_config = apps.get_app_config(app.split('.')[-1])
                with connection.cursor() as cursor:
                    cursor.execute(f"SELECT COUNT(*) FROM django_migrations WHERE app = %s", [app_config.label])
                    if cursor.fetchone()[0] == 0:
                        unmigrated.append(app)
            except Exception:
                continue
        if unmigrated:
            errors.append(f"Apps missing migrations: {unmigrated}")
        # Check demo data
        try:
            from students.models import Student
            student_count = Student.objects.count()
            if student_count < 1:
                errors.append("No demo students found. Run seed_demo_data.")
        except Exception as e:
            errors.append(f"Demo data check failed: {e}")
        # Output
        if errors:
            for err in errors:
                self.stdout.write(self.style.ERROR(err))
            self.stdout.write(self.style.WARNING("Validation completed with errors."))
        else:
            self.stdout.write(self.style.SUCCESS("Crown platform installation and demo data validated successfully."))
