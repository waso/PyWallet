from django import forms

class ExpenseAddForm(forms.Form):
    amount = forms.FloatField()
    currency = forms.CharField(max_length = 3)
    name = forms.CharField(max_length = 100)
    date = forms.CharField(max_length = 20)

class ExpenseEditForm(forms.Form):
    expense_id = forms.IntegerField()
    expense_amount = forms.FloatField()
    expense_currency = forms.CharField(max_length = 3)
    expense_name = forms.CharField(max_length = 100)
    expense_date = forms.CharField(max_length = 20)