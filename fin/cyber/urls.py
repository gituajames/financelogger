from django.urls import path, include
from . import views

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('mobilebankingmessage', views.MobileBankingMessageViewSet)



urlpatterns = [
    path('service_upload_form/', views.service_upload_form, name='service_upload_form'),
    path('cyber_dash_summury/', views.cyber_dash_summury, name='cyber_dash_summury'),
    path('inventory', views.inventory, name='inventory'),
    path('', include(router.urls)),
]