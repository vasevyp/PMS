from django.shortcuts import render, redirect
# from register.models import RecipeIngredient
from .models import DailyRequirement


def buffer(request):
    title='Buffer'
    # items=RecipeIngredient.objects.all()
    items = DailyRequirement.objects.all()
    context={
        'title':title,
        'items':items
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
