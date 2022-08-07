from django.urls import path

from .views import impex_post
from .addimpex import post_impex_category, post_impex_item, post_impex_product

urlpatterns = [
    path('import/', impex_post, name='impex'),    
    path('x-category/', post_impex_category, name='xcategory'),
    path('x-item', post_impex_item, name='xitem'),
    path('x-product', post_impex_product, name='xproduct')
]