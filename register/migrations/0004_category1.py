# Generated by Django 4.0.5 on 2022-08-11 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0003_alter_category_code_alter_supplier_code'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(help_text='Не более 5 цифр', max_length=5, unique=True, verbose_name='Код')),
                ('name', models.CharField(db_index=True, help_text='Не более 200 знаков', max_length=200, verbose_name='Категория')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='Url')),
            ],
            options={
                'verbose_name': 'Категория продукта',
                'verbose_name_plural': 'Категории продуктов',
                'ordering': ['name'],
            },
        ),
    ]
