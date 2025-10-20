from rest_framework.decorators import api_view
from rest_framework.response import Response
from students.models import Student
from backend.finance.models import TuitionPayment, FinancialAid
from backend.financial_aid.models import AidApplication
from backend.donations.models import Donation
FinanceRecord = None  # Remove reference, use backend.finance models
from django.db.models import Sum

@api_view(["GET"])
def health(request):
    return Response({"status":"ok"})

@api_view(["GET"])
def totals(request):
    data = {
        "students": Student.objects.count(),
        "tuition": float(TuitionPayment.objects.aggregate(s=Sum("amount_paid"))["s"] or 0),
        "aid": float(FinancialAid.objects.aggregate(s=Sum("amount_awarded"))["s"] or 0),
        "donations": float(Donation.objects.aggregate(s=Sum("amount"))["s"] or 0),
    }
    return Response(data)
