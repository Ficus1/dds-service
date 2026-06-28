# Веб-сервис ДДС

Веб-приложение для учёта движения денежных средств на Django.

## Технологии

- Python 3.10+
- Django 4.2
- SQLite
- Bootstrap 5

## Установка и запуск

### 1. Клонировать репозиторий
git clone https://github.com/ВАШ_ЛОГИН/dds-service.git
cd dds-service

### 2. Создать и активировать виртуальное окружение
python -m venv venv
source venv/bin/activate        # macOS/Linux
venv\Scripts\activate           # Windows

### 3. Установить зависимости
pip install -r requirements.txt

### 4. Применить миграции
python manage.py migrate

### 5. Загрузить начальные данные
python manage.py seed

### 6. Создать суперпользователя
python manage.py createsuperuser

### 7. Запустить сервер
python manage.py runserver

Приложение: http://127.0.0.1:8000/
Админ-панель: http://127.0.0.1:8000/admin/

## Функциональность

- Создание, редактирование, удаление записей ДДС
- Фильтрация по дате, статусу, типу, категории и подкатегории
- Каскадный выбор: тип → категория → подкатегория
- Управление справочниками
- Валидация на клиенте и сервере
```

---

## Итоговый порядок действий (быстрый чеклист)

```
[ ] git clone + cd
[ ] python -m venv venv && активировать
[ ] pip install django && pip freeze > requirements.txt
[ ] django-admin startproject dds_project .
[ ] python manage.py startapp dds
[ ] Добавить 'dds' в INSTALLED_APPS
[ ] Написать models.py
[ ] python manage.py makemigrations && migrate
[ ] Написать admin.py
[ ] Создать forms.py
[ ] Написать views.py
[ ] Создать dds/urls.py, обновить dds_project/urls.py
[ ] Создать 6 шаблонов в dds/templates/dds/
[ ] Создать management/commands/seed.py
[ ] python manage.py seed
[ ] python manage.py createsuperuser
[ ] python manage.py runserver — проверить всё в браузере
[ ] git add . && git commit && git push