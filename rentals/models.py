from django.db import models

# Create your models here.

from bikes.models import Bike
from customers.models import Customer


class Rental(models.Model):

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    bike = models.ForeignKey(Bike, on_delete=models.CASCADE)

    rent_date = models.DateField()

    return_date = models.DateField()

    daily_rent = models.DecimalField(max_digits=10, decimal_places=2)

    security_deposit = models.DecimalField(max_digits=10, decimal_places=2)

    advance_payment = models.DecimalField(max_digits=10, decimal_places=2)

    status = models.CharField(
        max_length=20,
        default="Active"
    )

    def __str__(self):
        return f"{self.customer} - {self.bike}"