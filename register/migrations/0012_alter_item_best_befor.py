# Generated by Django 4.0.5 on 2022-09-06 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0011_alter_item_pack_height_alter_item_pack_length_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='best_befor',
            field=models.DateField(blank=True, null=True),
        ),
    ]
