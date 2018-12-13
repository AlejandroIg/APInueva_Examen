from django.db import models

# Create your models here.
class Producto( models.Model ):
    
    PRODUCTO = (
        ('Celulares', 'Celulares'),
        ('ComponectesPC', 'ComponectesPC'),
        ('Monitores','Monitores'),
        ('Accesorios', 'Accesorios'),
    )   


    id = models.AutoField( primary_key = True )
    nombre = models.CharField( max_length = 60 )
    imageUrl = models.CharField( max_length = 255, default = '' )
    descripcion = models.CharField( max_length = 255 )
    precio = models.CharField( max_length = 255 )
    tipo = models.CharField( max_length = 255,default= 'celulares' ,choices= PRODUCTO )

    def __str__( self ):
        return self.nombre