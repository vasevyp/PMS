from django.db import models
from django.urls import reverse
from datetime import timedelta, date

# from django.db.models.functions import Upper
# from django.db.models.indexes import Index

from django.template.defaultfilters import slugify  # new


UNITS=(
        (None, 'Выбрать ед.изм.'),
        ('кг', 'кг'),      
        ('л', 'л'),
        ('шт.',' шт.'),
        
    )

'''Модель поставщиков закупаемых товаров'''
class Supplier(models.Model):
    code=models.CharField(max_length=4, null=True)
    name = models.CharField(max_length=200, help_text="Не более 200 знаков",db_index=True)
    slug= models.SlugField(max_length=255, verbose_name='Url', unique=True)
    address = models.CharField(max_length=220)
    contact=models.CharField(max_length=250, null=True)
    created_date = models.DateField(auto_now_add=True)

    def get_absolute_url(self):        
        return reverse('supplier', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['name']
        verbose_name = 'Поставщик'
        verbose_name_plural = 'Поставщики'              
        
    def __str__(self):
        return self.name  

'''Модель категорий закупаемых товаров'''
class CategoryItem(models.Model):
    code= models.DecimalField(max_digits=5, help_text="Не более 5 цифр", decimal_places=0, unique=True,verbose_name='Код')
    name = models.CharField(max_length=200, help_text="Не более 200 знаков", db_index=True, verbose_name='Категория')
    slug= models.SlugField(max_length=255, verbose_name='Url', unique=True)
    created_date= models.DateField(auto_now_add=True, verbose_name='Создан',null=True)
    updated_date = models.DateField(auto_now=True,  verbose_name='Изменен', null=True) 
    
    def get_absolute_url(self):        
        return reverse('categoryitem', kwargs={'slug': self.slug})
    
    class Meta:
        ordering = ['name']
        verbose_name = 'Категория товара'
        verbose_name_plural = 'Категории товаров'

    def __str__(self):
        return self.name
    
        
'''Модель закупаемых товаров'''
class Item(models.Model):   
    code=models.DecimalField(max_digits=12, unique=True, help_text="Не более 12 знаков",decimal_places=0,null=True,verbose_name='Код')
    name = models.CharField(max_length=200, help_text="Не более 200 знаков", unique=True,db_index=True)
    category = models.ForeignKey(
        CategoryItem, related_name='item', on_delete=models.CASCADE)
    supplier=models.ForeignKey(Supplier, related_name='item',on_delete=models.CASCADE)
    unit = models.CharField(max_length=50, help_text="Не более 50 знаков", choices=UNITS ) # pounds, lbs, oz ,grams, etc
    unit_cost = models.DecimalField(max_digits=10, help_text="Не более 10 знаков",decimal_places=2)
    description = models.TextField(blank=True, null=True)
    # available = models.BooleanField(default=True)
    slug= models.SlugField(max_length=255, verbose_name='Url', unique=True)
    delivery_time = models.IntegerField(verbose_name='Дней', null=True)
    supply_pack = models.IntegerField(verbose_name='Упаковка, ед.', null=True, default=1)
    pack_weight= models.FloatField(verbose_name='вес упаковки', blank=True, null=True)
    pack_length=models.FloatField(verbose_name='длина упаковки', blank=True, null=True)
    pack_width = models.FloatField(verbose_name='ширина упаковки', blank=True, null=True)
    pack_height = models.FloatField(verbose_name='высота упаковки', blank=True, null=True)
    best_befor = models.DateField(blank=True, null=True, default=date.today()+timedelta(days=30))
    created_date= models.DateField(auto_now_add=True, verbose_name='Создан',null=True)
    updated_date = models.DateField(auto_now=True,  verbose_name='Изменен', null=True)
    
    def get_absolute_url(self):        
        return reverse('item', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['category','name']
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        

    def __str__(self):
        return self.name  
    
    
'''Модель ингредиентов для рецептов''' 

class RecipeIngredient(models.Model): 
    product=models.ForeignKey('Product', null=True, verbose_name='Рецепт на Продукт',  on_delete=models.CASCADE)#related_name='product_name',
    code=models.DecimalField(max_digits=10, help_text="Не более 10 знаков", verbose_name='Код продукта',decimal_places=0, null=True)
    ingredient= models.ForeignKey(Item, related_name='recipe_ingredient',  on_delete=models.CASCADE)
    code_ingr= models.DecimalField(max_digits=12, help_text="Не более 12 знаков",decimal_places=0, verbose_name='Код ингредиента', null=True)
    unit = models.CharField(max_length=10, help_text="Не более 10 знаков", default='kg', choices=UNITS, null=True ) 
    unit_cost = models.DecimalField(max_digits=10, help_text="Не более 10 знаков",decimal_places=2, null=True)
    ratio= models.DecimalField(max_digits=10, help_text="Не более 10 знаков",decimal_places=3, default=1, null=True) 
    ingredient_cost=models.DecimalField(max_digits=10, help_text="Не более 10 знаков",decimal_places=2, null=True) 
    created_at= models.DateTimeField(auto_now_add=True, verbose_name='Создан')
    updated_at = models.DateTimeField(auto_now=True,  verbose_name='Изменен') 
    
    def get_absolute_url(self):        
        return reverse('recipeingredient', kwargs={'code': self.code})
    
    class Meta:
        ordering = ['product', 'ingredient']
        verbose_name = 'Рецепт с ингредиентами'
        verbose_name_plural = 'Рецепты с ингредиентами'
    
    # @property
    # def ingredient_cost22(self):
    #     return format((float(self.unit_cost) * float(self.ratio)), '.2f')    


'''Модель категорий готовых продуктов'''
class Category(models.Model):
    code= models.CharField(max_length=5, help_text="Не более 5 цифр",  unique=True,verbose_name='Код')
    name = models.CharField(max_length=200, help_text="Не более 200 знаков", db_index=True, verbose_name='Категория')
    slug= models.SlugField(max_length=255, verbose_name='Url', unique=True)
    created_date= models.DateField(auto_now_add=True, verbose_name='Создан',null=True)
    updated_date = models.DateField(auto_now=True,  verbose_name='Изменен', null=True) 

    def get_absolute_url(self):        
        return reverse('category', kwargs={'slug': self.slug})
    
    class Meta:
        ordering = ['name']
        verbose_name = 'Категория продукта'
        verbose_name_plural = 'Категории продуктов'

    def __str__(self):
        return self.name       
        
'''Модель готовых продуктов'''

class Product(models.Model):
    DIFFICULTY_LEVELS = (
        ('Easy', 'Easy'),
        ('Medium', 'Medium'),
        ('Hard', 'Hard'),
    )
    code=models.DecimalField(max_digits=10, help_text="Не более 10 знаков", decimal_places=0, unique=True)    
    name = models.CharField(max_length=200,help_text="Не более 200 знаков", db_index=True, verbose_name='Продукт')
    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE)    
    ingredient = models.ManyToManyField(Item, through=RecipeIngredient)
    difficulty = models.CharField(choices=DIFFICULTY_LEVELS, max_length=10)
    price = models.DecimalField(max_digits=10,help_text="Не более 10 знаков", decimal_places=2)
    description = models.TextField(blank=True, null=True)
    cooking= models.TextField(blank=True, null = True)
    slug= models.SlugField(max_length=255, verbose_name='Url', unique=True)
    weekday_forecast=models.PositiveIntegerField(verbose_name='Будни', null = True)
    weekend_forecast=models.PositiveIntegerField(verbose_name='Выходные', null = True)
    avrg_forecast= models.PositiveIntegerField(editable=False, verbose_name='Суточные', default=1, null = True)
    holiday_forecast=models.PositiveIntegerField(verbose_name='Праздники', null = True)
    promotion_forecast=models.PositiveIntegerField(verbose_name='Промо', null = True)
    created_date= models.DateField(auto_now_add=True, verbose_name='Создан',null=True)
    updated_date = models.DateField(auto_now=True,  verbose_name='Изменен', null=True) 
    
    def save(self, *args, **kwargs):
        avrg_forecast = (int(self.weekday_forecast)*5 + int(self.weekend_forecast)*2)/7
        super(Product, self).save(*args, **kwargs)
    
    
    def get_absolute_url(self):        
        return reverse('product', kwargs={'slug': self.slug})
    
    class Meta:
        ordering = ['category', 'name']
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.name         



