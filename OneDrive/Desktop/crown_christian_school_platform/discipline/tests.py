from django.test import TestCase
from discipline.models import *

from discipline.models import DisciplineIncident
from students.models import Student

class DisciplineModelTest(TestCase):
    def test_discipline_incident_creation(self):
        student = Student.objects.create(first_name="Test", last_name="Student", grade_level="5")
        incident = DisciplineIncident.objects.create(student=student, date="2025-10-19", incident_type="TARDY")
        self.assertIn("TARDY", str(incident))
