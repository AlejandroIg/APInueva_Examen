from .models import Producto
from rest_framework import serializers



class ProductoSerializer ( serializers.HyperlinkedModelSerializer ):
    class Meta:
        model = Producto
        fields = ( 'id','nombre','imageUrl', 'descripcion', 'precio', 'tipo' )