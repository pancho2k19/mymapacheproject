from django import forms
from django.db import models
from django.forms import ModelForm
from .models import Pieza
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class PiezaForm(ModelForm):

  nombre = forms.CharField( min_length = 3 , max_length = 50)
  descripcion = forms.CharField( min_length = 10 , max_length = 100)


  class Meta:
    model = Pieza
    fields = ['nombre' , 'stock' , 'autor' , 'precio' , 'imagen' , 'descripcion' , 'usuario' ,'imagenprueba']



class UserForm(UserCreationForm):
    model = User
    class Meta:
      model = User
      fields = ['first_name' , 'last_name' , 'email' , 'username' , 'password1' , 'password2' ]
