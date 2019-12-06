from django.db import models
from django.urls import reverse
import uuid




class Usuario(models.Model):
    rut =  models.CharField(primary_key=True, max_length=50, help_text="ID único para el usuario")
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    mail = models.EmailField(max_length=100)
    telefono = models.CharField(max_length=15)
    comuna = models.ForeignKey('Comuna', on_delete = models.SET_NULL , null = True)


    reputacion_lista = (  ('e' , 'pesima ') , ('d' , 'deficiente') , ('c' , 'normal') , ('b' , 'buena' ) , ('a' , 'muy buena') , ('n/a' , 'sin calificar'),
    )

    reputacion = models.CharField(max_length=3 , choices = reputacion_lista  , default = 'n/a' )

    def str(self):
        return self.id

class Autor(models.Model):

    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    contacto = models.CharField(max_length=100)
    informacion = models.CharField(max_length=100)


    def str(self):
        return f'{self.nombre}, {self.apellido}'


class Tipo(models.Model):

    nombre = models.CharField(max_length=50)

    def str(self):
        return self.id


class Comuna(models.Model):

    nombre = models.CharField(max_length=50)
    region = models.ForeignKey('Region', on_delete=models.SET_NULL, null=True)

    def str(self):
        return self.nombre

class Region(models.Model):

    nombre = models.CharField(max_length=50)

    def str(self):
        return self.nombre

class Pieza(models.Model):

    nombre = models.CharField(max_length=50)
    stock = models.IntegerField(  )
    autor = models.ForeignKey('Autor', on_delete=models.SET_NULL, null=True)
    precio = models.IntegerField(  )
    imagen = models.ImageField(upload_to = 'images/%Y/%m/%d', null = True)
    descripcion = models.CharField(max_length=100)
    tipo = models.ForeignKey('Tipo', on_delete=models.SET_NULL, null=True)
    usuario = models.ForeignKey('Usuario', on_delete=models.SET_NULL, null=True)

    def str(self):
        return self.nombre

    def get_detalle(self):
        return reverse('detalle', args=[str(self.id)])