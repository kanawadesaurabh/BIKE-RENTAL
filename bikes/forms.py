from django import forms
from .models import Bike


class BikeForm(forms.ModelForm):

    class Meta:
        model = Bike

        fields = "__all__"

        widgets = {

            "bike_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter Bike Name"
                }
            ),

            "brand": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter Brand Name"
                }
            ),

            "model": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter Model"
                }
            ),

            "registration_number": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter Registration Number"
                }
            ),

            "color": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter Bike Color"
                }
            ),

            "year": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter Manufacturing Year"
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

            "status": forms.Select(
                attrs={
                    "class": "form-select"
                }
            ),

        }