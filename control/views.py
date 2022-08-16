from django.shortcuts import render, redirect
from django.views.generic import ListView

from .models import BuyItem, StockItem, SaleProduct, TransferItem, WasteItem, MoveItem
from .forms import BuyItemForm, SoldProductForm, TransferItemForm, WasteItemForm, MoveItemForm

from register.models import Product, RecipeIngredient, Item


def control(request):
    buyitems = BuyItem.objects.all()
    stockitems = StockItem.objects.all()
    saleproducts=SaleProduct.objects.all()
    # orderitems=OrderItem.objects.all()
    # deliveritems=DeliverItem.objects.all()
    
    context = {
        'buyitems': buyitems,
        'stockitems': stockitems,
        'saleproducts': saleproducts,
        # 'orderitems': orderitems,
        # 'deliveritems': deliveritems,
        'title':'Control'
    }
    
    return render(request, template_name='lists/control.html', context=context)

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
            buy_item=StockItem.objects.filter(name=name)
            for i in buy_item:
                actual=i.open +i.received-i.sales-i.transfer-i.waste 
                i.unit_cost=((actual*i.unit_cost + unit_cost*quantity)/(actual+quantity)) 
                i.received=(i.received + quantity)
                i.save()               
                       
           # запись в BuyItem и в buy_items_list
            BuyItem.objects.create(item=name, code=code, unit=unit, unit_cost=unit_cost, quantity=quantity, item_supplier=supplier, invoice=invoice)       
            
            return redirect('buy_item')
    
    context = {
        'form': form,
            }
    return render(request, 'forms/buy_item.html', context)

class BuyItemsListView(ListView):
    model=BuyItem
    template_name = 'lists/buy_items_list.html'
    context_object_name = 'buyitems'
     

class InventoryListView(ListView):
    model = StockItem
    template_name='lists/inventory_list.html'
    context_object_name='stockitems'
    
def inventory_about(request):
    return render(request,'lists/inventory_about.html')    
    
# Продажа товара с занесением проданных ингредиентов в Остатки
def sold_product(request):
    form = SoldProductForm()
    if request.method == 'POST':
        form = SoldProductForm(request.POST)
        if form.is_valid():
            name= form.cleaned_data.get("name")
            sold= form.cleaned_data.get("sold")
            p=Product.objects.filter(name=name)
            
            for i in p:
                code=i.code 
                price=i.price    
            recipe_product=RecipeIngredient.objects.filter(code=code)  
            n=recipe_product.count() #количество ингредиентов в продукте            
            for j in range(n):
                icode=recipe_product[j].code_ingr
                irecipe=RecipeIngredient.objects.get(code=code, code_ingr=icode)
                rate=irecipe.ratio
                i_stock=StockItem.objects.get(code=icode)
                i_stock.sales=i_stock.sales + sold*rate
                i_stock.save()
            # запись в SaleProduct и в SaleProduct_list
            SaleProduct.objects.create(product=name,code=code, price=price, sold=sold)  
            return redirect('sold_product')
        
    context = {
        'form': form
    }
    return render(request, 'forms/sold_product.html', context)    
    
class SoldProductListView(ListView):
    model=SaleProduct
    template_name = 'lists/sold_product_list.html'
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


def add_transfer_item(request):
    form = TransferItemForm()
    if request.method == 'POST':
        form = TransferItemForm(request.POST)
        if form.is_valid():
            name= form.cleaned_data.get("name")
            unit= form.cleaned_data.get("unit")
            unit_cost= form.cleaned_data.get("unit_cost")
            quantity= form.cleaned_data.get("quantity")
            partner= form.cleaned_data.get("partner")
            invoice= form.cleaned_data.get("invoice")
            #Запись трансфера в StockItem 
            code=Item.objects.get(name=name).code
            item=StockItem.objects.filter(name=name)
            for i in item:
                i.transfer=( i.transfer + quantity)
                i.save()               
                       
           # запись в TransferItem и в transfer_list
            TransferItem.objects.create(item=name, code=code, unit=unit, unit_cost=unit_cost, quantity=quantity, partner=partner, invoice=invoice)       
            
            return redirect('transfer')
    
    context = {
        'form': form,
            }
    return render(request, 'forms/transfer.html', context)

class TransferItemsListView(ListView):
    model=TransferItem
    template_name = 'lists/transfer_list.html'
    context_object_name = 'transfers'


def add_waste_item(request):
    form = WasteItemForm()
    if request.method == 'POST':
        form = WasteItemForm(request.POST)
        if form.is_valid():
            name= form.cleaned_data.get("name")
            unit= form.cleaned_data.get("unit")
            unit_cost= form.cleaned_data.get("unit_cost")
            quantity= form.cleaned_data.get("quantity")
            partner= form.cleaned_data.get("partner")
            invoice= form.cleaned_data.get("invoice")
            #Запись списания в StockItem 
            code=Item.objects.get(name=name).code
            buy_item=StockItem.objects.filter(name=name)
            for i in buy_item:
                i.waste=(i.waste + quantity)
                i.save()               
                       
           # запись в BuyItem и в buy_items_list
            WasteItem.objects.create(item=name, code=code, unit=unit, unit_cost=unit_cost, quantity=quantity, partner=partner, invoice=invoice)       
            
            return redirect('waste')
    
    context = {
        'form': form,
            }
    return render(request, 'forms/waste.html', context)
    
class WasteItemsListView(ListView):
    model=WasteItem
    template_name = 'lists/waste_list.html'
    context_object_name = 'wastes'        
                


def move_item(request):
    form = MoveItemForm()
    if request.method == 'POST':
        form = MoveItemForm(request.POST)
        if form.is_valid():
            name= form.cleaned_data.get("name")
            place= form.cleaned_data.get("place")
            form.save()
            item=StockItem.objects.get(name=name)
            item.place=place
            item.save()
            return redirect('move-item')
    context = {
        'form': form,
        }
    return render(request, 'forms/move_item.html', context)

class PlaceItemsListView(ListView):
    model=MoveItem
    template_name = 'lists/place_list.html'
    context_object_name = 'places' 