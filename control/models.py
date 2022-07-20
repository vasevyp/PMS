from django.db import models
from django.urls import reverse
from register.models import Item, Product, Supplier

'''Модель покупок товаров''' 
class BuyItem(models.Model):
    code=models.ForeignKey(Item, related_name='code_buy', on_delete=models.PROTECT)
    name = models.ForeignKey(Item,related_name='name_buy', on_delete=models.PROTECT)
    slug= models.SlugField(max_length=255, verbose_name='Url', unique=True)
    unit= models.ForeignKey(Item, related_name='unit_buy', on_delete=models.PROTECT)
    unit_cost=models.ForeignKey(Item, related_name='unit_cost_buy', on_delete=models.PROTECT)
    quantity= models.DecimalField(max_digits=10, decimal_places=2)
    cost= models.DecimalField(max_digits=10, decimal_places=2)
    created_date = models.DateField(auto_now_add=True)

    def get_absolute_url(self):        
        return reverse('buy', kwargs={'slug': self.slug})

    class Meta:
        ordering = ('name',)
        verbose_name = 'Закупка'
        verbose_name_plural = 'Закупки' 
        
    def __str__(self):
        return self.name  

'''Модель склада товаров'''
class StockItem(models.Model):
    code=models.ForeignKey(Item, related_name='code_stock', on_delete=models.PROTECT)
    name = models.ForeignKey(Item,related_name='name_stock', on_delete=models.PROTECT)
    slug= models.SlugField(max_length=255, verbose_name='Url', unique=True)
    unit= models.ForeignKey(Item, related_name='unit_stock', on_delete=models.PROTECT)
    unit_cost=models.ForeignKey(Item, related_name='unit_cost_stock', on_delete=models.PROTECT)
    open=models.DecimalField(max_digits=10, decimal_places=0)
    sales =	models.DecimalField(max_digits=10, decimal_places=0)
    received = models.DecimalField(max_digits=10, decimal_places=0)
    transfer =models.DecimalField(max_digits=10, decimal_places=0)
    move =models.DecimalField(max_digits=10, decimal_places=0)
    waste=models.DecimalField(max_digits=10, decimal_places=0)
    actual=models.DecimalField(max_digits=10, decimal_places=0)
    actual_cost=models.DecimalField(max_digits=12, decimal_places=2)	

    def get_absolute_url(self):        
        return reverse('stock', kwargs={'slug': self.slug})

    class Meta:
        ordering = ('name',)
        verbose_name = 'Остаток'
        verbose_name_plural = 'Остатки' 
        
    def __str__(self):
        return self.name  


'''Модель продаж продуктов''' 
class SaleProduct(models.Model):
    code=models.ForeignKey(Product, related_name='code_sale', on_delete=models.PROTECT)
    name = models.ForeignKey(Product,related_name='name_sale', on_delete=models.PROTECT)
    slug= models.SlugField(max_length=255, verbose_name='Url', unique=True)
    # unit= models.ForeignKey(Product, related_name='unit_buy', on_delete=models.PROTECT)
    price=models.ForeignKey(Product, related_name='price_sale', on_delete=models.PROTECT)
    quantity= models.DecimalField(max_digits=10, decimal_places=2)
    revenue= models.DecimalField(max_digits=10, decimal_places=2)
    created_date = models.DateField(auto_now_add=True)
    

    def get_absolute_url(self):        
        return reverse('sale', kwargs={'slug': self.slug})

    class Meta:
        ordering = ('name',)
        verbose_name = 'Продажа'
        verbose_name_plural = 'Продажи' 
        
    def __str__(self):
        return self.name  


'''Модель заказа товаров''' 
class OrderItem(models.Model):
    STATUS_CHOICE = (
        ('pending', 'Pending'),
        ('decline', 'Decline'),
        ('approved', 'Approved'),
        ('processing', 'Processing'),
        ('complete', 'Complete'),
        ('bulk', 'Bulk'),
    )
    order_number = models.CharField(max_length=10)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    code=models.ForeignKey(Product, related_name='code_order',on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='product_order', on_delete=models.CASCADE)
    slug= models.SlugField(max_length=255, verbose_name='Url', unique=True)
    order_quantity = models.PositiveIntegerField(null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICE)
    created_date = models.DateField(auto_now_add=True)


    def get_absolute_url(self):        
        return reverse('order', kwargs={'slug': self.slug})

    class Meta:
        ordering = ('order_number',)
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы' 
        
    def __str__(self):
        return self.product  

'''Модель товаров в стадии поставки (на путях)''' 
class DeliverItem(models.Model):
    STATUS_CHOICE = (
        ('pending', 'Pending'),
        ('decline', 'Decline'),
        ('approved', 'Approved'),
        ('processing', 'Processing'),
        ('complete', 'Complete'),
        ('bulk', 'Bulk'),
    )
    order_number = models.ForeignKey(OrderItem, related_name='order_deliver', on_delete=models.CASCADE)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    code=models.ForeignKey(Product, related_name='code_deliver',on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='product_deliver', on_delete=models.CASCADE)
    slug= models.SlugField(max_length=255, verbose_name='Url', unique=True)
    order_quantity = models.PositiveIntegerField(null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICE)
    created_date = models.DateField(auto_now_add=True)

    def get_absolute_url(self):        
        return reverse('deliver', kwargs={'slug': self.slug})

    class Meta:
        ordering = ('order_number',)
        verbose_name = 'На пути'
        verbose_name_plural = 'На путях' 
        
    def __str__(self):
        return self.product 
