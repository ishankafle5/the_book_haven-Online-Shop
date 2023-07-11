from django.contrib import admin
from django.urls import path
from .views import AddToCart, AllProductView, HomeView, EachProducts, CheckOut


app_name = 'shopapp'
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('allproducts', AllProductView.as_view(), name='allproducts'),
    path('product/<slug:slug>/', EachProducts.as_view(), name='productdetails'),
    path('add-to-cart/<int:id>/', AddToCart.as_view(), name='addtocart'),
    path('checkout/<int:id>/', CheckOut.as_view(), name='cardid'),
]
