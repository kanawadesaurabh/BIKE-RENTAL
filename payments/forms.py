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

            "amount": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter payment amount",
                    "min": "1",
                    "step": "0.01",
                }
            ),

            "payment_mode": forms.Select(
                attrs={
                    "class": "form-select",
                }
            ),

            "remarks": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 3,
                    "placeholder": "Optional remarks...",
                }
            ),
        }

    def clean_amount(self):

        amount = self.cleaned_data.get("amount")

        if amount is None:
            raise forms.ValidationError(
                "Please enter payment amount."
            )

        if amount <= 0:
            raise forms.ValidationError(
                "Payment amount must be greater than ₹0."
            )

        return amount