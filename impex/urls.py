from django.urls import path

from .views_csv_download import impex_post, download_sales,  download_transfer_item, download_waste_item, download_buy_item,download_category,download_supplier, download_categoryitem
from .views import csv_category, post_impex_item, post_impex_product, post_impex_recipe, csv_category_item, csv_supplier,csv_transfer_item, csv_buyitem,csv_waste_item, csv_sale_product

urlpatterns = [
    path('import/', impex_post, name='impex'), 
    path('download-category/', download_category, name='download_category'),   #+
    path('csv-category/', csv_category, name='csv_category'), #+
    path('download-categoryitem', download_categoryitem, name='download_categoryitem'), #+
    path('csv-categoryitem/', csv_category_item, name='csv_categoryitem'), #+
    path('download-supplier/', download_supplier, name='download_supplier'), #+
    path('csv-supplier/', csv_supplier, name='csv_supplier'), #+
    path('csv-item/', post_impex_item, name='xitem'),
    path('csv-product/', post_impex_product, name='xproduct'),
    path('csv-recipe/', post_impex_recipe, name='xrecipe'),
    path('download-sales/', download_sales, name='download_sales'),#+
    path('csv-sale-product/', csv_sale_product, name='csv_saleproduct'),#+
    path('download_buy_item/', download_buy_item, name='download_buy_item'),#+
    path('csv-buy-item/', csv_buyitem, name='csv_buyitem'),#+
    path('download-transfer/', download_transfer_item, name='download_transfer_item'),#+
    path('csv-transfer-item/',csv_transfer_item, name='csv_transfer_item'),#+
    path('download-waste-csv/', download_waste_item, name='download_waste_item'),#+
    path('csv-waste-item/',csv_waste_item, name='csv_waste_item'),#+
]