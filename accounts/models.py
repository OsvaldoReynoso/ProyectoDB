from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	first_name = models.CharField(max_length=30, blank=True)
	last_name = models.CharField(max_length=30, blank=True)
	birth_date = models.DateField(null=True, blank=True)

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create(user=instance)
	instance.profile.save()

# Create your models here.
class Usuario(models.Model):
	usuario_nombre = models.CharField(max_length=25)
	usuario_correo = models.CharField(max_length=50)
	usuario_password = models.CharField(max_length=20)

	def __str__(self):
		return self.usuario_nombre

