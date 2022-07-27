from django.contrib import admin

from .models import Category, CategoryItem, Supplier, Item, Product, RecipeIngredient

class SupplierAdmin(admin.ModelAdmin):
    list_display = ['code', 'name' ]
    prepopulated_fields= {'slug': ('name',)}  
    save_on_top = True
    search_fields = ['name',]
    list_filter= ('name', 'code')
admin.site.register(Supplier, SupplierAdmin)



class CategoryItemAdmin(admin.ModelAdmin):
    list_display = ['code', 'name', ]
    prepopulated_fields= {'slug': ('name',)}
    save_on_top = True
    search_fields = ['name',]
    list_filter= ('name',)
    
    # class Meta:
    #     # abstract = True
    #     ordering = ['code'] #Sort in desc order
admin.site.register(CategoryItem, CategoryItemAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['code', 'name', ]
    prepopulated_fields= {'slug': ('name',)}
    save_on_top = True
    search_fields=['name',]
    list_filter= ('name',)
    
    # class Meta:
    #     ordering = ['code'] #Sort in desc order
admin.site.register(Category, CategoryAdmin)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['code', 'name', 'category', 'supplier', 'unit_cost',] 
    prepopulated_fields= {'slug': ('name',)}  
    save_on_top = True
    search_fields = ('name',  'code')
    list_filter= ('name', 'code')
admin.site.register(Item, ItemAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['code','name', 'created_date' ]
    prepopulated_fields= {'slug': ('name',)}
    save_on_top = True
    search_fields = ('name','code')
    list_filter = ['code','name']
 
    
admin.site.register(Product, ProductAdmin)
class RecipeIngredientAdmin(admin.ModelAdmin):
    list_display = ['recipe_name','ingredient', 'unit', 'unit_cost', 'quantity', 'updated_at']
    # prepopulated_fields= {'slug': ('recipe_name',)}
    save_on_top = True
    search_fields = ['recipe_name__name', 'ingredient__name']
    list_filter= ('recipe_name', 'ingredient')
admin.site.register(RecipeIngredient, RecipeIngredientAdmin)

