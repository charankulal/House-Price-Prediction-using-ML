from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from django.forms.widgets import PasswordInput, TextInput
from . import data


# User creation
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


# User Authentication
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password=forms.CharField(widget=PasswordInput())

class PredictionForm(forms.Form):
    CITY_CHOICES = [
        ('', 'Select City'),
        ('Bangalore', 'Bangalore'),
        ('Chennai', 'Chennai'),
        ('Delhi', 'Delhi'),
        ('Hyderabad', 'Hyderabad'),
        ('Kolkata', 'Kolkata'),
        ('Mumbai', 'Mumbai'),
    ]

    city = forms.ChoiceField(choices=CITY_CHOICES, required=True, label='Enter City')
    location = forms.ChoiceField(choices=[('', 'Select Location')], required=True, label='Enter Location')
    area = forms.IntegerField(label='Enter Area (sq ft)')
    bedrooms = forms.IntegerField(label='Enter Number of Bedrooms')