from django.db import models

class Service(models.Model):
    service = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    count = models.IntegerField(default=0)
    description = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.service

class Expenses(models.Model):
    expense = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    description = models.CharField(max_length=300)
    # date_of_expense = models.DateField()
    date_created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.expense

# Create your models here.
