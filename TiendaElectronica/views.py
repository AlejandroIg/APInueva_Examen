from rest_framework import viewsets
from .models import Producto
from TiendaElectronica.serializers import ProductoSerializer

# Create your views here.
class ProductoViewSet ( viewsets.ModelViewSet ):
    queryset = Producto.objects.all().order_by( 'nombre' )
    serializer_class = ProductoSerializer