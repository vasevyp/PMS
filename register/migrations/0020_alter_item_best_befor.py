# Generated by Django 4.0.5 on 2022-11-07 17:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0019_alter_item_best_befor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='best_befor',
            field=models.DateField(blank=True, default=datetime.date(2022, 12, 7), null=True),
        ),
    ]
