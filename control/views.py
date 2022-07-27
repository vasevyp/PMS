from django.shortcuts import render

from .models import BuyItem, StockItem, SaleProduct, OrderItem, DeliverItem

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

