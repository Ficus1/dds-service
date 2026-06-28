from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.contrib import messages
from .models import Transaction, Status, TransactionType, Category, Subcategory
from .forms import (
    TransactionForm, StatusForm, TransactionTypeForm, CategoryForm, SubcategoryForm
)

# ───────────────────────── Главная — список записей ──────────────────────────

def index(request):
    qs = Transaction.objects.select_related(
        'status', 'transaction_type', 'category', 'subcategory'
    )

    # Фильтры
    date_from  = request.GET.get('date_from')
    date_to    = request.GET.get('date_to')
    status_id  = request.GET.get('status')
    type_id    = request.GET.get('transaction_type')
    cat_id     = request.GET.get('category')
    subcat_id  = request.GET.get('subcategory')

    if date_from:
        qs = qs.filter(date__gte=date_from)
    if date_to:
        qs = qs.filter(date__lte=date_to)
    if status_id:
        qs = qs.filter(status_id=status_id)
    if type_id:
        qs = qs.filter(transaction_type_id=type_id)
    if cat_id:
        qs = qs.filter(category_id=cat_id)
    if subcat_id:
        qs = qs.filter(subcategory_id=subcat_id)

    context = {
        'transactions':  qs,
        'statuses':      Status.objects.all(),
        'types':         TransactionType.objects.all(),
        'categories':    Category.objects.all(),
        'subcategories': Subcategory.objects.all(),
        'filters': {
            'date_from':        date_from or '',
            'date_to':          date_to or '',
            'status':           status_id or '',
            'transaction_type': type_id or '',
            'category':         cat_id or '',
            'subcategory':      subcat_id or '',
        },
    }
    return render(request, 'dds/index.html', context)


# ──────────────────── Создание и редактирование записи ───────────────────────

def transaction_create(request):
    form = TransactionForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Запись успешно создана.')
        return redirect('dds:index')
    return render(request, 'dds/record_form.html', {'form': form, 'title': 'Новая запись'})


def transaction_edit(request, pk):
    obj  = get_object_or_404(Transaction, pk=pk)
    form = TransactionForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        messages.success(request, 'Запись обновлена.')
        return redirect('dds:index')
    return render(request, 'dds/record_form.html', {'form': form, 'title': 'Редактирование записи', 'object': obj})


def transaction_delete(request, pk):
    obj = get_object_or_404(Transaction, pk=pk)
    if request.method == 'POST':
        obj.delete()
        messages.success(request, 'Запись удалена.')
        return redirect('dds:index')
    return render(request, 'dds/confirm_delete.html', {'object': obj})


# ──────────────────────── AJAX для каскадных списков ─────────────────────────

def api_categories(request):
    type_id = request.GET.get('type_id')
    data = list(Category.objects.filter(transaction_type_id=type_id).values('id', 'name'))
    return JsonResponse(data, safe=False)


def api_subcategories(request):
    cat_id = request.GET.get('category_id')
    data = list(Subcategory.objects.filter(category_id=cat_id).values('id', 'name'))
    return JsonResponse(data, safe=False)


# ───────────────────────── Справочники ───────────────────────────────────────

def references(request):
    context = {
        'statuses':      Status.objects.all(),
        'types':         TransactionType.objects.all(),
        'categories':    Category.objects.all(),
        'subcategories': Subcategory.objects.all(),
    }
    return render(request, 'dds/references.html', context)


# --- Статусы ---
def status_create(request):
    form = StatusForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Статус добавлен.')
        return redirect('dds:references')
    return render(request, 'dds/ref_form.html', {'form': form, 'title': 'Добавить статус'})

def status_edit(request, pk):
    obj  = get_object_or_404(Status, pk=pk)
    form = StatusForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        messages.success(request, 'Статус обновлён.')
        return redirect('dds:references')
    return render(request, 'dds/ref_form.html', {'form': form, 'title': 'Редактировать статус'})

def status_delete(request, pk):
    obj = get_object_or_404(Status, pk=pk)
    if request.method == 'POST':
        obj.delete()
        messages.success(request, 'Статус удалён.')
        return redirect('dds:references')
    return render(request, 'dds/confirm_delete.html', {'object': obj})


# --- Типы ---
def type_create(request):
    form = TransactionTypeForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Тип добавлен.')
        return redirect('dds:references')
    return render(request, 'dds/ref_form.html', {'form': form, 'title': 'Добавить тип'})

def type_edit(request, pk):
    obj  = get_object_or_404(TransactionType, pk=pk)
    form = TransactionTypeForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        messages.success(request, 'Тип обновлён.')
        return redirect('dds:references')
    return render(request, 'dds/ref_form.html', {'form': form, 'title': 'Редактировать тип'})

def type_delete(request, pk):
    obj = get_object_or_404(TransactionType, pk=pk)
    if request.method == 'POST':
        obj.delete()
        messages.success(request, 'Тип удалён.')
        return redirect('dds:references')
    return render(request, 'dds/confirm_delete.html', {'object': obj})


# --- Категории ---
def category_create(request):
    form = CategoryForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Категория добавлена.')
        return redirect('dds:references')
    return render(request, 'dds/ref_form.html', {'form': form, 'title': 'Добавить категорию'})

def category_edit(request, pk):
    obj  = get_object_or_404(Category, pk=pk)
    form = CategoryForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        messages.success(request, 'Категория обновлена.')
        return redirect('dds:references')
    return render(request, 'dds/ref_form.html', {'form': form, 'title': 'Редактировать категорию'})

def category_delete(request, pk):
    obj = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        obj.delete()
        messages.success(request, 'Категория удалена.')
        return redirect('dds:references')
    return render(request, 'dds/confirm_delete.html', {'object': obj})


# --- Подкатегории ---
def subcategory_create(request):
    form = SubcategoryForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Подкатегория добавлена.')
        return redirect('dds:references')
    return render(request, 'dds/ref_form.html', {'form': form, 'title': 'Добавить подкатегорию'})

def subcategory_edit(request, pk):
    obj  = get_object_or_404(Subcategory, pk=pk)
    form = SubcategoryForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        messages.success(request, 'Подкатегория обновлена.')
        return redirect('dds:references')
    return render(request, 'dds/ref_form.html', {'form': form, 'title': 'Редактировать подкатегорию'})

def subcategory_delete(request, pk):
    obj = get_object_or_404(Subcategory, pk=pk)
    if request.method == 'POST':
        obj.delete()
        messages.success(request, 'Подкатегория удалена.')
        return redirect('dds:references')
    return render(request, 'dds/confirm_delete.html', {'object': obj})