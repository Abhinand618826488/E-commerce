from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)

class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    address = models.TextField()

class Order(models.Model):
    customer = models.CharField(max_length=100)
    product = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    total_price = models.DecimalField(
        max_digits=10, decimal_places=2, default=0
    )
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=20, default="Pending"
    )
