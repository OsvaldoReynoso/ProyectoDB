from django.urls import path, include
from . import views
from django.contrib.auth.views import login

app_name = 'orientacion'

urlpatterns = [
	path('resultados/', views.resultados, name='resultados'),
	path('encuesta/', views.encuesta, name='encuesta'),
]