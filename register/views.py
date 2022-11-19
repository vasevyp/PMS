from django.shortcuts import render,redirect
from django.views.generic import ListView
from django.db.models import Avg, Max, Sum, F
from datetime import datetime, timedelta

from .models import Supplier, Item, Product, RecipeIngredient, Category, CategoryItem 
from .forms import AddSupplierForm, AddCategoryForm, AddCategoryItemForm, AddItemForm, AddProductForm, AddRecipeIngredientForm
from control.models import StockItem, SaleProduct
from acore.models import ToOrder, ToOrder_3, LastOrder

from impex.views import do_slug


def index(request):
    summ_toorder = ToOrder.objects.aggregate(sum_order=Sum('order_sum')).get('sum_order')
    summ_toorder_3 = ToOrder_3.objects.aggregate(sum_order=Sum('order_sum')).get('sum_order')
    if summ_toorder:
        dif_summa=summ_toorder_3 - summ_toorder
        count_toorder= ToOrder.objects.all().count()
        count_toorder_3= ToOrder_3.objects.all().count()
        dif_count=count_toorder_3-count_toorder
    else:
        dif_summa=0
        summ_toorder=0
        count_toorder= ToOrder.objects.all().count()
        count_toorder_3= ToOrder_3.objects.all().count()
        dif_count=count_toorder_3-count_toorder    
    count_stock=StockItem.objects.all()
    stock_actual_cost = StockItem.objects.aggregate(sum_order=Sum('actual_cost')).get('sum_order')
    summa_stock=stock_actual_cost
    last_order=LastOrder.objects.all()
    summ_lastorder = LastOrder.objects.aggregate(sum_order=Sum('order_cost')).get('sum_order')
    # Критическая номенклатура товаров, остаток на 3 дня и менее
    critical_stock=StockItem.objects.all()
    #Товары на путях
    delivery=StockItem.objects.exclude(delivery = 0)
    summ_delivery=StockItem.objects.exclude(delivery = 0).aggregate(sum_order=Sum('delivery_cost')).get('sum_order')
    # Среднесуточные продажи    
    sales7=SaleProduct.objects.filter(date__range=(datetime.today()-timedelta(days=7), datetime.today())).aggregate(sum_revenue=Sum('revenue')).get('sum_revenue')
    weeksales=sales7/7/1000
    sales7_7=SaleProduct.objects.filter(date__range=(datetime.today()-timedelta(days=14), datetime.today()-timedelta(days=8))).aggregate(sum_revenue=Sum('revenue')).get('sum_revenue')
    weeksales_7=sales7_7/7/1000
    pr_week=(weeksales/weeksales_7-1)*100
    sales30=SaleProduct.objects.filter(date__range=(datetime.today()-timedelta(days=30), datetime.today())).aggregate(sum_revenue=Sum('revenue')).get('sum_revenue')
    monthsales=sales30/30/1000
    sales30_30=SaleProduct.objects.filter(date__range=(datetime.today()-timedelta(days=60), datetime.today()-timedelta(days=31))).aggregate(sum_revenue=Sum('revenue')).get('sum_revenue')
    monthsales_30=sales30_30/30/1000
    pr_month=(monthsales/monthsales_30-1)*100
    
    daily_s=StockItem.objects.aggregate(s=Sum(F('last_cost')*F('daily_requirement') ) )['s']
    daily_sum=daily_s*30/1000
    
    
    
    context={
        'title': 'Main',
        'summa':summ_toorder,
        'summa_3':summ_toorder_3,
        'order_count':count_toorder,
        'order_count_3':count_toorder_3,
        'stock_count':count_stock,
        'stock_sum':summa_stock,
        'dif_count':dif_count,
        'dif_summa':dif_summa,
        'last_order': last_order,
        'summ_lastorder':summ_lastorder,
        'critical_stock':critical_stock,
        'delivery':delivery,
        'summ_delivery':summ_delivery,
        'weeksales':weeksales,
        'monthsales': monthsales,
        'pr_week':pr_week,
        'pr_month': pr_month,
        'daily_sum':daily_sum,
                
    }
    return render(request, template_name='register/index.html', context=context)


def memo(request):
    return render(request, template_name='memo/memo.html', context={'title':'Заметки'})


def materials(request):
    
    daily_s=StockItem.objects.aggregate(s=Sum(F('last_cost')*F('daily_requirement') ) )['s']
    daily_sum=daily_s*30/1000
    items = StockItem.objects.all()
    # result = StockItem.objects.all().annotate(prod=F('last_cost') * F('daily_requirement'))
    for i in items:
        i.daily_cost=i.last_cost*i.daily_requirement*30
        i.save()        

    context = {
        
        'items': items,
        'daily_sum':daily_sum,
       
        
    }
    
    return render(request, template_name='register/materials.html', context=context)
 
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
            supplier= form.cleaned_data.get("supplier")
            unit= form.cleaned_data.get("unit")
            unit_cost= form.cleaned_data.get("unit_cost")
            delivery_time= form.cleaned_data.get("delivery_time")
            StockItem.objects.create(code=code, name=name, slug=do_slug(name), unit=unit, unit_cost=unit_cost, first_cost=unit_cost, last_cost=unit_cost, delivery_time=delivery_time, supplier=supplier)             
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
'''
Добавление позиции рецепта продукта в базу данных RecipeIngredient.
'''
def add_to_recipe(request):
    form = AddRecipeIngredientForm()
    if request.method == 'POST':
        form = AddRecipeIngredientForm(request.POST)
        if form.is_valid():
            product= form.cleaned_data.get("product")
            ingredient= form.cleaned_data.get("ingredient")
            ratio= form.cleaned_data.get("ratio")
            code=Product.objects.get(name=product).code            
            code_ingr=Item.objects.get(name=ingredient).code
            unit=Item.objects.get(name=ingredient).unit
            unit_cost=Item.objects.get(name=ingredient).unit_cost
            print(product,'=',code,'---ingr=',ingredient,'-',code_ingr )
            RecipeIngredient.objects.get_or_create(product=product, ingredient=ingredient, code=code, code_ingr=code_ingr, unit=unit, unit_cost=unit_cost, ratio=ratio, ingredient_cost=unit_cost*ratio)
            print('recipe_item.save()')
           
            return redirect('add-to-recipe')
           
    context = {
        'form': form,        
    }
    return render(request, 'forms/addToProductRecipe.html', context) 
 