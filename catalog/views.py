from django.shortcuts import render
from.models import Autor, Usuario, Comuna , Region , Pieza, Tipo
from django.views import generic

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy



#Create your views here.
def index(request):

	#Contador de objetos
	num_Autor = Autor.objects.all().count()
	num_Usuario = Usuario.objects.all().count()
	num_Comuna = Comuna.objects.all().count()
	num_Region = Region.objects.all().count()
	num_Pieza = Pieza.objects.all().count()
	num_Tipo = Tipo.objects.all().count()

	num_visits = request.session.get('num_visits', 0)
	num_visits = request.session['num_visits'] = num_visits+1

	# mostrar estado
	# aqui podria ponerse algo relacionado con el stock

	return render( request , 'index.html' ,	context = { 'num_Autor':num_Autor , 'num_Usuario':num_Usuario ,'num_Pieza':num_Pieza,'num_Comuna':num_Comuna ,
	'num_Region':num_Region ,'num_Tipo':num_Tipo , 'num_visits':num_visits} ,
        )




class PiezaListView(generic.ListView):
    model = Pieza
    paginate_by = 10

class PiezaDetailView(generic.DetailView):
    model = Pieza



class PiezaCreate(CreateView):
    model = Pieza
    fields = '__all__'
    initial={'nombre':'prueba'}

class PiezaUpdate(UpdateView):
    model = Pieza
    fields = ['nombre','stock' , 'autor', 'precio ', 'imagen' , 'descripcion' , 'tipo' , 'usuario']

class PiezaDelete(DeleteView):
    model = Pieza
    success_url = reverse_lazy('authors')