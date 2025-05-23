# Generated by Django 4.0.5 on 2022-09-07 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('control', '0017_alter_stockitem_daily_requirement'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stockitem',
            name='delivery_time',
            field=models.IntegerField(default=5, null=True, verbose_name='Буфер, дней'),
        ),
        migrations.AlterField(
            model_name='stockitem',
            name='fullstock_days',
            field=models.DecimalField(decimal_places=0, default=0, help_text='Не более 4 знаков', max_digits=4, null=True, verbose_name='Запас, дней'),
        ),
    ]
