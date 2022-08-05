from django.shortcuts import render, redirect
from django.views.generic import ListView

from .models import BuyItem, StockItem, SaleProduct, OrderItem, DeliverItem
from .forms import BuyItemForm, SoldProductForm

from register.models import Product, RecipeIngredient, Item


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

def add_buy_item(request):
    form = BuyItemForm()
    if request.method == 'POST':
        form = BuyItemForm(request.POST)
        if form.is_valid():
            name= form.cleaned_data.get("name")
            unit= form.cleaned_data.get("unit")
            unit_cost= form.cleaned_data.get("unit_cost")
            quantity= form.cleaned_data.get("quantity")
            supplier= form.cleaned_data.get("supplier")
            invoice= form.cleaned_data.get("invoice")
            #Запись покупки в StockItem 
            code=Item.objects.get(name=name).code
            bitem=StockItem.objects.filter(name=name)
            for i in bitem:
                actual=i.open +i.received-i.sales-i.transfer-i.waste 
                i.unit_cost=((actual*i.unit_cost + unit_cost*quantity)/(actual+quantity)) 
                i.received=(i.received + quantity)
                i.save()
            # bitem.save()               
                       
           # запись в BuyItem и в buy_items_list
            BuyItem.objects.create(item=name, code=code, unit=unit, unit_cost=unit_cost, quantity=quantity, item_supplier=supplier, invoice=invoice)       
            
            return redirect('buy_item')
    
    context = {
        'form': form,
            }
    return render(request, 'forms/buy_item.html', context)

class BuyItemsListView(ListView):
    model=BuyItem
    template_name = 'control/buy_items_list.html'
    context_object_name = 'buyitems'
     

class InventoryListView(ListView):
    model = StockItem
    template_name='control/inventory_list.html'
    context_object_name='stockitems'
    
def inventory_about(request):
    return render(request,'control/inventory_about.html')    
    

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
    return render(request, 'forms/sold_product.html', context)    
    
class SoldProductListView(ListView):
    model=SaleProduct
    template_name = 'control/sold_product_list.html'
    context_object_name = 'sold_products'
    
# def sold_product_list(request):
#     product=Product.objects.all()
#     sold=SaleProduct.all()
    
#     context = {
#         'buyitems': buyitems,
#         'stockitems': stockitems,
#         'saleproducts': saleproducts,
#         'orderitems': orderitems,
#         'deliveritems': deliveritems,
#         'title':'Control'
#     }
    
#     return render(request, template_name='control/control.html', context=context)
    
    
        
                
                
    