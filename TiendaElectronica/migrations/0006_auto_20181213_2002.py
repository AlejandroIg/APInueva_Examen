# Generated by Django 2.1.4 on 2018-12-13 23:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TiendaElectronica', '0005_vendedor_password'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tienda',
            name='correo',
        ),
        migrations.RemoveField(
            model_name='tienda',
            name='encargado',
        ),
    ]
