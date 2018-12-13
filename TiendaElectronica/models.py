from django.db import models

# Create your models here.


class Producto(models.Model):

    PRODUCTO = (
        ('Celulares', 'Celulares'),
        ('ComponectesPC', 'ComponectesPC'),
        ('Monitores', 'Monitores'),
        ('Accesorios', 'Accesorios'),
    )
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=60)
    imageUrl = models.CharField(max_length=255, default='')
    descripcion = models.CharField(max_length=255)
    precio = models.CharField(max_length=255)
    tipo = models.CharField(
        max_length=255, default='celulares', choices=PRODUCTO)

    def __str__(self):
        return self.nombre


class Vendedor(models.Model):
    username = models.CharField(primary_key=True, max_length=30, default='')
    correo = models.CharField(max_length=100, default='')
    password = models.CharField(max_length=40, default='')

    def __str__(self):
        return self.username


class Tienda(models.Model):
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=50)
    comuna = models.CharField(max_length=50)
    telefono = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre
