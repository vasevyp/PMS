# Generated by Django 4.0.5 on 2022-07-20 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0002_remove_recipeingredient_slug_alter_item_code_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipeingredient',
            name='unit',
            field=models.CharField(choices=[('kg', 'кг'), ('gram', 'г'), ('liter', 'л'), ('piece', ' шт.'), ('meter', 'м'), ('m2', 'м2'), ('m3', 'м3')], default='gram', help_text='Не более 10 знаков', max_length=10, null=True),
        ),
    ]
