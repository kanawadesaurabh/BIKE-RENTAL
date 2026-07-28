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

            "remarks": forms.Textarea(
                attrs={
                    "rows": 3
                }
            )

        }