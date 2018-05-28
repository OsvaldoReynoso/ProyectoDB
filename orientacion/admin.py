from django.contrib import admin
from .models import Perfil, Area, Encuesta, Pregunta, Carrera, Institucion, Orientador, Carrera_Institucion, Carrera_Area, Respuesta

# Register your models here.
admin.site.register(Area)
admin.site.register(Respuesta)
admin.site.register(Encuesta)
admin.site.register(Pregunta)
admin.site.register(Institucion)
admin.site.register(Carrera)
admin.site.register(Orientador)
admin.site.register(Carrera_Institucion)
admin.site.register(Carrera_Area)