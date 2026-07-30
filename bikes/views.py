from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q

from .models import Bike
from .forms import BikeForm


# ==========================
# Bike List
# ==========================
def bike_list(request):

    search = request.GET.get("search")

    if search:

        bikes = Bike.objects.filter(
            Q(bike_name__icontains=search) |
            Q(brand__icontains=search) |
            Q(model__icontains=search) |
            Q(registration_number__icontains=search) |
            Q(color__icontains=search)
        )

    else:

        bikes = Bike.objects.all()

    return render(
        request,
        "bikes/bike_list.html",
        {
            "bikes": bikes,
            "search": search,
        }
    )


# ==========================
# Add Bike
# ==========================
def add_bike(request):

    if request.method == "POST":

        form = BikeForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect("bike_list")

    else:

        form = BikeForm()

    return render(
        request,
        "bikes/add_bike.html",
        {
            "form": form
        }
    )


# ==========================
# Edit Bike
# ==========================
def edit_bike(request, id):

    bike = get_object_or_404(Bike, id=id)

    if request.method == "POST":

        form = BikeForm(
            request.POST,
            instance=bike
        )

        if form.is_valid():

            form.save()

            return redirect("bike_list")

    else:

        form = BikeForm(instance=bike)

    return render(
        request,
        "bikes/add_bike.html",
        {
            "form": form
        }
    )


# ==========================
# Delete Bike
# ==========================
def delete_bike(request, id):

    bike = get_object_or_404(Bike, id=id)

    bike.delete()

    return redirect("bike_list")