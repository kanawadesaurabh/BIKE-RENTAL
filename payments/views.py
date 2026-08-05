from decimal import Decimal

from django.shortcuts import render, redirect, get_object_or_404

from .models import Payment
from .forms import PaymentForm
from rentals.models import Rental


# ==========================
# Payment List
# ==========================
def payment_list(request):

    payments = Payment.objects.select_related(
        "rental",
        "rental__customer",
        "rental__bike"
    ).order_by("-payment_date", "-id")

    return render(
        request,
        "payments/payment_list.html",
        {
            "payments": payments
        }
    )


# ==========================
# Add Payment
# ==========================
def add_payment(request, rental_id):

    rental = get_object_or_404(
        Rental,
        id=rental_id
    )

    # Current remaining amount
    remaining_amount = rental.remaining_amount or Decimal("0.00")

    if request.method == "POST":

        form = PaymentForm(request.POST)

        if form.is_valid():

            payment_amount = form.cleaned_data["amount"]

            # Prevent zero / negative payment
            if payment_amount <= 0:

                form.add_error(
                    "amount",
                    "Payment amount must be greater than ₹0."
                )

            # Prevent overpayment
            elif payment_amount > remaining_amount:

                form.add_error(
                    "amount",
                    f"Maximum payment allowed is ₹{remaining_amount}."
                )

            else:

                payment = form.save(commit=False)

                payment.rental = rental

                payment.save()

                # Update remaining amount
                rental.remaining_amount = (
                    remaining_amount - payment_amount
                )

                if rental.remaining_amount < 0:
                    rental.remaining_amount = Decimal("0.00")

                rental.save(
                    update_fields=["remaining_amount"]
                )

                return redirect(
                    "rental_detail",
                    id=rental.id
                )

    else:

        form = PaymentForm()

    return render(
        request,
        "payments/add_payment.html",
        {
            "form": form,
            "rental": rental,
            "remaining_amount": remaining_amount,
        }
    )