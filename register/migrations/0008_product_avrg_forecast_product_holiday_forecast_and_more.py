# Generated by Django 4.0.5 on 2022-08-23 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0007_alter_item_lot_height_alter_item_lot_length_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='avrg_forecast',
            field=models.PositiveIntegerField(editable=False, null=True, verbose_name='Суточные'),
        ),
        migrations.AddField(
            model_name='product',
            name='holiday_forecast',
            field=models.PositiveIntegerField(null=True, verbose_name='Праздники'),
        ),
        migrations.AddField(
            model_name='product',
            name='promotion_forecast',
            field=models.PositiveIntegerField(null=True, verbose_name='Промо'),
        ),
        migrations.AddField(
            model_name='product',
            name='weekday_forecast',
            field=models.PositiveIntegerField(null=True, verbose_name='Будни'),
        ),
        migrations.AddField(
            model_name='product',
            name='weekend_forecast',
            field=models.PositiveIntegerField(null=True, verbose_name='Выходные'),
        ),
    ]
