from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from . import forms
from . import models
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.urls import reverse, reverse_lazy
from django.views import generic, View

class signup(generic.CreateView):
	form_class = forms.SignupForm
	template_name = 'accounts/signup3.html'

	def get_success_url(self):
		return reverse('accounts:login')


def menu(request):
	return render(request, 'accounts/menu.html', {})

# def login(request):
# 	username = request.POST['username']
# 	password = request.POST['password']
# 	user = authenticate(request, username=username, password=password)

# 	if user is not None:
# 		login(request, user)
# 	else
	


# def login(request):
# 	form_class = AuthenticationForm
# 	success_url = reverse_lazy('/accounts/home')
# 	template_name = 'accounts/login.html'

# def signup(request):
# 	if request.method == 'POST':
# 		form = forms.SignupForm(request.POST)
# 		if form.is_valid():
# 			new_user = User(username=request.POST['username'], first_name=request.POST['nombre'], email_address=request.POST['correo'], password=request.POST['password'])
# 			user = new_user.save()
# 			user.refresh_from_db()
# 			user.profile.birth_date = request.POST['birth_date']
# 			user.save()
# 			raw_password = form.cleaned_data.get('password')
# 			#user = authenticate(username=user.username, password=raw_password)
# 			#login(request, user)
# 			return redirect('/accounts/login')
# 	else:
# 		form = forms.SignupForm()
# 	return render(request, 'accounts/signup2.html', {'form':form})

# Create your views here.

def loginV(request):	
	form = AuthenticationForm
	return render(request, 'accounts/login.html', {'form': form})

#View para Registrar
# def signup(request):
# 	if request.method == 'POST':
# 		form = forms.SignupForm(request.POST)
# 		if form.is_valid():
# 			nuevo_usuario = models.Usuario(usuario_nombre=request.POST['usuario_nombre'], usuario_correo=request.POST['usuario_correo'], usuario_password=request.POST['usuario_password'])
# 			nuevo_usuario.save()
# 			#Retorna al siguiente URL despues de registrar exitosamente
# 			return redirect('/accounts/login')
# 	else:
# 		form = forms.SignupForm()
# 	return render(request, 'accounts/signup2.html', {'form':form})