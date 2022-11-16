from django.urls import path

from .views_csv_download import impex_post, download_sales,  download_transfer_item, download_waste_item, download_buy_item,download_category,download_supplier, download_categoryitem, download_product, download_item, download_recipe
from .views import csv_category, csv_item, csv_product, csv_recipe, csv_category_item, csv_supplier,csv_transfer_item, csv_buyitem,csv_waste_item, csv_sale_product

urlpatterns = [
    path('import/', impex_post, name='impex'), 
    path('download-category/', download_category, name='download_category'),   #+
    path('csv-category/', csv_category, name='csv_category'), #+
    path('download-categoryitem', download_categoryitem, name='download_categoryitem'), #+
    path('csv-categoryitem/', csv_category_item, name='csv_categoryitem'), #+
    path('download-supplier/', download_supplier, name='download_supplier'), #+
    path('csv-supplier/', csv_supplier, name='csv_supplier'), #+
    path('download-item', download_item, name='download_item'),
    path('csv-item/', csv_item, name='csv_item'),
    path('download-product', download_product, name='download_product'),#+
    path('csv-product/', csv_product, name='csv_product'),#+
    path('download-recipe', download_recipe, name='download_recipe'),
    path('csv-recipe/', csv_recipe, name='csv_recipe'),
    path('download-sales/', download_sales, name='download_sales'),#+
    path('csv-sale-product/', csv_sale_product, name='csv_saleproduct'),#+
    path('download_buy_item/', download_buy_item, name='download_buy_item'),#+
    path('csv-buy-item/', csv_buyitem, name='csv_buyitem'),#+
    path('download-transfer/', download_transfer_item, name='download_transfer_item'),#+
    path('csv-transfer-item/',csv_transfer_item, name='csv_transfer_item'),#+
    path('download-waste-csv/', download_waste_item, name='download_waste_item'),#+
    path('csv-waste-item/',csv_waste_item, name='csv_waste_item'),#+
]