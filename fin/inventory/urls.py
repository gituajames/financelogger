from django.urls import path
from inventory.views import inventory_index

urlpatterns = [
    path('', inventory_index, name="index"),
]