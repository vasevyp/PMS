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
                'uploaded_file_url': uploaded_file_url
            })    
    except Exception as identifier:            
        print(identifier)
     
    return render(request, 'downloads/download_sales.html',{})



'''2.Загрузка закупок из csv file with pandas'''
 
def download_buy_item(request):
    print('start download_buy_item')               
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
                'uploaded_file_url': uploaded_file_url
            })    
    except Exception as identifier:            
        print(identifier)
     
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
                'uploaded_file_url': uploaded_file_url
            })    
    except Exception as identifier:            
        print(identifier)
     
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
                'uploaded_file_url': uploaded_file_url
            })    
    except Exception as identifier:            
        print(identifier)
     
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
                'uploaded_file_url': uploaded_file_url
            })    
    except Exception as identifier:            
        print(identifier)
     
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
                'uploaded_file_url': uploaded_file_url
            })    
    except Exception as identifier:            
        print(identifier)
     
    return render(request, 'downloads/download_category_item.html',{})