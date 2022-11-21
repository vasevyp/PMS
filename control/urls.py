from django.urls import path

from .views import  add_buy_item, sold_product,  BuyItemsListView, SoldProductListView, InventoryListView,inventory_about, add_transfer_item, TransferItemsListView, add_waste_item, WasteItemsListView, move_item, PlaceItemsListView

urlpatterns = [
    path('buy_item/', add_buy_item, name='buy_item'),
    path('buy_item_list/', BuyItemsListView.as_view(), name='buy_item_list'),
    path('sold_product/', sold_product, name='sold_product'),
    path('sold_product_list/', SoldProductListView.as_view(), name='sold_product_list'),
    path('inventory/', InventoryListView.as_view(), name='inventory'),
    path('inventory_about/', inventory_about, name='inventory_about'),
    path('transfer/', add_transfer_item, name='transfer'),
    path('transfer_list/', TransferItemsListView.as_view(), name='transfer_list'),
    path('waste/', add_waste_item, name='waste'),
    path('waste_list/', WasteItemsListView.as_view(), name='waste_list'),
    path('move_item/', move_item, name='move-item'),
     path('place_list/', PlaceItemsListView.as_view(), name='place-list'),
    
]