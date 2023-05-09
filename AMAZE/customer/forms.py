from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from customer.models import customer
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
    class Meta:
        model = customer
        fields = (
            'username',
            'password1',
            'password2',
            'first_name',
            'last_name',
            'email',
            # 'dob',
            'gender',
            'phone',
        )


class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", required=True, max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
    password = forms.CharField(label="Password", required=True, max_length=50, widget=forms.TextInput(attrs={"type":"password","class":"form-control"}))
