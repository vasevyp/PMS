from django.urls import path

from .views import impex_post, from_excel
from .addimpex import post_impex_category, post_impex_item, post_impex_product, post_impex_buyitem, post_impex_transfer_item, post_impex_waste_item, post_impex_recipe, post_impex_category_item, post_impex_supplier, post_impex_sale_product

urlpatterns = [
    path('import/', impex_post, name='impex'),    
    path('x-category/', post_impex_category, name='xcategory'),
    path('x-categoryitem/', post_impex_category_item, name='xcategoryitem'),
    path('x-supplier/', post_impex_supplier, name='xsupplier'),
    path('x-item/', post_impex_item, name='xitem'),
    path('x-product/', post_impex_product, name='xproduct'),
    path('x-sold/', post_impex_sale_product, name='xsold'),
    path('x-buyitem/', post_impex_buyitem, name='xbuyitem'),
    path('x-transfer/', post_impex_transfer_item, name='xtransfer'),
    path('x-waste/', post_impex_waste_item, name='xwaste'),
    path('x-recipe/', post_impex_recipe, name='xrecipe'),
    path('download_sales_csv/', from_excel, name='download_sales')
]