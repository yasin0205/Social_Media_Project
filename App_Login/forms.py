from django import forms
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User


class CreateNewUser(UserCreationForm):
    email = forms.EmailField(required=True, label="",
                             widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    username = forms.CharField(required=True, label="",
                               widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password1 = forms.CharField(required=True, label="",
                                widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    password2 = forms.CharField(required=True, label="",
                                widget=forms.PasswordInput(attrs={'placeholder': 'Confirm your password'}))
    class Meta:
        model = User
        fields = ('email', 'username', 'password1', 'password2')
