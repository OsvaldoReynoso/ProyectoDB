from django import forms
from . import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
	username = forms.CharField(max_length=25, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de Usuario'}))
	password1 = forms.CharField(max_length=20, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña'}))
	password2 = forms.CharField(max_length=20, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Verificar Contraseña'}))
	first_name = forms.CharField(max_length=25, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre(s)'}))
	last_name = forms.CharField(max_length=25, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apellido(s)'}))
	birth_date = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Fecha Nacimiento: MM/DD/AAAA'}))
	email = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Correo'}))


# class SignupForm(forms.Form):
# 	usuario_nombre = forms.CharField(max_length=25, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre Usuario'}))
# 	usuario_correo = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Correo'}))
# 	usuario_password = forms.CharField(max_length=20, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña'}))

	