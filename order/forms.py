from django import forms
from order.models import ShippingDetail



class ShippingDetailForm(forms.ModelForm):
    class Meta:
        model=ShippingDetail
        fields = (
            'firstname',
            'lastname',
            'companyname',
            'address',
            'town',
            'country',
            'email',
            'phone'
        )



