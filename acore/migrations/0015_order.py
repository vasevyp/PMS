# Generated by Django 4.0.5 on 2022-10-24 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acore', '0014_toorder_supplier_toorder_3_supplier'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.DecimalField(decimal_places=0, help_text='Не более 12 знаков', max_digits=12, null=True, verbose_name='Код')),
                ('name', models.CharField(db_index=True, help_text='Не более 200 знаков', max_length=200)),
                ('order_number', models.CharField(help_text='Не более 10 знаков', max_length=10, unique=True)),
                ('order', models.IntegerField(verbose_name='Заказ, ед.')),
                ('order_cost', models.DecimalField(decimal_places=2, help_text='Не более 10 знаков', max_digits=10, null=True)),
                ('supply_pack', models.IntegerField(default=1, null=True, verbose_name='Упаковка, ед.')),
                ('supplier', models.CharField(help_text='Не более 200 знаков', max_length=200, null=True)),
                ('delivery_time', models.DateField(verbose_name='Дата поставки')),
                ('created_date', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказ',
                'ordering': ['supplier', 'name'],
            },
        ),
    ]
