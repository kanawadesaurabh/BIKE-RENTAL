from django.shortcuts import render
from django.utils import timezone
from django.db.models import Sum
from decimal import Decimal
from datetime import timedelta

from bikes.models import Bike
from customers.models import Customer
from rentals.models import Rental
from payments.models import Payment
from expenses.models import Expense


# =====================================================
# DASHBOARD
# =====================================================

def dashboard(request):

    # =========================
    # TODAY
    # =========================

    today = timezone.localdate()

    # =========================
    # TOMORROW
    # =========================

    tomorrow = today + timedelta(days=1)


    # =========================
    # BIKE SUMMARY
    # =========================

    total_bikes = Bike.objects.count()

    available_bikes = Bike.objects.filter(
        status="Available"
    ).count()

    rented_bikes = Bike.objects.filter(
        status="Rented"
    ).count()


    # =========================
    # CUSTOMER SUMMARY
    # =========================

    total_customers = Customer.objects.count()


    # =========================
    # ACTIVE RENTALS
    # =========================

    active_rentals = Rental.objects.filter(
        status="Active"
    ).count()


    # =========================
    # RETURN TODAY
    # =========================

    return_today = Rental.objects.filter(
        status="Active",
        expected_return_date__date=today
    ).select_related(
        "customer",
        "bike"
    ).order_by(
        "expected_return_date"
    )


    # =========================
    # OVERDUE RENTALS
    # =========================

    overdue_rentals = Rental.objects.filter(
        status="Active",
        expected_return_date__date__lt=today
    ).select_related(
        "customer",
        "bike"
    ).order_by(
        "expected_return_date"
    )


    # =========================
    # UPCOMING RETURNS
    # TOMORROW
    # =========================

    upcoming_returns = Rental.objects.filter(
        status="Active",
        expected_return_date__date=tomorrow
    ).select_related(
        "customer",
        "bike"
    ).order_by(
        "expected_return_date"
    )


    # =========================
    # PENDING PAYMENTS
    # =========================

    pending_rentals = Rental.objects.filter(
        status="Active",
        remaining_amount__gt=0
    ).select_related(
        "customer",
        "bike"
    ).order_by(
        "-remaining_amount"
    )


    pending_payments = pending_rentals.count()


    # =========================
    # TODAY INCOME
    # =========================

    today_income = Payment.objects.filter(
        payment_date=today
    ).aggregate(
        total=Sum("amount")
    )["total"] or Decimal("0.00")


    # =========================
    # MONTHLY INCOME
    # =========================

    current_month = today.month
    current_year = today.year

    monthly_income = Payment.objects.filter(
        payment_date__month=current_month,
        payment_date__year=current_year
    ).aggregate(
        total=Sum("amount")
    )["total"] or Decimal("0.00")


    # =========================
    # TOTAL INCOME
    # =========================

    total_income = Payment.objects.aggregate(
        total=Sum("amount")
    )["total"] or Decimal("0.00")


    # =========================
    # TOTAL EXPENSE
    # =========================

    total_expense = Expense.objects.aggregate(
        total=Sum("amount")
    )["total"] or Decimal("0.00")


    # =========================
    # TODAY EXPENSE
    # =========================

    today_expense = Expense.objects.filter(
        expense_date=today
    ).aggregate(
        total=Sum("amount")
    )["total"] or Decimal("0.00")


    # =========================
    # TOTAL PROFIT
    # =========================

    total_profit = total_income - total_expense

    total_profit = total_profit.quantize(
        Decimal("0.01")
    )


    # =========================
    # RECENT PAYMENTS
    # =========================

    recent_payments = Payment.objects.select_related(
        "rental",
        "rental__customer",
        "rental__bike"
    ).order_by(
        "-payment_date"
    )[:5]


    # =========================
    # RECENT RENTALS
    # =========================

    recent_rentals = Rental.objects.select_related(
        "customer",
        "bike"
    ).order_by(
        "-rent_date"
    )[:5]


    # =========================
    # RECENT EXPENSES
    # =========================

    recent_expenses = Expense.objects.order_by(
        "-expense_date"
    )[:5]


    # =========================
    # DASHBOARD CONTEXT
    # =========================

    context = {

        # Date
        "today": today,

        # Bikes
        "total_bikes": total_bikes,
        "available_bikes": available_bikes,
        "rented_bikes": rented_bikes,

        # Customers
        "total_customers": total_customers,

        # Rentals
        "active_rentals": active_rentals,

        # Alerts
        "return_today": return_today,
        "overdue_rentals": overdue_rentals,
        "upcoming_returns": upcoming_returns,

        # Payments
        "pending_rentals": pending_rentals,
        "pending_payments": pending_payments,

        # Income
        "today_income": today_income,
        "monthly_income": monthly_income,
        "total_income": total_income,

        # Expenses
        "today_expense": today_expense,
        "total_expense": total_expense,

        # Profit
        "total_profit": total_profit,

        # Recent activity
        "recent_payments": recent_payments,
        "recent_rentals": recent_rentals,
        "recent_expenses": recent_expenses,
    }


    return render(
        request,
        "dashboard/dashboard.html",
        context
    )


# =====================================================
# BIKE SEARCH
# =====================================================

def bike_search(request):

    registration_number = request.GET.get(
        "registration_number"
    )

    bike = None
    rental = None

    if registration_number:

        bike = Bike.objects.filter(
            registration_number__iexact=registration_number
        ).first()

        if bike:

            rental = Rental.objects.filter(
                bike=bike,
                status="Active"
            ).select_related(
                "customer",
                "bike"
            ).first()


    return render(
        request,
        "dashboard/bike_search.html",
        {
            "bike": bike,
            "rental": rental,
            "registration_number": registration_number,
            "today": timezone.localdate(),
        }
    )