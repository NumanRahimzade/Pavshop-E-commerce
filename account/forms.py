from django import forms
from django_countries.widgets import CountrySelectWidget
from django.contrib.auth import get_user_model


USER = get_user_model()


class RegisterForm(forms.ModelForm):
    confirm_password = forms.CharField(label='*CONFIRM PASSWORD', label_suffix="", max_length=50, widget=forms.PasswordInput(attrs={
                'class': 'form-control',
    }))

    password = forms.CharField(label='*PASSWORD', label_suffix="", max_length=50, widget=forms.PasswordInput(attrs={
                'class': 'form-control',
    }))

    # country = forms.CharField(label='*COUNTRY', label_suffix="", max_length=50, widget=CountrySelectWidget(attrs={
    #     'class': 'form-control',
        
    # }))     #country ucun

    first_name = forms.CharField(label='*FIRST NAME', label_suffix="", max_length=50, widget=forms.TextInput(attrs={
        'class': 'form-control',
        
    }))

    last_name = forms.CharField(label='*LAST NAME', label_suffix="", max_length=50, widget=forms.TextInput(attrs={
        'class': 'form-control',
        
    }))

    email = forms.EmailField(label='*EMAIL', label_suffix="", max_length=40, widget=forms.EmailInput(attrs={
        'class': 'form-control',
    }))

    phone = forms.CharField(label='*PHONE', label_suffix="", max_length=20, widget=forms.TextInput(attrs={
        'class': 'form-control',
    }))

    address = forms.CharField(label='*ADDRESS', label_suffix="", max_length=20, widget=forms.TextInput(attrs={
        'class': 'form-control',
    }))

    username = forms.CharField(label='*USERNAME', label_suffix="", max_length=20, widget=forms.TextInput(attrs={
        'class': 'form-control',
    }))

    town_city = forms.CharField(label='*TOWN/CITY', label_suffix="", max_length=20, widget=forms.TextInput(attrs={
        'class': 'form-control',
    }))

    class Meta:
        model = USER
        fields = (
            'first_name',
            'last_name',
            'username',
            'email',
            'phone',
            'password',
            'confirm_password',
            # 'country',    #country ucun
            'address',
            'town_city'

        )

        # widgets = {
        #     'first_name': forms.TextInput(attrs={
        #         'class': 'form-control',
        #         'label': 'First Name'
        #     }),
        #     'last_name': forms.TextInput(attrs={
        #         'class': 'form-control',
        #         'placeholder': 'Last Name'
        #     }),
        #     'email': forms.EmailInput(attrs={
        #         'class': 'form-control',
        #         'placeholder': 'Email'
        #     }),
        #     'phone': forms.TextInput(attrs={
        #         'class': 'form-control',
        #         'placeholder': 'phone'
        #     }),
        #     'password': forms.PasswordInput(attrs={
        #         'class': 'form-control',
        #         'placeholder': 'Password'
        #     }),
        #     'address_line1': forms.TextInput(attrs={
        #         'class': 'form-control',
        #         'placeholder': 'address_line1'
        #     }),
        #     'address_line2': forms.TextInput(attrs={
        #         'class': 'form-control',
        #         'placeholder': 'address_line2'
        #     }),
        #     'town_city': forms.TextInput(attrs={
        #         'class': 'form-control',
        #         'placeholder': 'town_city'
        #     }),
        # }

    def clean(self):
        data = self.cleaned_data
        if data['password'] != data['confirm_password']:
            raise forms.ValidationError("//// Confirm_password does not match")
        return super().clean()


class LoginForm(forms.Form):
    username = forms.CharField(label='USERNAME', label_suffix="", widget=forms.TextInput(attrs={
        'class': 'form-control',
        
    }))
    password = forms.CharField(label='PASSWORD', label_suffix="", widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        
    }))