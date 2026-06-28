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
