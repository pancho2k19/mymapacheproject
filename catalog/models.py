from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
import uuid




class Usuario(models.Model):

    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    mail = models.EmailField(max_length=100)
    nombre_usuario = models.CharField(max_length=50)


    def __str__(self):
        return self.nombre_usuario

class Autor(models.Model):

    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    contacto = models.CharField(max_length=100)
    informacion = models.CharField(max_length=100)


    def __str__(self):
        return f'{self.nombre}  {self.apellido}'



class Pieza(models.Model):

    nombre = models.CharField(max_length=50)
    stock = models.IntegerField(  )
    autor = models.ForeignKey('Autor', on_delete=models.SET_NULL, null=True)
    precio = models.IntegerField(  )
    descripcion = models.CharField(max_length=100)
    usuario = models.ForeignKey( 'Usuario' ,  on_delete=models.SET_NULL, null=True)
    imagenprueba = models.ImageField( null = True , blank = True)

    def __str__(self):
        return self.nombre

    def get_detalle(self):
        return reverse('detalle', args=[str(self.id)])
