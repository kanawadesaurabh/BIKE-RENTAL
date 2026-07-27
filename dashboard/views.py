from django.shortcuts import render

from bikes.models import Bike
from customers.models import Customer
from rentals.models import Rental


def dashboard(request):

    total_bikes = Bike.objects.count()

    available_bikes = Bike.objects.filter(
        status="Available"
    ).count()

    rented_bikes = Bike.objects.filter(
        status="Rented"
    ).count()

    total_customers = Customer.objects.count()

    active_rentals = Rental.objects.filter(
        status="Active"
    ).count()

    today_income = 0

    context = {

        "total_bikes": total_bikes,
        "available_bikes": available_bikes,
        "rented_bikes": rented_bikes,
        "total_customers": total_customers,
        "active_rentals": active_rentals,
        "today_income": today_income,

    }

    return render(
        request,
        "dashboard/dashboard.html",
        context
    )