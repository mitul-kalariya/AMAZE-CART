from django.urls import path
from products import views

urlpatterns = [
    path("home/",views.home_view.as_view(), name="home")
]