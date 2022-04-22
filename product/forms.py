from django import forms
from product.models import ProductReview


class ReviewForm(forms.ModelForm):

    full_name = forms.CharField(label='*NAME', label_suffix="", widget=forms.TextInput(attrs={
        'class': 'form-control',
        
    }))

    # user = forms.CharField(label='*NAME', label_suffix="", widget=forms.TextInput(attrs={
    #     'class': 'form-control',
        
    # }))

    email = forms.EmailField(label='*EMAIL', label_suffix="", widget=forms.EmailInput(attrs={
        'class': 'form-control',
    }))

    review = forms.CharField(label='*YOUR REVIEW', label_suffix="", widget=forms.Textarea(attrs={
        'class': 'form-control',
        'rows': 10,
    }))


    class Meta:
        model = ProductReview
       
        fields = (
            'full_name',
            # 'user',
            'email',
            'review',
            
        )
    