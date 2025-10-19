from django.test import TestCase
from admissions.models import *

from admissions.models import Application

class AdmissionsModelTest(TestCase):
    def test_application_creation(self):
        app = Application.objects.create(first_name="Test", last_name="User", grade_applied="5")
        self.assertEqual(str(app), "Test User (5)")
