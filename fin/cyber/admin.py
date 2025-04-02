from django.contrib import admin
from .models import Service, Expenses


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('service', 'price', 'count', 'description', 'date', 'paid_status')
# admin.site.register(Service)


@admin.register(Expenses)
class ExpensesAdmin(admin.ModelAdmin):
    list_display = ('expense', 'price', 'description', 'date_created')



# Register your models here.
