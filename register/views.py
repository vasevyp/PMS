from django.shortcuts import render,redirect
from django.views.generic import ListView

from .models import Supplier, Item, Product, RecipeIngredient, Category, CategoryItem
from .forms import AddSupplierForm, AddCategoryForm, AddItemCategoryForm, AddItemForm, AddProductForm, AddRecipeIngredientForm

def index(request):
    context={
        'title': 'Main'
    }
    return render(request, template_name='register/index.html', context=context)

def register(request):
    suppliers = Supplier.objects.all()
    items = Item.objects.all()
    products=Product.objects.all()
    recipes=RecipeIngredient.objects.all()
    categoryitems=CategoryItem.objects.all()
    categories = Category.objects.all() # Передано в news/templatetags/news_tags.py
    context = {
        'suppliers': suppliers,
        'items': items,
        'products': products,
        'recipes': recipes,
        'categoryitems': categoryitems,
        'categories': categories,
        'title':'Register'
    }
    
    return render(request, template_name='register/register.html', context=context)


# def suppliers(request):
#     suppliers = Supplier.objects.all()
#     context={
#         'suppliers': suppliers,
#         'title': 'Suppliers'
#     }
#     return render(request, template_name='register/items/suppliers.html', context=context)    
class SupplierListView(ListView):
    model = Supplier
    template_name = 'register/items/suppliers.html'
    context_object_name = 'suppliers'

class ItemCategoriesListView(ListView):
    model = CategoryItem
    template_name = 'register/items/categoryitems.html'
    context_object_name = 'categoryitems'

class ProductCategoriesListView(ListView):
    model = Category
    template_name = 'register/items/category.html'
    context_object_name = 'categories'
    
class ItemsListView(ListView):
    model=Item
    template_name = 'register/items/items.html'
    context_object_name = 'items'    
class ProductListView(ListView):
    model= Product
    template_name = 'register/products/products.html'
    context_object_name = 'products'
    
class ResiperListView(ListView):
    model= RecipeIngredient
    template_name = 'register/products/recipes.html'
    context_object_name = 'recipes'


def add_supplier(request):
    form = AddSupplierForm()
    if request.method == 'POST':
        form = AddSupplierForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('supplier-list')
    context = {
        'form': form
    }
    return render(request, 'forms/addSupplier.html', context)
    
def add_category(request):
    form = AddCategoryForm()
    if request.method == 'POST':
        form = AddCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categories-list')
    context = {
        'form': form
    }
    return render(request, 'forms/addCategory.html', context) 

def add_categoryItem(request):
    form = AddItemCategoryForm()
    if request.method == 'POST':
        form = AddItemCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('itemcategories-list')
    context = {
        'form': form
    }
    return render(request, 'forms/addItemCategory.html', context) 

def add_item(request):
    form = AddItemForm()
    if request.method == 'POST':
        form = AddItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('items-list')
    context = {
        'form': form
    }
    return render(request, 'forms/addItem.html', context)

def add_product(request):
    form = AddProductForm()
    if request.method == 'POST':
        form = AddProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('products-list')
    context = {
        'form': form
    }
    return render(request, 'forms/addProduct.html', context)

def add_to_recipe(request):
    form = AddRecipeIngredientForm()
    if request.method == 'POST':
        form = AddRecipeIngredientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add-to-recipe')
    context = {
        'form': form
    }
    return render(request, 'forms/addToProductRecipe.html', context)   