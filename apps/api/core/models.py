import uuid
from django.db import models


class Family(models.Model):
    household_id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=255)
    address = models.TextField(blank=True)
    phone = models.CharField(max_length=50, blank=True)

    class Meta:
        db_table = 'core_family'


class Guardian(models.Model):
    guardian_id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    family = models.ForeignKey(Family, on_delete=models.CASCADE, related_name='guardians')
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=50, blank=True)

    class Meta:
        db_table = 'core_guardian'


class Student(models.Model):
    student_id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    family = models.ForeignKey(Family, on_delete=models.CASCADE, related_name='students')
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    dob = models.DateField(null=True, blank=True)
    grade_level = models.CharField(max_length=20, blank=True)
    status = models.CharField(max_length=20, default='active')

    class Meta:
        db_table = 'core_student'


# Additional core models
class Term(models.Model):
    term_id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()

    class Meta:
        db_table = 'core_term'


class Course(models.Model):
    course_id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    code = models.CharField(max_length=50)
    name = models.CharField(max_length=255)
    credits = models.DecimalField(max_digits=5, decimal_places=2, default=0)

    class Meta:
        db_table = 'core_course'


class Section(models.Model):
    section_id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='sections')
    term = models.ForeignKey(Term, on_delete=models.CASCADE, related_name='sections')
    teacher = models.CharField(max_length=255, blank=True)
    period = models.CharField(max_length=50, blank=True)
    room = models.CharField(max_length=50, blank=True)

    class Meta:
        db_table = 'core_section'


class Enrollment(models.Model):
    ENROLL_STATUS = (
        ('active', 'Active'),
        ('withdrawn', 'Withdrawn'),
        ('completed', 'Completed'),
    )
    enrollment_id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='enrollments')
    section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name='enrollments')
    status = models.CharField(max_length=20, choices=ENROLL_STATUS, default='active')

    class Meta:
        db_table = 'core_enrollment'
        unique_together = ('student', 'section')


class Attendance(models.Model):
    attendance_id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='attendance')
    section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name='attendance')
    date = models.DateField()
    code = models.CharField(max_length=20)
    note = models.TextField(blank=True)

    class Meta:
        db_table = 'core_attendance'
        unique_together = ('student', 'section', 'date')


class Grade(models.Model):
    grade_id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='grades')
    section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name='grades')
    term = models.ForeignKey(Term, on_delete=models.CASCADE, related_name='grades')
    score = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    scale = models.CharField(max_length=50, blank=True)
    comment = models.TextField(blank=True)

    class Meta:
        db_table = 'core_grade'
        unique_together = ('student', 'section', 'term')


class Ledger(models.Model):
    ledger_id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    family = models.ForeignKey(Family, on_delete=models.CASCADE, related_name='ledgers')
    opened_on = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'core_ledger'


class LedgerLine(models.Model):
    KIND_CHOICES = (
        ('INVOICE', 'Invoice'),
        ('PAYMENT', 'Payment'),
        ('ADJUST', 'Adjust'),
    )
    line_id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    ledger = models.ForeignKey(Ledger, on_delete=models.CASCADE, related_name='lines')
    kind = models.CharField(max_length=20, choices=KIND_CHOICES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    memo = models.CharField(max_length=512, blank=True)
    posted_on = models.DateField(auto_now_add=True)
    external_ref = models.CharField(max_length=255, blank=True)

    class Meta:
        db_table = 'core_ledgerline'


class Communication(models.Model):
    CHANNEL_CHOICES = (
        ('EMAIL', 'Email'),
        ('SMS', 'SMS'),
        ('TEAMS', 'Teams'),
    )
    comm_id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    audience = models.CharField(max_length=255)
    channel = models.CharField(max_length=20, choices=CHANNEL_CHOICES)
    template = models.TextField()
    sent_on = models.DateTimeField(null=True, blank=True)
    meta = models.JSONField(default=dict, blank=True)

    class Meta:
        db_table = 'core_communication'
