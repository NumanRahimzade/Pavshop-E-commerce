from django import forms
from django.contrib.admin.widgets import AdminFileWidget
from blog.models import Comment, Blog



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


class BlogForm(forms.ModelForm):
    
    class Meta:
        model = Blog
        fields = (
            'category',
            'tags',
            'title',
            'description',
            'image',
        )
        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': 'Title',
                'class': 'form-control'
            }),
            'category': forms.Select(attrs={
                'placeholder': 'Category',
                'class': 'form-control'
            }),
            'image': AdminFileWidget(attrs={
                'placeholder': 'Image',
                'class': 'form-control'
            }),
            'description': forms.Textarea(attrs={
                'placeholder': 'Description',
                'class': 'form-control'
            }),
            'tags': forms.SelectMultiple(attrs={
                'placeholder': 'tags',
                'class': 'form-control'
            }),
            
        }