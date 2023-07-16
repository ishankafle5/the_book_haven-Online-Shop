from datetime import datetime
from django.db import models
from django.contrib.auth.models import User


def upload_to(instance, filname):
    current_time = datetime.now()
    return 'productimage/'+str(current_time)+filname


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=255,blank=True,null= None,default=None)
    quantity = models.IntegerField(default=0)
    price = models.IntegerField(default=0)


class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=150)
    quantity = models.IntegerField(default=0)
    slug = models.SlugField()
    marked_price = models.PositiveIntegerField()
    selling_price = models.PositiveIntegerField()
    description = models.TextField()
    warranty = models.CharField(max_length=50)
    return_policy = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=upload_to, blank=True, null=True)

    def __str__(self):
        return f"{self.title},{str(self.marked_price)},{str(self.selling_price)}"


class Cart(models.Model):
    user = models.ForeignKey(
        Customer, on_delete=models.SET_NULL, null=True, blank=True)
    total = models.PositiveBigIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)


class CartProducts(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rate = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()
    sub_total = models.PositiveIntegerField()

    # def __str__(self):
    #     return self.


ORDER_STATUS = (
    ("Order Receiving", "Order Receiving"),
    ("Order Processing", "Order Processing"),
    ("On The Way", "On The Way")
)


class Order(models.Model):
    cart = models.OneToOneField(Cart, on_delete=models.CASCADE)
    ordered_by = models.CharField(max_length=200,)
    shipping_address = models.CharField(max_length=200)
    mobile = models.CharField(max_length=15)
    email = models.EmailField(blank=True, null=True)
    subtotal = models.PositiveIntegerField()
    discount = models.PositiveIntegerField()
    total = models.PositiveIntegerField()
    order_status = models.CharField(max_length=150, choices=ORDER_STATUS,default='Order Receiving')
    created_at = models.DateTimeField(auto_now=True)

