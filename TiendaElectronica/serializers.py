from .models import Producto, Vendedor, Tienda
from rest_framework import serializers


class ProductoSerializer (serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Producto
        fields = ('id', 'nombre', 'imageUrl', 'descripcion', 'precio', 'tipo')


class TiendaSerializer (serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tienda
        fields = ('nombre', 'direccion', 'ciudad', 'comuna',
                  'telefono', 'correo', 'encargado')


class VendedorSerializer (serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Vendedor
        fields = ('username', 'correo', 'password')
