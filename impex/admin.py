from django.contrib import admin
from .models import ImpexCategory, ImpexCategoryItem, ImpexSupplier, ImpexItem, ImpexProduct, ImpexRecipeIngredient, ImpexBuyItem, ImpexStockItem, ImpexSaleProduct, ImpexTransferItem, ImpexWasteItem, ImpexOrderItem, ImpexDeliverItem
from import_export.admin import ImportExportModelAdmin



@admin.register(ImpexSupplier)
class ImpexSupplierAdmin(ImportExportModelAdmin):
    list_display = ['code', 'name' ]
    prepopulated_fields= {'slug': ('name',)}  
    save_on_top = True
    search_fields = ['name',]
    list_filter= ('name', 'code')

@admin.register(ImpexCategory)
class ImpexCategoryAdmin(ImportExportModelAdmin):
    list_display = ['code', 'name', ]
    prepopulated_fields= {'slug': ('name',)}
    save_on_top = True
    search_fields=['name', 'code']
    list_filter= ('name',)
    
@admin.register(ImpexItem)
class ImpexItemAdmin(ImportExportModelAdmin):
    list_display = ['code', 'name', 'category', 'supplier', 'unit_cost',] 
    prepopulated_fields= {'slug': ('name',)}  
    save_on_top = True
    search_fields = ('name',  'code')
    list_filter= ('name', 'code')

@admin.register(ImpexProduct)
class ImpexProductAdmin(ImportExportModelAdmin):
    list_display = ['code','name', 'price','category', 'created_date' ]
    prepopulated_fields= {'slug': ('name',)}
    save_on_top = True
    search_fields = ('name','code')
    list_filter = ['category','code','name']

@admin.register(ImpexRecipeIngredient)
class ImpexRecipeIngredientAdmin(ImportExportModelAdmin):
    list_display = ['product', 'code','ingredient', 'code_ingr', 'unit', 'unit_cost', 'ratio', 'updated_at']
    # prepopulated_fields= {'slug': ('product',)}
    save_on_top = True
    search_fields = ['product__name', 'code', 'code_ingr','ingredient__name']
    list_filter= ('product', 'ingredient')



@admin.register(ImpexBuyItem)
class ImpexBuyItemAdmin(ImportExportModelAdmin):
    list_display = ['item','code', 'unit','unit_cost','quantity','created_date' ]
    prepopulated_fields= {'slug': ('name',)}  
    save_on_top = True
    search_fields = ['code','name__name',]
    list_filter= ('name',)



@admin.register(ImpexStockItem)
class ImpexStockItemAdmin(ImportExportModelAdmin):
    list_display = ['code', 'name', 'unit','unit_cost','place','open', 'sales', 'received', 'transfer', 'waste' ]
    prepopulated_fields= {'slug': ('name',)}  
    save_on_top = True
    search_fields = ['name', 'code']
    list_filter= ('name', 'code')


@admin.register(ImpexSaleProduct)
class ImpexSaleProductAdmin(ImportExportModelAdmin):
    list_display = [ 'product', 'code','price','sold', 'unit','created_date' ]
    # prepopulated_fields= {'slug': ('name',)}  
    save_on_top = True
    search_fields = ['code', 'product', 'created_date']
    list_filter= ('product', 'code', 'created_date')
   


@admin.register(ImpexTransferItem)
class ImpexTransferItemAdmin(ImportExportModelAdmin):
    list_display = ['item','code', 'unit','unit_cost','quantity', 'partner', 'created_date' ]
    prepopulated_fields= {'slug': ('item',)}  
    save_on_top = True
    search_fields = ['code','item', 'partner',]
    list_filter= ('name', 'partner',)



@admin.register(ImpexWasteItem)
class ImpexWasteItemAdmin(ImportExportModelAdmin):
    list_display = ['item','code', 'unit','unit_cost','quantity', 'partner', 'created_date' ]
    prepopulated_fields= {'slug': ('item',)}  
    save_on_top = True
    search_fields = ['code','item', 'partner']
    list_filter= ('name', 'partner',)



@admin.register(ImpexOrderItem)
class ImpexOrderItemAdmin(ImportExportModelAdmin):
    list_display = ['item', 'order_number', 'supplier','unit','order_quantity', 'unit_cost','created_date', 'status' ]
    prepopulated_fields= {'slug': ('item','order_number')}  
    save_on_top = True
    search_fields = ['item__name', 'order_number', 'supplier__name']
    list_filter= ('item', 'order_number')




@admin.register(ImpexDeliverItem)
class ImpexDeliverItemAdmin(ImportExportModelAdmin):
    list_display = ['code', 'product', 'order_number', 'supplier','unit','order_quantity', 'created_date', 'status' ]
    prepopulated_fields= {'slug': ('product','order_number')}  
    save_on_top = True
    search_fields = ['product', 'order_number', 'supplier']
    list_filter= ('product', 'order_number')
