from django.db import models

# Create your models here.
from django.db import models
from django.urls import reverse


from django.template.defaultfilters import slugify  # new



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


'''Модель IMPEX поставщиков закупаемых товаров'''
class ImpexSupplier(models.Model):
    code=models.DecimalField(max_digits=4, help_text="Не более 4 знаков", decimal_places=0, unique=True)
    name = models.CharField(max_length=200, help_text="Не более 200 знаков",db_index=True)
    slug= models.SlugField(max_length=255, verbose_name='Url', unique=True)
    address = models.CharField(max_length=220)
    created_date = models.DateField(auto_now_add=True)

    def get_absolute_url(self):        
        return reverse('supplier', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['name']
        verbose_name = 'X-Поставщик'
        verbose_name_plural = 'X-Поставщики' 

        
    def __str__(self):
        return self.name  

'''Модель IMPEX категорий закупаемых товаров'''
class ImpexCategoryItem(models.Model):
    code= models.DecimalField(max_digits=5, help_text="Не более 5 цифр", decimal_places=0, unique=True,verbose_name='Код')
    name = models.CharField(max_length=200, help_text="Не более 200 знаков", db_index=True, verbose_name='Категория')
    slug= models.SlugField(max_length=255, verbose_name='Url', unique=True)
    
    def get_absolute_url(self):        
        return reverse('categoryitem', kwargs={'slug': self.slug})
    
    class Meta:
        ordering = ['name']
        verbose_name = 'X-Категория товара'
        verbose_name_plural = 'X-Категории товаров'
        
    def __str__(self):
        return self.name
    
      
        
'''Модель IMPEX закупаемых товаров -РАБОТАЕТ'''
class ImpexItem(models.Model):   
    code=models.DecimalField(max_digits=12, unique=True, help_text="Не более 12 знаков",decimal_places=0,null=True,verbose_name='Код')
    name = models.CharField(max_length=200, help_text="Не более 200 знаков", unique=True,db_index=True)
    category = models.CharField(max_length=200, help_text="Не более 200 знаков",)
    supplier=models.CharField(max_length=200, help_text="Не более 200 знаков",)
    unit = models.CharField(max_length=50, help_text="Не более 50 знаков", choices=UNITS ) # pounds, lbs, oz ,grams, etc
    unit_cost = models.DecimalField(max_digits=10, help_text="Не более 10 знаков",decimal_places=2)
    description = models.TextField(blank=True, null=True)
    available = models.BooleanField(default=True)
    slug= models.SlugField(max_length=255, verbose_name='Url', unique=True)
    created_date= models.DateField(auto_now_add=True, verbose_name='Создан',null=True)
    updated_date = models.DateField(auto_now=True,  verbose_name='Изменен', null=True)
    
    def get_absolute_url(self):        
        return reverse('item', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['category','name']
        verbose_name = 'X-Товар'
        verbose_name_plural = 'X-Товары'
        
    def __str__(self):
        return self.name  
    
    
'''Модель IMPEX ингредиентов для рецептов''' 

class ImpexRecipeIngredient(models.Model): 
    product=models.CharField(max_length=200, help_text="Не более 200 знаков")#related_name='product_name',
    code=models.DecimalField(max_digits=10, help_text="Не более 10 знаков", verbose_name='Код продукта',decimal_places=0, null=True)
    ingredient= models.CharField(max_length=200, help_text="Не более 200 знаков")
    code_ingr= models.DecimalField(max_digits=12, help_text="Не более 12 знаков",decimal_places=0, verbose_name='Код ингредиента', null=True)
    unit = models.CharField(max_length=10, help_text="Не более 10 знаков", default='kg', choices=UNITS, null=True ) 
    unit_cost = models.DecimalField(max_digits=10, help_text="Не более 10 знаков",decimal_places=2, null=True)
    ratio= models.DecimalField(max_digits=10, help_text="Не более 10 знаков",decimal_places=3, default=1, null=True)  
    # slug= models.SlugField(max_length=255, verbose_name='Url', unique=True) 
    created_at= models.DateTimeField(auto_now_add=True, verbose_name='Создан')
    updated_at = models.DateTimeField(auto_now=True,  verbose_name='Изменен') 
    
    def get_absolute_url(self):        
        return reverse('recipeingredient', kwargs={'slug': self.slug})
    
    class Meta:
        ordering = ['product', 'ingredient']
        verbose_name = 'X-Рецепт с ингредиентами'
        verbose_name_plural = 'X-Рецепты с ингредиентами'
    
    @property
    def ingredient_cost(self):
        return format((float(self.unit_cost) * float(self.ratio)), '.2f')    


'''Модель IMPEX категорий готовых продуктов -РАБОТАЕТ'''
class ImpexCategory(models.Model):
    code= models.DecimalField(max_digits=5, help_text="Не более 5 цифр", decimal_places=0, unique=True,verbose_name='Код')
    name = models.CharField(max_length=200, help_text="Не более 200 знаков", db_index=True, verbose_name='Категория')
    slug= models.SlugField(max_length=255, verbose_name='Url', unique=True)

    def get_absolute_url(self):        
        return reverse('category', kwargs={'slug': self.slug})
    
    class Meta:
        ordering = ['name']
        verbose_name = 'X-Категория продукта'
        verbose_name_plural = 'X-Категории продуктов'

    def __str__(self):
        return self.name   
    
    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)     
        
'''Модель IMPEX готовых продуктов -РАБОТАЕТ'''

class ImpexProduct(models.Model):
    DIFFICULTY_LEVELS = (
        ('Easy', 'Easy'),
        ('Medium', 'Medium'),
        ('Hard', 'Hard'),
    )
    code=models.DecimalField(max_digits=10, help_text="Не более 10 знаков", decimal_places=0, null=True,verbose_name='Код')    
    name = models.CharField(max_length=200,help_text="Не более 200 знаков", null=True, verbose_name='Продукт')
    category = models.CharField(max_length=200, null=True, help_text="Не более 200 знаков")
    # category_id = models.CharField(max_length=200, null=True, help_text="Не более 200 знаков")     
    # ingredient = models.CharField(max_length=200,null=True, blank=True, help_text="Не более 200 знаков",)
    difficulty = models.CharField(choices=DIFFICULTY_LEVELS, max_length=10)
    price = models.DecimalField(max_digits=10,help_text="Не более 10 знаков", null=True, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    cooking= models.TextField(blank=True, null = True)
    slug= models.SlugField(max_length=255, verbose_name='Url', null=True)
    created_date= models.DateField(auto_now_add=True, verbose_name='Создан',null=True)
    updated_date = models.DateField(auto_now=True,  verbose_name='Изменен', null=True) 
    
    def get_absolute_url(self):        
        return reverse('product', kwargs={'slug': self.slug})
    
    class Meta:
        ordering = ['category', 'name']
        verbose_name = 'X-Продукт'
        verbose_name_plural = 'X-Продукты'


    def __str__(self):
        return self.name         


'''Модель IMPEX покупок товаров -РАБОТАЕТ''' 

# cost = ('BuyItem'.objects.aggregate(total=Sum(F('unit_cost') * F('quantity'))) 
#     ['cost'])  
class ImpexBuyItem(models.Model):
    code=models.DecimalField(max_digits=12, help_text="Не более 12 знаков",decimal_places=0,null=True,verbose_name='Код')
    # item =models.CharField(max_length=200, help_text="Не более 200 знаков", db_index=True)#отражение в buy_items_list.html
    name = models.CharField(max_length=200, help_text="Не более 200 знаков")# для form buy_item.html
    slug= models.SlugField(max_length=255, verbose_name='Url',blank=True, null=True)
    unit = models.CharField(max_length=10,verbose_name='Ед.изм.',  choices=UNITS, null=True ,default='kg')
    unit_cost=models.PositiveIntegerField(verbose_name='Цена, руб', default=0,null=True)
    quantity= models.PositiveIntegerField(verbose_name='Кол.',default=0)
    cost= models.PositiveIntegerField(verbose_name='Сумма, руб', blank=True,null=True)
    # item_supplier=models.CharField(max_length=200, help_text="Не более 200 знаков", null=True)#отражение в buy_items_list.html
    supplier= models.CharField(max_length=200, help_text="Не более 200 знаков", null=True)
    invoice= models.CharField(max_length=250,verbose_name='Накладная',  null=True ,default='Накладная №     , дата   ')   
    created_date = models.DateField(auto_now_add=True, verbose_name='Дата',)
    # updated_date = models.DateField(auto_now=True,  verbose_name='Изменен', null=True)
    
    def get_absolute_url(self):        
        return reverse('buy', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['name']
        verbose_name = 'X-Закупка'
        verbose_name_plural = 'X-Закупки' 
        
    def __str__(self):
        return str(self.name)  
    @property
    def get_cost(self):
        return self.unit_cost * self.quantity
 
 

'''Модель IMPEX передачи товаров (transfer)''' 
 
class ImpexTransferItem(models.Model):
    code=models.DecimalField(max_digits=12, help_text="Не более 12 знаков",decimal_places=0,null=True,verbose_name='Код')
    item =models.CharField(max_length=200, help_text="Не более 200 знаков", db_index=True)#отражение в transfer_list.html
    name = models.CharField(max_length=200, help_text="Не более 200 знаков")# для form buy_item.html
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
        ordering = ['name']
        verbose_name = 'X-Передача'
        verbose_name_plural = 'X-Передачи' 
        
    def __str__(self):
        return str(self.name)  
    @property
    def get_cost(self):
        return self.unit_cost * self.quantity


'''Модель IMPEX  для списания товаров (waste)''' 
 
class ImpexWasteItem(models.Model):
    code=models.DecimalField(max_digits=12, help_text="Не более 12 знаков",decimal_places=0,null=True,verbose_name='Код')
    item =models.CharField(max_length=200, help_text="Не более 200 знаков", db_index=True)#отражение в transfer_list.html
    name = models.CharField(max_length=200, help_text="Не более 200 знаков")# для form buy_item.html
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
        ordering = ['name']
        verbose_name = 'X-Списание'
        verbose_name_plural = 'X-Списания' 
        
    def __str__(self):
        return str(self.name)  
    @property
    def get_cost(self):
        return self.unit_cost * self.quantity


'''Модель IMPEX продаж продуктов''' 
class ImpexSaleProduct(models.Model):    
    name = models.CharField(max_length=200, help_text="Не более 200 знаков", null=True)
    product=models.CharField(max_length=200, help_text="Не более 200 знаков", null=True, db_index=True)#отражение в sold_product_list.html
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
        verbose_name = 'X-Продажа'
        verbose_name_plural = 'X-Продажи' 
        
    def __str__(self):
        return str(self.code) 
    
    @property
    def get_revenue(self):
        # return format((float(self.price) * float(self.sold)), '.2f')
        return self.price*self.sold
    


'''Модель IMPEX заказа товаров''' 
class ImpexOrderItem(models.Model):    
    order_number = models.CharField(max_length=10, unique=True, help_text="Не более 10 знаков",)
    supplier = models.CharField(max_length=200, help_text="Не более 200 знаков")
    item = models.CharField(max_length=200, help_text="Не более 200 знаков", null=True)
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
        verbose_name = 'X-Заказ'
        verbose_name_plural = 'X-Заказы' 
        
    def __str__(self):
        return str(self.item)
    @property
    def get_order_cost(self):
        return self.unit_cost * self.order_quantity

'''Модель IMPEX товаров в стадии поставки (на путях)''' 
class ImpexDeliverItem(models.Model):
  
    order_item = models.CharField(max_length=200, help_text="Не более 200 знаков", null=True)
    order_number=models.DecimalField(max_digits=10,decimal_places=0,null=True,verbose_name='Номер заказа')
    supplier = models.CharField(max_length=200, help_text="Не более 200 знаков")
    code=models.DecimalField(max_digits=12, help_text="Не более 12 знаков",decimal_places=0,null=True,verbose_name='Код')
    product = models.CharField(max_length=200, help_text="Не более 200 знаков")
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
        verbose_name = 'X-На пути'
        verbose_name_plural = 'X-На путях' 
        
    def __str__(self):
        return str(self.order_item) 
    
    @property
    def get_deliver_cost(self):
        return int(self.unit_cost) * int(self.order_quantity)
