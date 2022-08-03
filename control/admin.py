from django.contrib import admin
from  .models import BuyItem, StockItem, SaleProduct, OrderItem, DeliverItem

# Register your models here.
class BuyItemAdmin(admin.ModelAdmin):
    list_display = ['name','code', 'unit','unit_cost','quantity','created_date' ]
    prepopulated_fields= {'slug': ('name',)}  
    save_on_top = True
    search_fields = ['code','name__name',]
    list_filter= ('name',)
admin.site.register(BuyItem, BuyItemAdmin)


class StockItemAdmin(admin.ModelAdmin):
    list_display = ['code', 'name', 'unit','unit_cost','open', 'sales', 'received', 'transfer', 'move', 'waste' ]
    prepopulated_fields= {'slug': ('name',)}  
    save_on_top = True
    search_fields = ['name', 'code']
    list_filter= ('name', 'code')
admin.site.register(StockItem, StockItemAdmin)

@admin.register(SaleProduct)
class SaleProductAdmin(admin.ModelAdmin):
    list_display = [ 'name', 'code','price','sold', 'unit','created_date' ]
    # prepopulated_fields= {'slug': ('name',)}  
    save_on_top = True
    search_fields = ['code', 'name__name', 'created_date']
    list_filter= ('name', 'code', 'created_date')
    # list_horizontal =('code', 'name', 'price')
# admin.site.register(SaleProduct, SaleProductAdmin)


class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['item', 'order_number', 'supplier','unit','order_quantity', 'unit_cost','created_date', 'status' ]
    prepopulated_fields= {'slug': ('item','order_number')}  
    save_on_top = True
    search_fields = ['item__name', 'order_number', 'supplier__name']
    list_filter= ('item', 'order_number')
admin.site.register(OrderItem, OrderItemAdmin)



class DeliverItemAdmin(admin.ModelAdmin):
    list_display = ['code', 'product', 'order_number', 'supplier','unit','order_quantity', 'created_date', 'status' ]
    prepopulated_fields= {'slug': ('product','order_number')}  
    save_on_top = True
    search_fields = ['product', 'order_number', 'supplier']
    list_filter= ('product', 'order_number')
admin.site.register(DeliverItem, DeliverItemAdmin)