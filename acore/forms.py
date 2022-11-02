from django import forms
from django.forms import ModelForm
from .models import Order

''' 
Форма для пересчета суточной потребности в товарах (ингредиентах) 
для формирования точки заказа и Заказа.

from acore.models import *

In [2]: from register.models import *

In [3]: from control.models import *

start_date = models.DateField(blank=True, null=True)

SaleProduct.objects.filter(date__range=(start_date, end_date))

ss2=SaleProduct.objects.filter(date__range=('2022-08-11', '2022-08-14'))

In [17]: for i in ss2:
    ...:     if i.date.isoweekday()>5:
    ...:        WeekendSale.objects.create(product= , code= , sold= , date= , first_day= '2022-08-11', last_day='2022-08-14' )
    ...:     else:
    ...:         print(i.date)

sales1=SaleProduct.objects.all()
In [40]: for i in sales1:
            WeekdaySale.objects.all().delete()
            WeekendSale.objects.all().delete()
    ...:    if i.date.isoweekday()<6:

                
    ...:         ms=SaleProduct.objects.filter(code=i.code).aggregate(Max('sold'))
    ...:         m=int(ms['sold__max'])

sales2=SaleProduct.objects.all()

In [7]: for i in sales2:
   ...:     weekend=WeekendSale.objects.filter(code=i.code).aggregate(Avg('sold'))
   ...:     we=int(weekend['sold__avg'])
   ...:     weekday=WeekdaySale.objects.filter(code=i.code).aggregate(Avg('sold'))
   ...:     wd=int(weekday['sold__avg'])
   ...:     i.weekend_forecast=we
   ...:     i.weekday_forecast=wd
   ...:     i.avrg_forecast=(we*2+wd*5)/7
   ...:     rq=DailyRequirement.objects.filter(code=i.code)
   ...:     for j in rq:
   ...:         j.avrg_forecas=(we*2+wd*5)/7
   ...:         j.save()
   ...:     i.save()

In [4]: sale=Product.objects.all()

for i in sale:
    ...:     weekend=WeekendSale.objects.filter(code=i.code).aggregate(Avg('sold'))
    ...:     we=int(weekend['sold__avg'])
    ...:     weekday=WeekdaySale.objects.filter(code=i.code).aggregate(Avg('sold'))
    ...:     wd=int(weekday['sold__avg'])
    ...:     i.weekend_forecast=we
    ...:     i.weekday_forecast=wd
    ...:     i.avrg_forecast=(we*2+wd*5)/7
    ...:     rq=DailyRequirement.objects.filter(code=i.code)
    ...:     for j in rq:
    ...:         j.avrg_forecast=(we*2+wd*5)/7
    ...:         j.daily_requirement=float(j.avrg_forecast)*float(j.ratio)
                 stock=StockItem.objects.filter(code=j.code_ingr)
                 for s in stock:
                    s.daily_requirement=j.daily_requirement
                    s.save()    
    ...:         j.save()
    ...:     i.save()

'''

MODEL=(
       ('1','Avg'),
       ('2','Max'),
       ('3','Avg+20%')
       )
    
    
class RecalculationForm(forms.Form):    
    first_date=forms.DateField(label='Начало периода для перерасчета ', input_formats=['%d/%m/%Y'], 
        widget=forms.DateInput(attrs={'type': 'date'})
    )
    last_date=forms.DateField(label='Конец периода для перерасчета ',input_formats=['%d/%m/%Y'], 
        widget=forms.DateInput(attrs={'type': 'date'})
    )
    recalculation_model = forms.ChoiceField(label='Модель пересчета, Avg, Max, среднее', choices=MODEL, initial='Avg' )


'''Форма для редактирования Заказа'''
class OrderEditForm(ModelForm):
    class Meta:
        model=Order 
        fields=['order' ]
        widgets={
            'order':forms.NumberInput(attrs={'class':'form-control'}),
        } 