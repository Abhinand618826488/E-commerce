from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from shop.models import Product, Customer, Order
from shop.serializers import (
    ProductSerializer,
    CustomerSerializer,
    OrderSerializer
)


# Product List and Create
class ProductListCreateView(APIView):

    def get(self, request):
        qs = Product.objects.all()
        serializer_instance = ProductSerializer(qs, many=True)
        return Response(data=serializer_instance.data)

    def post(self, request):
        form_data = request.data
        serializer_instance = ProductSerializer(data=form_data)

        if serializer_instance.is_valid():
            actual_data = serializer_instance.validated_data
            Product.objects.create(**actual_data)

            return Response(
                data={"message": "Product added successfully"}
            )
        else:
            return Response(data={"error": serializer_instance.errors})


# Retrieve, Update and Delete Product
class ProductRetrieveView(APIView):

    def get(self, request, pk):
        qs = Product.objects.get(id=pk)
        serializer_instance = ProductSerializer(qs)
        return Response(data=serializer_instance.data)

    def put(self, request, pk):
        form_data = request.data
        serializer_instance = ProductSerializer(data=form_data)

        if serializer_instance.is_valid():
            actual_data = serializer_instance.validated_data
            Product.objects.filter(id=pk).update(**actual_data)
            return Response(data={"message": "Product updated successfully"})
        else:
            return Response(data={"error": serializer_instance.errors})

    def delete(self, request, pk):
        Product.objects.filter(id=pk).delete()
        return Response(data={"message": "Product deleted successfully"})


# Customer List and Create
class CustomerListCreateView(APIView):

    def get(self, request):
        qs = Customer.objects.all()
        serializer_instance = CustomerSerializer(qs, many=True)
        return Response(data=serializer_instance.data)

    def post(self, request):
        form_data = request.data
        serializer_instance = CustomerSerializer(data=form_data)

        if serializer_instance.is_valid():
            actual_data = serializer_instance.validated_data
            Customer.objects.create(**actual_data)

            return Response(
                data={"message": "Customer added successfully"}
            )
        else:
            return Response(data={"error": serializer_instance.errors})


# Retrieve, Update and Delete Customer
class CustomerRetrieveView(APIView):

    def get(self, request, pk):
        qs = Customer.objects.get(id=pk)
        serializer_instance = CustomerSerializer(qs)
        return Response(data=serializer_instance.data)

    def put(self, request, pk):
        form_data = request.data
        serializer_instance = CustomerSerializer(data=form_data)

        if serializer_instance.is_valid():
            actual_data = serializer_instance.validated_data
            Customer.objects.filter(id=pk).update(**actual_data)
            return Response(data={"message": "Customer updated successfully"})
        else:
            return Response(data={"error": serializer_instance.errors})

    def delete(self, request, pk):
        Customer.objects.filter(id=pk).delete()
        return Response(data={"message": "Customer deleted successfully"})


# Order List and Create
class OrderListCreateView(APIView):

    def get(self, request):
        qs = Order.objects.all()
        serializer_instance = OrderSerializer(qs, many=True)
        return Response(data=serializer_instance.data)

    def post(self, request):
        form_data = request.data
        serializer_instance = OrderSerializer(data=form_data)

        if serializer_instance.is_valid():
            actual_data = serializer_instance.validated_data
            Order.objects.create(**actual_data)

            return Response(
                data={"message": "Order added successfully"}
            )
        else:
            return Response(data={"error": serializer_instance.errors})


# Retrieve, Update and Delete Order
class OrderRetrieveView(APIView):

    def get(self, request, pk):
        qs = Order.objects.get(id=pk)
        serializer_instance = OrderSerializer(qs)
        return Response(data=serializer_instance.data)

    def put(self, request, pk):
        form_data = request.data
        serializer_instance = OrderSerializer(data=form_data)

        if serializer_instance.is_valid():
            actual_data = serializer_instance.validated_data
            Order.objects.filter(id=pk).update(**actual_data)
            return Response(data={"message": "Order updated successfully"})
        else:
            return Response(data={"error": serializer_instance.errors})

    def delete(self, request, pk):
        Order.objects.filter(id=pk).delete()
        return Response(data={"message": "Order deleted successfully"})
# Create your views here.
