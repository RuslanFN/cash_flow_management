from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Transaction

# Create your views here.
class TransactionsView(TemplateView):
    template_name = 'transactions/transactions.html'
    async def get(self, request, *args, **kwargs):
        queryset = Transaction.objects.select_related(
            'status',
            'category',
            'type_transaction',
            'sub_category').all()
        transactions = [transaction async for transaction in queryset]
        context = {'transactions': transactions}
        return render(request, self.template_name, context) 
    
