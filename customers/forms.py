from django import forms
from .models import Customer


class CustomerForm(forms.ModelForm):

    class Meta:
        model = Customer

        fields = "__all__"

        widgets = {

            "customer_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter Customer Name"
                }
            ),

            "mobile": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter Mobile Number"
                }
            ),

            "aadhaar_number": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter Aadhaar Number"
                }
            ),

            "driving_license": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter Driving License Number"
                }
            ),

            "address": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 3,
                    "placeholder": "Enter Address"
                }
            ),
        }