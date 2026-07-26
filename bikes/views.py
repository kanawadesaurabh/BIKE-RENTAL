from django.shortcuts import render, redirect
from .models import Bike
from .forms import BikeForm

def bike_list(request):
    bikes = Bike.objects.all()

    return render(request, "bikes/bike_list.html", {
        "bikes": bikes
    })


def add_bike(request):

    if request.method == "POST":

        form = BikeForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect("bike_list")

    else:

        form = BikeForm()

    return render(request, "bikes/add_bike.html", {
        "form": form
    })

def edit_bike(request, id):

    bike = Bike.objects.get(id=id)

    if request.method == "POST":
        form = BikeForm(request.POST, instance=bike)

        if form.is_valid():
            form.save()
            return redirect("bike_list")

    else:
        form = BikeForm(instance=bike)

    return render(request, "bikes/add_bike.html", {
        "form": form
    })

def delete_bike(request, id):
    bike = Bike.objects.get(id=id)
    bike.delete()

    return redirect("bike_list")