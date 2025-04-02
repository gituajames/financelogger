from django.contrib import admin
from . models import Transaction, TransactionCost
# from cyber.models import Service


# admin.site.register(Transaction)
# admin.site.register(TransactionCost)

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('category_of_the_transaction', 'type_of_transaction', 'name_of_recipients', 'amount')
# admin.site.register(Service)

# Register your models here.
