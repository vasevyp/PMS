from django.db import models
from django.urls import reverse
from control.models import STATUS_CHOICE


    
'''
Модель временная, данные будут перенесены в StockItem'''
class StockForecastDays(models.Model):
    code=models.DecimalField(max_digits=12, help_text="Не более 12 знаков",decimal_places=0,null=True,verbose_name='Код')
    name = models.CharField(max_length=200, help_text="Не более 200 знаков", db_index=True)
    slug= models.SlugField(max_length=255, verbose_name='Url')
    unit = models.CharField(max_length=10,verbose_name='Ед.изм.',  null=True ,default='kg')
    unit_cost = models.DecimalField(max_digits=10, help_text="Не более 10 знаков",decimal_places=2, null=True)
    actual=models.DecimalField(max_digits=10, help_text="Не более 10 знаков", decimal_places=0, default=0)
    actual_cost=models.DecimalField(max_digits=12, help_text="Не более 12 знаков", decimal_places=2, default=0)
    daily_requirement= models.DecimalField(verbose_name='Суточная потребность', null=True, max_digits=10, decimal_places=4)
    stock_days=models.DecimalField(max_digits=4, help_text="Не более 4 знаков", decimal_places=0)
    	
     
    def get_absolute_url(self):        
        return reverse('stock', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['name']
        verbose_name = 'Остаток в днях'
        verbose_name_plural = 'Остатки в днях'
        
        
    def __str__(self):
        return str(self.name)  
    
'''
Модель временная, данные будут перенесены в StockItem
'''
class FullStock(models.Model):
    code=models.DecimalField(max_digits=12, help_text="Не более 12 знаков",decimal_places=0,null=True,verbose_name='Код')
    name = models.CharField(max_length=200, help_text="Не более 200 знаков", db_index=True)
    slug= models.SlugField(max_length=255, verbose_name='Url')
    unit = models.CharField(max_length=10,verbose_name='Ед.изм.',  null=True ,default='kg')
    unit_cost = models.DecimalField(max_digits=10, help_text="Не более 10 знаков",decimal_places=2, null=True)
    actual=models.DecimalField(max_digits=10, help_text="Не более 10 знаков", decimal_places=0, default=0)    
    delivery=models.DecimalField(max_digits=10, help_text="Не более 10 знаков", decimal_places=0, default=0)
    fullstock=models.DecimalField(max_digits=10, help_text="Не более 10 знаков", decimal_places=0, default=0)
    full_cost=models.DecimalField(max_digits=12, help_text="Не более 12 знаков", decimal_places=2, default=0)
    daily_requirement= models.DecimalField(verbose_name='Суточная потребность', null=True, max_digits=10, decimal_places=4)
    fullstock_days=models.DecimalField(max_digits=4, help_text="Не более 4 знаков", decimal_places=0)
    
'''
Модель рассчета позиций товаров, которые необходимо заказать сегодня, в день рассчета
'''    
class ToOrder(models.Model):
    code=models.DecimalField(max_digits=12, help_text="Не более 12 знаков",decimal_places=0,null=True,verbose_name='Код')
    name = models.CharField(max_length=200, help_text="Не более 200 знаков", db_index=True)
    supplier=models.CharField(max_length=200, help_text="Не более 200 знаков", null=True)
    supply_pack = models.IntegerField(verbose_name='Упаковка, ед.', null=True, default=1)
    delivery_time = models.IntegerField(verbose_name='Буфер, дней', null=True, default=5) #from Item -- Это буфер для товарной позиции
    fullstock_days=models.IntegerField( null=True,verbose_name='Запас, дней', default=0)
    daily_requirement= models.DecimalField(verbose_name='Суточная потребность', null=True, max_digits=10, decimal_places=4)
    to_order= models.IntegerField(verbose_name='Заказать, ед.')
    unit_cost = models.DecimalField(max_digits=10, help_text="Не более 10 знаков",decimal_places=2, null=True)
    to_orders= models.DecimalField(max_digits=10, help_text="Не более 10 знаков",verbose_name='Заказать, руб.', decimal_places=2, null=True)
    order_sum=models.DecimalField(max_digits=10, help_text="Не более 10 знаков",decimal_places=2, null=True)
    status = models.CharField(max_length=10, help_text="Не более 10 знаков", choices=STATUS_CHOICE)
    
    @property
    def toorders(self):        
        return float(self.unit_cost)*float(self.to_order)
    
    def get_absolute_url(self):        
        return reverse('to_order', kwargs={'name': self.name})

    class Meta:
        ordering = ['name']
        verbose_name = 'Заказать'
        verbose_name_plural = 'Заказать'
        
        
    def __str__(self):
        return str(self.name)  

'''
Модель рассчета позиций товаров, которые необходимо заказать через 3 дня от дня рассчета
'''

class ToOrder_3(models.Model):
    code=models.DecimalField(max_digits=12, help_text="Не более 12 знаков",decimal_places=0,null=True,verbose_name='Код')
    name = models.CharField(max_length=200, help_text="Не более 200 знаков", db_index=True)
    supplier=models.CharField(max_length=200, help_text="Не более 200 знаков", null=True)
    supply_pack = models.IntegerField(verbose_name='Упаковка, ед.', null=True, default=1)
    delivery_time = models.IntegerField(verbose_name='Буфер, дней', null=True, default=5) #from Item -- Это буфер для товарной позиции
    fullstock_days=models.IntegerField( null=True,verbose_name='Запас, дней', default=0)
    daily_requirement= models.DecimalField(verbose_name='Суточная потребность', null=True, max_digits=10, decimal_places=4)
    to_order= models.IntegerField(verbose_name='Заказать, ед.')
    unit_cost = models.DecimalField(max_digits=10, help_text="Не более 10 знаков",decimal_places=2, null=True)
    to_orders= models.DecimalField(max_digits=10, help_text="Не более 10 знаков",verbose_name='Заказать, руб.', decimal_places=2, null=True)
    order_sum=models.DecimalField(max_digits=10, help_text="Не более 10 знаков",decimal_places=2, null=True)
    status = models.CharField(max_length=10, help_text="Не более 10 знаков", choices=STATUS_CHOICE)
    
    @property
    def toorders(self):        
        return float(self.unit_cost)*float(self.to_order)
    
    def get_absolute_url(self):        
        return reverse('to_order', kwargs={'name': self.name})

    class Meta:
        ordering = ['name']
        verbose_name = 'Заказать - 3 дня'
        verbose_name_plural = 'Заказать - 3 дня'
        
        
    def __str__(self):
         return str(self.name)  
        
        
'''
Модель для подготовки бланка передачи Заказ "Сегодня" 
'''        
class Order(models.Model):
    code=models.DecimalField(max_digits=12, help_text="Не более 12 знаков",decimal_places=0,null=True,verbose_name='Код')
    name = models.CharField(max_length=200, help_text="Не более 200 знаков", db_index=True)
    order_number = models.CharField(max_length=10, help_text="Не более 10 знаков",)
    order= models.IntegerField(verbose_name='Заказ, ед.') 
    order_cost=models.DecimalField(max_digits=10, help_text="Не более 10 знаков",decimal_places=2, null=True)
    supply_pack = models.IntegerField(verbose_name='Упаковка, ед.', null=True, default=1)
    supplier=models.CharField(max_length=200, help_text="Не более 200 знаков", null=True)    
    delivery_date = models.DateField(verbose_name='Дата поставки')
    created_date = models.DateField(auto_now_add=True)
    
    def get_absolute_url(self):        
        return reverse('order', kwargs={'name': self.name})

    class Meta:
        ordering = ['-supplier','name']
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказ'
        
        
    def __str__(self):
         return str(self.name)
     

       
'''
Модель последнего Заказ "Сегодня" 
'''        
class LastOrder(models.Model):
    code=models.DecimalField(max_digits=12, help_text="Не более 12 знаков",decimal_places=0,null=True,verbose_name='Код')
    name = models.CharField(max_length=200, help_text="Не более 200 знаков", db_index=True)
    order_number = models.CharField(max_length=10, help_text="Не более 10 знаков",)
    order= models.IntegerField(verbose_name='Заказ, ед.') 
    order_cost=models.DecimalField(max_digits=10, help_text="Не более 10 знаков",decimal_places=2, null=True)
    supplier=models.CharField(max_length=200, help_text="Не более 200 знаков", null=True)    
    delivery_date = models.DateField(verbose_name='Дата поставки')
    created_date = models.DateField(auto_now_add=True)
    
    def get_absolute_url(self):        
        return reverse('order', kwargs={'name': self.name})

    class Meta:
        ordering = ['-supplier','name']
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказ'
        
        
    def __str__(self):
         return str(self.name) 

'''
Модель для списка Заказов "Сегодня" 
'''        
class OrderList(models.Model):
    code=models.DecimalField(max_digits=12, help_text="Не более 12 знаков",decimal_places=0,null=True,verbose_name='Код')
    name = models.CharField(max_length=200, help_text="Не более 200 знаков", db_index=True)
    order_number = models.CharField(max_length=10, help_text="Не более 10 знаков",)
    order= models.IntegerField(verbose_name='Заказ, ед.') 
    order_cost=models.DecimalField(max_digits=10, help_text="Не более 10 знаков",decimal_places=2, null=True)
    supplier=models.CharField(max_length=200, help_text="Не более 200 знаков", null=True)    
    delivery_date = models.DateField(verbose_name='Дата поставки')
    created_date = models.DateField(auto_now_add=True)
    
    def get_absolute_url(self):        
        return reverse('order', kwargs={'name': self.name})

    class Meta:
        ordering = ['-order_number','-supplier']
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказ'
        
        
    def __str__(self):
         return str(self.name) 
