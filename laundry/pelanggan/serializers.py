from rest_framework import serializers
from .models import Customer


class CustomerSerial(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'nama', 'alamat']
