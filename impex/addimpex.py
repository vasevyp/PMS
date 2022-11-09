from django.shortcuts import render,redirect


from .models import ImpexProduct,ImpexCategory, ImpexItem,ImpexBuyItem, ImpexTransferItem, ImpexWasteItem, ImpexRecipeIngredient, ImpexCategoryItem, ImpexSupplier, ImpexSaleProduct
from register.models import Category, Product, Item, Supplier, CategoryItem, RecipeIngredient
from control.models import StockItem,BuyItem, TransferItem, WasteItem, SaleProduct, DailyRequirement

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
        
        print(cat.name,'-OK.')
        cat.delete()
    success='Импорт Category выполнен успешно!'

    return render(request, 'impex/impex_post.html', context={'category_success':success})


'''Импорт списка Поставщиков в Базу Данных'''
def post_impex_supplier(request):    
    print('Выполняется Функция post_impex_supplier')
    supplier=ImpexSupplier.objects.all()
    for s in supplier:
        Supplier.objects.get_or_create(name=s.name, code=s.code, address=s.address, contact=s.contact, slug=do_slug(s.name))        
        print(s.name,' -OK')
        s.delete()
    success='Импорт Supplier выполнен успешно!'

    return render(request, 'impex/impex_post.html', context={'supplier_success':success})


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
        
        print(cat.name,' -OK.')
        cat.delete()
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
        
        print(i.name,'-OK.')
        i.delete()
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
                            delivery_time=i.delivery_time,
                            supply_pack=i.supply_pack,
                            pack_weight=i.pack_weight,
                            pack_length=i.pack_length,
                            pack_width=i.pack_width,
                            pack_height=i.pack_height,
                            best_befor=i.best_befor, 
                            slug=do_slug(i.name)
                            )
        StockItem.objects.get_or_create(code=i.code, name=i.name, slug=do_slug(i.name), unit=i.unit, first_cost=i.unit_cost, unit_cost=i.unit_cost, delivery_time=i.delivery_time) 
        
        print(i.name,'-OK')
        i.delete()
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
                            slug='buy-'+do_slug(i.name),
                            item_supplier=i.supplier,
                            name_id=n_id,
                            quantity=i.quantity,
                            supplier_id=s_id, 
                            invoice=i.invoice                            
                            )
        buy_item=StockItem.objects.filter(name=i.name)
        for item in buy_item:
                actual=item.open +item.received-item.sales-item.transfer-item.waste 
                if actual>=0:
                    item.unit_cost=((actual*item.unit_cost + unit_cost*quantity)/(actual+quantity))
                else:
                    item.unit_cost=unit_cost     
                item.received=(item.received + quantity)
                item.last_cost=unit_cost
                item.actual=actual+quantity
                if quantity>=item.delivery:
                    item.delivery=0
                else:
                    item.delivery=item.delivery-quantity
                item.actual_cost=item.actual*item.unit_cost                        
                item.delivery_cost=item.delivery*item.last_cost
                item.fullstock=item.actual+item.delivery
                item.fullstock_days=item.fullstock/item.daily_requirement
                item.save()      
        
        print(i.name,'-OK.')
        i.delete()
    success='Импорт BuyItems выполнен успешно!'

    return render(request, 'impex/impex_post.html', context={'buyitem_success':success})



'''Импорт списка Проданных Продуктов в Базу Данных'''
def post_impex_sale_product(request):    
    print('Выполняется Функция post_impex_sale_product')
    req=ImpexSaleProduct.objects.all()
    for i in req:    
        SaleProduct.objects.create(
            product=i.name,
            code=i.code, 
            slug='sold-'+do_slug(i.name),
            unit=i.unit, 
            price=i.price, 
            sold=i.sold,
            date=i.date,
            name_id=Product.objects.get(code=i.code).id
            )
        
        recipe_product=RecipeIngredient.objects.filter(code=i.code)  
        n=recipe_product.count() #количество ингредиентов в продукте            
        for j in range(n):
                icode=recipe_product[j].code_ingr
                irecipe=RecipeIngredient.objects.get(code=i.code, code_ingr=icode)
                rate=irecipe.ratio
                i_stock=StockItem.objects.get(code=icode)
                i_stock.sales=i_stock.sales + i.sold*rate
                i_stock.save()              
        
        print(i.name,i.date,'-OK.')
        i.delete()
    success='Импорт SaleProduct выполнен успешно!'

    return render(request, 'impex/impex_post.html', context={'sold_success':success})



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
        
        print(i.item_name,'-OK.')
        i.delete()
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
        
        print(i.item_name,'-OK.')
        i.delete()
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
        DailyRequirement.objects.get_or_create(
            product=Product.objects.get(code=i.code).name,
            code=Product.objects.get(code=i.code).code,
            ingredient=Item.objects.get(code=i.code_ingr).name,
            code_ingr=Item.objects.get(code=i.code_ingr).code,
            # unit=Item.objects.get(code=i.code_ingr).unit,
            # unit_cost=Item.objects.get(code=i.code_ingr).unit_cost,
            ratio=i.ratio,
            # ingredient_id=Item.objects.get(code=i.code_ingr).id,
            # product_id=Product.objects.get(code=i.code).id
            )
        
        print(i.name,i.name_ingr,'-OK.')
    success='Импорт Recipe выполнен успешно!'
    return render(request, 'impex/impex_post.html', context={'recipe_success':success})