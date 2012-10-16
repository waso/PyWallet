from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from forms import ExpenseAddForm, ExpenseEditForm
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

def remove(request):
    print "remove"
    if request.method == 'POST':
        print "POST"
        try:
            exp_id = int(request.POST["expense_id"])
            expense = Expense.objects.get(pk = exp_id)
        except Expense.DoesNotExist:
            return redirect ('/')

        expense.delete()
        return redirect ('/')
    else:
        return redirect ('/')

def update(request):
    print "update"
    if request.method == 'POST':
        form = ExpenseEditForm(request.POST)        
        if not form.is_valid():
            return redirect ('/')
        try:
            exp_id = form.cleaned_data['expense_id']
            expense = Expense.objects.get(pk = exp_id)
            expense.name = form.cleaned_data['expense_name']
            expense.amount = form.cleaned_data['expense_amount']
            expense.date = datetime.strptime(form.cleaned_data['expense_date'], '%d-%m-%Y')
            #expense.currency = form.cleaned_data['expense_currency']
            expense.save()
        except Expense.DoesNotExist:
            pass
        return redirect ('/')
    else:
        return redirect ('/')