from django.shortcuts import render
from students.models import Student
from finance.models import FinanceRecord
from financial_aid.models import AidApplication
from donations.models import Donation
from discipline.models import DisciplineIncident
from django.db.models import Sum

def home(request):
    totals = {
        "students": Student.objects.count(),
        "tuition": FinanceRecord.objects.filter(category="TUITION").aggregate(s=Sum("amount"))["s"] or 0,
        "aid": AidApplication.objects.aggregate(s=Sum("awarded_amount"))["s"] or 0,
        "donations": Donation.objects.aggregate(s=Sum("amount"))["s"] or 0,
    }
    recent_incidents = DisciplineIncident.objects.order_by("-date")[:10]
    return render(request, "dashboards/home.html", {"totals": totals, "recent_incidents": recent_incidents})
