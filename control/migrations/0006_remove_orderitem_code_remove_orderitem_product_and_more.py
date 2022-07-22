# Generated by Django 4.0.5 on 2022-07-20 16:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0003_alter_recipeingredient_unit'),
        ('control', '0005_alter_buyitem_cost'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='code',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='product',
        ),
        migrations.AddField(
            model_name='orderitem',
            name='item',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='item_order', to='register.item'),
        ),
    ]
