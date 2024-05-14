from django.urls import path

from store.views import *
app_name = 'store'


urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('category/<int:category_id>/', ProductView.as_view(), name='category'),
    path('page/<int:page>/', ProductView.as_view(), name='paginator'),
    path('products/', ProductView.as_view(), name='products'),
    path('baskets/add/<int:product_id>', BasketAddView.as_view(), name='basket_add'),
    path('baskets/remove/<int:basket_id>/', basket_remove, name='basket_remove'),
]
