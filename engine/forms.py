from django import forms

class ExpenseAddForm(forms.Form):
    amount = forms.FloatField()
    currency = forms.CharField(max_length = 3)
    name = forms.CharField(max_length = 100)
    date = forms.CharField(max_length = 20)