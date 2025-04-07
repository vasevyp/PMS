from django.urls import path

from .views import index, materials, add_supplier, add_category, add_category_item, add_item, add_product, add_to_recipe,SupplierListView, ProductCategoriesListView, ItemCategoriesListView, ItemsListView, ProductListView, ResiperListView


urlpatterns = [    
    path('materials', materials, name='materials'),
    path('', index, name='dashbord'),   
    path('supplier-list/', SupplierListView.as_view(), name='supplier-list'),
    path('categories-list/', ProductCategoriesListView.as_view(), name='categories-list'),
    path('itemcategories-list/', ItemCategoriesListView.as_view(), name='itemcategories-list'),
    path('items-list/', ItemsListView.as_view(), name='items-list'),
    path('products-list/', ProductListView.as_view(), name='products-list'),
    path('recipes-list/', ResiperListView.as_view(), name='recipes-list'),
    path('add-supplier/', add_supplier, name='addsupplier'),
    path('add-category/', add_category, name='add-category'),
    path('add-categoryitem/', add_category_item, name='add-categoryitem'),
    path('add-to-recipe/', add_to_recipe, name='add-to-recipe'),
    path('add-item/',add_item, name='add-item' ),
    path('add-product/',add_product, name='add-product' ),

    
   
]