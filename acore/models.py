from django.db import models
from django.urls import reverse

    

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
    

