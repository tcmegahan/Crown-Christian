from rest_framework import serializers
from .models import (
 Family,
 Guardian,
 Student,
 Term,
 Course,
 Section,
 Enrollment,
 Attendance,
 Grade,
 Ledger,
 LedgerLine,
 Communication,
)

class FamilySerializer(serializers.ModelSerializer):
 class Meta:
  model = Family
  fields = ('household_id', 'name', 'address', 'phone')

class GuardianSerializer(serializers.ModelSerializer):
 class Meta:
  model = Guardian
  fields = ('guardian_id', 'family', 'first_name', 'last_name', 'email', 'phone')

class StudentSerializer(serializers.ModelSerializer):
 class Meta:
  model = Student
  fields = ('student_id', 'family', 'first_name', 'last_name', 'dob', 'grade_level', 'status')

class TermSerializer(serializers.ModelSerializer):
 class Meta:
  model = Term
  fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
 class Meta:
  model = Course
  fields = '__all__'

class SectionSerializer(serializers.ModelSerializer):
 class Meta:
  model = Section
  fields = '__all__'

class EnrollmentSerializer(serializers.ModelSerializer):
 class Meta:
  model = Enrollment
  fields = '__all__'

class AttendanceSerializer(serializers.ModelSerializer):
 class Meta:
  model = Attendance
  fields = '__all__'

class GradeSerializer(serializers.ModelSerializer):
 class Meta:
  model = Grade
  fields = '__all__'

class LedgerSerializer(serializers.ModelSerializer):
 class Meta:
  model = Ledger
  fields = '__all__'

class LedgerLineSerializer(serializers.ModelSerializer):
 class Meta:
  model = LedgerLine
  fields = '__all__'

class CommunicationSerializer(serializers.ModelSerializer):
 class Meta:
  model = Communication
  fields = ('comm_id', 'audience', 'channel', 'template', 'sent_on', 'meta')
