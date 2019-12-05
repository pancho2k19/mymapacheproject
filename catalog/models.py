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
    id =  models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="ID único para el autor")
    nombre = models.CharField(max_length=100)
    contacto = models.CharField(max_length=100)
    informacion = models.CharField(max_length=100)


    def str(self):
        return self.id


class Tipo(models.Model):
    id =  models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="ID único para el tipo")
    nombre = models.CharField(max_length=50)

    def str(self):
        return self.id


class Comuna(models.Model):
    id =  models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="ID único para la comuna")
    nombre = models.CharField(max_length=50)
    region = models.ForeignKey('Region', on_delete=models.SET_NULL, null=True)

    def str(self):
        return self.nombre

class Region(models.Model):
    id =  models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="ID único para la region")
    nombre = models.CharField(max_length=50)

    def str(self):
        return self.nombre

class Pieza(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="ID único para la pieza")
    nombre = models.CharField(max_length=50)
    stock = precio = models.IntegerField(  )
    id_autor = models.ForeignKey('Autor', on_delete=models.SET_NULL, null=True)
    precio = models.IntegerField(  )
    imagen = models.ImageField(upload_to = 'images/%Y/%m/%d')
    descripcion = models.CharField(max_length=100)
    id_tipo = models.ForeignKey('Tipo', on_delete=models.SET_NULL, null=True)
    id_usuario = models.ForeignKey('Usuario', on_delete=models.SET_NULL, null=True)
    def str(self):
        return self.id
