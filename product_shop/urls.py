from django.contrib import admin
from django.urls import path
from .views import AllProductView, HomeView, EachProducts


app_name = 'shopapp'
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('allproducts', AllProductView.as_view(), name='allproducts'),
    path('product/<slug:slug>/', EachProducts.as_view(), name='productdetails'),
]
