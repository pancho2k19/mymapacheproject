from django import forms
from django.db import models
from django.forms import ModelForm
from .models import Pieza
from .models import Usuario
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class PiezaForm(ModelForm):

  nombre = forms.CharField( min_length = 3 , max_length = 50)
  descripcion = forms.CharField( min_length = 10 , max_length = 100)
  precio = forms.IntegerField( min_value = 0 , max_value = 9999999)
  stock = forms.IntegerField( min_value = 0 , max_value = 9999999)


  class Meta:
    model = Pieza
    fields = ['nombre' , 'stock' , 'autor' , 'precio' , 'descripcion' , 'usuario' , 'imagenprueba']



class UserForm(UserCreationForm):

    class Meta:
      model = User
      fields = ['first_name' , 'last_name' , 'email' , 'username' , 'password1' , 'password2' ]


class UsuarioForm(ModelForm):

    class Meta:
      model = Usuario
      fields = ['nombre' , 'apellido'  , 'mail' ,'nombre_usuario'  ]
