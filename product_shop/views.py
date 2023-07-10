from typing import Any, Dict
from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
from .models import Product, Category


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
