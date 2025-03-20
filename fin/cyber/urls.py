from django.urls import path
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path("finlogger/", include("finlogger.urls")),
    path('', views.index, name='index'),
    path('home', views.home, name='home'),
    # path('inventory/', include("inventory.urls"))
]