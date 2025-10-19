from rest_framework.decorators import api_view
from rest_framework.response import Response
from students.models import Student
from finance.models import FinanceRecord
from financial_aid.models import AidApplication
from donations.models import Donation
from django.db.models import Sum

@api_view(["GET"])
def health(request):
    return Response({"status":"ok"})

@api_view(["GET"])
def totals(request):
    data = {
        "students": Student.objects.count(),
        "tuition": float(FinanceRecord.objects.filter(category="TUITION").aggregate(s=Sum("amount"))["s"] or 0),
        "aid": float(AidApplication.objects.aggregate(s=Sum("awarded_amount"))["s"] or 0),
        "donations": float(Donation.objects.aggregate(s=Sum("amount"))["s"] or 0),
    }
    return Response(data)
