from django.forms import ModelForm
from . models import Service


class ServiceForm(ModelForm):
    class Meta:
        model = Service
        fields = '__all__'
        # fields = ['service', 'price', 'count']