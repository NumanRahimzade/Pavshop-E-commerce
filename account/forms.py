from django import forms
# from django.contrib.admin.widgets import AdminFileWidget, AdminTextareaWidget, AdminEmailInputWidget
from django.contrib.auth import get_user_model
from django.utils.translation import gettext, gettext_lazy as _
from django_countries.widgets import CountrySelectWidget
from django_countries import countries
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, PasswordResetForm, SetPasswordForm
from .models import User


USER = get_user_model()


#forget password#
class CustomSetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(
                                    widget=forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'New Password'
            }))
    new_password2 = forms.CharField(
                                    widget=forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Confirm New Password'
            }))


class ResetPasswordForm(PasswordResetForm):
    email = forms.EmailField(label=_("Email"), widget=forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email'
            }), max_length=254)
#forget password#

class RegisterForm(forms.ModelForm):
    confirm_password = forms.CharField(label='*CONFIRM PASSWORD', label_suffix="", max_length=50, widget=forms.PasswordInput(attrs={
                'class': 'form-control',
    }))

    password = forms.CharField(label='*PASSWORD', label_suffix="", max_length=50, widget=forms.PasswordInput(attrs={
                'class': 'form-control',
    }))

    country = forms.ChoiceField(label='*COUNTRY', choices=countries, label_suffix="", widget=CountrySelectWidget(attrs={
        'class': 'selectpicker',
        
    }))     #country ucun

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
            'address',
            'country',
            'town_city' 
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


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'username',
            'email',
            'phone',
            'address',
            'country',
            'town_city',
            'bio',
            'image',
        )
        # widgets = {
            # 'first_name': AdminTextareaWidget(attrs={
            #     'placeholder': 'First_name',
            #     'class': 'form-control'
            # }),
            # 'last_name': AdminTextareaWidget(attrs={
            #     'placeholder': 'Last_name',
            #     'class': 'form-control'
            # }),
            # 'image': AdminFileWidget(attrs={
            #     'placeholder': 'Image',
            #     'class': 'form-control'
            # }),
            # 'username': AdminTextareaWidget(attrs={
            #     'placeholder': 'Username',
            #     'class': 'form-control'
            # }),
            # 'email': AdminEmailInputWidget(attrs={
            #     'placeholder': 'Email',
            #     'class': 'form-control'
            # }),
            # 'phone': AdminTextareaWidget(attrs={
            #     'placeholder': 'Phone',
            #     'class': 'form-control'
            # }),
            # 'address': AdminTextareaWidget(attrs={
            #     'placeholder': 'Address',
            #     'class': 'form-control'
            # }),
            # 'country': AutocompleteSelectMultiple(attrs={
            #     'placeholder': 'Country',
            #     'class': 'form-control'
            # }),
            # 'town_city': AdminTextareaWidget(attrs={
            #     'placeholder': 'Town_city',
            #     'class': 'form-control'
            # }),
            # 'bio': AdminTextareaWidget(attrs={
            #     'placeholder': 'Bio',
            #     'class': 'form-control'
            # }),
            
        # }