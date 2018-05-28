from django.db import models
from django.template import defaultfilters
from django.contrib.auth.models import User

##################################################

###################  CHOICES  ####################

##################################################

GENDER_CHOICES = [
	('M', 'M'),
	('F', 'F'),
]

RESPUESTA_CHOICES = [
	(1, 1),
	(2, 2),
	(3, 3),
	(4, 4),
]

TEMA_CHOICES = [
	('', ''),
]

AREA_CHOICES = [
	('Realista', 'REALISTA'),
	('Investigativo', 'INVESTIGATIVO'),
	('Social', 'SOCIAL'),
	('Artista', 'ARTISTA'),
	('Emprendedor', 'EMPRENDEDOR'),
	('Convencional', 'CONVENCIONAL'),
	('Manual', 'MANUAL'),
	('Mecanica', 'MECANICA'),
	('Cientifica', 'CIENTIFICA'),
	('Percepcion_Espacial', 'PERCEPCION ESPACIAL'),
	('Prosocial', 'PROSOCIAL'),
	('Enseñanza', 'ENSEÑANZA'),
	('Creativa_Artistica', 'CREATIVA_ARTISTICA'),
	('Literaria', 'LITERARIA'),
	('Liderazgo', 'LIDERAZGO'),
	('Gerencial', 'GERENCIAL'),
	('Organizacion', 'ORGANIZACION'),
	('Manejo_de_Datos', 'MANEJO_DE_DATOS'),
]



##################################################

###################  CLASES  #####################

##################################################

class Perfil(models.Model):

	user = models.OneToOneField(User, on_delete=models.CASCADE)

	user_edad = models.IntegerField()
	user_sexo = models.CharField(max_length=1, choices=GENDER_CHOICES, default='M')

	# Este podria ser nuestro metodo str
	# def __str__(self):
	# 	return "{0} {1}".format(self.usuario.first_name, self.usuario.last_name)


class Area(models.Model):
	area_nombre = models.CharField(max_length=40, choices=AREA_CHOICES)

	def __str__(self):
		return self.area_nombre


class Encuesta(models.Model):
	encuesta_tipo = models.CharField(max_length=25)

	def __str__(self):
		return self.encuesta_tipo


class Pregunta(models.Model):
	pregunta_texto = models.CharField(max_length=150)
	area_id = models.ForeignKey(Area, on_delete=models.CASCADE)
	encuesta_id = models.ForeignKey(Encuesta, on_delete=models.CASCADE)

	def __str__(self):
		return self.pregunta_texto


class Institucion(models.Model):
	institucion_nombre = models.CharField(max_length=50)
	institucion_direccion = models.CharField(max_length=100)
	institucion_correo = models.EmailField()
	institucion_telefono = models.IntegerField()

	def __str__(self):
		return self.institucion_nombre


class Carrera(models.Model):
	carrera_nombre = models.CharField(max_length=40)
	institucion = models.ManyToManyField(Institucion, through='Carrera_Institucion')
	area_id = models.ManyToManyField(Area, through='Carrera_Area')

	def __str__(self):
		return self.carrera_nombre


class Orientador(models.Model):
	orientador_nombre = models.CharField(max_length=35)
	orientador_ap_paterno = models.CharField(max_length=35)
	orientador_ap_materno = models.CharField(max_length=35)
	orientador_edad = models.IntegerField()
	orientador_sexo = models.CharField(max_length=1, choices=GENDER_CHOICES, default='M')
	orientador_correo = models.EmailField()
	orientador_area = models.CharField(max_length=35, blank=True, null=True)
	institucion = models.ForeignKey(Institucion, on_delete=models.CASCADE)
	orientador_slug = models.SlugField(max_length=100)

	def __str__(self):
		return self.orientador_nombre


class Respuesta(models.Model):
	respuesta_valor = models.IntegerField(choices = RESPUESTA_CHOICES)
	area_id = models.ForeignKey(Area, on_delete=models.CASCADE)
	pregunta_id = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
	usuario_id = models.ForeignKey(User, on_delete=models.CASCADE)


##################################################

##############  CLASES INTERMEDIAS  ##############

##################################################

class Carrera_Institucion(models.Model):
	carrera_id = models.ForeignKey(Carrera, on_delete=models.CASCADE)
	institucion_id = models.ForeignKey(Institucion, on_delete=models.CASCADE)


class Carrera_Area(models.Model):
	carrera_id = models.ForeignKey(Carrera, on_delete=models.CASCADE)
	area_id = models.ForeignKey(Area, on_delete=models.CASCADE)