from django.db import models

from bikes.models import Bike
from customers.models import Customer


class Rental(models.Model):

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    bike = models.ForeignKey(Bike, on_delete=models.CASCADE)

    rent_date = models.DateField()

    return_date = models.DateField(
        null=True,
        blank=True
    )

    daily_rent = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    security_deposit = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    advance_payment = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    late_fine = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    damage_charge = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    deposit_refund = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    remarks = models.TextField(
        blank=True,
        null=True
    )

    total_days = models.IntegerField(
        default=0
    )

    total_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    remaining_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    status = models.CharField(
        max_length=20,
        default="Active"
    )

    def __str__(self):
        return f"{self.customer} - {self.bike}"