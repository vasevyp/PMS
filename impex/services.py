from django.template.defaultfilters import slugify
from control.models import StockItem

'''Функция для создания slug из имени на кирилице'''
def do_slug(name):
    my_string = str(name).translate(str.maketrans("абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ","abvgdeejzijklmnoprstufhzcss_y_euaABVGDEEJZIJKLMNOPRSTUFHZCSS_Y_EUA"))
    slug=slugify(my_string)
    return slug


'''Перерассчет базы данных StockItem'''
def stock_recalculation():
    stocks=StockItem.objects.all()
    for i in stocks:
        i.actual=i.open+i.received-i.sales-i.transfer-i.waste
        i.actual_cost=i.actual*i.unit_cost
        i.stock_days=i.actual/i.daily_requirement
        i.delivery_cost=i.delivery*i.last_cost
        i.fullstock=i.actual+i.delivery
        i.fullstock_days=i.fullstock/i.daily_requirement
        i.save()

