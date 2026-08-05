from django.db import models
from rentals.models import Rental


class Payment(models.Model):

    PAYMENT_MODE = [
        ("Cash", "Cash"),
        ("UPI", "UPI"),
        ("Card", "Card"),
        ("Bank", "Bank Transfer"),
    ]

    rental = models.ForeignKey(
        Rental,
        on_delete=models.CASCADE,
        related_name="payments"
    )

    payment_date = models.DateField(
        auto_now_add=True
    )

    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    payment_mode = models.CharField(
        max_length=20,
        choices=PAYMENT_MODE,
        default="Cash"
    )

    remarks = models.TextField(
        blank=True,
        null=True
    )

    def __str__(self):
        return f"{self.rental} - ₹{self.amount}"