from django.shortcuts import render, redirect

from .models import BuyItem, StockItem, SaleProduct, OrderItem, DeliverItem
from .forms import BuyItemForm, SoldProductForm

from register.models import Product, RecipeIngredient


def control(request):
    buyitems = BuyItem.objects.all()
    stockitems = StockItem.objects.all()
    saleproducts=SaleProduct.objects.all()
    orderitems=OrderItem.objects.all()
    deliveritems=DeliverItem.objects.all()
    
    context = {
        'buyitems': buyitems,
        'stockitems': stockitems,
        'saleproducts': saleproducts,
        'orderitems': orderitems,
        'deliveritems': deliveritems,
        'title':'Control'
    }
    
    return render(request, template_name='control/control.html', context=context)

def buy_item(request):
    form = BuyItemForm()
    if request.method == 'POST':
        form = BuyItemForm(request.POST)
        if form.is_valid():
            name= form.cleaned_data.get("name")
            code= form.cleaned_data.get("code")
            unit_cost= form.cleaned_data.get("unit_cost")
            quantity= form.cleaned_data.get("quantity")
            item=StockItem.objects.get(name=name)
            actual=item.open +item.received-item.sales-item.transfer-item.move-item.waste           
            item.unit_cost=((actual*item.unit_cost + unit_cost*quantity)/(actual+quantity))            
            item.received=(item.received + quantity)
            item.save()                       
            form.save()
            return redirect('buy_item')
    
    context = {
        'form': form,
            }
    return render(request, 'forms/buyItem.html', context)

def sold_product(request):
    form = SoldProductForm()
    if request.method == 'POST':
        form = SoldProductForm(request.POST)
        if form.is_valid():
            name= form.cleaned_data.get("name")
            sold= form.cleaned_data.get("sold")
            p=Product.objects.filter(name=name)
            for i in p:
                product_code=i.code 
            recipe_product=RecipeIngredient.objects.filter(code=product_code)  
            n=recipe_product.count() #количество ингредиентов в продукте
            
            for j in range(n):
                icode=recipe_product[j].code_ingr
                irecipe=RecipeIngredient.objects.get(code=product_code, code_ingr=icode)
                rate=irecipe.ratio
                istock=StockItem.objects.get(code=icode)
                istock.sales=istock.sales + sold*rate
                istock.save()
            form.save()
            return redirect('sold_product')
        
    context = {
        'form': form
    }
    return render(request, 'forms/sales.html', context)    
    # context = {
    #     'form': form
    # }
    # return render(request, 'forms/sales.html', context)    
                
                
    