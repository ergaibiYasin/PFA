from django import forms
from django.contrib.auth import get_user_model


User=get_user_model()



class ContactForm(forms.Form):
    fullname = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"your full name"}))

    email    = forms.EmailField(widget=forms.EmailInput(attrs={"class":"form-control", "placeholder":"your email"}))

    content  =forms.CharField(widget=forms.Textarea(attrs={"class":"form-control", "placeholder":"your message"}))



    def clean_email(self):
        email=self.cleaned_data.get("email")
        if not "gmail.com" in email:
            raise forms.ValidationError("email has to be gmail.com")
        return email



