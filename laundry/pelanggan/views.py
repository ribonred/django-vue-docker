from django.shortcuts import render
from rest_framework import viewsets
from .models import Customer
from .serializers import CustomerSerial

class Custview(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerial
