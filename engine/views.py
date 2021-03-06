from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from forms import ExpenseAddForm, ExpenseEditForm
from models import Currency, ExpenseBucket
from datetime import datetime


def sign_in(request):
    #redirect user to main page if he's already signed in
    if request.user.is_authenticated():
        return redirect('/')

    #if signin form sent, authenticate
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect ('/')
            else:
                return redirect ('/')
        else:
            return redirect ('/')
    else:
        return render_to_response('login.html', {},
             context_instance = RequestContext(request))

@login_required
def sign_out(request):
    logout(request)
    return redirect ('/')

@login_required
def home(request):
    expense_buckets = ExpenseBucket.objects.all().order_by('-date', '-store')
    for bucket in expense_buckets:
        expenses[bucket.id] = Expense.objects.filter(bucket = bucket.id)
    date = datetime.now()
    return render_to_response('base.html', {
            'expense_buckets' : expense_buckets,
            'expenses' : expenses,
            'date' : date},
             context_instance = RequestContext(request))

@login_required
def add(request):
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

@login_required
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

@login_required
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
