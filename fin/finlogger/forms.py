from django.forms import DateTimeField, widgets, ModelForm
from django.forms import ModelForm
from django import forms

from .models import Transaction, TransactionCost

class UploadMpesaMessageForm(ModelForm):
    class Meta:
        model = Transaction
        # fields = '__all__'
        fields = [
            # 'date_of_transaction',
            'transaction_message',
            'geolocation_of_the_transaction',
            'location_description',
            'category_of_the_transaction',
            'description_of_the_transaction',
        
        ]

        widgets = {
            'date_of_transaction' : widgets.DateTimeInput(
                
                attrs={'type':'date',
                }),
        }
        