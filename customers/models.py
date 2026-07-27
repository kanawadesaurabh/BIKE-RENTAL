from django.db import models

class Customer(models.Model):

    customer_name = models.CharField(max_length=100)

    mobile = models.CharField(max_length=15)

    aadhaar_number = models.CharField(max_length=20)

    driving_license = models.CharField(max_length=30)

    address = models.TextField()

    def __str__(self):
        return self.customer_name