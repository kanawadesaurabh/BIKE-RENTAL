from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q

from .models import Customer
from .forms import CustomerForm


# ==========================
# Customer List
# ==========================
def customer_list(request):

    search = request.GET.get("search")

    if search:
        customers = Customer.objects.filter(
            Q(customer_name__icontains=search) |
            Q(mobile__icontains=search) |
            Q(aadhaar_number__icontains=search) |
            Q(driving_license__icontains=search)
        )
    else:
        customers = Customer.objects.all()

    return render(
        request,
        "customers/customer_list.html",
        {
            "customers": customers,
            "search": search,
        }
    )


# ==========================
# Add Customer
# ==========================
def add_customer(request):

    if request.method == "POST":

        form = CustomerForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("customer_list")

    else:

        form = CustomerForm()

    return render(
        request,
        "customers/add_customer.html",
        {
            "form": form
        }
    )


# ==========================
# Edit Customer
# ==========================
def edit_customer(request, id):

    customer = get_object_or_404(Customer, id=id)

    if request.method == "POST":

        form = CustomerForm(
            request.POST,
            instance=customer
        )

        if form.is_valid():
            form.save()
            return redirect("customer_list")

    else:

        form = CustomerForm(instance=customer)

    return render(
        request,
        "customers/add_customer.html",
        {
            "form": form
        }
    )


# ==========================
# Delete Customer
# ==========================
def delete_customer(request, id):

    customer = get_object_or_404(Customer, id=id)

    customer.delete()

    return redirect("customer_list")