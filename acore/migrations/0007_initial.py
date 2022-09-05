# Generated by Django 4.0.5 on 2022-08-28 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('acore', '0006_delete_stockforecastdays'),
    ]

    operations = [
        migrations.CreateModel(
            name='StockForecastDays',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.DecimalField(decimal_places=0, help_text='Не более 12 знаков', max_digits=12, null=True, verbose_name='Код')),
                ('name', models.CharField(db_index=True, help_text='Не более 200 знаков', max_length=200)),
                ('slug', models.SlugField(max_length=255, verbose_name='Url')),
                ('unit', models.CharField(default='kg', max_length=10, null=True, verbose_name='Ед.изм.')),
                ('unit_cost', models.DecimalField(decimal_places=2, help_text='Не более 10 знаков', max_digits=10, null=True)),
                ('actual', models.DecimalField(decimal_places=0, default=0, help_text='Не более 10 знаков', max_digits=10)),
                ('actual_cost', models.DecimalField(decimal_places=2, default=0, help_text='Не более 12 знаков', max_digits=12)),
                ('daily_requirement', models.DecimalField(decimal_places=4, max_digits=10, null=True, verbose_name='Суточная потребность')),
                ('stock_days', models.DecimalField(decimal_places=0, help_text='Не более 4 знаков', max_digits=4)),
            ],
            options={
                'verbose_name': 'Остаток в днях',
                'verbose_name_plural': 'Остатки в днях',
                'ordering': ['-stock_days'],
            },
        ),
    ]
