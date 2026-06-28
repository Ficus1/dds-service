from django.db import models
from django.utils import timezone


class Status(models.Model):
    """Статус записи: Бизнес, Личное, Налог и т.д."""
    name = models.CharField('Название', max_length=100, unique=True)

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'

    def __str__(self):
        return self.name


class TransactionType(models.Model):
    """Тип операции: Пополнение, Списание и т.д."""
    name = models.CharField('Название', max_length=100, unique=True)

    class Meta:
        verbose_name = 'Тип'
        verbose_name_plural = 'Типы'

    def __str__(self):
        return self.name


class Category(models.Model):
    """Категория привязана к типу операции."""
    name = models.CharField('Название', max_length=100)
    transaction_type = models.ForeignKey(
        TransactionType,
        on_delete=models.CASCADE,
        related_name='categories',
        verbose_name='Тип'
    )

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        unique_together = ('name', 'transaction_type')

    def __str__(self):
        return f'{self.name} ({self.transaction_type})'


class Subcategory(models.Model):
    """Подкатегория привязана к категории."""
    name = models.CharField('Название', max_length=100)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='subcategories',
        verbose_name='Категория'
    )

    class Meta:
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'
        unique_together = ('name', 'category')

    def __str__(self):
        return f'{self.name} ({self.category.name})'


class Transaction(models.Model):
    """Запись о движении денежных средств."""
    date = models.DateField('Дата', default=timezone.now)
    status = models.ForeignKey(
        Status, on_delete=models.PROTECT, verbose_name='Статус'
    )
    transaction_type = models.ForeignKey(
        TransactionType, on_delete=models.PROTECT, verbose_name='Тип'
    )
    category = models.ForeignKey(
        Category, on_delete=models.PROTECT, verbose_name='Категория'
    )
    subcategory = models.ForeignKey(
        Subcategory, on_delete=models.PROTECT, verbose_name='Подкатегория'
    )
    amount = models.DecimalField('Сумма (руб.)', max_digits=12, decimal_places=2)
    comment = models.TextField('Комментарий', blank=True)
    created_at = models.DateTimeField('Создано', auto_now_add=True)

    class Meta:
        verbose_name = 'Запись ДДС'
        verbose_name_plural = 'Записи ДДС'
        ordering = ['-date', '-created_at']

    def __str__(self):
        return f'{self.date} | {self.transaction_type} | {self.amount} руб.'