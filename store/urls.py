from django.urls import path

from store.views import *
app_name = 'store'


urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('products/', ProductView.as_view(), name='products'),
]
