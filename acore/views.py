from django.shortcuts import render, redirect
from register.models import RecipeIngredient

def buffer(request):
    title='Buffer'
    items=RecipeIngredient.objects.all()
    context={
        'title':title,
        'items':items
    }
    
    return render(request, 'index.html', context)
    

# Create your views here.
