from django.shortcuts import render

def impex_post(request):    
    return render(request, 'impex/impex_post.html')

'''Импорт excel file with pandas'''
from .models import ImpexSaleProduct
import datetime as dt
import pandas as pd
import os
from django.conf import settings
from django.core.files.storage import FileSystemStorage

# def import2(request):
#     return render(request, 'list/importexcel.html')
 
def from_excel(request):
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