from django.contrib import admin

# Register your models here.

from django.contrib import admin

from . models import Usuario, Autor , Pieza , Comuna , Region , Tipo
admin.site.register(Usuario)
admin.site.register(Autor)
admin.site.register(Pieza)
admin.site.register(Comuna)
admin.site.register(Region)
admin.site.register(Tipo)
