from django.db import models
from django.urls import reverse

from django_pandas.managers import DataFrameManager

# from django.db.models.functions import Upper
# from django.db.models.indexes import Index

from django.db.models import F, Sum
from register.models import Item, Product, Supplier


UNITS=(
        (None, 'Выбрать ед.изм.'),
        ('кг', 'кг'),        
        ('л', 'л'),
        ('шт.',' шт.'),
    )

STATUS_CHOICE = (
        ('pending', 'ожидание '),
        ('decline', 'отклонить' ),
        ('approved', 'одобрено'),
    )


'''Модель покупок товаров''' 

# cost = ('BuyItem'.objects.aggregate(total=Sum(F('unit_cost') * F('quantity'))) 
#     ['cost'])  
class BuyItem(models.Model):
    code=models.DecimalField(max_digits=12, help_text="Не более 12 знаков",decimal_places=0,null=True,verbose_name='Код')
    item =models.CharField(max_length=200, help_text="Не более 200 знаков", db_index=True)#отражение в buy_items_list.html
    name = models.ForeignKey(Item, null=True, verbose_name='Наименование', on_delete=models.CASCADE)# для form buy_item.html
    slug= models.SlugField(max_length=255, verbose_name='Url',blank=True, null=True)
    unit = models.CharField(max_length=10,verbose_name='Ед.изм.',  choices=UNITS, null=True ,default='kg')
    unit_cost=models.PositiveIntegerField(verbose_name='Цена, руб', default=0,null=True)
    quantity= models.PositiveIntegerField(verbose_name='Кол.',default=0)
    cost= models.PositiveIntegerField(verbose_name='Сумма, руб', blank=True,null=True)
    item_supplier=models.CharField(max_length=200, help_text="Не более 200 знаков", null=True)#отражение в buy_items_list.html
    supplier= models.ForeignKey(Supplier, on_delete=models.CASCADE, null=True)
    invoice= models.CharField(max_length=250,verbose_name='Накладная',  null=True ,default='Накладная №     , дата   ')   
    created_date = models.DateField(auto_now_add=True, verbose_name='Дата',)
    
    
    def get_absolute_url(self):        
        return reverse('buy', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['-id']
        verbose_name = 'Закупка'
        verbose_name_plural = 'Закупки' 
        
    def __str__(self):
        return str(self.name)  
    @property
    def get_cost(self):
        return self.unit_cost * self.quantity

    
'''Модель склада товаров'''
class StockItem(models.Model):
    code=models.DecimalField(max_digits=12, help_text="Не более 12 знаков",decimal_places=0,null=True,verbose_name='Код')
    name = models.CharField(max_length=200, help_text="Не более 200 знаков", db_index=True)
    slug= models.SlugField(max_length=255, verbose_name='Url')
    supplier=models.CharField(max_length=200, help_text="Не более 200 знаков",verbose_name='Поставщик',null=True)
    daily_requirement= models.DecimalField(verbose_name='Суточная потребность', null=True, max_digits=10, decimal_places=4, default=1)
    unit = models.CharField(max_length=10,verbose_name='Ед.изм.',  choices=UNITS, null=True ,default='kg')
    first_cost = models.DecimalField(max_digits=10, help_text="Не более 10 знаков",decimal_places=2, null=True)
    last_cost = models.DecimalField(max_digits=10, help_text="Не более 10 знаков",decimal_places=2, null=True)
    unit_cost = models.DecimalField(max_digits=10, help_text="Не более 10 знаков",decimal_places=2, null=True)
    place = models.CharField(max_length=100,verbose_name='Место', null=True ,default='store')
    open=models.DecimalField(max_digits=10, help_text="Не более 10 знаков", decimal_places=0, null=True, default=0)
    sales =	models.DecimalField(max_digits=10, help_text="Не более 10 знаков", decimal_places=3, default=0)
    received = models.DecimalField(max_digits=10, help_text="Не более 10 знаков", null=True, decimal_places=0, default=0)
    transfer =models.DecimalField(max_digits=10, help_text="Не более 10 знаков",null=True, decimal_places=0, default=0)
    waste=models.DecimalField(max_digits=10, help_text="Не более 10 знаков",null=True, decimal_places=0, default=0)
    actual=models.DecimalField(max_digits=10, help_text="Не более 10 знаков",decimal_places=2, default=0)
    actual_cost=models.DecimalField(max_digits=12, help_text="Не более 12 знаков", decimal_places=2, default=0)
    stock_days=models.DecimalField(max_digits=4, help_text="Не более 4 знаков", decimal_places=0,null=True, default=3000,  verbose_name='Остаток в днях')
    delivery=models.DecimalField(max_digits=10, help_text="Не более 10 знаков", decimal_places=0, default=0,null=True,verbose_name='Пути') # from DeliverItem (сделать через aggregate)
    delivery_cost=models.DecimalField(max_digits=12, help_text="Не более 12 знаков", decimal_places=2, default=0,null=True,verbose_name='Пути, руб')
    fullstock=models.DecimalField(max_digits=10, help_text="Не более 10 знаков", decimal_places=0, default=0,null=True,verbose_name='Запас, ед.')
    fullstock_days=models.IntegerField( null=True,verbose_name='Запас, дней', default=3000)    
    delivery_time = models.IntegerField(verbose_name='Буфер, дней', null=True, default=5) #from Item -- Это буфер для товарной позиции
    daily_cost=models.DecimalField(max_digits=12, help_text="Не более 12 знаков", decimal_places=2, default=0,null=True,verbose_name='Суточная, руб')
    
    # def save(self, *args, **kwargs):
    #     actual = self.open-self.sales+self.received-self.transfer-self.waste
    #     actual_cost= self.actual*self.actual_cost
    #     super(StockItem, self).save(*args, **kwargs)

    def get_absolute_url(self):        
        return reverse('stock', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['name']
        verbose_name = 'Остаток'
        verbose_name_plural = 'Остатки'
        
        
    def __str__(self):
        return str(self.name)  
    
    # @property
    # def get_actual(self):
    #     return self.open-self.sales+self.received-self.transfer-self.waste 
    
    # @property
    # def get_actual_cost(self):
    #     return (self.open-self.sales+self.received-self.transfer-self.waste )*self.unit_cost
    
    objects = DataFrameManager()


'''Модель передачи товаров (transfer)''' 
 
class TransferItem(models.Model):
    code=models.DecimalField(max_digits=12, help_text="Не более 12 знаков",decimal_places=0,null=True,verbose_name='Код')
    item =models.CharField(max_length=200, help_text="Не более 200 знаков", db_index=True)#отражение в transfer_list.html
    name = models.ForeignKey(Item, null=True, verbose_name='Наименование', on_delete=models.CASCADE)# для form buy_item.html
    slug= models.SlugField(max_length=255, verbose_name='Url',blank=True, null=True)
    unit = models.CharField(max_length=10,verbose_name='Ед.изм.',  choices=UNITS, null=True ,default='kg')
    unit_cost=models.PositiveIntegerField(verbose_name='Цена, руб', default=0,null=True)
    quantity= models.PositiveIntegerField(verbose_name='Кол.',default=0)
    cost= models.PositiveIntegerField(verbose_name='Сумма, руб', blank=True,null=True)
    partner=models.CharField(max_length=200, help_text="Не более 200 знаков", null=True)#отражение в buy_items_list.html
    invoice= models.CharField(max_length=250,verbose_name='Накладная',  null=True ,default='Накладная №     , дата   ')   
    created_date = models.DateField(auto_now_add=True, verbose_name='Дата',)
    
    
    def get_absolute_url(self):        
        return reverse('buy', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['-id']
        verbose_name = 'Передача'
        verbose_name_plural = 'Передачи' 
        
    def __str__(self):
        return str(self.name)  
    @property
    def get_cost(self):
        return self.unit_cost * self.quantity


'''Модель  для списания товаров (waste)''' 
 
class WasteItem(models.Model):
    code=models.DecimalField(max_digits=12, help_text="Не более 12 знаков",decimal_places=0,null=True,verbose_name='Код')
    item =models.CharField(max_length=200, help_text="Не более 200 знаков", db_index=True)#отражение в transfer_list.html
    name = models.ForeignKey(Item, null=True, verbose_name='Наименование', on_delete=models.CASCADE)# для form buy_item.html
    slug= models.SlugField(max_length=255, verbose_name='Url',blank=True, null=True)
    unit = models.CharField(max_length=10,verbose_name='Ед.изм.',  choices=UNITS, null=True ,default='kg')
    unit_cost=models.PositiveIntegerField(verbose_name='Цена, руб', default=0,null=True)
    quantity= models.PositiveIntegerField(verbose_name='Кол.',default=0)
    cost= models.PositiveIntegerField(verbose_name='Сумма, руб', blank=True,null=True)
    approve=models.CharField(max_length=200, help_text="Не более 200 знаков", null=True)#отражение в buy_items_list.html
    document= models.CharField(max_length=250,verbose_name='Акт',  null=True ,default='Акт №     , дата   ')   
    created_date = models.DateField(auto_now_add=True, verbose_name='Дата',)
    
    
    def get_absolute_url(self):        
        return reverse('buy', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['-id','name']
        verbose_name = 'Списание'
        verbose_name_plural = 'Списания' 
        
    def __str__(self):
        return str(self.name)  
    @property
    def get_cost(self):
        return self.unit_cost * self.quantity


'''Модель продаж продуктов''' 
class SaleProduct(models.Model):    
    name = models.ForeignKey(Product,related_name='name_sale', null=True, on_delete=models.PROTECT)
    product=models.CharField(max_length=200, help_text="Не более 200 знаков", null=True, db_index=True)#отражение в sold_product_list.html
    code=models.DecimalField(max_digits=12, help_text="Не более 12 знаков",decimal_places=0,null=True,verbose_name='Код')    
    slug= models.SlugField(max_length=255, verbose_name='Url',blank=True, null=True)
    price=models.PositiveIntegerField(verbose_name='Цена, руб', default=1)
    sold= models.PositiveIntegerField(verbose_name='Sold, руб', default=1)
    unit = models.CharField(max_length=10,verbose_name='Ед.изм.',  choices=UNITS, null=True ,default='шт.')
    revenue= models.DecimalField(max_digits=10, help_text="Не более 10 знаков", decimal_places=2, default=0, blank=True, null=True)
    date= models.DateField( verbose_name='Дата', help_text="'2022-08-18", null=True)
    created_date = models.DateField(auto_now_add=True)      

    def get_absolute_url(self):        
        return reverse('sale', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['-date']
        verbose_name = 'Продажа'
        verbose_name_plural = 'Продажи' 
        
    def __str__(self):
        return str(self.code) 
    
    @property
    def get_revenue(self):
        return self.price*self.sold
    
    objects = DataFrameManager()


'''Модель Ввода места товара (Move - Place)''' 
 
class MoveItem(models.Model):
    name = models.ForeignKey(Item, null=True, verbose_name='Наименование', on_delete=models.CASCADE)# для form buy_item.html
    place= models.CharField(max_length=250,verbose_name='Место',  null=True ,help_text='Стеллаж - Ряд - Место',default='  ') 
    document= models.CharField(max_length=250,verbose_name='Заполнил',  null=True ,default='User ')   
    created_date = models.DateField(auto_now_add=True, verbose_name='Дата',)
    
    
    def get_absolute_url(self):        
        return reverse('buy', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['name','id']
        verbose_name = 'Место'
        verbose_name_plural = 'Место' 
        
    def __str__(self):
        return str(self.name)  
    
'''
Модель промежуточная, для временного хранения выборки продаж по будним дням
'''    
class WeekdaySale(models.Model):
    product=models.CharField(max_length=200, help_text="Не более 200 знаков", null=True, db_index=True)#отражение в sold_product_list.html
    code=models.DecimalField(max_digits=12, help_text="Не более 12 знаков",decimal_places=0,null=True,verbose_name='Код')    
    sold= models.PositiveIntegerField(verbose_name='Sold, руб', default=1)
    date= models.DateField( verbose_name='Дата', help_text="'2022-08-18", null=True)
    first_day= models.DateField(null=True)
    last_day= models.DateField(null=True)


'''
Модель промежуточная, для временного хранения выборки продаж по выходным дням
'''    
class WeekendSale(models.Model):
    product=models.CharField(max_length=200, help_text="Не более 200 знаков", null=True, db_index=True)#отражение в sold_product_list.html
    code=models.DecimalField(max_digits=12, help_text="Не более 12 знаков",decimal_places=0,null=True,verbose_name='Код')    
    sold= models.PositiveIntegerField(verbose_name='Sold, руб', default=1)
    date= models.DateField( verbose_name='Дата', help_text="'2022-08-18", null=True)
    first_day= models.DateField(null=True)
    last_day= models.DateField(null=True)
    

   
'''
Модель для получения суточной потребности товаров на основе прогноза продаж.
Структура модели -  из загрузки  модели рецептов
'''
class DailyRequirement(models.Model):
    product=models.CharField(max_length=200, verbose_name='Продукт')
    code=models.DecimalField(max_digits=10, help_text="Не более 10 знаков", verbose_name='Код продукта',decimal_places=0, null=True)
    avrg_forecast= models.PositiveIntegerField(verbose_name='Суточный прогноз', null=True)# прогноз продаж продуктов из register_Product
    ingredient= models.CharField(max_length=200, verbose_name='Ингредиент')
    code_ingr= models.DecimalField(max_digits=12, help_text="Не более 12 знаков",decimal_places=0, verbose_name='Код ингредиента', null=True)
    ratio= models.DecimalField(max_digits=10, help_text="Не более 10 знаков",decimal_places=4, default=1, null=True)  
    daily_requirement= models.DecimalField(verbose_name='Суточная потребность', null=True, max_digits=10, decimal_places=4)
    created_at= models.DateTimeField(auto_now_add=True, verbose_name='Создан')
    updated_at = models.DateTimeField(auto_now=True,  verbose_name='Изменен')
    
    
    def get_absolute_url(self):        
        return reverse('dailyrequirement', kwargs={'product': self.product})
    
    class Meta:
        ordering = ['product', 'ingredient']
        verbose_name = 'Суточная потребность'
        verbose_name_plural = 'Суточная потребность'

    def __str__(self):
        return str(self.product)


'''Модель заказа товаров''' 
class OrderItem(models.Model):    
    order_number = models.CharField(max_length=10, unique=True, help_text="Не более 10 знаков",)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, related_name='item_order', on_delete=models.CASCADE, null=True)
    code=models.DecimalField(max_digits=12, help_text="Не более 12 знаков",decimal_places=0,null=True,verbose_name='Код')   
    # slug= models.SlugField(max_length=255, verbose_name='Slug',blank=True, null=True)
    unit = models.CharField(max_length=10,verbose_name='Ед.изм.',  choices=UNITS, null=True ,default='kg')
    unit_cost = models.DecimalField(max_digits=10, help_text="Не более 10 знаков",decimal_places=2, null=True)
    order_quantity = models.PositiveIntegerField(null=True)
    order_cost= models.DecimalField(max_digits=10, help_text="Не более 10 знаков",decimal_places=2, null=True)
    status = models.CharField(max_length=10, help_text="Не более 10 знаков", choices=STATUS_CHOICE)
    created_date = models.DateField(auto_now_add=True)


    def get_absolute_url(self):        
        return reverse('order', kwargs={'order_number': self.order_number})

    class Meta:
        ordering = ['-created_date','order_number']
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы' 
        
    def __str__(self):
        return str(self.item)


'''Модель товаров в стадии поставки, на путях - ( уже заказаны, но еще не поставлены)''' 
class DeliverItem(models.Model):
    order_item = models.ForeignKey(OrderItem, related_name='order_deliver', on_delete=models.CASCADE, null=True)
    order_number=models.DecimalField(max_digits=10,decimal_places=0,null=True,verbose_name='Номер заказа')
    supplier = models.CharField(max_length=200, help_text="Не более 200 знаков", unique=True,db_index=True)
    code=models.DecimalField(max_digits=12, help_text="Не более 12 знаков",decimal_places=0,null=True,verbose_name='Код')
    item = models.CharField(max_length=200, help_text="Не более 200 знаков", unique=True,db_index=True)
    # slug= models.SlugField(max_length=255, verbose_name='Url',blank=True, null=True)
    unit = models.CharField(max_length=10,verbose_name='Ед.изм.',  choices=UNITS, null=True ,default='kg')
    unit_cost = models.DecimalField(max_digits=10, help_text="Не более 10 знаков",decimal_places=2, null=True)
    order_quantity = models.DecimalField(max_digits=10, help_text="Не более 10 знаков",decimal_places=2, null=True)
    status = models.CharField(max_length=10, help_text="Не более 10 знаков", choices=STATUS_CHOICE)
    created_date = models.DateField(auto_now_add=True)

    def get_absolute_url(self):        
        return reverse('deliver', kwargs={'order_number': self.order_number})

    class Meta:
        ordering = ['order_number']
        verbose_name = 'На пути'
        verbose_name_plural = 'На путях' 
        
    def __str__(self):
        return str(self.order_item) 
    