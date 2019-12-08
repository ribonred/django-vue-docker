from django.urls import path
from .views import Custview
urlpatterns = [
    path("/pelanggan", Custview.as_view(), name="customer"),
]
