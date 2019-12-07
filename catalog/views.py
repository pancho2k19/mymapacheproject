from django.shortcuts import render , redirect
from .models import Autor, Usuario,  Pieza
from django.views import generic
from .forms import PiezaForm , UserForm
from django.contrib.auth.decorators import login_required , permission_required
from django.contrib.auth import login , authenticate



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

def home(request):

		return render(request , 'catalog/home.html')

def donar(request):

		return render(request , 'catalog/donar.html')




def listado(request):
	piezas = Pieza.objects.all()
	data = { 'piezas':piezas }
	return render(request , 'catalog/listado_piezas.html' , data)

@login_required
@permission_required('catalog.add_pieza')
def registrar(request):
	data = {'form':PiezaForm()}

	if request.method == 'POST':
		formulario = PiezaForm(request.POST , files = request.FILES)
		if formulario.is_valid():
			formulario.save()
			data['mensaje'] = 'guardado correctamente'

	return render(request , 'catalog/registrar_pieza.html' , data)


def modificar(request , id):
	pieza = Pieza.objects.get(id=id)
	data = {'form':PiezaForm(instance = pieza)}
	if request.method == 'POST':
		formulario = PiezaForm(data = request.POST , instance = pieza, files = request.FILES)
		if formulario.is_valid():
			formulario.save()
			data['mensaje'] = 'modificado correctamente'
		data['form'] = PiezaForm( instance = Pieza.objects.get(id=id))
	return render(request , 'catalog/modificar_pieza.html' , data)

def eliminar(request, id):
	pieza = Pieza.objects.get(id = id)
	pieza.delete()
	return redirect( to="listado")


def mostrar(request):
	piezas = Pieza.objects.all()
	data = { 'piezas':piezas }
	return render(request , 'catalog/mostrador.html' , data)

def registro_usuario(request):
	data = {'form':UserForm()}

	if request.method == 'POST':
		formulario = UserForm(request.POST )
		if formulario.is_valid():
			formulario.save()
			username = formulario.cleaned_data['username']
			password = formulario.cleaned_data['password1']
			user = authenticate( username = username , password = password)
			login(request, user)
			return redirect( to = "home")

	return render(request , 'registration/registrar.html' , data)
