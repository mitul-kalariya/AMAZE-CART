from django.shortcuts import render
from django.views.generic import ListView
from products.models import Products
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

# class home_view(ListView):
#     model = 
#     def ():

class home_view(LoginRequiredMixin,ListView):
    model = Products
    template_name = 'Product/home.html'
    context_object_name = "products"
    paginate_by = 12
