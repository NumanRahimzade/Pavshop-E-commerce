from django import forms
from order.models import BillingDetail



class BillingDetailForm(forms.ModelForm):
    class Meta:
        model=BillingDetail
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



