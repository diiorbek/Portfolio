from django import forms
from .models import CommentModel
from django.core.exceptions import ValidationError
import re

class CommentForm(forms.ModelForm):
    class Meta:
        model = CommentModel
        fields = ['name', 'email', 'comment_text', 'rating']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ism',
                'required': 'true',
            }),
            'email': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email',
                'required': 'true',
            }),
            'comment_text': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Izoh',
                'rows': 4,
                'required': 'true',
            }),
            'rating': forms.Select(attrs={
                'class': 'form-select',
                'required': 'true',
            }, choices=[(1, '★☆☆☆☆'), (2, '★★☆☆☆'), (3, '★★★☆☆'), (4, '★★★★☆'), (5, '★★★★★')]),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].label = "Name"
        self.fields['email'].label = "Email"
        self.fields['comment_text'].label = "Comment"
        self.fields['rating'].label = "rating"
        
    def clean_email(self):
        email = self.cleaned_data.get('email')
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(email_regex, email):
            raise ValidationError("Введите корректный email-адрес.")
        return email
    

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    phone = forms.CharField(max_length=15)
    email = forms.EmailField()
    subject = forms.CharField(max_length=255)
    message = forms.CharField(widget=forms.Textarea)
