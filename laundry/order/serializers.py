from rest_framework import serializers
from .models import Orders, Customer
from django.db.models import F, Sum, FloatField, IntegerField
from decimal import Decimal


class Orderserializer(serializers.HyperlinkedModelSerializer):
    pelanggan = serializers.PrimaryKeyRelatedField(
        queryset=Customer.objects.all())
    nama_pelanggan = serializers.StringRelatedField(source='pelanggan')

    class Meta:
        model = Orders
        fields = ['id', 'pelanggan', 'nama_pelanggan',
                  'created', 'berat', 'tambahan', 'harga', 'Total', 'selesai', 'tgl_selesai']
