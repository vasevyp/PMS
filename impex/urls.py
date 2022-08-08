from django.urls import path

from .views import impex_post
from .addimpex import post_impex_category, post_impex_item, post_impex_product, post_impex_buyitem, post_impex_transfer_item, post_impex_waste_item

urlpatterns = [
    path('import/', impex_post, name='impex'),    
    path('x-category/', post_impex_category, name='xcategory'),
    path('x-item/', post_impex_item, name='xitem'),
    path('x-product/', post_impex_product, name='xproduct'),
    path('x-buyitem/', post_impex_buyitem, name='xbuyitem'),
    path('x-transfer/', post_impex_transfer_item, name='xtransfer'),
    path('x-waste/', post_impex_waste_item, name='xwaste'),
]