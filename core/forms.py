import email
from django import forms
from core.models import Contact, Subscription


class SubscribeForm(forms.ModelForm):
    email = forms.EmailField(max_length=40, widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter your email address'
    }))

    class Meta:
        model = Subscription
       
        fields = (
            'email',
            
        )


class ContactForm(forms.ModelForm):

    full_name = forms.CharField(label='FULL NAME *', label_suffix="", max_length=50, widget=forms.TextInput(attrs={
        'class': 'form-control',
        
    }))

    email = forms.EmailField(label='EMAIL *', label_suffix="", max_length=40, widget=forms.EmailInput(attrs={
        'class': 'form-control',
    }))

    phone = forms.CharField(label='PHONE *', label_suffix="", max_length=20, widget=forms.TextInput(attrs={
        'class': 'form-control',
    }))

    subject = forms.CharField(label='SUBJECT *', label_suffix="", max_length=50, widget=forms.TextInput(attrs={
        'class': 'form-control',
    }))
        
    message = forms.CharField(label='MESSAGE *', label_suffix="", widget=forms.Textarea(attrs={
        'class': 'form-control',
        'rows': 10,
    }))


    class Meta:
        model = Contact
       

        fields = (
            'full_name',
            'email',
            'phone',
            'subject',
            'message',
        )
        # widgets = {
        #     'full_name': forms.TextInput(attrs={
        #             'class': 'form-control',
        #             'placeholder': 'Your name'
        #     }),
        #     'message': forms.Textarea(attrs={
        #         'rows': 10,
        #         'class': 'form-control',
        #         'placeholder': 'Message'
        #     }),
        #     'subject': forms.Select(attrs={
        #         'class': 'form-control',
        #     })
        # }