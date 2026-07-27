from django.db import models

# Create your models here.
from datetime import date
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

    daily_rent = models.DecimalField(max_digits=10, decimal_places=2)

    security_deposit = models.DecimalField(max_digits=10, decimal_places=2)

    advance_payment = models.DecimalField(max_digits=10, decimal_places=2)

    status = models.CharField(
        max_length=20,
        default="Active"
    )

    def __str__(self):
        return f"{self.customer} - {self.bike}"

    

total_days = models.IntegerField(default=0)

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



def return_bike(request, id):

    rental = Rental.objects.get(id=id)

    today = date.today()

    rental.return_date = today

    rental.status = "Completed"

    total_days = (today - rental.rent_date).days

    if total_days <= 0:
        total_days = 1

    rental.total_days = total_days

    rental.total_amount = total_days * rental.daily_rent

    rental.remaining_amount = (
        rental.total_amount - rental.advance_payment
    )

    rental.save()

    bike = rental.bike
    bike.status = "Available"
    bike.save()

    return redirect("rental_list")