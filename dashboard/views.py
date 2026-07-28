from django.shortcuts import render
from django.db.models import Sum
from django.utils import timezone

from bikes.models import Bike
from customers.models import Customer
from rentals.models import Rental
from payments.models import Payment


def dashboard(request):

    # Bike Counts
    total_bikes = Bike.objects.count()

    available_bikes = Bike.objects.filter(
        status="Available"
    ).count()

    rented_bikes = Bike.objects.filter(
        status="Rented"
    ).count()

    # Customer Count
    total_customers = Customer.objects.count()

    # Active Rentals
    active_rentals = Rental.objects.filter(
        status="Active"
    ).count()

    # Today's Income
    today = timezone.now().date()

    today_income = Payment.objects.filter(
        payment_date=today
    ).aggregate(
        total=Sum("amount")
    )["total"] or 0

    # Monthly Income
    current_month = today.month
    current_year = today.year

    monthly_income = Payment.objects.filter(
        payment_date__month=current_month,
        payment_date__year=current_year
    ).aggregate(
        total=Sum("amount")
    )["total"] or 0

    # Pending Payments
    pending_payments = Rental.objects.filter(
        remaining_amount__gt=0
    ).count()

    context = {

        "total_bikes": total_bikes,

        "available_bikes": available_bikes,

        "rented_bikes": rented_bikes,

        "total_customers": total_customers,

        "active_rentals": active_rentals,

        "today_income": today_income,

        "monthly_income": monthly_income,

        "pending_payments": pending_payments,

    }

    return render(
        request,
        "dashboard/dashboard.html",
        context
    )