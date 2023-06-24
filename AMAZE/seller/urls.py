from django.urls import path
from . import views

urlpatterns = [
    path("", views.SellerHomepage.as_view(), name=""),
    path("create_profile/",views.BecomeASeller.as_view(), name="be_a_seller")
    ]
