from django.shortcuts import render,redirect
from django.views.generic import ListView

from .models import Supplier, Item, Product, RecipeIngredient, Category, CategoryItem
from .forms import AddSupplierForm, AddCategoryForm, AddCategoryItemForm, AddItemForm, AddProductForm, AddRecipeIngredientForm
from control.models import StockItem

from impex.addimpex import do_slug


def index(request):
    context={
        'title': 'Main'
    }
    return render(request, template_name='register/index.html', context=context)


def memo(request):
    return render(request, template_name='memo/memo.html', context={'title':'Заметки'})


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

'''
Добавление поставщика в базу данных Supplier
'''
def add_supplier(request):
    form = AddSupplierForm()
    if request.method == 'POST':
        form = AddSupplierForm(request.POST)
        if form.is_valid():
            name= form.cleaned_data.get("name")
            form.save() 
            item=Supplier.objects.get(name=name)
            item.slug=do_slug(name)
            item.save()           
            return redirect('supplier-list')        
        
    context = {
        'form': form
    }
    return render(request, 'forms/addSupplier.html', context)

'''
Добавление категории для продуктов в базу данных Category.
'''

def add_category(request):
    form = AddCategoryForm()
    if request.method == 'POST':
        form = AddCategoryForm(request.POST)
        if form.is_valid():
            name= form.cleaned_data.get("name")
            form.save() 
            s=Category.objects.get(name=name)
            s.slug=do_slug(name)
            s.save()           
            return redirect('categories-list')        
        
    context = {
        'form': form
    }
    return render(request, 'forms/addCategory.html', context)


'''
Добавление  категории для товара/ингредиента в базу данных CategoryItem
'''
def add_category_item(request):
    form = AddCategoryItemForm()
    if request.method == 'POST':
        form = AddCategoryItemForm(request.POST)
        if form.is_valid():
            name= form.cleaned_data.get("name")
            form.save() 
            s=CategoryItem.objects.get(name=name)
            s.slug=do_slug(name)
            s.save()           
            return redirect('itemcategories-list')        
        
    context = {
        'form': form
    }
    return render(request, 'forms/addItemCategory.html', context)



'''
Добавление товара/ингредиента в базу данных StockItem
'''
def add_item(request):
    form = AddItemForm()
    if request.method == 'POST':
        form = AddItemForm(request.POST)
        if form.is_valid():
            code= form.cleaned_data.get("code")
            name= form.cleaned_data.get("name")
            unit= form.cleaned_data.get("unit")
            unit_cost= form.cleaned_data.get("unit_cost")
            delivery_time= form.cleaned_data.get("delivery_time")
            StockItem.objects.create(code=code, name=name, slug=do_slug(name), unit=unit, unit_cost=unit_cost, first_cost=unit_cost, delivery_time=delivery_time)             
            form.save()
            it=Item.objects.get(name=name)
            it.slug=do_slug(name)
            it.delivery_time=delivery_time
            it.save()
            return redirect('add-item')
    context = {
        'form': form
    }
    return render(request, 'forms/addItem.html', context)

'''
Добавление продукта в базу данных Product.
'''
def add_product(request):
    form = AddProductForm()
    if request.method == 'POST':
        form = AddProductForm(request.POST)
        if form.is_valid():
            name= form.cleaned_data.get("name")
            form.save()
            p=Product.objects.get(name=name)
            p.slug=do_slug(name)
            p.save()
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
 