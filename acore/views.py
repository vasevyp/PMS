from django.shortcuts import render, redirect
# from register.models import RecipeIngredient
# from .models import DailyRequirement
from django.http import HttpResponse
from .forms import  RecalculationForm
from register.models import Supplier



    
def recalculation(request):
    if request.method == "POST":
        first_date = request.POST.get("first_date")
        last_date = request.POST.get("last_date")
        recalculation_model = request.POST.get("recalculation_model")
        print('PRINT!!', first_date, last_date, recalculation_model)
        s=Supplier.objects.all()
        print(s)
        return redirect('memo')
    else:
        form = RecalculationForm()
        title='Recalc'
        return render(request, "forms/recalculation.html", {"form": form, 'title':title})
    
        
    # if request.method == 'POST':
    #     form = RecalculationForm(request.POST)
    #     if form.is_valid():
    #         # first_date= form.cleaned_data
    #         # field=first_date['field']
    #         # last_date= request.POST.get("last_date")
    #         # recalculation_model= form.cleaned_data.get("recalculation_model")
    #         print('AAAAAAAA!!')
    #         # print('AAAAAAAA!!',recalculation_model)
    #         # print('ВНИМАНИЕ: ',first_date, last_date, recalculation_model)
    #         form.save()
        
    # else:
    #   form = RecalculationForm()
    # #   form.merge_from_initial()
    # context = {
    #     'form': form,
    #     # 'first_date':first_date,
    #     # 'last_date':last_date,
    #     # 'recalculation_model':recalculation_model
    # }
    # return render(request, 'forms/recalculation.html', context)      


def buffer(request):
    title='Buffer'
    # items=RecipeIngredient.objects.all()
    # items = DailyRequirement.objects.all()
    context={
        'title':title,
        # 'items':items
    }
    
    return render(request, 'index.html', context)

# def forecast(request):
#     title='Forecast'
#     items =  SellForecast.objects.all()
#     context={
#         'title':title,
#         'items':items        
#     }
#     return render(request, 'sell_forecast.html', context)
    

# Create your views here.
