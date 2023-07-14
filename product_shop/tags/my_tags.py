from django import template

from product_shop.models import Cart
from product_shop.views import returnform
from ..forms import OrderForm
from django.contrib.sessions.backends.db import SessionStore

register = template.Library()


@register.filter
def first_item(items):
    return items[0].cart.total


@register.filter
def card_Iid(items):
    return items[0].cart.id


@register.filter
def return5items(items):
    return items[0:5]


@register.filter
def categorytype(items):
    return items[0].category

@register.simple_tag
def order_form(request):
    
    form=returnform(request)
    return form
    # # id=SessionStore(session_key='cart_id')
    # id=(request.session['cart_id'])

    # print(f"This is session id")
    # # print((id.values))
    # print(request.method)
    # form_cart=Cart.objects.get(id=int(id))
    # total_amt=form_cart.total        
    # form=OrderForm(initial={ 'subtotal':total_amt})
    # # form=OrderForm()
    # if(request.method=='POST'):
    #     print("Post Method: ")
    #     return "HEllo"
    # return form
    



