from django.contrib import admin
from .models import Service, Expenses, Stock, Product, Mobile_banking_messages


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('service', 'price', 'count', 'description', 'date', 'paid_status')
# admin.site.register(Service)


@admin.register(Expenses)
class ExpensesAdmin(admin.ModelAdmin):
    list_display = ('expense', 'price', 'description', 'date_created')

@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ('stock_batch_number', 'stock_date', 'stock_description')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'product_name', 'stock_batch_number', 'product_category', 'product_retail_price',
        'product_quantity'
        )

@admin.register(Mobile_banking_messages)
class MobileBankingMessage(admin.ModelAdmin):
    list_display = ['mobile_bank_message']

# Register your models here.
