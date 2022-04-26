from django import forms
from product.models import Review


class ReviewForm(forms.ModelForm):

    comment = forms.CharField(label='*YOUR REVIEW', label_suffix="", widget=forms.Textarea(attrs={
        'class': 'form-control',
        'rows': 10,
    }))


    class Meta:
        model = Review
       
        fields = (
            'comment',
            
        )
    