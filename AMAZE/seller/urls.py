from django.urls import path
from . import views

urlpatterns = [
    path("", views.BecomeASeller.as_view(), name="become_a_seller"),
    path("home/",views.SellerHomepage.as_view(), name="home")
    ]
