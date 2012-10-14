from django.db import models

class Currency(models.Model):
    code = models.CharField(max_length = 3)

class User(models.Model):
    username = models.CharField(max_length = 100)
    password = models.CharField(max_length = 100)

class Expense(models.Model):
    transaction_id = models.IntegerField()
    date = models.DateField()
    name = models.CharField(max_length = 100)
    amount = models.DecimalField(max_digits = 10, decimal_places = 5)
