from django.shortcuts import render
from.models import Autor, Usuario, Comuna , Region , Pieza, Tipo
from django.views import generic

#Create your views here.
def index(request):

	#Contador de objetos
	num_Autor = Autor.objects.all().count()
	num_Usuario = Usuario.objects.all().count()
	num_Comuna = Comuna.objects.all().count()
	num_Region = Region.objects.all().count()
	num_Pieza = Pieza.objects.all().count()
	num_Tipo = Tipo.objects.all().count()

	# mostrar estado
	# aqui podria ponerse algo relacionado con el stock

	return render( request , 'index.html' , context = { 'num_Autor':num_Autor , 'num_Usuario':num_Usuario ,'num_Pieza':num_Pieza,'num_Comuna':num_Comuna ,'num_Region':num_Region ,'num_Tipo':num_Tipo} ,
        )

class PiezaListView(generic.ListView):
    model = Pieza

class PiezaDetailView(generic.DetailView):
 model = Pieza
