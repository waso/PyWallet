from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from forms import ExpenseAddForm
from models import Expense, Currency
from datetime import datetime

def home(request):
    if request.method == 'POST':
        form = ExpenseAddForm(request.POST)
        if form.is_valid():
            print form.cleaned_data['date']
            cur = Currency.objects.get(code__iexact = form.cleaned_data['currency'])
            exp = Expense()
            exp.transaction_id = 1
            exp.name = form.cleaned_data['name']
            exp.amount = form.cleaned_data['amount']
            exp.currency = cur
            exp.date = datetime.strptime(form.cleaned_data['date'], '%d-%m-%Y')
            exp.save()
            return redirect ('/')
        else:
            return redirect ('/')
    else:
        expenses = Expense.objects.all().order_by('-date','-transaction_id')
        date = datetime.now()
        return render_to_response('base.html', {
            'expenses' : expenses,
            'date' : date},
             context_instance = RequestContext(request))