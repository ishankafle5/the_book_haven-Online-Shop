from django.contrib import admin
from django.urls import path
from .views import AddToCart, AllProductView, CustomLoginView, HomeView, EachProducts, CheckOut, CategoryView, SearchProducts,ChangeQuantity, user_signup
from django.contrib.auth import views as auth_view

app_name = 'shopapp'
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('allproducts', AllProductView.as_view(), name='allproducts'),
    path('product/<slug:slug>/', EachProducts.as_view(), name='productdetails'),
    path('add-to-cart/<int:id>/', AddToCart.as_view(), name='addtocart'),
    path('checkout/<int:id>/', CheckOut.as_view(), name='cardid'),
    path('category/<slug:slug>/', CategoryView.as_view(), name='categorywise'),
    path('searched-products/', SearchProducts.as_view(), name='searchproduct'),
    path('increasequantity/',ChangeQuantity.increase,name="increase-cart"),
    path('decreasequantity/',ChangeQuantity.decrease,name="decrease-cart"),
    path('login/',CustomLoginView.as_view(),name='login'),
    path('logout/',auth_view.LogoutView.as_view(),name='logout'),
    path('signup/',user_signup,name='signup')
    
    
]
