from django.shortcuts import render
from django.views.generic import ListView

from store.models import Product, ProductCategory


class Index(ListView):
    template_name = 'store/index.html'

    def get_queryset(self):
        return []


class ProductView(ListView):
    template_name = 'store/products.html'
    context_object_name = 'products'

    def get_queryset(self):
        return Product.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = ProductCategory.objects.all()
        return context
