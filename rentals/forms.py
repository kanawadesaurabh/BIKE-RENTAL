from django import forms

from .models import Rental


# =========================================================
# RENTAL FORM
# =========================================================

class RentalForm(forms.ModelForm):

    class Meta:

        model = Rental

        fields = [
            "customer",
            "bike",
            "rental_type",
            "rental_days",
            "rent_date",
            "expected_return_date",
            "daily_rent",
            "security_deposit",
            "advance_payment",
        ]

        labels = {
            "customer": "Customer",
            "bike": "Bike",
            "rental_type": "Rental Type",
            "rental_days": "Rental Days",
            "rent_date": "OUT Date & Time",
            "expected_return_date": "Expected IN Date & Time",
            "daily_rent": "Rent Amount",
            "security_deposit": "Security Deposit",
            "advance_payment": "Advance Payment",
        }

        widgets = {

            "customer": forms.Select(
                attrs={
                    "class": "form-control"
                }
            ),

            "bike": forms.Select(
                attrs={
                    "class": "form-control"
                }
            ),

            "rental_type": forms.Select(
                attrs={
                    "class": "form-control",
                    "id": "id_rental_type"
                }
            ),

            "rental_days": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "min": "1",
                    "step": "1",
                    "placeholder": "Enter days"
                }
            ),

            # Bike customer ला दिल्याची date/time
            "rent_date": forms.DateTimeInput(
                format="%Y-%m-%dT%H:%M",
                attrs={
                    "type": "datetime-local",
                    "class": "form-control",
                    "id": "id_rent_date"
                }
            ),

            # Expected bike return date/time
            "expected_return_date": forms.DateTimeInput(
                format="%Y-%m-%dT%H:%M",
                attrs={
                    "type": "datetime-local",
                    "class": "form-control",
                    "id": "id_expected_return_date"
                }
            ),

            "daily_rent": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "step": "0.01",
                    "min": "0",
                    "placeholder": "₹ Enter rent"
                }
            ),

            "security_deposit": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "step": "0.01",
                    "min": "0",
                    "placeholder": "₹ Security deposit"
                }
            ),

            "advance_payment": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "step": "0.01",
                    "min": "0",
                    "placeholder": "₹ Advance payment"
                }
            ),
        }

        input_formats = [
            "%Y-%m-%dT%H:%M",
        ]


# =========================================================
# RETURN BIKE FORM
# =========================================================

class ReturnBikeForm(forms.ModelForm):

    class Meta:

        model = Rental

        fields = [
            "late_fine",
            "damage_charge",
            "manual_extra_charge",
            "deposit_refund",
            "remarks",
        ]

        labels = {
            "late_fine": "Late Fine",
            "damage_charge": "Damage Charge",
            "manual_extra_charge": "Manual Extra Charge",
            "deposit_refund": "Deposit Refund",
            "remarks": "Remarks",
        }

        widgets = {

            "late_fine": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "step": "0.01",
                    "min": "0",
                    "placeholder": "₹ Late fine"
                }
            ),

            "damage_charge": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "step": "0.01",
                    "min": "0",
                    "placeholder": "₹ Damage charge"
                }
            ),

            "manual_extra_charge": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "step": "0.01",
                    "min": "0",
                    "placeholder": "₹ Extra charge"
                }
            ),

            "deposit_refund": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "step": "0.01",
                    "min": "0",
                    "placeholder": "₹ Deposit refund"
                }
            ),

            "remarks": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 3,
                    "placeholder": "Enter remarks..."
                }
            ),
        }