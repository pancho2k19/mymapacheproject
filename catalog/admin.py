from django.contrib import admin

# Register your models here.

from django.contrib import admin

from . models import Usuario, Autor , Pieza 
admin.site.register(Usuario)
admin.site.register(Autor)
admin.site.register(Pieza)
