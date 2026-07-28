from django.shortcuts import render
from payments.models import Payment
from django.db.models import Sum
from django.utils import timezone


def report_dashboard(request):

    today = timezone.now().date()

    today_collection = Payment.objects.filter(
        payment_date=today
    ).aggregate(
        total=Sum("amount")
    )["total"] or 0

    monthly_collection = Payment.objects.filter(
        payment_date__month=today.month,
        payment_date__year=today.year
    ).aggregate(
        total=Sum("amount")
    )["total"] or 0

    payments = Payment.objects.all().order_by("-payment_date")

    return render(
        request,
        "reports/report_dashboard.html",
        {
            "today_collection": today_collection,
            "monthly_collection": monthly_collection,
            "payments": payments,
        }
    )