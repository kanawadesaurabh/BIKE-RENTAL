from decimal import Decimal

from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

from bikes.models import Bike

from .models import Rental
from .forms import RentalForm, ReturnBikeForm


# =========================================================
# RENTAL LIST
# =========================================================

def rental_list(request):

    rentals = Rental.objects.all().order_by("-id")

    return render(
        request,
        "rentals/rental_list.html",
        {
            "rentals": rentals
        }
    )


# =========================================================
# ADD RENTAL
# =========================================================

def add_rental(request):

    if request.method == "POST":

        form = RentalForm(request.POST)

        # फक्त Available bikes दाखवायच्या
        form.fields["bike"].queryset = Bike.objects.filter(
            status="Available"
        )

        if form.is_valid():

            rental = form.save(commit=False)

            # -------------------------------------------------
            # RENT DATE
            # -------------------------------------------------

            if not rental.rent_date:
                rental.rent_date = timezone.localtime()

            # -------------------------------------------------
            # RENTAL DAYS
            # -------------------------------------------------

            if not rental.rental_days or rental.rental_days < 1:
                rental.rental_days = 1

            # -------------------------------------------------
            # EXPECTED RETURN DATE
            # -------------------------------------------------

            from datetime import timedelta

            rental.expected_return_date = (
                rental.rent_date
                + timedelta(days=rental.rental_days)
            )

            # -------------------------------------------------
            # INITIAL TOTAL DAYS
            # -------------------------------------------------

            rental.total_days = rental.rental_days

            # -------------------------------------------------
            # INITIAL TOTAL AMOUNT
            # -------------------------------------------------

            if rental.rental_type == "Daily":

                rental.total_amount = (
                    Decimal(rental.rental_days)
                    * rental.daily_rent
                )

            else:

                # Monthly rent manually enter केलेले amount
                rental.total_amount = rental.daily_rent

            # -------------------------------------------------
            # REMAINING AMOUNT
            # -------------------------------------------------

            rental.remaining_amount = (
                rental.total_amount
                - rental.advance_payment
            )

            if rental.remaining_amount < Decimal("0.00"):
                rental.remaining_amount = Decimal("0.00")

            # -------------------------------------------------
            # STATUS
            # -------------------------------------------------

            rental.status = "Active"

            rental.save()

            # -------------------------------------------------
            # BIKE STATUS
            # -------------------------------------------------

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


# =========================================================
# RETURN BIKE
# =========================================================

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

            # -------------------------------------------------
            # ACTUAL RETURN DATE & TIME
            # -------------------------------------------------

            actual_return = timezone.localtime()

            rental.actual_return_date = actual_return

            # -------------------------------------------------
            # ACTUAL DURATION
            # -------------------------------------------------

            duration = (
                actual_return - rental.rent_date
            )

            total_seconds = duration.total_seconds()

            # -------------------------------------------------
            # ACTUAL DAYS
            # 24 hours = 1 day
            # थोडा जरी extra time झाला तर next day
            # -------------------------------------------------

            actual_days = int(
                (total_seconds + 86399) // 86400
            )

            if actual_days < 1:
                actual_days = 1

            rental.total_days = actual_days

            # -------------------------------------------------
            # BASIC RENT
            # -------------------------------------------------

            if rental.rental_type == "Daily":

                basic_rent = (
                    Decimal(actual_days)
                    * rental.daily_rent
                )

            else:

                # Monthly rent manually entered amount
                basic_rent = rental.daily_rent

            # -------------------------------------------------
            # LATE FINE
            # ₹100 PER EXTRA HOUR
            # -------------------------------------------------

            late_fine = Decimal("0.00")

            if (
                rental.expected_return_date
                and actual_return > rental.expected_return_date
            ):

                late_duration = (
                    actual_return
                    - rental.expected_return_date
                )

                late_seconds = (
                    late_duration.total_seconds()
                )

                late_hours = int(
                    (late_seconds + 3599) // 3600
                )

                if late_hours < 1:
                    late_hours = 1

                late_fine = (
                    Decimal(late_hours)
                    * Decimal("100.00")
                )

            rental.late_fine = late_fine

            # -------------------------------------------------
            # DAMAGE CHARGE
            # -------------------------------------------------

            damage_charge = (
                rental.damage_charge
                or Decimal("0.00")
            )

            # -------------------------------------------------
            # MANUAL EXTRA CHARGE
            # -------------------------------------------------

            manual_extra_charge = (
                rental.manual_extra_charge
                or Decimal("0.00")
            )

            # -------------------------------------------------
            # FINAL TOTAL
            # -------------------------------------------------

            rental.total_amount = (
                basic_rent
                + rental.late_fine
                + damage_charge
                + manual_extra_charge
            )

            # -------------------------------------------------
            # REMAINING AMOUNT
            # -------------------------------------------------

            rental.remaining_amount = (
                rental.total_amount
                - rental.advance_payment
            )

            if rental.remaining_amount < Decimal("0.00"):

                rental.remaining_amount = Decimal("0.00")

            # -------------------------------------------------
            # STATUS
            # -------------------------------------------------

            rental.status = "Completed"

            rental.save()

            # -------------------------------------------------
            # BIKE AVAILABLE
            # -------------------------------------------------

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


# =========================================================
# RENTAL DETAIL
# =========================================================

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


# =========================================================
# PRINT INVOICE
# =========================================================

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