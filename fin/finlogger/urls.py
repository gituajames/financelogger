from django.urls import path
from .views import index, uploadmpesamessage

urlpatterns = [
    path('', index, name="index"),
    path('upload/', uploadmpesamessage, name="uploadmpesamessage")
]