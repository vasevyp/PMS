# Generated by Django 4.0.5 on 2022-08-09 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('impex', '0009_alter_impexrecipeingredient_code_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='impexrecipeingredient',
            name='ratio',
            field=models.DecimalField(decimal_places=3, default=1, help_text='Не более 10 знаков', max_digits=10, null=True),
        ),
    ]
