# Django приложение: Управления закупками (Procurement Management System)

#### Приложение позволяет контролировать остатки ингредиентов для блюд общепита с учетом текущего уровня продаж.
#### Показывает критические позиции, которые необходимо заказать у поставщика.

### Порядок запуска приложения

#### Шаг 1: Создайте виртуальную среду:

Обязательно использовать версию Python 3.10 (в оригинале используется Python 3.10.14)

Пользователи Unix / Linux / macOS выполняют следующую команду

python3 -m venv env

Пользователи Windows запускают следующую команду

py -m venv env

#### Шаг 2: Активируйте виртуальную среду и проверьте ее:

Пользователи Unix / Linux / macOS выполняют следующую команду

source env/bin/activate

Пользователи Windows запускают следующую команду

.\env\Scripts\activate

#### Шаг 3:Устанавливаем необходимые пакеты из requirements.txt:

pip3 install -r requirements.txt

#### Шаг 4:Создание миграции для БД:

python manage.py makemigrations

#### Шаг 5:Миграция данных для таблиц:

python manage.py migrate

#### Шаг 6:Создать суперпользователя:

python manage.py createsuperuser

#### Шаг 7:Запуск локального сервера:

python manage.py runserver

#### Шаг 8: Открытие проекта в браузере:

Запуск сервера разработки в браузере по адресу http://127.0.0.1:8000/
## Для входа в админ панель демонстрационной базы данных
В демонстрационной базе db.sqlite3:  
 -  Имя суперпользователя:admin  
 -  Пароль:3333


