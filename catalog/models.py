from django.db import models
from django.urls import reverse
import uuid




class Usuario(models.Model):
    rut =  models.CharField(primary_key=True, max_length=50, help_text="ID único para el usuario")
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    mail = models.EmailField(max_length=100)
    telefono = models.CharField(max_length=15)



    reputacion_lista = (  ('e' , 'pesima ') , ('d' , 'deficiente') , ('c' , 'normal') , ('b' , 'buena' ) , ('a' , 'muy buena') , ('n/a' , 'sin calificar'),
    )

    reputacion = models.CharField(max_length=3 , choices = reputacion_lista  , default = 'n/a' )

    def __str__(self):
        return self.nombre

class Autor(models.Model):

    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    contacto = models.CharField(max_length=100)
    informacion = models.CharField(max_length=100)


    def __str__(self):
        return f'{self.nombre}, {self.apellido}'



class Pieza(models.Model):

    nombre = models.CharField(max_length=50)
    stock = models.IntegerField(  )
    autor = models.ForeignKey('Autor', on_delete=models.SET_NULL, null=True)
    precio = models.IntegerField(  )
    imagen = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)
    usuario = models.ForeignKey('Usuario', on_delete=models.SET_NULL, null=True)
    imagenprueba = models.ImageField( null = True , blank = True)

    def __str__(self):
        return self.nombre

    def get_detalle(self):
        return reverse('detalle', args=[str(self.id)])
