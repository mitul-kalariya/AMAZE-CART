from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class LoginForm(forms.Form):
    email = forms.EmailField(label="email", required=True)
    password  = forms.CharField(label="password",max_length=20, widget=forms.PasswordInput)


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            "email",
            "user_name",
            "password1",
            "password2",
            "phone",
            "first_name",
            "last_name",
        )
