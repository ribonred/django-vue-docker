from django.db import models
from decimal import Decimal
from pelanggan.models import Customer
from django.db.models import F, Sum
from datetime import datetime


class Orders(models.Model):
    pelanggan = models.ForeignKey(
        Customer, on_delete=models.CASCADE, related_name='cust')
    created = models.DateField(auto_now_add=True)
    berat = models.FloatField()
    tambahan = models.IntegerField(null=True, blank=True)
    harga = models.IntegerField()
    Total = models.IntegerField(blank=True, null=True, editable=False)
    selesai = models.BooleanField(default=False)
    tgl_selesai = models.DateField(blank=True, null=True, editable=False)

    def __str__(self):
        return self.pelanggan.nama

    def save(self, *args, **kwargs):
        self.Total = int(self.berat * self.harga + self.tambahan)
        if self.selesai:
            self.tgl_selesai = datetime.now().date()
        super().save(*args, **kwargs)
