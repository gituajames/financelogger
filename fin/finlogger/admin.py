from django.contrib import admin
from . models import Transaction, TransactionCost
from cyber.models import Service


admin.site.register(Transaction)
admin.site.register(TransactionCost)
admin.site.register(Service)

# Register your models here.
