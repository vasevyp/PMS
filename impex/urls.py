from django.urls import path

from .views_csv_download import impex_post, download_sales,  download_transfer_item, download_waste_item, download_buy_item,download_category
from .views import csv_category, post_impex_item, post_impex_product, post_impex_recipe, post_impex_category_item, post_impex_supplier,csv_transfer_item, csv_buyitem,csv_waste_item, csv_sale_product

urlpatterns = [
    path('import/', impex_post, name='impex'), 
    path('download_category/', download_category, name='download_category'),   
    path('x-category/', csv_category, name='csv_category'),
    path('x-categoryitem/', post_impex_category_item, name='xcategoryitem'),
    path('x-supplier/', post_impex_supplier, name='xsupplier'),
    path('x-item/', post_impex_item, name='xitem'),
    path('x-product/', post_impex_product, name='xproduct'),
    path('x-recipe/', post_impex_recipe, name='xrecipe'),
    path('download_sales_csv/', download_sales, name='download_sales'),
    path('x-sale_product/', csv_sale_product, name='csv_saleproduct'),
    path('download_buy_item_csv/', download_buy_item, name='download_buy_item'),
    path('x-buy_item/', csv_buyitem, name='csv_buyitem'),
    path('download_transfer_csv/', download_transfer_item, name='download_transfer_item'),
    path('x-transfer_item/',csv_transfer_item, name='csv_transfer_item'),
    path('download_waste_csv/', download_waste_item, name='download_waste_item'),
    path('x-waste_item/',csv_waste_item, name='csv_waste_item'),
]