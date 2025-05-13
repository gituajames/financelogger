from django.db import models

service_choices = [
    ("printing", "Printing"),
    ("photocopy","Photocopy"),
    ("scanning", "Scanning"),
    ("kra", "KRA"),
    ("SHA / SHIF", "SHA/SHIF"),
    ("emails", "mail services"),
    ("browsing", "Browsing"),
    ("passports", "Passport Photo"),
    ("ntsa", "NTSA"),
    ("HELB", "HELB"),
    ("Sale", "Sales"),
    ("lamination", "Lamination"),
    ("typsetting", "Typesetting"),
    ("songs", "Songs"),
    ("tse", "TSE"),
    ("mpesa statements", "M-pesa statements"),
    ("pension", "Pension"),
    ("others", "others"),
    ("E-Citizen", "E-Citizen"),
    ("Ghris", "Ghris"),

]

category_choices = [
    ("computing", "computing"),
    ("Storage", "Storage"),
    ("charging", "charging"),
    ("desktops", "desktops"),
    ("laptops", "laptops"),
    ("data cables", "data cables"),
]

mode_of_payment_choices = [
    ("Mpesa", "Mpesa"),
    ("KCB", "KCB"),
    ("CASH", "CASH")
]

class Mobile_banking_messages(models.Model):
    mobile_bank_message = models.CharField(max_length=1000)

class Service(models.Model):
    service = models.CharField(max_length=100, choices=service_choices)
    price = models.IntegerField(default=0)
    count = models.IntegerField(default=0)
    description = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now=True)
    mode_of_payment = models.CharField(max_length=50, choices=mode_of_payment_choices)
    paid_status = models.BooleanField(default=False)

    def __str__(self):
        return self.service

class Expenses(models.Model):
    expense = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    description = models.CharField(max_length=300)
    # date_of_expense = models.DateField()
    date_created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.expense

class Stock(models.Model):
    stock_batch_number = models.CharField(max_length=50)
    stock_date = models.DateField()
    stock_description = models.CharField(max_length=200)
    # stock_price_receipt


    def __str__(self):
        return self.stock_batch_number


class Product(models.Model):
    stock_batch_number = models.ForeignKey(Stock, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=50)
    product_retail_price = models.IntegerField(default=0)
    product_wholesale_price = models.IntegerField(default=0)
    product_category = models.CharField(max_length=50, choices=category_choices)
    product_description = models.CharField(max_length=200)
    product_quantity = models.IntegerField(default=0)

    def __str__(self):
        return self.product_name

# will have an api that uploads mpesa messages
# can also use mpesa daraja APIs
class PaymentMessages(models.Model):
    payment_message = models.CharField(max_length=200)
    payment_message_upload_time = models.DateField(auto_now=True)

    def __str__(Self):
        return self.payment_message

# class ProductPurchase(models.Model):
#     product_name = models.ForeignKey(Product, on_delete=models.CASCADE)
#     product_purchase_date = models.DateTimeField(auto_now=True)
#     product_purchase_price = models.IntegerField(default=0)
#     product_purchase_payment_message = models.
