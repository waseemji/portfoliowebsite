from django import forms
from .models import ContactMe
from django.forms import TextInput,Textarea,EmailInput

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMe
        fields = '__all__'
        labels =  {
            "user_name" : "Your Name",
            "user_email" : "Your Email",
            "subject": "Subject",
            "user_message": "Your Message"
        }
        widgets = {
            "user_name":TextInput(attrs={'placeholder':'Your Name', 'class':'form-control col-md-6 md-form  mb-0'}),
            "user_email":EmailInput(attrs={'placeholder':'Your Email','class':'form-control col-md-6 md-form  mb-0'}),
            "subject":TextInput(attrs={'placeholder':'Subject','class':'form-control md-form  col-md-12 mb-0'}),
            "user_message":Textarea(attrs={'placeholder':'Your Message','class':' form-control col-md-12 md-form  md-textarea'}),
        }