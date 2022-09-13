# Generated by Django 4.0.5 on 2022-09-07 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acore', '0008_fullstock_alter_stockforecastdays_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='ToOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.DecimalField(decimal_places=0, help_text='Не более 12 знаков', max_digits=12, null=True, verbose_name='Код')),
                ('name', models.CharField(db_index=True, help_text='Не более 200 знаков', max_length=200)),
                ('delivery_time', models.IntegerField(default=5, null=True, verbose_name='Буфер, дней')),
                ('fullstock_days', models.IntegerField(default=0, null=True, verbose_name='Запас, дней')),
                ('daily_requirement', models.DecimalField(decimal_places=4, max_digits=10, null=True, verbose_name='Суточная потребность')),
                ('to_order', models.IntegerField(verbose_name='Заказать, ед.')),
                ('to_orders', models.DecimalField(decimal_places=2, help_text='Не более 10 знаков', max_digits=10, null=True, verbose_name='Заказать, руб.')),
                ('status', models.CharField(choices=[('pending', 'ожидание '), ('decline', 'отклонить'), ('approved', 'одобрено')], help_text='Не более 10 знаков', max_length=10)),
            ],
        ),
    ]
