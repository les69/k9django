__author__ = 'les'

from django import forms

class LoginForm(forms.Form):
    password = forms.CharField(max_length=200)
    username = forms.CharField(max_length=200)