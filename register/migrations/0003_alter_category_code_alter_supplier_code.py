# Generated by Django 4.0.5 on 2022-08-11 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0002_supplier_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='code',
            field=models.CharField(help_text='Не более 5 цифр', max_length=5, unique=True, verbose_name='Код'),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='code',
            field=models.CharField(max_length=4, null=True),
        ),
    ]
