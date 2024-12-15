from django.shortcuts import render
from django.http import HttpResponse


def inventory_index(request):
    return HttpResponse('inventory')

# Create your views here.
