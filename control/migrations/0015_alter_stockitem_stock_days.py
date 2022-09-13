# Generated by Django 4.0.5 on 2022-09-06 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('control', '0014_stockitem_delivery_stockitem_delivery_cost_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stockitem',
            name='stock_days',
            field=models.DecimalField(decimal_places=0, help_text='Не более 4 знаков', max_digits=4, null=True, verbose_name='Остаток, дней'),
        ),
    ]
