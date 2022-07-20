from django.contrib import admin
from  .models import BuyItem, StockItem, SaleProduct, OrderItem, DeliverItem

# Register your models here.
class BuyItemAdmin(admin.ModelAdmin):
    list_display = ['code', 'name', 'unit','unit_cost','quantity', 'cost' ]
    prepopulated_fields= {'slug': ('name',)}  
    save_on_top = True
    search_fields = ['code','name',]
    list_filter= ('name', 'code')
admin.site.register(BuyItem, BuyItemAdmin)


class StockItemAdmin(admin.ModelAdmin):
    list_display = ['code', 'name', 'unit','unit_cost','open', 'sales', 'received', 'transfer', 'move', 'waste','actual','actual_cost' ]
    prepopulated_fields= {'slug': ('name',)}  
    save_on_top = True
    search_fields = ['name', 'code']
    list_filter= ('name', 'code')
admin.site.register(StockItem, StockItemAdmin)


class SaleProductAdmin(admin.ModelAdmin):
    list_display = ['code', 'name', 'price','quantity','revenue' ]
    prepopulated_fields= {'slug': ('name',)}  
    save_on_top = True
    search_fields = ['code','name',]
    list_filter= ('name', 'code')
admin.site.register(SaleProduct, SaleProductAdmin)


class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['code', 'product', 'order_number', 'supplier','unit','order_quantity', 'created_date', 'status' ]
    prepopulated_fields= {'slug': ('product','order_number')}  
    save_on_top = True
    search_fields = ['product', 'order_number']
    list_filter= ('product', 'order_number')
admin.site.register(OrderItem, OrderItemAdmin)



class DeliverItemAdmin(admin.ModelAdmin):
    list_display = ['code', 'product', 'order_number', 'supplier','unit','order_quantity', 'created_date', 'status' ]
    prepopulated_fields= {'slug': ('product','order_number')}  
    save_on_top = True
    search_fields = ['product', 'order_number']
    list_filter= ('product', 'order_number')
admin.site.register(DeliverItem, DeliverItemAdmin)