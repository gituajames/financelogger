from django import forms
from django.forms import ModelForm

from .models import Transaction, TransactionCost

class UploadMpesaMessageForm(ModelForm):
    class Meta:
        model = Transaction
        fields = '__all__'
        # fields = [
        #     'date_of_transaction',
        #     'transaction_message',
        #     'location_location_of_the_transaction',
        #     'location_description',
        #     'category_of_the_transaction',
        #     'description_of_the_transaction',
        #     'ammount',
        #     'name_of_recipients',
        #     'type_of_transaction',
        # ]