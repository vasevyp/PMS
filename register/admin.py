from django.contrib import admin

from .models import Category, CategoryItem, Supplier, Item, Product, RecipeIngredient


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['code', 'name', ]
    prepopulated_fields= {'slug': ('name',)}
    save_on_top = True
    search_fields=['name',]
    list_filter= ('name',)
    
    # class Meta:
    #     ordering = ['code'] #Sort in desc order
admin.site.register(Category, CategoryAdmin)

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

class SupplierAdmin(admin.ModelAdmin):
    list_display = ['code', 'name' ]
    prepopulated_fields= {'slug': ('name',)}  
    save_on_top = True
    search_fields = ['name',]
    list_filter= ('name', 'code')
admin.site.register(Supplier, SupplierAdmin)

class ItemAdmin(admin.ModelAdmin):
    list_display = ['code', 'name', 'category', 'supplier', 'unit_cost',] 
    prepopulated_fields= {'slug': ('name',)}  
    save_on_top = True
    search_fields = ('name',  'code')
    list_filter= ('name', 'code')
admin.site.register(Item, ItemAdmin)


class RecipeIngredientAdmin(admin.ModelAdmin):
    list_display = ['recipe_name','ingredient', 'unit','quantity']
    prepopulated_fields= {'slug': ('recipe_name',)}
    save_on_top = True
    search_fields = ['name__ingredient', ]
    list_filter= ('recipe_name', 'ingredient')
admin.site.register(RecipeIngredient, RecipeIngredientAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['code','name', ]
    prepopulated_fields= {'slug': ('name',)}
    save_on_top = True
    search_fields = ('name','code')
    list_filter = ['code','name']
 
    
admin.site.register(Product, ProductAdmin)