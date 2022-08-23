# порядок запуска программы
1. перейти в корневую папку :~/.../mms22-0730$ 
2. $source env22/bin/activate  - виртуальное окружение
3. python manage.py runserver  - запуск сервера
4. открыть в браузере http://localhost:8000/
# для входа в админ панель 
Имя пользователя:admin
Пароль:3333
# Выполнено
1. Модели Suppliers, Categories, Item, Product, Recipe.
2. Выведены на экран справочники по  Suppliers, Categories, Item, Product, Recipe.
3. Добавление в справочники новых записей.

# git log


commit d5f0d12c7d002f24a78da812b209c5ad428dbd49 (HEAD -> dev)
Author: Yury Vasev <vasevyp@mail.ru>
Date:   Sat Aug 20 01:40:52 2022 +0300

    В class Item() добавлены поля 'delivery_time', 'supply_lot', 'lot_weight', 'lot_length', 'lot_width', 'lot_height', 'best_befor'. Заведены в базу данные по этим полям для теста (кроме best_befor).

commit fd9a90827d2c88450c88cb67a04c68435f76fe07
Author: Yury Vasev <vasevyp@mail.ru>
Date:   Thu Aug 18 15:14:44 2022 +0300

    Установлен и подключен django-debug-toolbar

commit d99eaf42eb734abf78ef733217858fb2e96608fa
Author: Yury Vasev <vasevyp@mail.ru>
Date:   Tue Aug 16 12:24:41 2022 +0300

    Добавлено заведение места хранения товара, форма и список указания места. Место сразу д
commit d5f0d12c7d002f24a78da812b209c5ad428dbd49 (HEAD -> dev)
Author: Yury Vasev <vasevyp@mail.ru>
Date:   Sat Aug 20 01:40:52 2022 +0300

    В class Item() добавлены поля 'delivery_time', 'supply_lot', 'lot_weight', 'lot_length', 'lot_width', 'lot_height', 'best_befor'. Заведены в базу данные по этим полям для теста (кроме best_befor).

commit fd9a90827d2c88450c88cb67a04c68435f76fe07
Author: Yury Vasev <vasevyp@mail.ru>
Date:   Thu Aug 18 15:14:44 2022 +0300

    Установлен и подключен django-debug-toolbar

commit d99eaf42eb734abf78ef733217858fb2e96608fa
Author: Yury Vasev <vasevyp@mail.ru>
Date:   Tue Aug 16 12:24:41 2022 +0300

    Добавлено заведение места хранения товара, форма и список указания места. Место сразу д
обавляется с Inventory. Установленны пакеты pandas и numpy.

commit 0a42fd35ecc19ccf80368d5893cfd8cdfb1709df
Author: Yury Vasev <vasevyp@mail.ru>
Date:   Thu Aug 11 21:13:16 2022 +0300

    Сделано: при добавлении с экранной формы нового поставщика, категории, товара, продукта
 программно формируется слаг для Supplier, Category, CategoryItem, Item, Product.

commit 87ade5dce5f28543a306e5f8ea0356ef0764cc2c
Author: Yury Vasev <vasevyp@mail.ru>
Date:   Thu Aug 11 11:38:02 2022 +0300

    сделана проверка загрузки из Impex проданных товаров и переданных товаров. ОК

commit 9247e7bd268b14601bef02140fd783e06340821d
Author: Yury Vasev <vasevyp@mail.ru>
Date:   Thu Aug 11 07:34:38 2022 +0300

    В модель поставщика добавил поле Контакты

commit 614baf3cc6adf729a1d0cda2ff16ac74b6b96c40
Author: Yury Vasev <vasevyp@mail.ru>
Date:   Wed Aug 10 20:21:11 2022 +0300

    Удалена база данных, Поправлены модели, Все миграции на __init__.py

commit 5860568fe9cd65fdd82d8b3a0653d1c72db4e2de
Author: Yury Vasev <vasevyp@mail.ru>
Date:   Wed Aug 10 17:12:28 2022 +0300

     Сделано импортирование товаров и продуктов с получением slug из имени с помощью функфи
и do_slug(name).

commit 34836c9e279310d25ac263d5b90380d5492f0de0
Author: Yury Vasev <vasevyp@mail.ru>
Date:   Tue Aug 9 18:46:52 2022 +0300

    Поля модели ImpexRecipeIngedient исправлены на текстовые для получения импорта в базу д
анных.

commit 66bb5140c719c10ada70e6f36d59db3882e973ae
Author: Yury Vasev <vasevyp@mail.ru>
Date:   Tue Aug 9 17:40:39 2022 +0300

    343 git files saved. Code not changed.

commit bb0c721648cb8f820833692e93d1f11868e7e2fd
Author: Yury Vasev <vasevyp@mail.ru>
Date:   Tue Aug 9 17:33:58 2022 +0300

    Обновляю git, commit =Сделан Импорт списка "Переданных Товаров" и Импорт списка "Списан
ных Товаров" в Базу Данных и в запасы StockItem (transfer, waste).= код не менялся

commit 6840dae75de6b32f2e3dc539f38e6840e70ab44e
Author: Yury Vasev <vasevyp@mail.ru>
Date:   Mon Aug 8 20:47:00 2022 +0300

    Сделан Импорт списка "Переданных Товаров" и Импорт списка "Списанных Товаров" в Базу Да
нных и в запасы StockItem (transfer, waste).

commit 74a1d16ae2c94c1e14269603ca4e61a02fd5c181
Author: Yury Vasev <vasevyp@mail.ru>
Date:   Mon Aug 8 16:56:29 2022 +0300

    Изменения в моделях WasteItem и ImpexWasteItem (partner - approve, invoice - document) 
и связанных с ними админ, формах и шаблонах.

commit 5cca902e22c835287d7bfd5c765117b7ca582af4
Author: Yury Vasev <vasevyp@mail.ru>
Date:   Mon Aug 8 15:06:56 2022 +0300

    При импорте закупленного товара из Impex создается новая запись о закупке в BuyItem  и 
количество закупленного товара добавляется в базу данных StockItem (inventory).

commit 231d99ff9a2b4619eff2116890c484b4d7891dfa
Author: Yury Vasev <vasevyp@mail.ru>
Date:   Mon Aug 8 10:09:17 2022 +0300

    Сделано: при импортенового товара из Impex создается строчка в таблице запасов StockIte
m (Inventory).

commit e16a2a8e7298bc0265be64aa9ec3000548fa4ae8
Author: Yury Vasev <vasevyp@mail.ru>
Date:   Mon Aug 8 01:08:50 2022 +0300

    В Impex сделан импорт продуктов в Register.

commit d492fa95266c6b33e1d7b8a9a9f5aded1f7a0ead
Author: Yury Vasev <vasevyp@mail.ru>
Date:   Mon Aug 8 00:16:26 2022 +0300

    Удалена БД. В Impex сделан импорт товаров и категорий продуктов в Register. Установлен 
пакет import-export для загрузки и выгрузки данных из базы через админку.

commit 2a1796db156c3955e681dd69525e3d2a0648a99d
Author: Yury Vasev <vasevyp@mail.ru>
Date:   Sat Aug 6 13:44:03 2022 +0300

    Созданы приложения impex для обмена документами и acore - для аналитики.

commit f8d5d4bf1c0b5d3987495f716043e59aa1213f40
Author: Yury Vasev <vasevyp@mail.ru>
Date:   Sat Aug 6 12:59:03 2022 +0300

     Установлен в env22  пакет django-import-export,+ сопутствующие пакеты и пакет django-i
mport-export-celery - пока отключен.

commit 6b8752cf3b10a8b6a28fa1197ab6f673c5623dba
Author: Yury Vasev <vasevyp@mail.ru>
Date:   Sat Aug 6 01:18:51 2022 +0300

    Создал модели формы и листы для transfer и waste с внесением  transfer и waste в базу З
апасов StockItem. Также создается запись в листах  transfer_list и waste_list.

commit 5cf90753e543603ac0f90e9f270d39571d7a071a
Author: Yury Vasev <vasevyp@mail.ru>
Date:   Fri Aug 5 20:40:39 2022 +0300

    Поправлена форма добавления рецепта - добавлено поле кода продукта для  отображения код
а продукта в рецептах и админке.

commit 2379b54ff8a0411445a30f0edeeed45a23bd42a9
Author: Yury Vasev <vasevyp@mail.ru>
Date:   Fri Aug 5 18:39:54 2022 +0300

    Создал внесение  продажи в базу продаж и в базу Запасов StockItem. При продаже продукта
 создается запись в листе продаж, в листе остатков в поле продаж добавляются  товары в соот
ветствие с рецептов продукта.

commit e84dffe7f70c05a448b42f5deb2518b3212bd031
Author: Yury Vasev <vasevyp@mail.ru>
Date:   Fri Aug 5 16:35:54 2022 +0300

    Создал внесение  закупки в базу Запасов StockItem. Сейчас при создании товара создается
 запись в листе товаров и в листе остатков. При закупке товара создается запись в листе зак
упки, в листе остатков добавляется покупка (нарастающим итогом) и рассчитывается средневзве
шенная цена остатков.

commit 661cd2bff350a85c8a06fe3a586835958d422630
Author: Yury Vasev <vasevyp@mail.ru>
Date:   Fri Aug 5 15:45:15 2022 +0300

    Создал  - при создании товара создается запись в базе Запасов StockItem.

commit 48710d782bfc680e869577dab8dbd8a242b53498
Author: Yury Vasev <vasevyp@mail.ru>
Date:   Fri Aug 5 15:19:58 2022 +0300

    Запасов StockItem пока нет. Отменил - при создании товара создается запись в базе Товар
ов Items , в базе Закупок Buy Item, в базе Запасов StockItem.

commit cd5e69ea823cd04f01f405bcfb34f5648582926e
Author: Yury Vasev <vasevyp@mail.ru>
Date:   Thu Aug 4 22:30:52 2022 +0300

    При создании товара создается запись в базе Товаров Items , в базе Закупок Buy Item, в 
базе Запасов StockItem .

commit 51c8835434661990c437fd5c62b9bea046a3d1d0
Author: Yury Vasev <vasevyp@mail.ru>
Date:   Thu Aug 4 19:03:35 2022 +0300

    control.views.py - def add_item(request): - добавлено создание строки в BuyItem. Но Val
ueError: Cannot assign "10111110": "BuyItem.code" must be a "Item" instance, потому что пол
е ForeingKey

commit 31e1de25590a59e1168bfe94e653559d8f869cf6
Author: Yury Vasev <vasevyp@mail.ru>
Date:   Thu Aug 4 17:29:39 2022 +0300

    Изменения в items.html, suppliers.html, products.html, recipe.html, - порядок полей изм
енен

commit dac560f018cc0521eadd77104751cf2d919e94e0
Author: Yury Vasev <vasevyp@mail.ru>
Date:   Thu Aug 4 14:38:23 2022 +0300

    Выполнен показ из Dashbord страниц Inventory: About , View

commit 6239c9e83909a5c456839262acba2fda025e0210
Author: Yury Vasev <vasevyp@mail.ru>
Date:   Wed Aug 3 19:14:25 2022 +0300

    Добавлены формы Buy Item, Sold Product - Add/View

commit 0c57f0a37f7ebc7a79bd13e9b9bb52ee41eb322c
Author: Yury Vasev <vasevyp@mail.ru>
Date:   Wed Aug 3 13:30:03 2022 +0300

    2022-08-03 Перенесен код из экземпляра mms22-0730

commit 6102d923a9c5ff08b2f3ccb8d02a6d31dfa7cb31
Author: Yury Vasev <vasevyp@mail.ru>
Date:   Fri Jul 29 13:01:32 2022 +0300

    Изменены style.css, Почищена база данныз по продуктам, рецептам и др. таблицы

commit 9e5d6d571cd45f6d85a39c355b058ccaca280810
Author: Yury Vasev <vasevyp@mail.ru>
Date:   Wed Jul 27 22:14:02 2022 +0300

    Commit on branch develop

commit 11c0166418cad6c1181d97f2c4d3e5ad37728f19
Author: Yury Vasev <vasevyp@mail.ru>
Date:   Wed Jul 27 21:01:37 2022 +0300

    Выполнено

    Созданы миграции моделей для приложений register и control + admin.py. База данных пустая.

commit b3c45d8de1df1a79a5709389ab96efceee621faf
Author: Yury Vasev <vasevyp@mail.ru>
Date:   Wed Jul 20 11:32:26 2022 +0300

    Init commit

