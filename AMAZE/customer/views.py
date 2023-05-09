from django.shortcuts import render,redirect
from django.contrib.auth import authenticate , login
from .forms import SignupForm,LoginForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
def home_view(request):
    return render(request, "home.html")

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request,user)
                return redirect(home_view)
        else:
            return render(request,'login.html',{"invalid":True,'form': LoginForm()})
    else:
        if request.GET.get('user_created') == 'success':
            form = LoginForm()
            return render(request, "login.html", {'form':LoginForm(),'user_created':True})
    return render(request, "login.html", {'form':LoginForm()})

def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            url = "/login/?user_created=success"
            return redirect(url)
        else:
            return render(request,'signup.html',{'form':form})
    else:
        form = SignupForm()
    return render(request,'signup.html',{'form':form})
