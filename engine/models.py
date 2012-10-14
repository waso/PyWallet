from django.db import models

class Currency(models.Model):
    code = models.CharField(max_length = 3)
    def __unicode__(self):
        return self.code


class User(models.Model):
    username = models.CharField(max_length = 100)
    password = models.CharField(max_length = 100)
    def __unicode__(self):
        return self.username

class Expense(models.Model):
    transaction_id = models.IntegerField()
    date = models.DateField()
    name = models.CharField(max_length = 100)
    amount = models.DecimalField(max_digits = 10, decimal_places = 5)
    currency = models.ForeignKey(Currency)
