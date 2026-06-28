from django.core.management.base import BaseCommand
from dds.models import Status, TransactionType, Category, Subcategory


class Command(BaseCommand):
    help = 'Заполняет базу начальными данными'

    def handle(self, *args, **kwargs):
        # Статусы
        for name in ['Бизнес', 'Личное', 'Налог']:
            Status.objects.get_or_create(name=name)

        # Типы
        debit,  _ = TransactionType.objects.get_or_create(name='Списание')
        credit, _ = TransactionType.objects.get_or_create(name='Пополнение')

        # Категории и подкатегории для Списания
        marketing, _ = Category.objects.get_or_create(name='Маркетинг', transaction_type=debit)
        Subcategory.objects.get_or_create(name='Farpost', category=marketing)
        Subcategory.objects.get_or_create(name='Avito',   category=marketing)

        infra, _ = Category.objects.get_or_create(name='Инфраструктура', transaction_type=debit)
        Subcategory.objects.get_or_create(name='VPS',   category=infra)
        Subcategory.objects.get_or_create(name='Proxy', category=infra)

        # Категории для Пополнения
        income, _ = Category.objects.get_or_create(name='Доход', transaction_type=credit)
        Subcategory.objects.get_or_create(name='Клиенты',   category=income)
        Subcategory.objects.get_or_create(name='Партнёры',  category=income)

        self.stdout.write(self.style.SUCCESS('✅ Начальные данные загружены'))