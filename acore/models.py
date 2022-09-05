from django.db import models
from django.urls import reverse


    
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