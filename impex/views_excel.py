from django.shortcuts import render

import datetime as dt
import pandas as pd
import os
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from .models import ImpexSaleProduct, ImpexBuyItem, ImpexTransferItem, ImpexWasteItem
from register.models import Product, Item, Supplier, RecipeIngredient
from control.models import StockItem,BuyItem, SaleProduct, TransferItem, WasteItem
from impex.addimpex import do_slug



'''Загрузка/Импорт продаж из csv file with pandas'''
 
def download_sales(request):
    print('s')               
    try:
        if request.method == 'POST' and request.FILES['myfile']:
          
            myfile = request.FILES['myfile']        
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            uploaded_file_url = fs.url(filename)
            excel_file = uploaded_file_url
            print('excel_file:',excel_file) 
            empexceldata = pd.read_csv("."+excel_file,encoding='utf-8')
            print('type(empexceldata):',type(empexceldata))
            dbframe = empexceldata
            for dbframe in dbframe.itertuples():                 
                # fromdate_time_obj = dt.datetime.strptime('%d-%m-%Y')
                obj = ImpexSaleProduct.objects.create(name=dbframe.name,code=dbframe.code, unit=dbframe.unit,
                                                price=dbframe.price, sold=dbframe.sold, date=dbframe.date)
               
                print('type obj:',type(obj))
                obj.save()
 
            return render(request, 'downloads/download_sales.html', {
                'uploaded_file_url': uploaded_file_url
            })    
    except Exception as identifier:            
        print(identifier)
     
    return render(request, 'downloads/download_sales.html',{})



'''Сохранение импортированного из csv файла списка Проданных Продуктов в Базу Данных'''
def csv_sale_product(request):    
    print('Выполняется Функция post_impex_sale_product')
    req=ImpexSaleProduct.objects.all()
    for i in req:  
        product=Product.objects.get(code=i.code) 
        SaleProduct.objects.create(
            product=product.name,
            code=i.code, 
            slug='sold-'+do_slug(product.name),
            unit='шт.',
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
                # добавить перерасчет Inventory
                i_stock.save()              
        
        print(i.code,i.date,'-OK.')
        i.delete()
    # ImpexSaleProduct.objects.all().delete()
    stocks=StockItem.objects.all()
    for i in stocks:
        i.actual=i.open+i.received-i.sales-i.transfer-i.waste
        i.actual_cost=i.actual*i.unit_cost
        i.stock_days=i.actual/i.daily_requirement
        i.delivery_cost=i.delivery*i.last_cost
        i.fullstock=i.actual+i.delivery
        i.fullstock_days=i.fullstock/i.daily_requirement
        i.save()
            
    success='Загрузка и сохранение продаж в SaleProduct выполнена успешно!'

    return render(request, 'downloads/download_sales.html', context={'sold_success':success})

'''Загрузка/Импорт закупок из csv file with pandas'''
 
def download_buy_item(request):
    print('s')               
    try:
        if request.method == 'POST' and request.FILES['myfile']:
          
            myfile = request.FILES['myfile']        
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            uploaded_file_url = fs.url(filename)
            excel_file = uploaded_file_url
            print('excel_file:',excel_file) 
            empexceldata = pd.read_csv("."+excel_file,encoding='utf-8')
            print('type(empexceldata):',type(empexceldata))
            dbframe = empexceldata
            for dbframe in dbframe.itertuples():                 
                # fromdate_time_obj = dt.datetime.strptime('%d-%m-%Y')
                obj = ImpexBuyItem.objects.create(name=dbframe.name,code=dbframe.code, unit=dbframe.unit,
                                                unit_cost=dbframe.unit_cost, quantity=dbframe.quantity, cost=dbframe.cost, supplier=dbframe.supplier, invoice=dbframe.invoice,)
               
                print('type obj:',type(obj))
                obj.save()
 
            return render(request, 'downloads/download_buy_item.html', {
                'uploaded_file_url': uploaded_file_url
            })    
    except Exception as identifier:            
        print(identifier)
     
    return render(request, 'downloads/download_buy_item.html',{})



'''Сохранение импортированного из csv файла списка Закупленных Товаров в Базу Данных'''
def csv_buyitem(request):    
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
                item.save() 
                     
        
        print(i.name,'-OK.')
        i.delete()
    
    stocks=StockItem.objects.all()
    for i in stocks:
        i.actual=i.open+i.received-i.sales-i.transfer-i.waste
        i.actual_cost=i.actual*i.unit_cost
        i.stock_days=i.actual/i.daily_requirement
        i.delivery_cost=i.delivery*i.last_cost
        i.fullstock=i.actual+i.delivery
        i.fullstock_days=i.fullstock/i.daily_requirement
        i.save()
    success='Загрузка и сохранение закупок в BuyItem выполнена успешно!'

    return render(request, 'downloads/download_buy_item.html', context={'buyitem_success':success})




'''Загрузка/Импорт Трансфера/Передачи из csv file with pandas'''
 
def download_transfer_item(request):
    print('s')               
    try:
        if request.method == 'POST' and request.FILES['myfile']:
          
            myfile = request.FILES['myfile']        
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            uploaded_file_url = fs.url(filename)
            excel_file = uploaded_file_url
            print('excel_file:',excel_file) 
            empexceldata = pd.read_csv("."+excel_file,encoding='utf-8')
            print('type(empexceldata):',type(empexceldata))
            dbframe = empexceldata
            for dbframe in dbframe.itertuples():                 
                obj = ImpexTransferItem.objects.create(item_name=dbframe.item_name,code=dbframe.code, unit=dbframe.unit,
                                                unit_cost=dbframe.unit_cost, quantity=dbframe.quantity, cost=dbframe.cost, partner=dbframe.partner, invoice=dbframe.invoice,)
                               
                print('type obj:',type(obj))
                obj.save()
 
            return render(request, 'downloads/download_transfer_item.html', {
                'uploaded_file_url': uploaded_file_url
            })    
    except Exception as identifier:            
        print(identifier)
     
    return render(request, 'downloads/download_transfer_item.html',{})



'''Сохранение импортированного из csv файла списка Трансфера/Передачи Товаров в Базу Данных'''
def csv_transfer_item(request):    
    print('Выполняется Функция csv_transfer_item')
    req=ImpexTransferItem.objects.all()
    for i in req:   
        quantity=i.quantity
        slug=Item.objects.get(code=i.code).slug   
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
        
        item=StockItem.objects.filter(code=i.code)
        for t in item:
            t.transfer=( t.transfer + quantity)
            t.save()      
        
        print(i.item_name,'-OK.')
        i.delete()
    stocks=StockItem.objects.all()
    for i in stocks:
        i.actual=i.open+i.received-i.sales-i.transfer-i.waste
        i.actual_cost=i.actual*i.unit_cost
        i.stock_days=i.actual/i.daily_requirement
        i.delivery_cost=i.delivery*i.last_cost
        i.fullstock=i.actual+i.delivery
        i.fullstock_days=i.fullstock/i.daily_requirement
        i.save()
    success='Загрузка и сохранение переданных товаров в TransferItem выполнен успешно!'

    return render(request, 'downloads/download_transfer_item.html', context={'transferitem_success':success})

