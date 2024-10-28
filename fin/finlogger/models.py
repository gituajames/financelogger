from django.db import models

# upload an mpesa message extract bellow info and save to db
# send email notifications of reports

# transactions - >
class Transaction(models.Model):


    TYPE_OF_TRANSACTION_CHOICES = {
        "paid" : "Paid",
        "received" : "Received",
        "sent" : "Sent"
    }
    
    date_of_mpesa_msg_upload = models.DateTimeField(auto_now_add = True)
    date_of_mpesa_msg_modify = models.DateTimeField(auto_now = True)
    date_of_transaction = models.DateTimeField() # 09/10/12
    transaction_message = models.CharField(max_length=1000) # mpesa message
    geolocation_of_the_transaction = models.CharField(max_length=200) # lat lon if possible
    location_description = models.CharField(max_length=200) # name of place e.g city link hardware
    category_of_the_transaction = models.CharField(max_length=50) # food, entertainment etc
    # add choices
    description_of_the_transaction = models.TextField() # paid for services, prodct etc
    amount = models.IntegerField(default=0) # amount of cash used
    name_of_recipients = models.CharField(max_length=50) # name of recipients
    type_of_transaction = models.CharField(max_length=20, choices=TYPE_OF_TRANSACTION_CHOICES) # paid, sent or received
    transaction_cost  = models.IntegerField(default=0) # actual transaction cost

    def __str__(self):
        return f"{self.name_of_recipients}, {self.amount}"

# transaction costs acossiated with a transaction - >
class TransactionCost(models.Model):
    transaction_id = models.ForeignKey(Transaction, on_delete=models.CASCADE) # foreign key
    transaction_cost  = models.IntegerField(default=0) # actual transaction cost


# Create your models here.
