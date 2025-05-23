from django.shortcuts import render
import datetime as dt
import pandas as pd
import os
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from .models import ImpexSaleProduct, ImpexBuyItem, ImpexTransferItem, ImpexWasteItem,ImpexCategory,ImpexSupplier,ImpexCategoryItem,ImpexProduct, ImpexItem, ImpexRecipeIngredient

def impex_post(request):
    return render(request, 'impex/impex_post.html')


'''1.Загрузка продаж из csv file with pandas'''
 
def download_sales(request):
    print('start download_sales')               
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
                'uploaded_file_url': uploaded_file_url, 'myfile':myfile
            })    
    except Exception as identifier:            
        print('Exception as identifier=',identifier)
     
    return render(request, 'downloads/download_sales.html',{})



'''2.Загрузка закупок из csv file with pandas'''
 
def download_buy_item(request):
    print('start download_buy_item')               
    try:
        if request.method == 'POST' and request.FILES['myfile']:
            print('1==123')          
            myfile = request.FILES['myfile']      
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            uploaded_file_url = fs.url(filename)
            excel_file = uploaded_file_url
            print('2==excel_file:',excel_file) 
            empexceldata = pd.read_csv("."+excel_file,encoding='utf-8')
            print('3==type(empexceldata):',type(empexceldata))
            dbframe = empexceldata
            for dbframe in dbframe.itertuples():                 
                obj = ImpexBuyItem.objects.create(name=dbframe.name,code=dbframe.code, unit=dbframe.unit,
                                                unit_cost=dbframe.unit_cost, quantity=dbframe.quantity, cost=dbframe.cost, supplier=dbframe.supplier, invoice=dbframe.invoice,)
                print('4==type obj:',type(obj))
                obj.save()        
 
            return render(request, 'downloads/download_buy_item.html', {
                'uploaded_file_url': uploaded_file_url, 'myfile':myfile })    
    except Exception as identifier:
        print('Exception as identifier=',identifier)
    
    return render(request, 'downloads/download_buy_item.html',{})



'''3.Загрузка Трансфера/Передачи из csv file with pandas'''
 
def download_transfer_item(request):
    print('start download_transfer_item')               
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
                obj = ImpexTransferItem.objects.create(item_name=dbframe.item_name,code=dbframe.code, unit=dbframe.unit, unit_cost=dbframe.unit_cost, quantity=dbframe.quantity, cost=dbframe.cost, partner=dbframe.partner, invoice=dbframe.invoice,)
                               
                print('type obj:',type(obj))
                obj.save()
 
            return render(request, 'downloads/download_transfer_item.html', {
                'uploaded_file_url': uploaded_file_url, 'myfile':myfile
            })    
    except Exception as identifier:            
        print('Exception as identifier=',identifier)
     
    return render(request, 'downloads/download_transfer_item.html',{})



'''4.Загрузка Waste/Убытка из csv file with pandas'''
 
def download_waste_item(request):
    print('start download_waste_item')               
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
                obj = ImpexWasteItem.objects.create(item_name=dbframe.item_name,code=dbframe.code, unit=dbframe.unit, unit_cost=dbframe.unit_cost, quantity=dbframe.quantity, cost=dbframe.cost, approve=dbframe.approve, document=dbframe.document,)
                               
                print('type obj:',type(obj))
                obj.save()
 
            return render(request, 'downloads/download_waste_item.html', {
                'uploaded_file_url': uploaded_file_url, 'myfile':myfile
            })    
    except Exception as identifier:            
        print('Exception as identifier=',identifier)
     
    return render(request, 'downloads/download_waste_item.html',{})



'''5.Загрузка списка Категории Продуктов из csv file with pandas'''
 
def download_category(request):
    print('start download_category')               
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
                obj = ImpexCategory.objects.create(name=dbframe.name,code=dbframe.code)
                               
                print('type obj:',type(obj))
                obj.save()
 
            return render(request, 'downloads/download_category.html', {
                'uploaded_file_url': uploaded_file_url, 'myfile':myfile
            })    
    except Exception as identifier:            
        print('Exception as identifier=',identifier)
     
    return render(request, 'downloads/download_category.html',{})


'''6.Загрузка списка Поставщиков из csv file with pandas''' 
def download_supplier(request):
    print('start download_supplier')               
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
                obj = ImpexSupplier.objects.create(name=dbframe.name,code=dbframe.code, contact=dbframe.contact, address=dbframe.address)
                               
                print('type obj:',type(obj))
                obj.save()
 
            return render(request, 'downloads/download_supplier.html', {
                'uploaded_file_url': uploaded_file_url, 'myfile':myfile
            })    
    except Exception as identifier:            
        print('Exception as identifier=',identifier)
     
    return render(request, 'downloads/download_supplier.html',{})

'''7.Загрузка списка Категорий товаров из csv file with pandas''' 
def download_categoryitem(request):
    print('start download_categoryitem')               
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
                obj = ImpexCategoryItem.objects.create(name=dbframe.name,code=dbframe.code)
                               
                print('type obj:',type(obj))
                obj.save()
 
            return render(request, 'downloads/download_category_item.html', {
                'uploaded_file_url': uploaded_file_url, 'myfile':myfile
            })    
    except Exception as identifier:            
        print('Exception as identifier=',identifier)
     
    return render(request, 'downloads/download_category_item.html',{})


'''8.Загрузка списка Продуктов из csv file with pandas''' 
def download_product(request):
    print('start download_product')               
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
                obj = ImpexProduct.objects.create(name=dbframe.name,code=dbframe.code, difficulty=dbframe.difficulty,description=dbframe.description, price=dbframe.price, category=dbframe.category, cooking=dbframe.cooking,weekday_forecast=dbframe.weekday_forecast, weekend_forecast=dbframe.weekend_forecast, holiday_forecast=dbframe.holiday_forecast,promotion_forecast=dbframe.promotion_forecast)
                               
                print('type obj:',type(obj))
                obj.save()
 
            return render(request, 'downloads/download_product.html', {
                'uploaded_file_url': uploaded_file_url, 'myfile':myfile
            })    
    except Exception as identifier:            
        print('Exception as identifier=',identifier)
     
    return render(request, 'downloads/download_product.html',{})

'''9.Загрузка списка Товаров из csv file with pandas'''
 
def download_item(request):
    print('start download_item')               
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
                obj = ImpexItem.objects.create(name=dbframe.name,code=dbframe.code, category=dbframe.category, supplier=dbframe.supplier,unit=dbframe.unit,unit_cost=dbframe.unit_cost,description=dbframe.description,delivery_time=dbframe.delivery_time,supply_pack=dbframe.supply_pack,pack_weight=dbframe.pack_weight,pack_length=dbframe.pack_length,pack_width=dbframe.pack_width,pack_height=dbframe.pack_height,best_befor=dbframe.best_befor)
                               
                print('type obj:',type(obj))
                obj.save()
 
            return render(request, 'downloads/download_item.html', {
                'uploaded_file_url': uploaded_file_url, 'myfile':myfile
            })    
    except Exception as identifier:            
        print('Exception as identifier=',identifier)
     
    return render(request, 'downloads/download_item.html',{})

'''10.Загрузка списка Рецептов из csv file with pandas'''
 
def download_recipe(request):
    print('start download_recipe')               
    try:
        if request.method == 'POST' and request.FILES['myfile']:          
            myfile = request.FILES['myfile']
            print('1==123')        
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            uploaded_file_url = fs.url(filename)
            excel_file = uploaded_file_url
            print('2==excel_file:',excel_file) 
            empexceldata = pd.read_csv("."+excel_file,encoding='utf-8')
            print('3==type(empexceldata):',type(empexceldata))
            dbframe = empexceldata
            for dbframe in dbframe.itertuples():                 
                obj = ImpexRecipeIngredient.objects.create(name=dbframe.name,code=dbframe.code, name_ingr=dbframe.name_ingr,code_ingr=dbframe.code_ingr,unit=dbframe.unit,ratio=dbframe.ratio)
                               
                print('4==type obj:',type(obj))
                obj.save()
 
            return render(request, 'downloads/download_recipe.html', {
                'uploaded_file_url': uploaded_file_url,'myfile':myfile
            })    
    except Exception as identifier:            
        print('Exception as identifier=',identifier)
     
    return render(request, 'downloads/download_recipe.html',{})