from django.urls import path
from finlogger.views import index, uploadmpesamessage

urlpatterns = [
    path('summary', index, name="index"),
    path('upload/', uploadmpesamessage, name="uploadmpesamessage")
]