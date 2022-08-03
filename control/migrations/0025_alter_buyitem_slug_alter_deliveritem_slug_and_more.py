# Generated by Django 4.0.5 on 2022-08-01 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('control', '0024_alter_buyitem_options_alter_deliveritem_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buyitem',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, null=True, verbose_name='Url'),
        ),
        migrations.AlterField(
            model_name='deliveritem',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, null=True, verbose_name='Url'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, null=True, verbose_name='Url'),
        ),
    ]
