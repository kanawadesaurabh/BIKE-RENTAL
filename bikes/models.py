from django.db import models

class Bike(models.Model):

    bike_name = models.CharField(max_length=100)

    brand = models.CharField(max_length=50)

    model = models.CharField(max_length=50)

    registration_number = models.CharField(max_length=20, unique=True)

    color = models.CharField(max_length=30)

    year = models.IntegerField()

    daily_rent = models.DecimalField(max_digits=8, decimal_places=2)

    security_deposit = models.DecimalField(max_digits=8, decimal_places=2)

    STATUS_CHOICES = [
        ('Available', 'Available'),
        ('Rented', 'Rented'),
        ('Service', 'Service'),
    ]

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Available')

    def __str__(self):
        return f"{self.bike_name} ({self.registration_number})"