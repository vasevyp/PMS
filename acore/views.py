from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.db.models import Avg, Max, Sum
from register.models import RecipeIngredient, Product, Item, Supplier
from control.models import DailyRequirement, SaleProduct, WeekendSale, WeekdaySale, StockItem
from .forms import  RecalculationForm
from .models import StockForecastDays, ToOrder, ToOrder_3
import datetime, math

'''Рассчет среднесуточной потребности в товарах/ингредиентах. 
1. Задается период фактических продаж продуктов для перерасчета прогноза продаж продуктов. Разделяем фактические продажи на две базы - weekday (рабочие дни) и weekend (выходные).
2. Прогноз (Forecast) можно сделать по 3-м моделям (выбирается): 1)как среднее по weekday и среднее по weekend; 2) как максимальное по weekday и максимальное по weekend; 3) как как среднее по weekday и среднее по weekend увеличенное на 20%. 
3. Прогноз по продуктам загружаем в модель Product, поля weekday_forecast и weekend_forecast. Делаем рассчет средневзвешенных продаж продуктов и записываем его в поле avrg_forecast.
4. Рассчет средневзвешенных продаж продуктов avrg_forecast загружаем в модель DailyRequirement, в ней рассчитываем средневзвешенную суточную потребность в товарах/ингредиентах для обеспечения прогноза продаж, как daily_requirement = ratio * avrg_forecast.
5. Загружаем суточную потребность (daily_requirement) в модель StockItem (Inventory) в поле суточной потребности daily_requirement.
'''
    
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
                        s.actual=s.open+s.received-s.sales-s.transfer-s.waste
                        s.actual_cost=s.actual*s.unit_cost
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
                        s.actual=s.open+s.received-s.sales-s.transfer-s.waste
                        s.actual_cost=s.actual*s.unit_cost
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
                        s.actual=s.open+s.received-s.sales-s.transfer-s.waste
                        s.actual_cost=s.actual*s.unit_cost
                        crs = DailyRequirement.objects.filter(code_ingr=code).aggregate(Sum('daily_requirement'))
                        s.daily_requirement=(crs['daily_requirement__sum'])
                        s.save()
                    j.save()
                i.save() 
                                            
        
        print('SUCCESS!!', first_date, last_date, recalculation_model)
        # WeekendSale.objects.all().delete()
        # WeekdaySale.objects.all().delete()
        return redirect('stock_item_days')
    else:
        form = RecalculationForm()
        title='Recalc'
        return render(request, "forms/recalculation.html", {"form": form, 'title':title})
    
def stock_item_days(request):
    context={
        'title':'StockItem days',
    }    
    return render(request, 'stock_item_days.html', context)





'''Формируем запас товаров/итгредиентов в днях продаж.'''
def stock_forecast_days(request):
    StockForecastDays.objects.all().delete()    
    print('Выполняется формирование запасов в днях продаж')
    stock=StockItem.objects.all()
    for i in stock:
        if  i.daily_requirement > 0:
            i.actual=i.open +i.received-i.sales-i.transfer-i.waste
            print(i.actual)
            i.stock_days=i.actual/i.daily_requirement
            i.save()
            
            StockForecastDays.objects.create(
                code=StockItem.objects.get(code=i.code).code,
                name=StockItem.objects.get(code=i.code).name,
                unit=StockItem.objects.get(code=i.code).unit,
                unit_cost=StockItem.objects.get(code=i.code).unit_cost,
                actual=StockItem.objects.get(code=i.code).actual,
                actual_cost=StockItem.objects.get(code=i.code).actual_cost,
                daily_requirement=StockItem.objects.get(code=i.code).daily_requirement,
                stock_days=i.actual/i.daily_requirement
                               
         )
        else:
            i.stock_days=9999
            i.save()
            StockForecastDays.objects.create(
                code=StockItem.objects.get(code=i.code).code,
                name=StockItem.objects.get(code=i.code).name,
                unit=StockItem.objects.get(code=i.code).unit,
                unit_cost=StockItem.objects.get(code=i.code).unit_cost,
                actual=StockItem.objects.get(code=i.code).actual,
                actual_cost=StockItem.objects.get(code=i.code).actual_cost,
                daily_requirement=StockItem.objects.get(code=i.code).daily_requirement,
                stock_days=9999
                               
         )
        
        print(i.name,i.code, i.stock_days,'-OK.')
        
    success='Расчет остатков в днях выполнен успешно!'
    return render(request, 'stock_item_days.html', context={'stock_success':success})

'''Вывод сформированного запаса товаров/итгредиентов в днях продаж.'''
class StockForecastDaysView(ListView):
    model=StockForecastDays
    template_name = 'list/stock_in_days.html'
    context_object_name = 'stockdays' 
    

def order_required(request):
    title='Required to Order'
    stock=StockItem.objects.all()
    ToOrder.objects.all().delete()
    d=3 
    for i in stock:
        i.actual_cost=i.actual*i.unit_cost
        i.save()
        if i.fullstock_days<i.delivery_time+1:
            i.supply_pack=Item.objects.get(name=i.name).supply_pack
            i.supplier_id=Item.objects.get(name=i.name).supplier_id
            i.supplier=Supplier.objects.get(id=i.supplier_id).name
            ToOrder.objects.create(code=i.code, name=i.name, supplier=i.supplier, delivery_time=i.delivery_time, supply_pack=i.supply_pack, daily_requirement=i.daily_requirement, to_order=math.ceil((i.delivery_time+d-i.fullstock_days)*i.daily_requirement), to_orders=math.ceil((i.delivery_time+d-i.fullstock_days)*i.daily_requirement/i.supply_pack)*i.supply_pack, order_sum =i.last_cost*math.ceil((i.delivery_time+d-i.fullstock_days)*i.daily_requirement/i.supply_pack)*i.supply_pack,  status=i.last_cost)
            
    toorder=ToOrder.objects.all()
    summ_toorder = ToOrder.objects.aggregate(sum_order=Sum('order_sum')).get('sum_order')
    summa=summ_toorder
            
    
    context={
        'title':title,
        'toorders': toorder,
        'summa':summa
    }
    return render(request,  'list/order_required.html', context)

class StockForecastDaysView(ListView):
    model=StockForecastDays
    template_name = 'list/stock_in_days.html'
    context_object_name = 'stockdays' 
    

def order_required_3(request):
    title='Required to Order_3'
    stock=StockItem.objects.all()
    ToOrder_3.objects.all().delete()
    d=6
    for i in stock:
        i.actual_cost=i.actual*i.unit_cost
        i.save()
        if i.fullstock_days<i.delivery_time+4:
            i.supply_pack=Item.objects.get(name=i.name).supply_pack
            i.supplier_id=Item.objects.get(name=i.name).supplier_id
            i.supplier=Supplier.objects.get(id=i.supplier_id).name
            ToOrder_3.objects.create(code=i.code, name=i.name, supplier=i.supplier, delivery_time=i.delivery_time, supply_pack=i.supply_pack, daily_requirement=i.daily_requirement, to_order=math.ceil((i.delivery_time+d-i.fullstock_days)*i.daily_requirement), to_orders=math.ceil((i.delivery_time+d-i.fullstock_days)*i.daily_requirement/i.supply_pack)*i.supply_pack, order_sum =i.last_cost*math.ceil((i.delivery_time+d-i.fullstock_days)*i.daily_requirement/i.supply_pack)*i.supply_pack,  status=i.last_cost)
            
    toorder=ToOrder_3.objects.all()
    summ_toorder = ToOrder_3.objects.aggregate(sum_order=Sum('order_sum')).get('sum_order')
    summa=summ_toorder
            
    
    context={
        'title':title,
        'toorders_3': toorder,
        'summa_3':summa
    }
    return render(request,  'list/order_required_3.html', context)


def buffer(request):
    title='Buffer'
    # items=RecipeIngredient.objects.all()
    # items = DailyRequirement.objects.all()
    context={
        'title':title,
        # 'items':items
    }
    
    return render(request, 'index.html', context)

