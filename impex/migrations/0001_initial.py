# Generated by Django 4.0.5 on 2022-08-07 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ImpexBuyItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.DecimalField(decimal_places=0, help_text='Не более 12 знаков', max_digits=12, null=True, verbose_name='Код')),
                ('item', models.CharField(db_index=True, help_text='Не более 200 знаков', max_length=200)),
                ('name', models.CharField(help_text='Не более 200 знаков', max_length=200)),
                ('slug', models.SlugField(blank=True, max_length=255, null=True, verbose_name='Url')),
                ('unit', models.CharField(choices=[(None, 'Выбрать ед.изм.'), ('кг', 'кг'), ('л', 'л'), ('шт.', ' шт.')], default='kg', max_length=10, null=True, verbose_name='Ед.изм.')),
                ('unit_cost', models.PositiveIntegerField(default=0, null=True, verbose_name='Цена, руб')),
                ('quantity', models.PositiveIntegerField(default=0, verbose_name='Кол.')),
                ('cost', models.PositiveIntegerField(blank=True, null=True, verbose_name='Сумма, руб')),
                ('item_supplier', models.CharField(help_text='Не более 200 знаков', max_length=200, null=True)),
                ('supplier', models.CharField(help_text='Не более 200 знаков', max_length=200, null=True)),
                ('invoice', models.CharField(default='Накладная №     , дата   ', max_length=250, null=True, verbose_name='Накладная')),
                ('created_date', models.DateField(auto_now_add=True, verbose_name='Дата')),
                ('updated_date', models.DateField(auto_now=True, null=True, verbose_name='Изменен')),
            ],
            options={
                'verbose_name': 'X-Закупка',
                'verbose_name_plural': 'X-Закупки',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='ImpexCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.DecimalField(decimal_places=0, help_text='Не более 5 цифр', max_digits=5, unique=True, verbose_name='Код')),
                ('name', models.CharField(db_index=True, help_text='Не более 200 знаков', max_length=200, verbose_name='Категория')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='Url')),
            ],
            options={
                'verbose_name': 'X-Категория продукта',
                'verbose_name_plural': 'X-Категории продуктов',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='ImpexCategoryItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.DecimalField(decimal_places=0, help_text='Не более 5 цифр', max_digits=5, unique=True, verbose_name='Код')),
                ('name', models.CharField(db_index=True, help_text='Не более 200 знаков', max_length=200, verbose_name='Категория')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='Url')),
            ],
            options={
                'verbose_name': 'X-Категория товара',
                'verbose_name_plural': 'X-Категории товаров',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='ImpexDeliverItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_item', models.CharField(help_text='Не более 200 знаков', max_length=200, null=True)),
                ('order_number', models.DecimalField(decimal_places=0, max_digits=10, null=True, verbose_name='Номер заказа')),
                ('supplier', models.CharField(help_text='Не более 200 знаков', max_length=200)),
                ('code', models.DecimalField(decimal_places=0, help_text='Не более 12 знаков', max_digits=12, null=True, verbose_name='Код')),
                ('product', models.CharField(help_text='Не более 200 знаков', max_length=200)),
                ('slug', models.SlugField(blank=True, max_length=255, null=True, verbose_name='Url')),
                ('unit', models.CharField(choices=[(None, 'Выбрать ед.изм.'), ('кг', 'кг'), ('л', 'л'), ('шт.', ' шт.')], default='kg', max_length=10, null=True, verbose_name='Ед.изм.')),
                ('unit_cost', models.DecimalField(decimal_places=2, help_text='Не более 10 знаков', max_digits=10, null=True)),
                ('order_quantity', models.DecimalField(decimal_places=2, help_text='Не более 10 знаков', max_digits=10, null=True)),
                ('status', models.CharField(choices=[('pending', 'ожидание '), ('decline', 'отклонить'), ('approved', 'одобрено'), ('processing', 'обработка'), ('complete', 'готов')], help_text='Не более 10 знаков', max_length=10)),
                ('created_date', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'X-На пути',
                'verbose_name_plural': 'X-На путях',
                'ordering': ['order_number'],
            },
        ),
        migrations.CreateModel(
            name='ImpexItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.DecimalField(decimal_places=0, help_text='Не более 12 знаков', max_digits=12, null=True, unique=True, verbose_name='Код')),
                ('name', models.CharField(db_index=True, help_text='Не более 200 знаков', max_length=200, unique=True)),
                ('category', models.CharField(help_text='Не более 200 знаков', max_length=200)),
                ('supplier', models.CharField(help_text='Не более 200 знаков', max_length=200)),
                ('unit', models.CharField(choices=[(None, 'Выбрать ед.изм.'), ('кг', 'кг'), ('л', 'л'), ('шт.', ' шт.')], help_text='Не более 50 знаков', max_length=50)),
                ('unit_cost', models.DecimalField(decimal_places=2, help_text='Не более 10 знаков', max_digits=10)),
                ('description', models.TextField(blank=True, null=True)),
                ('available', models.BooleanField(default=True)),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='Url')),
                ('created_date', models.DateField(auto_now_add=True, null=True, verbose_name='Создан')),
                ('updated_date', models.DateField(auto_now=True, null=True, verbose_name='Изменен')),
            ],
            options={
                'verbose_name': 'X-Товар',
                'verbose_name_plural': 'X-Товары',
                'ordering': ['category', 'name'],
            },
        ),
        migrations.CreateModel(
            name='ImpexOrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_number', models.CharField(help_text='Не более 10 знаков', max_length=10, unique=True)),
                ('supplier', models.CharField(help_text='Не более 200 знаков', max_length=200)),
                ('item', models.CharField(help_text='Не более 200 знаков', max_length=200, null=True)),
                ('code', models.DecimalField(decimal_places=0, help_text='Не более 12 знаков', max_digits=12, null=True, verbose_name='Код')),
                ('slug', models.SlugField(blank=True, max_length=255, null=True, verbose_name='Url')),
                ('unit', models.CharField(choices=[(None, 'Выбрать ед.изм.'), ('кг', 'кг'), ('л', 'л'), ('шт.', ' шт.')], default='kg', max_length=10, null=True, verbose_name='Ед.изм.')),
                ('unit_cost', models.DecimalField(decimal_places=2, help_text='Не более 10 знаков', max_digits=10, null=True)),
                ('order_quantity', models.PositiveIntegerField(null=True)),
                ('status', models.CharField(choices=[('pending', 'ожидание '), ('decline', 'отклонить'), ('approved', 'одобрено'), ('processing', 'обработка'), ('complete', 'готов')], help_text='Не более 10 знаков', max_length=10)),
                ('created_date', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'X-Заказ',
                'verbose_name_plural': 'X-Заказы',
                'ordering': ['order_number'],
            },
        ),
        migrations.CreateModel(
            name='ImpexProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.DecimalField(decimal_places=0, help_text='Не более 10 знаков', max_digits=10, null=True, verbose_name='Код')),
                ('name', models.CharField(help_text='Не более 200 знаков', max_length=200, null=True, verbose_name='Продукт')),
                ('category', models.CharField(help_text='Не более 200 знаков', max_length=200, null=True)),
                ('category_id', models.CharField(help_text='Не более 200 знаков', max_length=200, null=True)),
                ('ingredient', models.CharField(blank=True, help_text='Не более 200 знаков', max_length=200, null=True)),
                ('difficulty', models.CharField(choices=[('Easy', 'Easy'), ('Medium', 'Medium'), ('Hard', 'Hard')], max_length=10)),
                ('price', models.DecimalField(decimal_places=2, help_text='Не более 10 знаков', max_digits=10, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('cooking', models.TextField(blank=True, null=True)),
                ('slug', models.SlugField(max_length=255, null=True, verbose_name='Url')),
                ('created_date', models.DateField(auto_now_add=True, null=True, verbose_name='Создан')),
                ('updated_date', models.DateField(auto_now=True, null=True, verbose_name='Изменен')),
            ],
            options={
                'verbose_name': 'X-Продукт',
                'verbose_name_plural': 'X-Продукты',
                'ordering': ['category', 'name'],
            },
        ),
        migrations.CreateModel(
            name='ImpexRecipeIngredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(help_text='Не более 200 знаков', max_length=200)),
                ('code', models.DecimalField(decimal_places=0, help_text='Не более 10 знаков', max_digits=10, null=True, verbose_name='Код продукта')),
                ('ingredient', models.CharField(help_text='Не более 200 знаков', max_length=200)),
                ('code_ingr', models.DecimalField(decimal_places=0, help_text='Не более 12 знаков', max_digits=12, null=True, verbose_name='Код ингредиента')),
                ('unit', models.CharField(choices=[(None, 'Выбрать ед.изм.'), ('кг', 'кг'), ('л', 'л'), ('шт.', ' шт.')], default='kg', help_text='Не более 10 знаков', max_length=10, null=True)),
                ('unit_cost', models.DecimalField(decimal_places=2, help_text='Не более 10 знаков', max_digits=10, null=True)),
                ('ratio', models.DecimalField(decimal_places=3, default=1, help_text='Не более 10 знаков', max_digits=10, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Изменен')),
            ],
            options={
                'verbose_name': 'X-Рецепт с ингредиентами',
                'verbose_name_plural': 'X-Рецепты с ингредиентами',
                'ordering': ['product', 'ingredient'],
            },
        ),
        migrations.CreateModel(
            name='ImpexSaleProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Не более 200 знаков', max_length=200, null=True)),
                ('product', models.CharField(db_index=True, help_text='Не более 200 знаков', max_length=200, null=True)),
                ('code', models.DecimalField(decimal_places=0, help_text='Не более 12 знаков', max_digits=12, null=True, verbose_name='Код')),
                ('slug', models.SlugField(blank=True, max_length=255, null=True, verbose_name='Url')),
                ('price', models.PositiveIntegerField(default=1, verbose_name='Цена, руб')),
                ('sold', models.PositiveIntegerField(default=1, verbose_name='Sold, руб')),
                ('unit', models.CharField(choices=[(None, 'Выбрать ед.изм.'), ('кг', 'кг'), ('л', 'л'), ('шт.', ' шт.')], default='шт.', max_length=10, null=True, verbose_name='Ед.изм.')),
                ('revenue', models.DecimalField(blank=True, decimal_places=2, default=0, help_text='Не более 10 знаков', max_digits=10, null=True)),
                ('created_date', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'X-Продажа',
                'verbose_name_plural': 'X-Продажи',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='ImpexStockItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.DecimalField(decimal_places=0, help_text='Не более 12 знаков', max_digits=12, null=True, verbose_name='Код')),
                ('name', models.CharField(db_index=True, help_text='Не более 200 знаков', max_length=200)),
                ('slug', models.SlugField(max_length=255, verbose_name='Url')),
                ('unit', models.CharField(choices=[(None, 'Выбрать ед.изм.'), ('кг', 'кг'), ('л', 'л'), ('шт.', ' шт.')], default='kg', max_length=10, null=True, verbose_name='Ед.изм.')),
                ('unit_cost', models.DecimalField(decimal_places=2, help_text='Не более 10 знаков', max_digits=10, null=True)),
                ('place', models.CharField(default='store', max_length=100, null=True, verbose_name='Место')),
                ('open', models.DecimalField(decimal_places=0, default=0, help_text='Не более 10 знаков', max_digits=10, null=True)),
                ('sales', models.DecimalField(decimal_places=3, default=0, help_text='Не более 10 знаков', max_digits=10)),
                ('received', models.DecimalField(decimal_places=0, default=0, help_text='Не более 10 знаков', max_digits=10, null=True)),
                ('transfer', models.DecimalField(decimal_places=0, default=0, help_text='Не более 10 знаков', max_digits=10, null=True)),
                ('waste', models.DecimalField(decimal_places=0, default=0, help_text='Не более 10 знаков', max_digits=10, null=True)),
                ('actual', models.DecimalField(decimal_places=0, default=0, help_text='Не более 10 знаков', max_digits=10)),
                ('actual_cost', models.DecimalField(decimal_places=2, default=0, help_text='Не более 12 знаков', max_digits=12)),
            ],
            options={
                'verbose_name': 'X-Остаток',
                'verbose_name_plural': 'X-Остатки',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='ImpexSupplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.DecimalField(decimal_places=0, help_text='Не более 4 знаков', max_digits=4, unique=True)),
                ('name', models.CharField(db_index=True, help_text='Не более 200 знаков', max_length=200)),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='Url')),
                ('address', models.CharField(max_length=220)),
                ('created_date', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'X-Поставщик',
                'verbose_name_plural': 'X-Поставщики',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='ImpexTransferItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.DecimalField(decimal_places=0, help_text='Не более 12 знаков', max_digits=12, null=True, verbose_name='Код')),
                ('item', models.CharField(db_index=True, help_text='Не более 200 знаков', max_length=200)),
                ('name', models.CharField(help_text='Не более 200 знаков', max_length=200)),
                ('slug', models.SlugField(blank=True, max_length=255, null=True, verbose_name='Url')),
                ('unit', models.CharField(choices=[(None, 'Выбрать ед.изм.'), ('кг', 'кг'), ('л', 'л'), ('шт.', ' шт.')], default='kg', max_length=10, null=True, verbose_name='Ед.изм.')),
                ('unit_cost', models.PositiveIntegerField(default=0, null=True, verbose_name='Цена, руб')),
                ('quantity', models.PositiveIntegerField(default=0, verbose_name='Кол.')),
                ('cost', models.PositiveIntegerField(blank=True, null=True, verbose_name='Сумма, руб')),
                ('partner', models.CharField(help_text='Не более 200 знаков', max_length=200, null=True)),
                ('invoice', models.CharField(default='Накладная №     , дата   ', max_length=250, null=True, verbose_name='Накладная')),
                ('created_date', models.DateField(auto_now_add=True, verbose_name='Дата')),
            ],
            options={
                'verbose_name': 'X-Передача',
                'verbose_name_plural': 'X-Передачи',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='ImpexWasteItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.DecimalField(decimal_places=0, help_text='Не более 12 знаков', max_digits=12, null=True, verbose_name='Код')),
                ('item', models.CharField(db_index=True, help_text='Не более 200 знаков', max_length=200)),
                ('name', models.CharField(help_text='Не более 200 знаков', max_length=200)),
                ('slug', models.SlugField(blank=True, max_length=255, null=True, verbose_name='Url')),
                ('unit', models.CharField(choices=[(None, 'Выбрать ед.изм.'), ('кг', 'кг'), ('л', 'л'), ('шт.', ' шт.')], default='kg', max_length=10, null=True, verbose_name='Ед.изм.')),
                ('unit_cost', models.PositiveIntegerField(default=0, null=True, verbose_name='Цена, руб')),
                ('quantity', models.PositiveIntegerField(default=0, verbose_name='Кол.')),
                ('cost', models.PositiveIntegerField(blank=True, null=True, verbose_name='Сумма, руб')),
                ('partner', models.CharField(help_text='Не более 200 знаков', max_length=200, null=True)),
                ('invoice', models.CharField(default='Акт №     , дата   ', max_length=250, null=True, verbose_name='Акт')),
                ('created_date', models.DateField(auto_now_add=True, verbose_name='Дата')),
            ],
            options={
                'verbose_name': 'X-Списание',
                'verbose_name_plural': 'X-Списания',
                'ordering': ['name'],
            },
        ),
    ]
