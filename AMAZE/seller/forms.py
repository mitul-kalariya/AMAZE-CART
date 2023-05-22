from django import forms
from .models import SellerProfile


class SellerProfileForm(forms.ModelForm):
    class Meta:
        model = SellerProfile
        fields = (
            "org_name",
            "org_info",
            "org_email",
            "org_address",
            "org_contact",
            "inventory_address",
        )
