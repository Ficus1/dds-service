from django.contrib import admin
from .models import Status, TransactionType, Category, Subcategory, Transaction


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(TransactionType)
class TransactionTypeAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'transaction_type']
    list_filter = ['transaction_type']


@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'category']
    list_filter = ['category__transaction_type', 'category']


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ['date', 'status', 'transaction_type', 'category', 'subcategory', 'amount']
    list_filter = ['status', 'transaction_type', 'category']
    date_hierarchy = 'date'