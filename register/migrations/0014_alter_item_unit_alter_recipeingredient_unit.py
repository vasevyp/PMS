# Generated by Django 4.0.5 on 2022-07-29 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0013_alter_category_options_alter_categoryitem_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='unit',
            field=models.CharField(choices=[(None, 'Выбрать ед.изм.'), ('кг', 'кг'), ('л', 'л'), ('шт.', ' шт.')], help_text='Не более 50 знаков', max_length=50),
        ),
        migrations.AlterField(
            model_name='recipeingredient',
            name='unit',
            field=models.CharField(choices=[(None, 'Выбрать ед.изм.'), ('кг', 'кг'), ('л', 'л'), ('шт.', ' шт.')], default='kg', help_text='Не более 10 знаков', max_length=10, null=True),
        ),
    ]
