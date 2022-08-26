from django.shortcuts import render, redirect
from django.db.models import Avg, Max, Sum
from register.models import RecipeIngredient, Product
from control.models import DailyRequirement, SaleProduct, WeekendSale, WeekdaySale, StockItem
from .forms import  RecalculationForm
import datetime


    
def recalculation(request):
    if request.method == "POST":
        first_date = request.POST.get("first_date")
        last_date = request.POST.get("last_date")
        recalculation_model = request.POST.get("recalculation_model")
        print('START!!', first_date, last_date, recalculation_model)
        WeekendSale.objects.all().delete()
        WeekdaySale.objects.all().delete()
        print('WeekendSale -DELETE;  WeekdaySale - DELETE')
        sales=SaleProduct.objects.filter(date__range=(first_date, last_date))
        for s in sales:
            if s.date.isoweekday()>5:
                WeekendSale.objects.create(product=s.product, code=s.code, sold=s.sold, date=s.date, first_day=first_date, last_day=last_date)
            else:
                WeekdaySale.objects.create(product=s.product, code=s.code, sold=s.sold, date=s.date, first_day=first_date, last_day=last_date)
        if recalculation_model=='1':
            products=Product.objects.all()
            for i in products:
                weekend=WeekendSale.objects.filter(code=i.code).aggregate(Avg('sold'))
                we=int(weekend['sold__avg'])
                weekday=WeekdaySale.objects.filter(code=i.code).aggregate(Avg('sold'))
                wd=int(weekday['sold__avg'])
                i.weekend_forecast=we
                i.weekday_forecast=wd
                i.avrg_forecast=(we*2+wd*5)/7
                rq=DailyRequirement.objects.filter(code=i.code)
                for j in rq:
                    j.avrg_forecast=(we*2+wd*5)/7
                    j.daily_requirement=float((we*2+wd*5)/7) * float(j.ratio)
                    stock=StockItem.objects.filter(code=j.code_ingr)
                    for s in stock:
                        code=j.code_ingr
                        crs = DailyRequirement.objects.filter(code_ingr=code).aggregate(Sum('daily_requirement'))
                        s.daily_requirement=(crs['daily_requirement__sum'])
                        s.save()
                    j.save()
                i.save()  
            
            
       
        if recalculation_model=='2':
            products=Product.objects.all()
            for i in products:
                weekend=WeekendSale.objects.filter(code=i.code).aggregate(Max('sold'))
                we=int(weekend['sold__max'])
                weekday=WeekdaySale.objects.filter(code=i.code).aggregate(Max('sold'))
                wd=int(weekday['sold__max'])
                i.weekend_forecast=we
                i.weekday_forecast=wd
                i.avrg_forecast=(we*2+wd*5)/7
                rq=DailyRequirement.objects.filter(code=i.code)
                for j in rq:
                    j.avrg_forecast=(we*2+wd*5)/7
                    j.daily_requirement=float((we*2+wd*5)/7) * float(j.ratio)
                    stock=StockItem.objects.filter(code=j.code_ingr)
                    for s in stock:
                        code=j.code_ingr
                        crs = DailyRequirement.objects.filter(code_ingr=code).aggregate(Sum('daily_requirement'))
                        s.daily_requirement=(crs['daily_requirement__sum'])
                        s.save()
                    j.save()
                i.save()
                
        
        if recalculation_model=='3':
            products=Product.objects.all()
            for i in products:
                weekend=WeekendSale.objects.filter(code=i.code).aggregate(Avg('sold'))
                we=int(weekend['sold__avg'])*1.2
                weekday=WeekdaySale.objects.filter(code=i.code).aggregate(Avg('sold'))
                wd=int(weekday['sold__avg'])*1.2
                i.weekend_forecast=we
                i.weekday_forecast=wd
                i.avrg_forecast=(we*2+wd*5)/7
                rq=DailyRequirement.objects.filter(code=i.code)
                for j in rq:
                    j.avrg_forecast=(we*2+wd*5)/7
                    j.daily_requirement=float((we*2+wd*5)/7) * float(j.ratio)
                    stock=StockItem.objects.filter(code=j.code_ingr)
                    for s in stock:
                        code=j.code_ingr
                        crs = DailyRequirement.objects.filter(code_ingr=code).aggregate(Sum('daily_requirement'))
                        s.daily_requirement=(crs['daily_requirement__sum'])
                        s.save()
                    j.save()
                i.save() 
                                            
        
        print('SUCCESS!!', first_date, last_date, recalculation_model)
        # WeekendSale.objects.all().delete()
        # WeekdaySale.objects.all().delete()
        return redirect('memo')
    else:
        form = RecalculationForm()
        title='Recalc'
        return render(request, "forms/recalculation.html", {"form": form, 'title':title})
    
    

def buffer(request):
    title='Buffer'
    # items=RecipeIngredient.objects.all()
    # items = DailyRequirement.objects.all()
    context={
        'title':title,
        # 'items':items
    }
    
    return render(request, 'index.html', context)

