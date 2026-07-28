from django.shortcuts import render, redirect, get_object_or_404

from .models import Payment
from .forms import PaymentForm
from rentals.models import Rental


def payment_list(request):

    payments = Payment.objects.all().order_by("-payment_date")

    return render(
        request,
        "payments/payment_list.html",
        {
            "payments": payments
        }
    )


def add_payment(request, rental_id):

    rental = get_object_or_404(
        Rental,
        id=rental_id
    )

    if request.method == "POST":

        form = PaymentForm(request.POST)

        if form.is_valid():

            payment = form.save(commit=False)

            payment.rental = rental

            payment.save()

            rental.remaining_amount -= payment.amount

            if rental.remaining_amount < 0:
                rental.remaining_amount = 0

            rental.save()

            return redirect("payment_list")

    else:

        form = PaymentForm()

    return render(
        request,
        "payments/add_payment.html",
        {
            "form": form,
            "rental": rental
        }
    )