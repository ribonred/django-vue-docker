from django.db import models

class Customer(models.Model):
    nama = models.CharField(max_length=255)
    alamat = models.CharField(max_length=255)
    
    def __str__(self):
        return self.nama