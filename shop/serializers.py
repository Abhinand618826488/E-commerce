from rest_framework import serializers
from shop.models import *

from rest_framework import serializers
from shop.models import Product, Customer, Order


class ProductSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    description = serializers.CharField()
    category = serializers.CharField(max_length=100)
    price = serializers.DecimalField(
        max_digits=10, decimal_places=2
    )
    stock = serializers.IntegerField(default=0)


class CustomerSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    email = serializers.EmailField()
    phone = serializers.CharField(max_length=15)
    address = serializers.CharField()


class OrderSerializer(serializers.Serializer):
    customer = serializers.CharField(max_length=100)
    product = serializers.CharField(max_length=100)
    quantity = serializers.IntegerField()
    total_price = serializers.DecimalField(
        max_digits=10, decimal_places=2, read_only=True
    )
    order_date = serializers.DateTimeField(read_only=True)
    status = serializers.CharField(
        max_length=20, default="Pending"
    )