from django.shortcuts import render, redirect, get_object_or_404

from .models import Expense
from .forms import ExpenseForm
from django.db.models import Sum

# ==========================
# Expense List
# ==========================
def expense_list(request):

    expenses = Expense.objects.all().order_by("-expense_date", "-id")

    return render(
        request,
        "expenses/expense_list.html",
        {
            "expenses": expenses
        }
    )


# ==========================
# Add Expense
# ==========================
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


# ==========================
# Edit Expense
# ==========================
def edit_expense(request, id):

    expense = get_object_or_404(
        Expense,
        id=id
    )

    if request.method == "POST":

        form = ExpenseForm(
            request.POST,
            instance=expense
        )

        if form.is_valid():

            form.save()

            return redirect("expense_list")

    else:

        form = ExpenseForm(
            instance=expense
        )

    return render(
        request,
        "expenses/add_expense.html",
        {
            "form": form,
            "expense": expense
        }
    )


# ==========================
# Delete Expense
# ==========================
def delete_expense(request, id):

    expense = get_object_or_404(
        Expense,
        id=id
    )

    expense.delete()

    return redirect("expense_list")



def expense_list(request):

    expenses = Expense.objects.all().order_by(
        "-expense_date",
        "-id"
    )

    total_expense = Expense.objects.aggregate(
        total=Sum("amount")
    )["total"] or 0

    return render(
        request,
        "expenses/expense_list.html",
        {
            "expenses": expenses,
            "total_expense": total_expense,
        }
    )    