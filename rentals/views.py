from decimal import Decimal
from datetime import date

from django.shortcuts import render, redirect, get_object_or_404

from bikes.models import Bike
from .models import Rental
from .forms import RentalForm, ReturnBikeForm


# ==========================
# Rental List
# ==========================
def rental_list(request):

    rentals = Rental.objects.all().order_by("-id")

    return render(
        request,
        "rentals/rental_list.html",
        {
            "rentals": rentals
        }
    )


# ==========================
# Add Rental
# ==========================
def add_rental(request):

    if request.method == "POST":

        form = RentalForm(request.POST)

        form.fields["bike"].queryset = Bike.objects.filter(
            status="Available"
        )

        if form.is_valid():

            rental = form.save()

            bike = rental.bike
            bike.status = "Rented"
            bike.save()

            return redirect("rental_list")

    else:

        form = RentalForm()

        form.fields["bike"].queryset = Bike.objects.filter(
            status="Available"
        )

    return render(
        request,
        "rentals/add_rental.html",
        {
            "form": form
        }
    )


# ==========================
# Return Bike
# ==========================
def return_bike(request, id):

    rental = get_object_or_404(
        Rental,
        id=id
    )

    if request.method == "POST":

        form = ReturnBikeForm(
            request.POST,
            instance=rental
        )

        if form.is_valid():

            rental = form.save(commit=False)

            today = date.today()

            rental.return_date = today

            rental.status = "Completed"

            total_days = (today - rental.rent_date).days

            if total_days <= 0:
                total_days = 1

            rental.total_days = total_days

            rental.total_amount = (
                Decimal(total_days)
                * rental.daily_rent
            )

            rental.remaining_amount = (
                rental.total_amount
                + rental.late_fine
                + rental.damage_charge
                - rental.advance_payment
            )

            if rental.remaining_amount < 0:
                rental.remaining_amount = 0

            rental.save()

            bike = rental.bike

            bike.status = "Available"

            bike.save()

            return redirect(
                "rental_detail",
                id=rental.id
            )

    else:

        form = ReturnBikeForm(
            instance=rental
        )

    return render(
        request,
        "rentals/return_bike.html",
        {
            "form": form,
            "rental": rental
        }
    )


# ==========================
# Rental Detail
# ==========================
def rental_detail(request, id):

    rental = get_object_or_404(
        Rental,
        id=id
    )

    return render(
        request,
        "rentals/rental_detail.html",
        {
            "rental": rental
        }
    )


# ==========================
# Print Invoice
# ==========================
def print_invoice(request, id):

    rental = get_object_or_404(
        Rental,
        id=id
    )

    return render(
        request,
        "rentals/invoice.html",
        {
            "rental": rental
        }
    )