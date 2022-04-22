from django import forms
from django.contrib.auth import get_user_model
from django.utils.translation import gettext, gettext_lazy as _
from django_countries.widgets import CountrySelectWidget
from django_countries import countries
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm



USER = get_user_model()

class RegisterForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
               'class': 'form-control'
            }))

    country = forms.ChoiceField(label='*COUNTRY', choices=countries, label_suffix="", widget=CountrySelectWidget(attrs={
    'class': 'selectpicker',
    
    })) 
    class Meta:
        model = USER
        fields = (
            'first_name',
            'last_name',
            'username',
            'email',
            'phone_number',
            'password',
            'confirm_password',
            'address',
            'country',
            'city' 
        )
        widgets = {
            'password': forms.PasswordInput(attrs={
                'class': 'form-control'
            })
        }
  

    def clean(self):
        data = self.cleaned_data
        print(data)
        if data['password'] != data['confirm_password']:
            raise forms.ValidationError("Password and confirm_password does not match")
        return super().clean()


class LoginForm(AuthenticationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
    }))
    password=forms.CharField(widget=forms.PasswordInput(attrs={
        'class':'form-control',
    }))


class CustomPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label=_("Old password"),
                                   widget=forms.PasswordInput(attrs={
                                        'class': 'form-control',
                                        'placeholder': 'Old Password'
                                    }))
    new_password1 = forms.CharField(label=_("New password"),
                                    widget=forms.PasswordInput(attrs={'class': 'form-control',
                                'placeholder': 'New Password'}))
    new_password2 = forms.CharField(label=_("New password confirmation"),
                                    widget=forms.PasswordInput(attrs={'class': 'form-control',
                                'placeholder': 'Confirm Password'}))

