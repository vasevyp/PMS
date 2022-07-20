from django.db import models
from django.urls import reverse

'''Модель поставщиков закупаемых товаров'''
class Supplier(models.Model):
    code=models.DecimalField(max_digits=4, decimal_places=0, unique=True)
    name = models.CharField(max_length=200, db_index=True)
    slug= models.SlugField(max_length=255, verbose_name='Url', unique=True)
    address = models.CharField(max_length=220)
    created_date = models.DateField(auto_now_add=True)

    def get_absolute_url(self):        
        return reverse('supplier', kwargs={'slug': self.slug})

    class Meta:
        ordering = ('name',)
        verbose_name = 'Поставщик'
        verbose_name_plural = 'Поставщики' 
        
    def __str__(self):
        return self.name  

'''Модель категорий закупаемых товаров'''
class CategoryItem(models.Model):
    code= models.DecimalField(max_digits=5, help_text="Не более 5 цифр", decimal_places=0, unique=True,verbose_name='Код')
    name = models.CharField(max_length=200, help_text="Не более 200 знаков", db_index=True, verbose_name='Категория')
    slug= models.SlugField(max_length=255, verbose_name='Url', unique=True)
    
    def get_absolute_url(self):        
        return reverse('categoryitem', kwargs={'slug': self.slug})
    
    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория товара'
        verbose_name_plural = 'Категории товаров'

    def __str__(self):
        return self.name
    
      
        
'''Модель закупаемых товаров'''
class Item(models.Model):
    UNITS=(
        ('kg', 'кг'),
        ('gram', 'г'),
        ('liter', 'л'),
        ('piece',' шт.'),
        ('meter','м'),
        ('m2','м2'),
        ('m3','м3'),
        
    )
    code=models.DecimalField(max_digits=12, decimal_places=0, unique=True, verbose_name='Код товара')
    name = models.CharField(max_length=200, db_index=True)
    category = models.ForeignKey(
        CategoryItem, related_name='item', on_delete=models.CASCADE)
    supplier=models.ForeignKey(Supplier, related_name='item',on_delete=models.CASCADE)
    unit = models.CharField(max_length=50, choices=UNITS ) # pounds, lbs, oz ,grams, etc
    unit_cost = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    available = models.BooleanField(default=True)
    slug= models.SlugField(max_length=255, verbose_name='Url', unique=True)
    
    def get_absolute_url(self):        
        return reverse('item', kwargs={'slug': self.slug})

    class Meta:
        ordering = ('name',)
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name  
    
    
'''Модель ингредиентов для рецептов''' 

class RecipeIngredient(models.Model):
    UNITS=(
        ('kg', 'кг'),
        ('gram', 'г'),
        ('liter', 'л'),
        ('piece',' шт.'),
        ('meter','м'),
        ('m2','м2'),
        ('m3','м3'),
        
    )
    recipe_name=models.ForeignKey('Product', null=True,related_name='product', on_delete=models.CASCADE) 
    ingredient= models.ForeignKey(Item, related_name='recipe_ingredient',  on_delete=models.CASCADE)
    unit = models.CharField(max_length=50, choices=UNITS, null=True ) 
    quantity= models.FloatField(blank=True, null = True)  
    slug= models.SlugField(max_length=255, verbose_name='Url', unique=True)  
    
    def get_absolute_url(self):        
        return reverse('recipeingredient', kwargs={'slug': self.slug})
    
    class Meta:
        ordering = ('recipe_name',)
        verbose_name = 'Рецепт с ингредиентами'
        verbose_name_plural = 'Рецепты с ингредиентами'


'''Модель категорий готовых продуктов'''
class Category(models.Model):
    code= models.DecimalField(max_digits=5, help_text="Не более 5 цифр", decimal_places=0, unique=True,verbose_name='Код')
    name = models.CharField(max_length=200, help_text="Не более 200 знаков", db_index=True, verbose_name='Категория')
    slug= models.SlugField(max_length=255, verbose_name='Url', unique=True)

    def get_absolute_url(self):        
        return reverse('category', kwargs={'slug': self.slug})
    
    class Meta:
        ordering = ('name',)
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
    code=models.DecimalField(max_digits=10, decimal_places=0, unique=True)    
    name = models.CharField(max_length=200, db_index=True, verbose_name='Продукт')
    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE)    
    ingredient = models.ManyToManyField(Item, through=RecipeIngredient)
    difficulty = models.CharField(choices=DIFFICULTY_LEVELS, max_length=10)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    cooking= models.TextField(blank=True, null = True)
    slug= models.SlugField(max_length=255, verbose_name='Url', unique=True)
    
    def get_absolute_url(self):        
        return reverse('product', kwargs={'slug': self.slug})
    
    class Meta:
        ordering = ('code',)
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.name         
