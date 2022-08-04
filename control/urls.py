from django.urls import path

from .views import control, buy_item, sold_product,  BuyItemsListView, SoldProductListView, InventoryListView,inventory_about

urlpatterns = [
    path('', control, name='control'),
    path('buy_item/', buy_item, name='buy_item'),
    path('buy_item_list/', BuyItemsListView.as_view(), name='buy_item_list'),
    path('sold_product/', sold_product, name='sold_product'),
    path('sold_product_list/', SoldProductListView.as_view(), name='sold_product_list'),
    path('inventory/', InventoryListView.as_view(), name='inventory'),
    path('inventory_about/', inventory_about, name='inventory_about')
]