# Generated by Django 4.0.5 on 2022-07-20 08:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('register', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StockItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='Url')),
                ('open', models.DecimalField(decimal_places=0, max_digits=10)),
                ('sales', models.DecimalField(decimal_places=0, max_digits=10)),
                ('received', models.DecimalField(decimal_places=0, max_digits=10)),
                ('transfer', models.DecimalField(decimal_places=0, max_digits=10)),
                ('move', models.DecimalField(decimal_places=0, max_digits=10)),
                ('waste', models.DecimalField(decimal_places=0, max_digits=10)),
                ('actual', models.DecimalField(decimal_places=0, max_digits=10)),
                ('actual_cost', models.DecimalField(decimal_places=2, max_digits=12)),
                ('code', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='code_stock', to='register.item')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='name_stock', to='register.item')),
                ('unit', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='unit_stock', to='register.item')),
                ('unit_cost', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='unit_cost_stock', to='register.item')),
            ],
            options={
                'verbose_name': 'Остаток',
                'verbose_name_plural': 'Остатки',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='SaleProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='Url')),
                ('quantity', models.DecimalField(decimal_places=2, max_digits=10)),
                ('revenue', models.DecimalField(decimal_places=2, max_digits=10)),
                ('created_date', models.DateField(auto_now_add=True)),
                ('code', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='code_sale', to='register.product')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='name_sale', to='register.product')),
                ('price', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='price_sale', to='register.product')),
            ],
            options={
                'verbose_name': 'Продажа',
                'verbose_name_plural': 'Продажи',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_number', models.CharField(max_length=10)),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='Url')),
                ('order_quantity', models.PositiveIntegerField(null=True)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('decline', 'Decline'), ('approved', 'Approved'), ('processing', 'Processing'), ('complete', 'Complete'), ('bulk', 'Bulk')], max_length=10)),
                ('created_date', models.DateField(auto_now_add=True)),
                ('code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='code_order', to='register.product')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_order', to='register.product')),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='register.supplier')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
                'ordering': ('order_number',),
            },
        ),
        migrations.CreateModel(
            name='DeliverItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='Url')),
                ('order_quantity', models.PositiveIntegerField(null=True)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('decline', 'Decline'), ('approved', 'Approved'), ('processing', 'Processing'), ('complete', 'Complete'), ('bulk', 'Bulk')], max_length=10)),
                ('created_date', models.DateField(auto_now_add=True)),
                ('code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='code_deliver', to='register.product')),
                ('order_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_deliver', to='control.orderitem')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_deliver', to='register.product')),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='register.supplier')),
            ],
            options={
                'verbose_name': 'На пути',
                'verbose_name_plural': 'На путях',
                'ordering': ('order_number',),
            },
        ),
        migrations.CreateModel(
            name='BuyItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='Url')),
                ('quantity', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('created_date', models.DateField(auto_now_add=True)),
                ('code', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='code_buy', to='register.item')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='name_buy', to='register.item')),
                ('unit', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='unit_buy', to='register.item')),
                ('unit_cost', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='unit_cost_buy', to='register.item')),
            ],
            options={
                'verbose_name': 'Закупка',
                'verbose_name_plural': 'Закупки',
                'ordering': ('name',),
            },
        ),
    ]
