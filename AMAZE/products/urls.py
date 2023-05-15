from django.urls import path
from products import views

urlpatterns = [
    path("home/",views.home_view.as_view(), name="home"),
    path("search/",views.search_view.as_view(), name="search"),
    path("search_elk/",views.ProductsDocumentView.as_view({'get':'list'}), name="search")
]