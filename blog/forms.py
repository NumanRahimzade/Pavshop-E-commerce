from django import forms
from blog.models import Comment



class BlogCommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields = (
            # 'name',
            # 'email',
            'subject',
            'review'
        )
        widgets = {
            # 'name': forms.TextInput(attrs={
            #     'class': 'form-control',
                   
            # }),
            # 'email': forms.EmailInput(attrs={
            #     'class': 'form-control',
             
            # }),
            'subject': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'review': forms.Textarea(attrs={
                'class': 'form-control',
            })
        } 