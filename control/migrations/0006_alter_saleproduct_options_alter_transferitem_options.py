# Generated by Django 4.0.5 on 2022-08-24 17:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('control', '0005_alter_buyitem_options_alter_saleproduct_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='saleproduct',
            options={'ordering': ['-date'], 'verbose_name': 'Продажа', 'verbose_name_plural': 'Продажи'},
        ),
        migrations.AlterModelOptions(
            name='transferitem',
            options={'ordering': ['-created_date', 'name'], 'verbose_name': 'Передача', 'verbose_name_plural': 'Передачи'},
        ),
    ]
