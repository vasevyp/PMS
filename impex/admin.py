from django.contrib import admin
from .models import ImpexCategory, ImpexCategoryItem, ImpexSupplier, ImpexItem, ImpexProduct, ImpexRecipeIngredient, ImpexBuyItem, ImpexSaleProduct, ImpexTransferItem, ImpexWasteItem
from import_export.admin import ImportExportModelAdmin



@admin.register(ImpexSupplier)
class ImpexSupplierAdmin(ImportExportModelAdmin):
    list_display = ['code', 'name', 'contact', 'address']
    # prepopulated_fields= {'slug': ('name',)}  
    save_on_top = True
    search_fields = ['name',]
    list_filter= ('name', 'code')

@admin.register(ImpexCategory)
class ImpexCategoryAdmin(ImportExportModelAdmin):
    list_display = ['code', 'name', ]
    save_on_top = True
    search_fields=['name', 'code']
    list_filter= ('name',)
    
@admin.register(ImpexCategoryItem)
class ImpexCategoryItemAdmin(ImportExportModelAdmin):
    list_display = ['code', 'name', ]
    save_on_top = True
    search_fields=['name', 'code']
    list_filter= ('name',)    
    
@admin.register(ImpexItem)
class ImpexItemAdmin(ImportExportModelAdmin):
    list_display = ['code', 'name', 'category', 'supplier', 'unit_cost', 'delivery_time' , 'supply_pack','pack_weight', 'pack_length','pack_width', 'pack_height', 'best_befor' ]  
    save_on_top = True
    search_fields = ('name',  'code')
    list_filter= ('name', 'code')

@admin.register(ImpexProduct)
class ImpexProductAdmin(ImportExportModelAdmin):
    list_display = ['code','name', 'price','category', 'weekday_forecast', 'weekend_forecast', 'avrg_forecast', 'holiday_forecast','promotion_forecast', 'created_date' ]
    save_on_top = True
    search_fields = ('name','code')
    list_filter = ['category','code','name']

@admin.register(ImpexRecipeIngredient)
class ImpexRecipeIngredientAdmin(ImportExportModelAdmin):
    list_display = ['name', 'code','name_ingr', 'code_ingr', 'unit', 'ratio', 'updated_at']
    save_on_top = True
    list_filter= ('name', 'name_ingr')



@admin.register(ImpexBuyItem)
class ImpexBuyItemAdmin(ImportExportModelAdmin):
    list_display = ['name','code', 'unit','unit_cost','quantity', 'supplier', 'created_date' ] 
    save_on_top = True
    search_fields = ['code','name__name',]
    list_filter= ('name',)

@admin.register(ImpexSaleProduct)
class ImpexSaleProductAdmin(ImportExportModelAdmin):
    list_display = [  'code', 'name', 'unit', 'price', 'sold', 'date','created_date' ] 
    save_on_top = True
    search_fields = ['code', 'namet', 'created_date']
    list_filter= ('name', 'code', 'created_date')
   


@admin.register(ImpexTransferItem)
class ImpexTransferItemAdmin(ImportExportModelAdmin):
    list_display = ['item_name','code', 'unit','unit_cost','quantity', 'partner', 'created_date' ] 
    save_on_top = True
    search_fields = ['code','item_name', 'partner',]
    list_filter= ('item_name', 'partner',)



@admin.register(ImpexWasteItem)
class ImpexWasteItemAdmin(ImportExportModelAdmin):
    list_display = ['item_name','code', 'unit','unit_cost','quantity', 'approve', 'created_date' ] 
    save_on_top = True
    search_fields = ['code','item_name', 'approve']
    list_filter= ('item_name', 'approve',)



# @admin.register(ImpexOrderItem)
# class ImpexOrderItemAdmin(ImportExportModelAdmin):
#     list_display = ['item', 'order_number', 'supplier','unit','order_quantity', 'unit_cost','created_date', 'status' ]
#     # prepopulated_fields= {'slug': ('item','order_number')}  
#     save_on_top = True
#     search_fields = ['item__name', 'order_number', 'supplier__name']
#     list_filter= ('item', 'order_number')




# @admin.register(ImpexDeliverItem)
# class ImpexDeliverItemAdmin(ImportExportModelAdmin):
#     list_display = ['code', 'product', 'order_number', 'supplier','unit','order_quantity', 'created_date', 'status' ]
#     # prepopulated_fields= {'slug': ('product','order_number')}  
#     save_on_top = True
#     search_fields = ['product', 'order_number', 'supplier']
#     list_filter= ('product', 'order_number')
