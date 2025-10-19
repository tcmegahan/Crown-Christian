from django.test import TestCase
from finance.models import *

from finance.models import FinanceRecord
from students.models import Student

class FinanceModelTest(TestCase):
    def test_finance_record_creation(self):
        student = Student.objects.create(first_name="Test", last_name="Student", grade_level="5")
        record = FinanceRecord.objects.create(student=student, category="TUITION", amount=1000, date="2025-10-19")
        self.assertEqual(str(record), "TUITION $1000 on 2025-10-19")
