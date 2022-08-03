from django.urls import path

from .views import control, buy_item, sold_product

urlpatterns = [
    path('', control, name='control'),
    path('buy_item/', buy_item, name='buy_item'),
    path('sold_product/', sold_product, name='sold_product')
]