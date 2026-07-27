from django.shortcuts import render, redirect
from .models import Rental
from .forms import RentalForm
from bikes.models import Bike


def rental_list(request):

    rentals = Rental.objects.all()

    return render(
        request,
        "rentals/rental_list.html",
        {"rentals": rentals}
    )


def add_rental(request):

    if request.method == "POST":

        form = RentalForm(request.POST)

        # POST मध्येही फक्त Available Bikes
        form.fields['bike'].queryset = Bike.objects.filter(status="Available")

        if form.is_valid():

            rental = form.save()

            bike = rental.bike
            bike.status = "Rented"
            bike.save()

            return redirect("rental_list")

    else:

        form = RentalForm()
        form.fields['bike'].queryset = Bike.objects.filter(status="Available")

    return render(
        request,
        "rentals/add_rental.html",
        {"form": form}
    )