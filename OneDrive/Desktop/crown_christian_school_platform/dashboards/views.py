from django.shortcuts import render
from students.models import Student
from backend.finance.models import FinancialAid, TuitionPayment, BudgetLine
FinanceRecord = None  # Remove reference, use backend.finance models
from backend.financial_aid.models import AidApplication
from backend.donations.models import Donation
from backend.discipline.models import DisciplineIncident
from django.db.models import Sum

def home(request):
    totals = {
        "students": Student.objects.count(),
        "tuition": TuitionPayment.objects.aggregate(s=Sum("amount_paid"))["s"] or 0,
        "aid": FinancialAid.objects.aggregate(s=Sum("amount_awarded"))["s"] or 0,
        "donations": Donation.objects.aggregate(s=Sum("amount"))["s"] or 0,
    }
    recent_incidents = DisciplineIncident.objects.order_by("-date")[:10]
    return render(request, "dashboards/home.html", {"totals": totals, "recent_incidents": recent_incidents})
