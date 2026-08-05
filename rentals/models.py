from django.db import models

from customers.models import Customer
from bikes.models import Bike


class Rental(models.Model):

    STATUS_CHOICES = [
        ("Active", "Active"),
        ("Completed", "Completed"),
    ]

    RENTAL_TYPE_CHOICES = [
        ("Daily", "Daily"),
        ("Monthly", "Monthly"),
    ]

    # ==========================
    # CUSTOMER & BIKE
    # ==========================

    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE
    )

    bike = models.ForeignKey(
        Bike,
        on_delete=models.CASCADE
    )

    # ==========================
    # RENTAL TYPE
    # ==========================

    rental_type = models.CharField(
        max_length=20,
        choices=RENTAL_TYPE_CHOICES,
        default="Daily"
    )

    # Customer किती दिवसांसाठी bike घेत आहे
    # हे manually enter करता येईल
    rental_days = models.PositiveIntegerField(
        default=1
    )

    # ==========================
    # RENT DATE & TIME
    # ==========================

    # Bike customer ला नेमकी कधी दिली
    rent_date = models.DateTimeField()

    # Expected return date & time
    expected_return_date = models.DateTimeField(
        null=True,
        blank=True
    )

    # Bike प्रत्यक्षात कधी परत आली
    actual_return_date = models.DateTimeField(
        null=True,
        blank=True
    )

    # ==========================
    # RENT DETAILS
    # ==========================

    # Daily / Monthly rent manually enter करता येईल
    daily_rent = models.DecimalField(
        max_digits=8,
        decimal_places=2
    )

    security_deposit = models.DecimalField(
        max_digits=8,
        decimal_places=2
    )

    advance_payment = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        default=0
    )

    # ==========================
    # RETURN / BILL DETAILS
    # ==========================

    total_days = models.PositiveIntegerField(
        default=0
    )

    total_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    # ==========================
    # EXTRA / LATE CHARGES
    # ==========================

    # 24 hours / expected time नंतर
    # प्रति तास ₹100
    late_fine = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        default=0
    )

    # Damage charge
    damage_charge = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        default=0
    )

    # Manual extra charge
    manual_extra_charge = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        default=0
    )

    # Security deposit refund
    deposit_refund = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        default=0
    )

    # ==========================
    # PAYMENT
    # ==========================

    remaining_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    # ==========================
    # REMARKS
    # ==========================

    remarks = models.TextField(
        blank=True,
        null=True
    )

    # ==========================
    # STATUS
    # ==========================

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="Active"
    )

    # ==========================
    # STRING
    # ==========================

    def __str__(self):

        return (
            f"{self.customer.customer_name} - "
            f"{self.bike.registration_number}"
        )