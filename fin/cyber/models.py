from django.db import models

service_choices = [
    ("printing", "Printing"),
    ("photocopy","Photocopy"),
    ("scanning", "Scanning"),
    ("kra", "KRA"),
    ("SHA / SHIF", "SHA/SHIF"),
    ("emails", "mail services"),
    ("browsing", "Browsing"),
    ("passports", "Passport Photo"),
    ("ntsa", "NTSA"),
    ("HELB", "HELB"),
    ("Sale", "Sales"),
    ("lamination", "Lamination"),
    ("typsetting", "Typesetting"),
    ("songs", "Songs"),
    ("tse", "TSE"),
    ("mpesa statements", "M-pesa statements"),
    ("pension", "Pension"),
    ("others", "others"),

]

class Service(models.Model):
    service = models.CharField(max_length=100, choices=service_choices)
    price = models.IntegerField(default=0)
    count = models.IntegerField(default=0)
    description = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now=True)
    paid_status = models.BooleanField(default=False)

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
