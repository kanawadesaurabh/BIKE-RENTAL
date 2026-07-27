from django.shortcuts import render, redirect
from .models import Customer
from .forms import CustomerForm
from django.db.models import Q

def customer_list(request):

    customers = Customer.objects.all()

    return render(request,
                  "customers/customer_list.html",
                  {"customers": customers})


def add_customer(request):

    if request.method == "POST":

        form = CustomerForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("customer_list")

    else:

        form = CustomerForm()

    return render(request,
                  "customers/add_customer.html",
                  {"form": form})

def edit_customer(request, id):

    customer = Customer.objects.get(id=id)

    if request.method == "POST":
        form = CustomerForm(request.POST, instance=customer)

        if form.is_valid():
            form.save()
            return redirect("customer_list")

    else:
        form = CustomerForm(instance=customer)

    return render(request,
                  "customers/add_customer.html",
                  {"form": form})


def delete_customer(request, id):

    customer = Customer.objects.get(id=id)
    customer.delete()

    return redirect("customer_list")



def customer_list(request):

    search = request.GET.get('search')

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