def student_dashboard(request):
    # For demonstration, use the first student
    from students.models import Student
    from curriculum.models import Enrollment, Course
    from events.models import Event
    from devotions.models import Devotion
    student = Student.objects.first()
    # My schedule: courses enrolled
    enrollments = Enrollment.objects.filter(student=student) if student else []
    my_courses = [e.course for e in enrollments]
    # Assignments: placeholder (no model)
    assignments = []
    # Events: next 3 events
    upcoming_events = Event.objects.order_by('date')[:3]
    # Devotions: latest
    latest_devotion = Devotion.objects.order_by('-created').first()
    return render(request, "dashboards/student_dashboard.html", {
        "student": student,
        "my_courses": my_courses,
        "assignments": assignments,
        "upcoming_events": upcoming_events,
        "latest_devotion": latest_devotion,
    })
def parent_dashboard(request):
    # For demonstration, use the first guardian as the parent
    from students.models import Guardian, Student
    from communications.models import CommunicationMessage
    from events.models import Event
    parent = Guardian.objects.first()
    my_children = parent.students.all() if parent else []
    # School news: recent communication messages
    school_news = CommunicationMessage.objects.order_by('-created')[:5]
    # Events: next 3 events
    upcoming_events = Event.objects.order_by('date')[:3]
    return render(request, "dashboards/parent_dashboard.html", {
        "parent": parent,
        "my_children": my_children,
        "school_news": school_news,
        "upcoming_events": upcoming_events,
    })

def teacher_dashboard(request):
    # For demonstration, use the first staff member as the teacher
    from staff.models import StaffMember
    from curriculum.models import Course, LessonPlan, Enrollment
    teacher = StaffMember.objects.first()
    my_classes = Course.objects.filter(teacher=teacher)
    # Students per class
    class_students = {}
    for c in my_classes:
        enrollments = Enrollment.objects.filter(course=c)
        class_students[c] = [e.student for e in enrollments]
    # Lesson plans for teacher's classes
    lesson_plans = LessonPlan.objects.filter(course__in=my_classes)
    # Analytics: students per class
    analytics_labels = [c.title for c in my_classes]
    analytics_counts = [len(class_students[c]) for c in my_classes]
    analytics_data = {"labels": analytics_labels, "counts": analytics_counts}
    return render(request, "dashboards/teacher_dashboard.html", {
        "teacher": teacher,
        "my_classes": my_classes,
        "class_students": class_students,
        "lesson_plans": lesson_plans,
        "analytics_data": analytics_data,
    })

def staff_dashboard(request):
    # Placeholder for staff dashboard context
    return render(request, "dashboards/staff_dashboard.html")

from django.shortcuts import render
from students.models import Student
from backend.finance.models import FinancialAid, TuitionPayment, BudgetLine
from backend.financial_aid.models import AidApplication
from backend.donations.models import Donation
from backend.discipline.models import DisciplineIncident
from django.db.models import Sum, Count


def admin_dashboard(request):
    totals = {
        "students": Student.objects.count(),
        "tuition": TuitionPayment.objects.aggregate(s=Sum("amount_paid"))["s"] or 0,
        "aid": FinancialAid.objects.aggregate(s=Sum("amount_awarded"))["s"] or 0,
        "donations": Donation.objects.aggregate(s=Sum("amount"))["s"] or 0,
    }
    finance_data = {
        "labels": ["Tuition Paid", "Aid Awarded", "Donations"],
        "amounts": [totals["tuition"], totals["aid"], totals["donations"]],
    }
    import datetime
    from django.db.models.functions import TruncMonth
    now = datetime.date.today()
    last_year = now - datetime.timedelta(days=365)
    incidents_by_month = (
        DisciplineIncident.objects.filter(date__gte=last_year)
        .annotate(month=TruncMonth("date"))
        .values("month")
        .order_by("month")
        .annotate(count=Count("id"))
    )
    months = []
    counts = []
    for entry in incidents_by_month:
        months.append(entry["month"].strftime("%b %Y"))
        counts.append(entry["count"])
    discipline_trend = {"labels": months, "counts": counts}
    recent_incidents = DisciplineIncident.objects.order_by("-date")[:5]
    # Enrollment chart data (stub, replace with real logic if needed)
    enrollment_data = {
        "labels": ["K", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"],
        "counts": [Student.objects.filter(grade_level=g).count() for g in range(0, 13)],
    }
    return render(request, "dashboards/admin_dashboard.html", {
        "totals": totals,
        "recent_incidents": recent_incidents,
        "enrollment_data": enrollment_data,
        "finance_data": finance_data,
        "discipline_trend": discipline_trend,
    })
