from django.shortcuts import render
from bikes.models import Bike

def dashboard(request):

    total_bikes = Bike.objects.count()

    available_bikes = Bike.objects.filter(
        status="Available"
    ).count()

    rented_bikes = Bike.objects.filter(
        status="Rented"
    ).count()

    context = {

        "total_bikes": total_bikes,
        "available_bikes": available_bikes,
        "rented_bikes": rented_bikes,

    }

    return render(
        request,
        "dashboard/dashboard.html",
        context
    )