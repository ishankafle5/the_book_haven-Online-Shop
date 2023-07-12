from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    model = Order

    class Meta:
        model = Order
        fields = ('ordered_by', 'mobile', 'email',
                  'shipping_address', 'subtotal', 'discount', 'total')
        labels = {
            'ordered_by': "Your Name",
            'mobile': "Your Phone Number",
            'shipping_address': "Your current Address",
            'subtotal': "Amount",
            'Discount Price': "discount",
            'Total Price': "total",

        }
