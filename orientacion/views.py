from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from . import forms
from .models import Pregunta, Respuesta 
from django.db.models import Sum
from django.contrib.auth.models import User
from django.contrib.auth import (
	authenticate, get_user_model,
	login, logout,
)

#############################################

############### Encuestas ####################

#############################################

def home(request):
	return render(request, 'home.html')

def encuesta(request):
	usuarioActual = request.user
	preguntas = Pregunta.objects.filter()
	respuestas = Respuesta.objects.filter(usuario_id=usuarioActual.id)
	contexto={'preguntas':preguntas, 'respuestas':respuestas}
	return render(request, 'orientacion/encuesta.html', contexto)


def resultados(request):
	usuarioActual = request.user
	respuestas = Respuesta.objects.filter(usuario_id=usuarioActual.id).delete()
	
	for resp in filter(lambda key:key.startswith('resp'), request.POST.keys()):
		pregunta = Pregunta.objects.get(id = resp[4:])
		res = Respuesta()
		res.pregunta_id = pregunta
		res.area_id = pregunta.area_id
		res.respuesta_valor = request.POST[resp]
		res.usuario_id = usuarioActual
		res.save()

	resultados = Respuesta.objects.values('area_id__area_nombre').annotate(total=Sum('respuesta_valor'))
	context = {'resultados': resultados}
	return render(request, 'orientacion/resultados.html', context)