from typing import Any, Dict
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
from .models import Cart, CartProducts, Product, Category
from .forms import LoginForm, OrderForm, SignupForm
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth.views import LoginView

def user_login(request):
    if request.method == 'GET':
        form=LoginForm()
        return render(request,'registration/login.html')
    
    if request.method == 'POST':
        return HttpResponse("")


class CustomLoginView(LoginView):
    def get_success_url(self):
        # Add your custom logic here
        if self.request.user.is_staff:
            return '/admin'
        else:
            return '/'  # Redirect to user profile if user is not staff

def user_signup(request):
    if request.method == 'GET':
        form = SignupForm()
        return render(request,'registration/signup.html',{"form":form})
    if request.method =='POST':
        form=SignupForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            return render(request,'registration/signup.html',{'form',form})


class HomeView(LoginRequiredMixin,TemplateView):
    login_url='/login'
    template_name = 'shop/home.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # return super().get_context_data(**kwargs)
        

        
        print(self.request.session)
        product = Product.objects.all()

        context['product'] = product

        return context


class AllProductView(LoginRequiredMixin,TemplateView):
    login_url='/login'
    template_name = 'shop/allproducts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # return super().get_context_data(**kwargs)
        category = Category.objects.all()
        

        context['category'] = category

        return context


class CategoryView(LoginRequiredMixin,TemplateView):
    login_url='/login'
    template_name = 'shop/allproducts.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        url_slug = self.kwargs['slug']

        category_obj = Category.objects.get(slug=url_slug)
        product_obj = Product.objects.filter(category=category_obj)
        context['catproduct'] = product_obj
        return context

class EachProducts(LoginRequiredMixin,TemplateView):
    login_url='/login'
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

#    count = 10

#     for i in range(121, 125):
#         obj = Category.objects.get(title='Biography')

#         Product.objects.create(title=f'Product{i}', quantity=10, slug=f'product{i}', marked_price=4000, selling_price=3000,
#                                description="ksfdjksjdflksjfsldsdf dsfsdjlfjsd sdlfjsdlkf sdf jsdklfj sdklf jsdkfl jsdlffjsdf", warranty="No", return_policy='! years', category=obj, image="productimage/2023-07-12_233855.5902096a444ade0495480250d0f2fb0d498f47.jpg")
#         count += 14


class AddToCart(LoginRequiredMixin,TemplateView):
    login_url='/login'

    template_name = 'shop/addtocart.html'

    def get_context_data(self, **kwargs):
        
        context = super().get_context_data(**kwargs)
        product_id = self.kwargs['id']
        product_obj = Product.objects.get(id=product_id)

        cart_id = self.request.session.get('cart_id', None)
        
        if cart_id:
            template_name = 'shop/checkoutpage.html'

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
            cartproduct = CartProducts.objects.filter(cart=cart_id)
            total_price = 0
            for i in cartproduct:
                total_price += (i.sub_total)
            cart.total = total_price
            cart.save()
            cart = CartProducts.objects.filter(cart=cart_id)
            context['carts'] = cart
            print("Now")
            return context  # print(update_productqunatity)
        else:
            cart_obj = Cart.objects.create(total=0,user=self.request.user)
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
            cart_items = Cart.objects.get(id=cart_obj.id)
            cart_items = CartProducts.objects.filter(cart=cart_items)
            context['carts'] = cart_items
            
            return context
    def post(self,request,id):
        cart_id=self.request.session['cart_id']
        print(id)
        print("Post Method is come")
        if self.request.method=='POST':
            
            cart_id=(self.request.POST.get('cart'))
            object=Cart.objects.get(id=cart_id)
            print(request.method)
            form=OrderForm(self.request.POST)
            if form.is_valid():
                form.save()
                object.delete()
                return HttpResponse("Success")
            else:
                return HttpResponse("form invalid")
        else:
            print("Form invalied")
            return HttpResponse("NOt done")
        
class CheckoutForm(TemplateView):
    template_name = 'shop/checkoutpage.html'


class CheckOut(LoginRequiredMixin,TemplateView):
    login_url='/login'
    template_name = 'shop/checkoutpage.html'

    def get_context_data(self, **kwargs):
        cart_id = self.request.session.get('cart_id')

        context = super().get_context_data(**kwargs)
        cartobject = Cart.objects.get(id=cart_id)

        cartproduct = CartProducts.objects.filter(cart=cartobject)

        print(cartproduct)

        for i in cartproduct:

            products = Product.objects.get(id=i.product.id)
            # print("THis is products id")
            # print(i.product.id)
            # print(products)
            products.quantity = products.quantity-i.quantity

            products.save()
        cartobject.ordered = True
        cartobject.save()
        return context


class SearchProducts(LoginRequiredMixin,TemplateView):
    login_url='/login'
    template_name = 'shop/home.html'

    def post(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)

        data = self.request.POST.get('searchfield')
        print("THi si sdata")
        print(data)
        # searchedproduct
        
        searchedproduct = Product.objects.filter(title__icontains=data)
        context['searchedproduct'] = searchedproduct
        return context


# name__icontains


class ChangeQuantity():
    @csrf_exempt
    def increase(request):
        id=request.GET.get('card_id')
        print(id)
        print("THis is id")
        object=CartProducts.objects.get(id=id)
        object.quantity=object.quantity+1
        object.save()
        
        object=CartProducts.objects.get(id=id)
        object.sub_total=object.quantity*object.rate
        object.save()
        print("Object Length")
        # total_amt=Cart.objects.get(id=request.session['cart_id']).total
        cart_obj=Cart.objects.get(id=request.session['cart_id'])
        cart_pro_obj=CartProducts.objects.filter(cart=cart_obj)
        total_amt=0
        for i in cart_pro_obj:
            total_amt=i.sub_total+total_amt

        cart_obj.total=total_amt
        cart_obj.save()
        data={
            'quantity':object.quantity,
            'sub_total':object.sub_total,
            'total':total_amt
        }
        print("Object Length")
        # return JsonResponse({'quantity': '1000'})
        return HttpResponse(JsonResponse(data))


    @csrf_exempt
    def decrease(request):
        id=request.GET.get('card_id')
        print(id)
        print("THis is id")
        object=CartProducts.objects.get(id=id)
        object.quantity=object.quantity-1
        object.save()
        object=CartProducts.objects.get(id=id)
        object.sub_total=object.quantity*object.rate
        object.save()
        print("Object Length")
        
        cart_obj=Cart.objects.get(id=request.session['cart_id'])
        cart_pro_obj=CartProducts.objects.filter(cart=cart_obj)
        total_amt=0
        for i in cart_pro_obj:
            total_amt=i.sub_total+total_amt

        cart_obj.total=total_amt
        cart_obj.save()
               
        data={
            'quantity':object.quantity,
            'sub_total':object.sub_total,
            'total':total_amt
        }
        
        return HttpResponse(JsonResponse(data))

        pass
# def returnForm(rsequest):
@login_required
def returnform(request):
    cart_id=request.session['cart_id']
    
    form=OrderForm()
    return form
        # if form.is_valid():form.save()
        
