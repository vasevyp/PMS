from django.contrib import admin

from import_export.admin import ImportExportModelAdmin

from .models import Category, CategoryItem, Supplier, Item, Product, RecipeIngredient


class SupplierAdmin(ImportExportModelAdmin):
    list_display = ['code', 'name', 'contact' ]
    prepopulated_fields= {'slug': ('name',)}  
    save_on_top = True
    search_fields = ['name',]
    list_filter= ('name', 'code')
admin.site.register(Supplier, SupplierAdmin)



class CategoryItemAdmin(ImportExportModelAdmin):
    list_display = ['code', 'name', 'slug']
    prepopulated_fields= {'slug': ('name',)}
    save_on_top = True
    search_fields = ['name',]
    list_filter= ('name',)
    
    # class Meta:
    #     # abstract = True
    #     ordering = ['code'] #Sort in desc order
admin.site.register(CategoryItem, CategoryItemAdmin)

class CategoryAdmin(ImportExportModelAdmin):
    list_display = ['code', 'name', 'slug']
    prepopulated_fields= {'slug': ('name',)}
    save_on_top = True
    search_fields=['name', 'code']
    list_filter= ('name',)
    
    # class Meta:
    #     ordering = ['code'] #Sort in desc order
admin.site.register(Category, CategoryAdmin)
class ItemAdmin(ImportExportModelAdmin):
    list_display = ['code', 'name', 'category', 'supplier', 'unit_cost',] 
    prepopulated_fields= {'slug': ('name',)}  
    save_on_top = True
    search_fields = ('name',  'code')
    list_filter= ('name', 'code')
admin.site.register(Item, ItemAdmin)

class ProductAdmin(ImportExportModelAdmin):
    list_display = ['code','name', 'price','category', 'created_date' ]
    prepopulated_fields= {'slug': ('name',)}
    save_on_top = True
    search_fields = ('name','code')
    list_filter = ['category','code','name']
 
    
admin.site.register(Product, ProductAdmin)
class RecipeIngredientAdmin(ImportExportModelAdmin):
    list_display = ['product', 'code','ingredient', 'code_ingr', 'unit', 'unit_cost', 'ratio', 'updated_at']
    # prepopulated_fields= {'slug': ('product',)}
    save_on_top = True
    search_fields = ['product__name', 'code', 'code_ingr','ingredient__name']
    list_filter= ('product', 'ingredient')
admin.site.register(RecipeIngredient, RecipeIngredientAdmin)

