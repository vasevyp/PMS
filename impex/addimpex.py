from django.shortcuts import render,redirect


from .models import ImpexProduct,ImpexCategory, ImpexItem,ImpexBuyItem, ImpexTransferItem, ImpexWasteItem, ImpexRecipeIngredient, ImpexCategoryItem
from register.models import Category, Product, Item, Supplier, CategoryItem, RecipeIngredient
from control.models import StockItem,BuyItem, TransferItem, WasteItem

from django.template.defaultfilters import slugify

'''Функция для создания slug из имени на кирилице'''
def do_slug(name):
    my_string = str(name).translate(str.maketrans("абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ","abvgdeejzijklmnoprstufhzcss_y_euaABVGDEEJZIJKLMNOPRSTUFHZCSS_Y_EUA"))
    slug=slugify(my_string)
    return slug




'''Импорт списка Категории Продуктов в Базу Данных'''
def post_impex_category(request):    
    print('Выполняется Функция post_impex_category')
    category=ImpexCategory.objects.all()
    for cat in category:
        name=cat.name
        code=cat.code 
        slug=do_slug(cat.name)
        print('Это объект = ', cat, '--', name)
        Category.objects.get_or_create(name=name, code=code, slug=slug)
        
        print('Конец выполнения функции End-OK.')
    success='Импорт Category выполнен успешно!'

    return render(request, 'impex/impex_post.html', context={'category_success':success})

'''Импорт списка Категории Товаров в Базу Данных'''
def post_impex_category_item(request):    
    print('Выполняется Функция post_impex_category_item')
    category=ImpexCategoryItem.objects.all()
    for cat in category:
        name=cat.name
        code=cat.code 
        slug=do_slug(cat.name)
        print('Это объект = ', cat, '--', name)
        CategoryItem.objects.get_or_create(name=name, code=code, slug=slug)
        
        print('Конец выполнения функции End-OK.')
    success='Импорт Category выполнен успешно!'
    return render(request, 'impex/impex_post.html', context={'categoryitem_success':success})

'''Импорт списка Продуктов в Базу Данных'''
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
            slug=do_slug(i.name))
        
        print('Конец выполнения функции End-OK.')
    success='Импорт Product выполнен успешно!'

    return render(request, 'impex/impex_post.html', context={'product_success':success})
'''Импорт списка Товаров в Базу Данных'''
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
                            slug=do_slug(i.name)
                            )
        StockItem.objects.get_or_create(code=i.code, name=i.name, slug=do_slug(i.name), unit=i.unit, unit_cost=i.unit_cost) 
        
        print('Конец выполнения функции post_impex_item = End-OK.')
    success='Импорт Items выполнен успешно!'

    return render(request, 'impex/impex_post.html', context={'item_success':success})


'''Импорт списка Закупленных Товаров в Базу Данных'''
def post_impex_buyitem(request):    
    print('Выполняется Функция post_impex_buyitem')
    req=ImpexBuyItem.objects.all()
    for i in req:
        s_id=Supplier.objects.get(name=i.supplier).id
        n_id=Item.objects.get(name=i.name).id
        quantity=i.quantity
        unit_cost=i.unit_cost
        
        BuyItem.objects.get_or_create(
                            item=i.name,
                            code=i.code,
                            unit=i.unit,
                            unit_cost=i.unit_cost,
                            slug=i.slug,
                            item_supplier=i.supplier,
                            name_id=n_id,
                            quantity=i.quantity,
                            supplier_id=s_id, 
                            invoice=i.invoice                            
                            )
        buy_item=StockItem.objects.filter(name=i.name)
        for item in buy_item:
                actual=item.open +item.received-item.sales-item.transfer-item.waste 
                item.unit_cost=((actual*item.unit_cost + unit_cost*quantity)/(actual+quantity)) 
                item.received=(item.received + quantity)
                item.save()      
        
        print('Конец выполнения функции post_impex_buyitem = End-OK.')
    success='Импорт BuyItems выполнен успешно!'

    return render(request, 'impex/impex_post.html', context={'buyitem_success':success})


'''Импорт списка "Переданных Товаров" в Базу Данных'''
def post_impex_transfer_item(request):    
    print('Выполняется Функция post_impex_buyitem')
    req=ImpexTransferItem.objects.all()
    for i in req:   
        quantity=i.quantity
        slug=Item.objects.get(name=i.item_name).slug   
        TransferItem.objects.create(
            item=i.item_name,
            code=i.code, 
            slug=slug,
            unit=i.unit, 
            unit_cost=i.unit_cost, 
            quantity=quantity,
            partner=i.partner, 
            invoice=i.invoice
            ) 
        
        item=StockItem.objects.filter(name=i.item_name)
        for t in item:
            t.transfer=( t.transfer + quantity)
            t.save()      
        
        print('Конец выполнения функции post_impex_transfer_item = End-OK.')
    success='Импорт TransferItems выполнен успешно!'

    return render(request, 'impex/impex_post.html', context={'transferitem_success':success})


'''Импорт списка "Списанных Товаров" в Базу Данных'''
def post_impex_waste_item(request):    
    print('Выполняется Функция post_impex_waste_item')
    req=ImpexWasteItem.objects.all()
    for i in req:   
        quantity=i.quantity  
        slug=Item.objects.get(name=i.item_name).slug     
        WasteItem.objects.create(
            item=i.item_name,
            code=i.code, 
            slug=slug,
            unit=i.unit, 
            unit_cost=i.unit_cost, 
            quantity=quantity,
            approve=i.approve, 
            document=i.document
            ) 
        
        item=StockItem.objects.filter(name=i.item_name)
        for w in item:
            w.waste=( w.waste + quantity)
            w.save()      
        
        print('Конец выполнения функции post_impex_waste_item = End-OK.')
    success='Импорт WasteItems выполнен успешно!'

    return render(request, 'impex/impex_post.html', context={'wasteitem_success':success})



'''Импорт списка Рецептов продуктов в Базу Данных'''
def post_impex_recipe(request):    
    print('Выполняется Функция add_impex_recipe')
    req=ImpexRecipeIngredient.objects.all()
    for i in req:
        RecipeIngredient.objects.get_or_create(
            code=Product.objects.get(code=i.code).code,
            code_ingr=Item.objects.get(code=i.code_ingr).code,
            unit=Item.objects.get(code=i.code_ingr).unit,
            unit_cost=Item.objects.get(code=i.code_ingr).unit_cost,
            ratio=i.ratio,
            ingredient_id=Item.objects.get(code=i.code_ingr).id,
            product_id=Product.objects.get(code=i.code).id
            )
        
        print('Конец выполнения функции End-OK.')
    success='Импорт Recipe выполнен успешно!'
    return render(request, 'impex/impex_post.html', context={'recipe_success':success})