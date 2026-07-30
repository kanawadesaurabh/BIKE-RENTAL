from django import forms
from .models import Rental


class RentalForm(forms.ModelForm):

    class Meta:

        model = Rental

        fields = [
            "customer",
            "bike",
            "rent_date",
            "daily_rent",
            "security_deposit",
            "advance_payment",
        ]

        widgets = {

            "customer": forms.Select(
                attrs={
                    "class": "form-select"
                }
            ),

            "bike": forms.Select(
                attrs={
                    "class": "form-select"
                }
            ),

            "rent_date": forms.DateInput(
                attrs={
                    "class": "form-control",
                    "type": "date"
                }
            ),

            "daily_rent": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter Daily Rent"
                }
            ),

            "security_deposit": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter Security Deposit"
                }
            ),

            "advance_payment": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter Advance Payment"
                }
            ),

        }


class ReturnBikeForm(forms.ModelForm):

    class Meta:

        model = Rental

        fields = [
            "late_fine",
            "damage_charge",
            "deposit_refund",
            "remarks",
        ]

        widgets = {

            "late_fine": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter Late Fine"
                }
            ),

            "damage_charge": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter Damage Charge"
                }
            ),

            "deposit_refund": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter Deposit Refund"
                }
            ),

            "remarks": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 3,
                    "placeholder": "Enter Remarks"
                }
            ),

        }