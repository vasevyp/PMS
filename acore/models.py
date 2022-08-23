from django.db import models
from django.urls import reverse

from register.models import Product, Category

'''
Модель для фактических продаж по дням
'''    
class Sales(models.Model):
    name= models.CharField(max_length=250, verbose_name='Наименование', null=True, help_text="Не более 250 знаков")
    quantity= models.PositiveIntegerField(verbose_name='Кол')
    date= models.DateField( verbose_name='Дата', help_text="'2022-08-18")
    created_date= models.DateField(auto_now_add=True, verbose_name='Создан',null=True)
    

    def get_absolute_url(self):        
        return reverse('sellforecast', kwargs={'name': self.name})
    
    class Meta:
        ordering = ['name']
        verbose_name = 'Продаж'
        verbose_name_plural = 'Продажи'

    def __str__(self):
        return str(self.name) 

'''
Модель для прогноза продаж за день. Для получения суточной потребности в товарах/ингредиентах для обеспечения продаж.
'''
class SellForecast(models.Model):
    name=models.ForeignKey(Product, verbose_name='Продукт',on_delete=models.CASCADE)
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE)
    weekday_forecast=models.PositiveIntegerField(verbose_name='Будни')
    weekend_forecast=models.PositiveIntegerField(verbose_name='Выходные')
    avrg_forecast= models.PositiveIntegerField(editable=False, verbose_name='Суточные')
    holiday_forecast=models.PositiveIntegerField(verbose_name='Праздники')
    promotion_forecast=models.PositiveIntegerField(verbose_name='Промо')
    created_date= models.DateField(auto_now_add=True, verbose_name='Создан',null=True)
    updated_date = models.DateField(auto_now=True,  verbose_name='Изменен', null=True)
    
    def save(self, *args, **kwargs):
        avrg_forecast = (self.weekday_forecast*5 + self.weekend_forecast*2)/7
        super(SellForecast, self).save(*args, **kwargs)
    
    def get_absolute_url(self):        
        return reverse('sellforecast', kwargs={'name': self.name})
    
    class Meta:
        ordering = ['name']
        verbose_name = 'Прогноз продаж'
        verbose_name_plural = 'Прогнозы продаж'

    def __str__(self):
        return str(self.name) 
    

class DailyRequirement(models.Model):
    product=models.CharField(max_length=200, verbose_name='Продукт')#related_name='product_name',
    code=models.DecimalField(max_digits=10, help_text="Не более 10 знаков", verbose_name='Код продукта',decimal_places=0, null=True)
    avrg_forecast= models.PositiveIntegerField(verbose_name='Суточный прогноз')
    ingredient= models.CharField(max_length=200, verbose_name='Ингредиент')
    code_ingr= models.DecimalField(max_digits=12, help_text="Не более 12 знаков",decimal_places=0, verbose_name='Код ингредиента', null=True)
    ratio= models.DecimalField(max_digits=10, help_text="Не более 10 знаков",decimal_places=4, default=1, null=True)  
    daily_requirement= models.DecimalField(verbose_name='Суточная потребность', null=True, max_digits=10, decimal_places=4)
    created_at= models.DateTimeField(auto_now_add=True, verbose_name='Создан')
    updated_at = models.DateTimeField(auto_now=True,  verbose_name='Изменен')
    
    def save(self, *args, **kwargs):
        daily_requirement = (self.avrg_forecast* self.ratio)
        super(DailyRequirement, self).save(*args, **kwargs)
    
    def get_absolute_url(self):        
        return reverse('dailyrequirement', kwargs={'product': self.product})
    
    class Meta:
        ordering = ['product']
        verbose_name = 'Суточная потребность'
        verbose_name_plural = 'Суточная потребность'

    def __str__(self):
        return str(self.product) 
    

