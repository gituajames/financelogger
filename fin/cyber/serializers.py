from rest_framework import serializers
from .models import Mobile_banking_messages


class MobileBankingMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mobile_banking_messages
        fields = ['mobile_bank_message']

