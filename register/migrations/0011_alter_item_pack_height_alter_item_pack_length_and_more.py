# Generated by Django 4.0.5 on 2022-09-06 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0010_rename_lot_height_item_pack_height_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='pack_height',
            field=models.FloatField(blank=True, null=True, verbose_name='высота упаковки'),
        ),
        migrations.AlterField(
            model_name='item',
            name='pack_length',
            field=models.FloatField(blank=True, null=True, verbose_name='длина упаковки'),
        ),
        migrations.AlterField(
            model_name='item',
            name='pack_weight',
            field=models.FloatField(blank=True, null=True, verbose_name='вес упаковки'),
        ),
        migrations.AlterField(
            model_name='item',
            name='pack_width',
            field=models.FloatField(blank=True, null=True, verbose_name='ширина упаковки'),
        ),
        migrations.AlterField(
            model_name='item',
            name='supply_pack',
            field=models.IntegerField(null=True, verbose_name='Упаковка, ед.'),
        ),
    ]
