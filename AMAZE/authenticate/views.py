from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse

from .forms import LoginForm, RegistrationForm

# Create your views here.


class LoginView(View):
    def get(self, request):
        if request.GET.get("user_created") == "success":
            form = LoginForm()
            return render(
                request,
                "authenticate/login.html",
                {"form": LoginForm(), "user_created": True},
            )
        else:
            return render(request, "authenticate/login.html", {"form": LoginForm()})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect("home")
            else:
                return render(
                    request,
                    "authenticate/login.html",
                    {"invalid": True, "form": LoginForm()},
                )


class RegistrationView(View):
    def get(self, request):
        form = RegistrationForm()
        return render(request, "authenticate/signup.html", {"form": form})

    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('login') + '?user_created=success')
        else:
            return render(request, "authenticate/signup.html", {"form": form})
