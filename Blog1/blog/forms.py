from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True,min_length=8)


class RegisterForm(forms.Form):
    username=forms.CharField(required=True)
    password=forms.CharField(required=True,min_length=8)
    email=forms.EmailField(required=True)

