# Generated by Django 4.0.5 on 2022-07-23 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0003_alter_recipeingredient_unit'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipeingredient',
            name='unit_cost',
            field=models.DecimalField(decimal_places=2, help_text='Не более 10 знаков', max_digits=10, null=True),
        ),
    ]
