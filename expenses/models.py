from django.db import models


class Expense(models.Model):

    CATEGORY = [
        ("Fuel", "Fuel"),
        ("Service", "Service"),
        ("Spare Parts", "Spare Parts"),
        ("Salary", "Salary"),
        ("Electricity", "Electricity"),
        ("Office", "Office"),
        ("Other", "Other"),
    ]

    expense_date = models.DateField(auto_now_add=True)

    category = models.CharField(
        max_length=30,
        choices=CATEGORY
    )

    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    description = models.TextField(
        blank=True,
        null=True
    )

    def __str__(self):
        return f"{self.category} - ₹{self.amount}"