from rest_framework import viewsets
from .serializers import Orderserializer
from .models import Orders


class Orderview(viewsets.ModelViewSet):
    queryset = Orders.objects.all()
    serializer_class = Orderserializer
