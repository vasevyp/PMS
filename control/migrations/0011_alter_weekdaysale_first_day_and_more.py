# Generated by Django 4.0.5 on 2022-08-25 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('control', '0010_weekdaysale_date_weekendsale_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weekdaysale',
            name='first_day',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='weekdaysale',
            name='last_day',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='weekendsale',
            name='first_day',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='weekendsale',
            name='last_day',
            field=models.DateField(null=True),
        ),
    ]
