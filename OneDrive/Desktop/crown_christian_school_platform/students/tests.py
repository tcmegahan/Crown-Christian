from django.test import TestCase

# Add your students app tests herefrom django.test import TestCase
from students.models import Guardian, Student

class GuardianModelTest(TestCase):
    def test_guardian_creation(self):
        guardian = Guardian.objects.create(first_name="John", last_name="Doe", email="john@example.com", phone="1234567890")
        self.assertEqual(str(guardian), "John Doe")

class StudentModelTest(TestCase):
    def test_student_creation(self):
        guardian = Guardian.objects.create(first_name="Jane", last_name="Smith")
        student = Student.objects.create(first_name="Alice", last_name="Brown", grade_level="5")
        student.guardians.add(guardian)
        self.assertEqual(student.full_name, "Alice Brown")
        self.assertIn(guardian, student.guardians.all())
