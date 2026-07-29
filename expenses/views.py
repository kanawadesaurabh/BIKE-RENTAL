from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect

from .models import Expense
from .forms import ExpenseForm


def expense_list(request):

    expenses = Expense.objects.all().order_by("-expense_date")

    return render(
        request,
        "expenses/expense_list.html",
        {
            "expenses": expenses
        }
    )




def add_expense(request):

    if request.method == "POST":

        form = ExpenseForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect("expense_list")

    else:

        form = ExpenseForm()

    return render(
        request,
        "expenses/add_expense.html",
        {
            "form": form
        }
    )

from django.shortcuts import get_object_or_404


def edit_expense(request, id):

    expense = get_object_or_404(Expense, id=id)

    if request.method == "POST":

        form = ExpenseForm(request.POST, instance=expense)

        if form.is_valid():

            form.save()

            return redirect("expense_list")

    else:

        form = ExpenseForm(instance=expense)

    return render(
        request,
        "expenses/add_expense.html",
        {
            "form": form
        }
    )


def delete_expense(request, id):

    expense = get_object_or_404(Expense, id=id)

    expense.delete()

    return redirect("expense_list")