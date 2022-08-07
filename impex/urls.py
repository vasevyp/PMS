from django.urls import path

from .views import impex_post
from .addimpex import post_impex_category, post_impex_item

urlpatterns = [
    path('import/', impex_post, name='impex'),    
    path('x-category/', post_impex_category, name='xcategory'),
    path('x-item', post_impex_item, name='xitem')
]