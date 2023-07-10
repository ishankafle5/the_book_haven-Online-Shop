from django.contrib import admin

from product_shop.models import Category, Customer, Product, Cart, CartProducts, Order

# Register your models here.
admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(CartProducts)
admin.site.register(Order)
