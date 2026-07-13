from django.shortcuts import render
from django.views.generic import TemplateView

from .models import Transaction, Status, TypeTransaction, Category, SubCategory
from .forms import TransactionForm
# Create your views here.

# Возвращает список транзаций с формой фильтрации
class TransactionsView(TemplateView):
    template_name = 'transactions/transactions.html'
    async def get_form_data(self):
        status_set = Status.objects.all()
        type_transaction_set = TypeTransaction.objects.all()
        category_set = Category.objects.all()
        form_data = {
            'statuses': [('', '---------')] + [(status.id, status.title) async for status in status_set],
            'categories': [('', '---------')] + [(category.id, category.title) async for category in category_set],
            'type_transactions': [('', '---------')] + [(type_transaction.id, type_transaction.title) async for type_transaction in type_transaction_set],
        }
        return form_data
    
    async def get_sub_categories(self):
        sub_category_set = SubCategory.objects.select_related('category').all()
        sub_categories = [('', '---------')] + [(sub_category.id, sub_category.title, sub_category.category.id) async for sub_category in sub_category_set]
        return sub_categories
    
    async def get(self, request, *args, **kwargs):
        queryset = Transaction.objects.select_related(
            'status',
            'category',
            'type_transaction',
            'sub_category').all()
        form_data = await self.get_form_data()
        transactions = [transaction async for transaction in queryset]
        form = TransactionForm(choises_data=form_data)
        sub_categories = await self.get_sub_categories()
        context = {
            'transactions': transactions,
            'form': form,
            'sub_categories': sub_categories}
        return render(request, self.template_name, context) 
    
    async def post(self, request, *args, **kwargs):
        form = TransactionForm(request.POST)
        queryset = Transaction.objects.select_related(
            'status',
            'category',
            'type_transaction',
            'sub_category')
        if form.is_valid():
            cleaned_data = form.cleaned_data
            created_at_from = cleaned_data['created_at_from']
            created_at_to = cleaned_data['created_at_to']
            status_id = cleaned_data['status']
            type_transaction_id = cleaned_data['type_transaction']
            category_id = cleaned_data['category']
            sub_category_id = cleaned_data['sub_category']
            if created_at_from:
                queryset = queryset.filter(created_at__gte=created_at_from)
            if created_at_to:
                queryset = queryset.filter(created_at__lte=created_at_to)
            if status_id:
                queryset = queryset.filter(status_id=status_id)
            if type_transaction_id:
                queryset = queryset.filter(type_transaction_id=type_transaction_id)
            if category_id:
                queryset = queryset.filter(category_id=category_id)
            if sub_category_id:
                queryset = queryset.filter(sub_category_id=sub_category_id)
        print(form.errors)
        queryset = queryset.all()
        form_data = await self.get_form_data()
        transactions = [transaction async for transaction in queryset]
        form = TransactionForm(choises_data=form_data)
        sub_categories = await self.get_sub_categories()
        context = {
            'transactions': transactions,
            'form': form,
            'sub_categories': sub_categories}
        return render(request, self.template_name, context)
    
