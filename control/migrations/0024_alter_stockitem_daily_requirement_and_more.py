# Generated by Django 4.0.5 on 2022-11-17 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('control', '0023_stockitem_supplier'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stockitem',
            name='daily_requirement',
            field=models.DecimalField(decimal_places=4, default=1, max_digits=10, null=True, verbose_name='Суточная потребность'),
        ),
        migrations.AlterField(
            model_name='stockitem',
            name='fullstock_days',
            field=models.IntegerField(default=3000, null=True, verbose_name='Запас, дней'),
        ),
    ]
