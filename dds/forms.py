from django import forms
from .models import Transaction, Status, TransactionType, Category, Subcategory
import datetime


class TransactionForm(forms.ModelForm):
    date = forms.DateField(
        label='Дата',
        initial=datetime.date.today,
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})
    )

    class Meta:
        model = Transaction
        fields = ['date', 'status', 'transaction_type', 'category', 'subcategory', 'amount', 'comment']
        widgets = {
            'status':           forms.Select(attrs={'class': 'form-select'}),
            'transaction_type': forms.Select(attrs={'class': 'form-select'}),
            'category':         forms.Select(attrs={'class': 'form-select'}),
            'subcategory':      forms.Select(attrs={'class': 'form-select'}),
            'amount':           forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'comment':          forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
        labels = {
            'status':           'Статус',
            'transaction_type': 'Тип',
            'category':         'Категория',
            'subcategory':      'Подкатегория',
            'amount':           'Сумма (руб.)',
            'comment':          'Комментарий',
        }

    def clean(self):
        """Серверная валидация каскадных зависимостей."""
        cleaned_data = super().clean()
        t_type   = cleaned_data.get('transaction_type')
        category = cleaned_data.get('category')
        subcat   = cleaned_data.get('subcategory')

        if category and t_type and category.transaction_type != t_type:
            self.add_error('category', 'Эта категория не относится к выбранному типу.')

        if subcat and category and subcat.category != category:
            self.add_error('subcategory', 'Эта подкатегория не относится к выбранной категории.')

        return cleaned_data


class StatusForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = ['name']
        widgets = {'name': forms.TextInput(attrs={'class': 'form-control'})}
        labels  = {'name': 'Название'}


class TransactionTypeForm(forms.ModelForm):
    class Meta:
        model = TransactionType
        fields = ['name']
        widgets = {'name': forms.TextInput(attrs={'class': 'form-control'})}
        labels  = {'name': 'Название'}


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'transaction_type']
        widgets = {
            'name':             forms.TextInput(attrs={'class': 'form-control'}),
            'transaction_type': forms.Select(attrs={'class': 'form-select'}),
        }
        labels = {'name': 'Название', 'transaction_type': 'Тип'}


class SubcategoryForm(forms.ModelForm):
    class Meta:
        model = Subcategory
        fields = ['name', 'category']
        widgets = {
            'name':     forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
        }
        labels = {'name': 'Название', 'category': 'Категория'}