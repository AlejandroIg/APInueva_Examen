from rest_framework import viewsets
from .models import Producto, Vendedor, Tienda
from TiendaElectronica.serializers import ProductoSerializer, VendedorSerializer, TiendaSerializer


class ProductoViewSet (viewsets.ModelViewSet):
    queryset = Producto.objects.all().order_by('nombre')
    serializer_class = ProductoSerializer


class VendedorViewSet (viewsets.ModelViewSet):
    queryset = Vendedor.objects.all().order_by('username')
    serializer_class = VendedorSerializer


class TiendaViewSet (viewsets.ModelViewSet):
    queryset = Tienda.objects.all().order_by('nombre')
    serializer_class = TiendaSerializer
