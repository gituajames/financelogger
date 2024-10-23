from django.contrib import admin
from . models import Transaction, TransactionCost


admin.site.register(Transaction)
admin.site.register(TransactionCost)

# Register your models here.
