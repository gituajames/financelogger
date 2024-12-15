from django.db import models
from django.forms import ModelForm

# upload an mpesa message extract bellow info and save to db
# send email notifications of reports

# transactions - >

# TYPE_OF_THE_TRANSACTION_CHOICES = {
#         "paid" : "Paid",
#         "received" : "Received",
#         "sent" : "Sent",
#     }


class Transaction(models.Model):
    # extracted from the m-pesa message
    # transaction_id = models.CharField(max_length=100)
    date_of_transaction = models.DateTimeField() # 09/10/12
    amount = models.FloatField(default=0) # amount of cash used
    type_of_transaction = models.CharField(max_length=200) # paid, sent or received
    name_of_recipients = models.CharField(max_length=50) # name of recipients
    transaction_cost  = models.FloatField(default=0) # actual transaction cost

    transaction_message = models.CharField(max_length=1000) # mpesa message


    # additatiion info on the transaction
    geolocation_of_the_transaction = models.CharField(max_length=200) # lat lon if possible
    location_description = models.CharField(max_length=200) # name of place e.g city link hardware
    category_of_the_transaction = models.CharField(max_length=50) # food, entertainment etc
    
    description_of_the_transaction = models.TextField() # paid for services, prodct etc
    date_of_mpesa_msg_upload = models.DateTimeField(auto_now_add = True)
    date_of_mpesa_msg_modify = models.DateTimeField(auto_now = True)

    def __str__(self):
        return f"{self.name_of_recipients}, {self.amount}"

# transaction costs acossiated with a transaction - >
class TransactionCost(models.Model):
    transaction_id = models.ForeignKey(Transaction, on_delete=models.CASCADE) # foreign key
    transaction_cost  = models.IntegerField(default=0) # actual transaction cost


# Create your models here.
