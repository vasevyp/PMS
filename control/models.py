from django.db import models
from django.urls import reverse

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
        ('processing', 'обработка'),
        ('complete', 'готов')
    )


'''Модель покупок товаров''' 

# cost = ('BuyItem'.objects.aggregate(total=Sum(F('unit_cost') * F('quantity'))) 
#     ['cost'])  
class BuyItem(models.Model):
    code=models.DecimalField(max_digits=12, help_text="Не более 12 знаков",decimal_places=0,null=True,verbose_name='Код')
    item =models.CharField(max_length=200, help_text="Не более 200 знаков", db_index=True)
    name = models.ForeignKey(Item, null=True, verbose_name='Наименование', on_delete=models.CASCADE)
    slug= models.SlugField(max_length=255, verbose_name='Url',blank=True, null=True)
    unit = models.CharField(max_length=10,verbose_name='Ед.изм.',  choices=UNITS, null=True ,default='kg')
    unit_cost=models.PositiveIntegerField(verbose_name='Цена, руб', default=0,null=True)
    quantity= models.PositiveIntegerField(verbose_name='Кол.',default=0)
    cost= models.PositiveIntegerField(verbose_name='Сумма, руб', blank=True,null=True)
    supplier= models.ForeignKey(Supplier, on_delete=models.CASCADE, null=True)
    invoice= models.CharField(max_length=250,verbose_name='Накладная',  null=True ,default='Накладная №         , дата 202_-__-__')   
    created_date = models.DateField(auto_now_add=True, verbose_name='Дата',)
    updated_date = models.DateField(auto_now=True,  verbose_name='Изменен', null=True)
    
    def get_absolute_url(self):        
        return reverse('buy', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['name']
        verbose_name = 'Закупка'
        verbose_name_plural = 'Закупки' 
        
    def __str__(self):
        return str(self.name)  
    @property
    def get_cost(self):
        return self.unit_cost * self.quantity
# def save(self, *args, **kwargs):
#     cost = self.unit_cost * self.quantity
#     super(BuyItem, self).save(*args, **kwargs)
    
# cost = (BuyItem.objects.aggregate(total=Sum(F('unit_cost') * F('quantity')))['cost'])    
    
'''Модель склада товаров'''
class StockItem(models.Model):
    code=models.DecimalField(max_digits=12, help_text="Не более 12 знаков",decimal_places=0,null=True,verbose_name='Код')
    name = models.CharField(max_length=200, help_text="Не более 200 знаков", db_index=True)
    slug= models.SlugField(max_length=255, verbose_name='Url')
    unit = models.CharField(max_length=10,verbose_name='Ед.изм.',  choices=UNITS, null=True ,default='kg')
    unit_cost = models.DecimalField(max_digits=10, help_text="Не более 10 знаков",decimal_places=2, null=True)
    place = models.CharField(max_length=100,verbose_name='Место', null=True ,default='store')
    open=models.DecimalField(max_digits=10, help_text="Не более 10 знаков", decimal_places=0, default=0)
    sales =	models.DecimalField(max_digits=10, help_text="Не более 10 знаков", decimal_places=0, default=0)
    received = models.DecimalField(max_digits=10, help_text="Не более 10 знаков", decimal_places=0, default=0)
    transfer =models.DecimalField(max_digits=10, help_text="Не более 10 знаков", decimal_places=0, default=0)
    waste=models.DecimalField(max_digits=10, help_text="Не более 10 знаков", decimal_places=0, default=0)
    actual=models.DecimalField(max_digits=10, help_text="Не более 10 знаков", decimal_places=0, default=0)
    actual_cost=models.DecimalField(max_digits=12, help_text="Не более 12 знаков", decimal_places=2, default=0)	

    def get_absolute_url(self):        
        return reverse('stock', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['name']
        verbose_name = 'Остаток'
        verbose_name_plural = 'Остатки'
        # indexes = [
        #     Index(Upper('name'), name='name_upper_index'),
        #            ] 
        
    def __str__(self):
        return str(self.name)  
    
    @property
    def get_actual(self):
        return self.open-self.sales+self.received-self.transfer-self.waste 
    
    @property
    def get_actual_cost(self):
        return (self.open-self.sales+self.received-self.transfer-self.waste )*self.unit_cost


'''Модель продаж продуктов''' 
class SaleProduct(models.Model):    
    name = models.ForeignKey(Product,related_name='name_sale', on_delete=models.PROTECT)
    code=models.DecimalField(max_digits=12, help_text="Не более 12 знаков",decimal_places=0,null=True,verbose_name='Код')    
    slug= models.SlugField(max_length=255, verbose_name='Url',blank=True, null=True)
    price=models.PositiveIntegerField(verbose_name='Цена, руб', default=1)
    sold= models.PositiveIntegerField(verbose_name='Sold, руб', default=1)
    unit = models.CharField(max_length=10,verbose_name='Ед.изм.',  choices=UNITS, null=True ,default='шт.')
    revenue= models.DecimalField(max_digits=10, help_text="Не более 10 знаков", decimal_places=2, default=0, blank=True, null=True)
    created_date = models.DateField(auto_now_add=True)      

    def get_absolute_url(self):        
        return reverse('sale', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['name']
        verbose_name = 'Продажа'
        verbose_name_plural = 'Продажи' 
        
    def __str__(self):
        return str(self.code) 
    
    @property
    def get_revenue(self):
        # return format((float(self.price) * float(self.sold)), '.2f')
        return self.price*self.sold
    


'''Модель заказа товаров''' 
class OrderItem(models.Model):    
    order_number = models.CharField(max_length=10, unique=True, help_text="Не более 10 знаков",)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, related_name='item_order', on_delete=models.CASCADE, null=True)
    code=models.DecimalField(max_digits=12, help_text="Не более 12 знаков",decimal_places=0,null=True,verbose_name='Код')   
    slug= models.SlugField(max_length=255, verbose_name='Url',blank=True, null=True)
    unit = models.CharField(max_length=10,verbose_name='Ед.изм.',  choices=UNITS, null=True ,default='kg')
    unit_cost = models.DecimalField(max_digits=10, help_text="Не более 10 знаков",decimal_places=2, null=True)
    order_quantity = models.PositiveIntegerField(null=True)
    status = models.CharField(max_length=10, help_text="Не более 10 знаков", choices=STATUS_CHOICE)
    created_date = models.DateField(auto_now_add=True)


    def get_absolute_url(self):        
        return reverse('order', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['order_number']
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы' 
        
    def __str__(self):
        return str(self.item)
    @property
    def get_order_cost(self):
        return self.unit_cost * self.order_quantity

'''Модель товаров в стадии поставки (на путях)''' 
class DeliverItem(models.Model):
  
    order_item = models.ForeignKey(OrderItem, related_name='order_deliver', on_delete=models.CASCADE, null=True)
    order_number=models.DecimalField(max_digits=10,decimal_places=0,null=True,verbose_name='Номер заказа')
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    code=models.DecimalField(max_digits=12, help_text="Не более 12 знаков",decimal_places=0,null=True,verbose_name='Код')
    product = models.ForeignKey(Item, related_name='item_deliver', on_delete=models.CASCADE)
    slug= models.SlugField(max_length=255, verbose_name='Url',blank=True, null=True)
    unit = models.CharField(max_length=10,verbose_name='Ед.изм.',  choices=UNITS, null=True ,default='kg')
    unit_cost = models.DecimalField(max_digits=10, help_text="Не более 10 знаков",decimal_places=2, null=True)
    order_quantity = models.DecimalField(max_digits=10, help_text="Не более 10 знаков",decimal_places=2, null=True)
    status = models.CharField(max_length=10, help_text="Не более 10 знаков", choices=STATUS_CHOICE)
    created_date = models.DateField(auto_now_add=True)

    def get_absolute_url(self):        
        return reverse('deliver', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['order_number']
        verbose_name = 'На пути'
        verbose_name_plural = 'На путях' 
        
    def __str__(self):
        return str(self.order_item) 
    
    @property
    def get_deliver_cost(self):
        return int(self.unit_cost) * int(self.order_quantity)
