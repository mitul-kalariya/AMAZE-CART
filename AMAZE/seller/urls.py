from django.urls import path
from . import views

urlpatterns = [

    path("become-a-seller/", views.BecomeASeller.as_view(),name="become_a_seller")
]
