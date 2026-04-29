from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, label="Adresse email")
    adress = forms.CharField(max_length=30, required=True, label="Adresse")
    phone_number = forms.CharField(max_length=15, required=True, label="Numéro de téléphone")
    gender = forms.ChoiceField(choices=[('M', 'Masculin'), ('F', 'Féminin')], required=True, label="Genre")
    birth_date = forms.DateField(required=True, label="Date de naissance")

    class Meta:
        model = User
        fields = ["username", "email","first_name", "last_name", "password1", "password2"]
from .models import Profile


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name"]

        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "first_name": forms.TextInput(attrs={"class": "form-control"}),
            "last_name": forms.TextInput(attrs={"class": "form-control"}),
        }


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["address", "phone_number", "gender", "birth_date"]

        widgets = {
            "address": forms.TextInput(attrs={"class": "form-control"}),
            "phone_number": forms.TextInput(attrs={"class": "form-control"}),
            "gender": forms.Select(attrs={"class": "form-select"}),
            "birth_date": forms.DateInput(attrs={"class": "form-control", "type": "date"}),
        }