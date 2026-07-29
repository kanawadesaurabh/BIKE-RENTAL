from django.shortcuts import render
from django.db.models import Sum
from django.utils import timezone

from bikes.models import Bike
from customers.models import Customer
from rentals.models import Rental
from payments.models import Payment
from expenses.models import Expense


def dashboard(request):

    # ==========================
    # Bike Details
    # ==========================
    total_bikes = Bike.objects.count()

    available_bikes = Bike.objects.filter(
        status="Available"
    ).count()

    rented_bikes = Bike.objects.filter(
        status="Rented"
    ).count()

    # ==========================
    # Customer Details
    # ==========================
    total_customers = Customer.objects.count()

    # ==========================
    # Rental Details
    # ==========================
    active_rentals = Rental.objects.filter(
        status="Active"
    ).count()

    pending_payments = Rental.objects.filter(
        remaining_amount__gt=0
    ).count()

    # ==========================
    # Today's Date
    # ==========================
    today = timezone.now().date()

    # ==========================
    # Income
    # ==========================
    today_income = Payment.objects.filter(
        payment_date=today
    ).aggregate(
        total=Sum("amount")
    )["total"] or 0

    monthly_income = Payment.objects.filter(
        payment_date__month=today.month,
        payment_date__year=today.year
    ).aggregate(
        total=Sum("amount")
    )["total"] or 0

    total_income = Payment.objects.aggregate(
        total=Sum("amount")
    )["total"] or 0

    # ==========================
    # Expense
    # ==========================
    today_expense = Expense.objects.filter(
        expense_date=today
    ).aggregate(
        total=Sum("amount")
    )["total"] or 0

    total_expense = Expense.objects.aggregate(
        total=Sum("amount")
    )["total"] or 0

    # ==========================
    # Profit
    # ==========================
    total_profit = total_income - total_expense

    # ==========================
    # Recent Records
    # ==========================
    recent_rentals = Rental.objects.order_by("-id")[:5]

    recent_payments = Payment.objects.order_by("-id")[:5]

    recent_expenses = Expense.objects.order_by("-id")[:5]

    # ==========================
    # Context
    # ==========================
    context = {

        "total_bikes": total_bikes,
        "available_bikes": available_bikes,
        "rented_bikes": rented_bikes,

        "total_customers": total_customers,
        "active_rentals": active_rentals,

        "today_income": today_income,
        "today_expense": today_expense,

        "monthly_income": monthly_income,

        "total_income": total_income,
        "total_expense": total_expense,
        "total_profit": total_profit,

        "pending_payments": pending_payments,

        "recent_rentals": recent_rentals,
        "recent_payments": recent_payments,
        "recent_expenses": recent_expenses,

    }

    return render(
        request,
        "dashboard/dashboard.html",
        context
    )