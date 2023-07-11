from typing import Any, Dict
from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
from .models import Cart, CartProducts, Product, Category


class HomeView(TemplateView):
    template_name = 'shop/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # return super().get_context_data(**kwargs)
        product = Product.objects.all()

        context['product'] = product

        return context


class AllProductView(TemplateView):
    template_name = 'shop/allproducts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # return super().get_context_data(**kwargs)
        category = Category.objects.all()

        context['category'] = category

        return context


class EachProducts(TemplateView):
    template_name = 'shop/eachproduct.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # return super().get_context_data(**kwargs)
        url_slug = self.kwargs['slug']
        print('SLug')
        print(url_slug)
        slugwise = Product.objects.get(slug=url_slug)
        context['product'] = slugwise

        return context


class AddToCart(TemplateView):
    template_name = 'shop/addtocart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product_id = self.kwargs['id']
        product_obj = Product.objects.get(id=product_id)

        cart_id = self.request.session.get('cart_id', None)

        if cart_id:
            print("Card id exist")
            print(cart_id)
            print(product_id)
            cart_object = CartProducts.objects.filter(
                cart=cart_id, product=product_id)

            if (cart_object):
                for object in cart_object:
                    object.quantity += 1
                    object.sub_total = object.quantity*object.rate
                    object.save()
                print("This is the object product quantity")
            else:
                cart_obj = Cart.objects.get(id=cart_id)
                print("This is card id")
                print(cart_id)
                card_product = CartProducts.objects.create(
                    cart=cart_obj,
                    product=product_obj,
                    rate=product_obj.selling_price,
                    quantity=1,
                    sub_total=product_obj.selling_price
                )
            cart = Cart.objects.get(id=cart_id)
            context['carts'] = cart
            # for i in cart_items:
            #     for i in i.cart_products:
            #         print(i)
            return context  # print(update_productqunatity)
        else:
            cart_obj = Cart.objects.create(total=0)
            self.request.session['cart_id'] = cart_obj.id
            card_product = CartProducts.objects.create(
                cart=cart_obj,
                product=product_obj,
                rate=product_obj.selling_price,
                quantity=1,
                sub_total=product_obj.selling_price
            )

            cart_obj.total += product_obj.selling_price
            cart_obj.save()
            cart_data = Cart.objects.all()
            cart_items = Cart.objects.get(id=cart_obj.id)

            context['carts'] = cart_items
            return context
