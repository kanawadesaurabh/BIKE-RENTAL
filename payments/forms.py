from django import forms
from .models import Payment


class PaymentForm(forms.ModelForm):

    class Meta:
        model = Payment

        fields = [
            "amount",
            "payment_mode",
            "remarks",
        ]

        widgets = {

            "remarks": forms.Textarea(
                attrs={
                    "rows": 3
                }
            )

        }