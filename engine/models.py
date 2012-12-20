from django.db import models

class Currency(models.Model):
    code = models.CharField(max_length = 3)
    def __unicode__(self):
        return self.code

class Store(models.Model):
    name = models.CharField(max_length = 100)

class FormOfPayment(models.Model):
    name = models.CharField(max_length = 100)

class ExpenseType(models.Model):
    name = models.CharField(max_length = 100)

class User(models.Model):
    username = models.CharField(max_length = 100)
    password = models.CharField(max_length = 100)
    def __unicode__(self):
        return self.username

class ExpenseBucket(models.Model):
    date = models.DateField()
    store = models.ForeignKey(Store)
    form_of_payment = models.ForeignKey(FormOfPayment)

class Expense(models.Model):
    #transaction_id = models.IntegerField()
    #date = models.DateField()
    #name = models.CharField(max_length = 100)
    bucket = models.ForeignKey(ExpenseBucket)
    expense_type = models.ForeignKey(ExpenseType)
    amount = models.DecimalField(max_digits = 10, decimal_places = 5)
    currency = models.ForeignKey(Currency)
    comment = models.CharField(max_length = 100)
    
