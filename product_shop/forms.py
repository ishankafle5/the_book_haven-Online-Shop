from django import forms
from .models import Customer, Order
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class OrderForm(forms.ModelForm):
    model = Order

    class Meta:
        model = Order
        # fields = ('ordered_by', 'mobile', 'email',
        #           'shipping_address', 'subtotal', 'discount', 'total')
        fields='__all__'
        labels = {
            'cart':"",
            'ordered_by': "Your Name",
            'mobile': "Your Phone Number",
            'shipping_address': "Your current Address",
            'subtotal': "Amount",
            'discount': "Discount",
            'total': "Total",
            'order_status':""

        }        
 
class LoginForm(forms.ModelForm):
    model= User
     
    class Meta:
        model=User
        fields=('first_name',)
     
     
class SignupForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model=User
        fields = ('username', 'email', 'password1', 'password2')     
# class (mode)