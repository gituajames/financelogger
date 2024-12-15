from django.db import models

# Create your models here.

class Category(models.Model):
    product_category = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.product_category}"


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=200)
    product_description = models.TextField()
    product_price = models.IntegerField(default=0)
    stock_quantity = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.product_name}"

class ProductTransaction(models.Model):
    # product_id = 
    quantity = models.IntegerField(default=0) # number purchased
    transaction_type = models.CharField(max_length=3) # in or out
    date = models.DateField(auto_now_add=True)


# expensenses, reccuring costs such as rent and power and water bills and date they are suppposed to be paid

# profits to be calculated after expenses deductions