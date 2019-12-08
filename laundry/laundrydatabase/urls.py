from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from rest_framework import routers
from pelanggan.views import Custview
from order.views import Orderview


router = routers.DefaultRouter()
router.register(r'pelanggan', Custview)
router.register(r'orders', Orderview)
urlpatterns = [
    url(r'^', include(router.urls)),
    path('admin/', admin.site.urls),
    path(r'api/', include('rest_framework.urls', namespace='rest_framework')),
]
