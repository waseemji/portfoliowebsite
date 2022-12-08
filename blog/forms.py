from django import forms
from .models import Comments
from django.forms import TextInput,EmailInput,Textarea

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        exclude = ["post"]
        labels = {
            "user_name" : "Your Name",
            "user_email" : "Your Email",
            "user_comment" : "Your Comment",
            "date_time" : "date_time"
        }
        widgets = {
            'user_name':TextInput(attrs={'placeholder':'Your Name','class':'form-input'}),
            'user_email':EmailInput(attrs={'placeholder':'Your Email','class':'form-input'}),
            'user_comment':Textarea(attrs={'placeholder':'Your Comment','class':'form-input'}),
        }