from django.contrib import admin
from django.urls import path
from rest_framework import routers
from TiendaElectronica.models import Producto
from TiendaElectronica import views
from django.conf.urls import url, include

router = routers.DefaultRouter()
router.register( r'productos', views.ProductoViewSet )

urlpatterns = [
    path('admin/', admin.site.urls),
    url( r'^', include( router.urls ) ),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
