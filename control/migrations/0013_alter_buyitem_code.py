# Generated by Django 4.0.5 on 2022-07-21 14:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0003_alter_recipeingredient_unit'),
        ('control', '0012_buyitem_code_alter_buyitem_unit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buyitem',
            name='code',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='register.item', to_field='code'),
        ),
    ]
