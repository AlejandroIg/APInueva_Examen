from django.contrib import admin
from .models import Tienda, Producto, Vendedor

# Register your models here.
admin.site.register(Producto)
admin.site.register(Vendedor)
admin.site.register(Tienda)
