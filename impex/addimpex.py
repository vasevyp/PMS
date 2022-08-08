from django.shortcuts import render,redirect

from impex.models import ImpexProduct,ImpexItem
from . models import ImpexProduct,ImpexCategory
from register.models import Category, Product, Item, Supplier, CategoryItem
from control.models import StockItem

def post_impex_category(request):    
    print('Выполняется Функция add_impex_product2')
    category=Category.objects.all()
    for cat in category:
        name=cat.name
        code=cat.code 
        slug=cat.slug
        print('Это объект = ', cat, '--', name)
        ImpexCategory.objects.get_or_create(name=name, code=code, slug=slug)
        
        print('Конец выполнения функции End-OK.')
    success='Импорт Category выполнен успешно!'

    return render(request, 'impex/impex_post.html', context={'category_success':success})

def post_impex_product(request):    
    print('Выполняется Функция add_impex_product')
    req=ImpexProduct.objects.all()
    for i in req:
        c_id=Category.objects.get(name=i.category).id
        Product.objects.get_or_create(
            name=i.name,
            code=i.code,
            difficulty=i.difficulty,
            description=i.description,
            price=i.price,
            category_id=c_id,
            cooking=i.cooking,
            slug=i.slug)
        
        print('Конец выполнения функции End-OK.')
    success='Импорт Product выполнен успешно!'

    return render(request, 'impex/impex_post.html', context={'product_success':success})

def post_impex_item(request):    
    print('Выполняется Функция post_impex_item')
    req=ImpexItem.objects.all()
    for i in req:
        s_id=Supplier.objects.get(name=i.supplier).id
        c_id=CategoryItem.objects.get(name=i.category).id
        
        Item.objects.get_or_create(
                            name=i.name,
                            code=i.code,
                            unit=i.unit,
                            unit_cost=i.unit_cost,
                            description=i.description,
                            category_id=c_id,
                            supplier_id=s_id, 
                            available=i.available, 
                            slug=i.slug
                            )
        StockItem.objects.get_or_create(code=i.code, name=i.name, slug=i.slug, unit=i.unit, unit_cost=i.unit_cost) 
        
        print('Конец выполнения функции post_impex_item = End-OK.')
    success='Импорт Items выполнен успешно!'

    return render(request, 'impex/impex_post.html', context={'item_success':success})


