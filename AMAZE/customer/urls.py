from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("search/", views.SearchView.as_view(), name="search"),
    path(
        "seller-request/", views.PreSellerRequestView.as_view(), name="seller-request"
    ),
]
