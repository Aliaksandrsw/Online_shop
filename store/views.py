from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DeleteView, TemplateView

from store.models import Product, ProductCategory, Basket


class Index(TemplateView):
    template_name = 'store/index.html'


class ProductView(ListView):
    model = Product
    template_name = 'store/products.html'
    paginate_by = 2
    context_object_name = 'products'

    def get_queryset(self):
        queryset = super().get_queryset()
        category_id = self.kwargs.get('category_id')
        return queryset.filter(category_id=category_id) if category_id else queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = ProductCategory.objects.all()
        return context


class BasketAddView(LoginRequiredMixin, View):
    model = Basket

    def get(self, request, *args, **kwargs):
        product_id = kwargs.get('product_id')
        Basket.create_or_update(product_id, request.user)
        return redirect(request.META.get('HTTP_REFERER', '/'))


@login_required
def basket_remove(request, basket_id):
    basket = Basket.objects.get(id=basket_id)
    basket.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])
