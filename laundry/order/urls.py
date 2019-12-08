from django.urls import path
from .views import Orderview
urlpatterns = [
    path("/order", Orderview.as_view(), name="orders"),
]
