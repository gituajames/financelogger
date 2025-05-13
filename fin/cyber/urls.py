from django.urls import path
from . import views

urlpatterns = [
    path('service_upload_form/', views.service_upload_form, name='service_upload_form'),
    path('cyber_dash_summury/', views.cyber_dash_summury, name='cyber_dash_summury'),
    path('inventory', views.inventory, name='inventory')
    # path('inventory/', include("inventory.urls"))
]