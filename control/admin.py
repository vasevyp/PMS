from django.contrib import admin
from  .models import BuyItem, StockItem, SaleProduct, OrderItem, DeliverItem

# Register your models here.
class BuyItemAdmin(admin.ModelAdmin):
    list_display = ['code', 'name' ]
    prepopulated_fields= {'slug': ('name',)}  
    save_on_top = True
    search_fields = ['name',]
    list_filter= ('name', 'code')
admin.site.register(BuyItem, BuyItemAdmin)