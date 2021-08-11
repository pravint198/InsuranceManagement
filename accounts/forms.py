from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
import re

class RegisterForm(forms.Form):
    firstname = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First name'}))
    lastname=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last name'}))
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Username'}))
    email=forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email'}))
    password1=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Password'}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Confirm Password'}))
    
    def clean(self):
        cleaned_data = super().clean()
        firstname = cleaned_data.get("firstname")
        lastname = cleaned_data.get("lastname")
        username = cleaned_data.get("username")
        email = cleaned_data.get("email")
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        x=re.search(r"^[a-z0-9]{3,}$", firstname,re.IGNORECASE)
        if x is None:
            self.add_error('firstname','First name should only contain characters and numbers. '
            'Minimum 3 characters')
        x=re.search(r"^[a-z0-9]*$",lastname,re.IGNORECASE)
        if x is None:
            self.add_error('lastname','Last name should only contain characters and numbers')
        x=re.search(r"^[a-z0-9]+$",username,re.IGNORECASE)
        if x is None:
            self.add_error('username','Username should only contain characters and numbers.')
        x=re.search(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',email,re.IGNORECASE)
        if x is None:
            self.add_error('email','Invalid email')
        
        if len(password1)==0 or password1!=password2:
            self.add_error('password2','Password cannot be left blank or both the passwords do not match')


            
        if User.objects.filter(username=username).exists():
            self.add_error('username','Username already taken')
        if User.objects.filter(email=email).exists():
            self.add_error('email','Email already registered')

   
class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Username'}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Password'}))

    
        