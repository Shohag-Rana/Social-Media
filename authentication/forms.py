from django import forms
from . models import Person
from django.contrib.auth.forms import UsernameField, AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.utils.translation import gettext, gettext_lazy as _ 


class SignUpForm(UserCreationForm):
	password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
	password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
	class Meta:
		model = Person
		fields = ['username', 'email', 'dob', 'gender', 'country', 'profile_pic']
		labels = {
		'username': 'Your Name',
		'email': 'Your Email',
		'dob': 'Date of Birth',
		}
		widgets = {
		'username': forms.TextInput(attrs={'class':'form-control'}),
		'dob': forms.DateInput(attrs={'class': 'form-control', 'id': 'datepicker'}),
		'email': forms.EmailInput(attrs={'class':'form-control'}),
		'gender': forms.Select(attrs={'class':'form-control'}),
		'country': forms.TextInput(attrs={'class':'form-control'}),
		'profile_pic': forms.FileInput(attrs={'class':'form-control'}),
		} 

class LoginForm(AuthenticationForm):
     username = UsernameField(widget= forms.TextInput(attrs={'autofocus': True, 'class': 'form-control'}))
     password = forms.CharField(label=_("Password"), strip= False, widget= forms.PasswordInput(attrs={'autocomplete': 'current-password', 'class': 'form-control'}))

