# Generated by Django 4.0.5 on 2022-07-29 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('control', '0023_alter_deliveritem_order_quantity'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='buyitem',
            options={'ordering': ['name'], 'verbose_name': 'Закупка', 'verbose_name_plural': 'Закупки'},
        ),
        migrations.AlterModelOptions(
            name='deliveritem',
            options={'ordering': ['order_number'], 'verbose_name': 'На пути', 'verbose_name_plural': 'На путях'},
        ),
        migrations.AlterModelOptions(
            name='orderitem',
            options={'ordering': ['order_number'], 'verbose_name': 'Заказ', 'verbose_name_plural': 'Заказы'},
        ),
        migrations.AlterModelOptions(
            name='saleproduct',
            options={'ordering': ['name'], 'verbose_name': 'Продажа', 'verbose_name_plural': 'Продажи'},
        ),
        migrations.AlterModelOptions(
            name='stockitem',
            options={'ordering': ['name'], 'verbose_name': 'Остаток', 'verbose_name_plural': 'Остатки'},
        ),
        migrations.AlterField(
            model_name='buyitem',
            name='unit',
            field=models.CharField(choices=[(None, 'Выбрать ед.изм.'), ('кг', 'кг'), ('л', 'л'), ('шт.', ' шт.')], default='kg', max_length=10, null=True, verbose_name='Ед.изм.'),
        ),
        migrations.AlterField(
            model_name='deliveritem',
            name='status',
            field=models.CharField(choices=[('pending', 'ожидание '), ('decline', 'отклонить'), ('approved', 'одобрено'), ('processing', 'обработка'), ('complete', 'готов')], help_text='Не более 10 знаков', max_length=10),
        ),
        migrations.AlterField(
            model_name='deliveritem',
            name='unit',
            field=models.CharField(choices=[(None, 'Выбрать ед.изм.'), ('кг', 'кг'), ('л', 'л'), ('шт.', ' шт.')], default='kg', max_length=10, null=True, verbose_name='Ед.изм.'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='status',
            field=models.CharField(choices=[('pending', 'ожидание '), ('decline', 'отклонить'), ('approved', 'одобрено'), ('processing', 'обработка'), ('complete', 'готов')], help_text='Не более 10 знаков', max_length=10),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='unit',
            field=models.CharField(choices=[(None, 'Выбрать ед.изм.'), ('кг', 'кг'), ('л', 'л'), ('шт.', ' шт.')], default='kg', max_length=10, null=True, verbose_name='Ед.изм.'),
        ),
        migrations.AlterField(
            model_name='stockitem',
            name='unit',
            field=models.CharField(choices=[(None, 'Выбрать ед.изм.'), ('кг', 'кг'), ('л', 'л'), ('шт.', ' шт.')], default='kg', max_length=10, null=True, verbose_name='Ед.изм.'),
        ),
    ]
